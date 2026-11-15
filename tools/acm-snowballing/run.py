from __future__ import annotations

import argparse
import csv
import json
import re
import time
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).with_name("config.json")
OC_INDEX = "https://api.opencitations.net/index/v2"
OPENALEX = "https://api.openalex.org"
CROSSREF = "https://api.crossref.org/v1"
HEADERS = {"User-Agent": "SWT301-SLR-Snowballing/1.1 (mailto:slr-team@example.invalid)"}


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def norm(value: str) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value)
    value = re.sub(r"^https?://dl\.acm\.org/doi/", "", value)
    value = re.sub(r"^doi:\s*", "", value)
    return value.strip(" .;,)")


def norm_title(value: str) -> str:
    value = (value or "").lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def extract_doi(text: str) -> str:
    m = re.search(r"(?i)(?:doi:\s*)?(10\.\d{4,9}/[-._;()/:a-z0-9]+)", text or "")
    return norm(m.group(1)) if m else ""


def get_json(url: str, params: dict | None = None, retries: int = 3):
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=60)
            if r.status_code == 200:
                return r.json()
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            return None
        except requests.RequestException:
            time.sleep(2 ** attempt)
    return None


def oc_collect(doi: str):
    result = []
    for direction, endpoint in (
        ("BACKWARD", f"{OC_INDEX}/references/doi:{doi}"),
        ("FORWARD", f"{OC_INDEX}/citations/doi:{doi}"),
    ):
        data = get_json(endpoint)
        if not isinstance(data, list):
            continue
        for item in data:
            field = "cited" if direction == "BACKWARD" else "citing"
            candidate = extract_doi(item.get(field, ""))
            if candidate and candidate != doi:
                result.append((direction, candidate, "OpenCitations"))
    return result


def openalex_work(doi: str):
    url = f"{OPENALEX}/works/https://doi.org/{doi}"
    return get_json(url)


def openalex_collect(doi: str, max_pages: int):
    work = openalex_work(doi)
    if not work or not work.get("id"):
        return [], "OpenAlex DOI lookup failed"

    rows = []
    for ref in work.get("referenced_works", []) or []:
        data = get_json(ref)
        if isinstance(data, dict):
            candidate = extract_doi(data.get("doi", ""))
            if candidate and candidate != doi:
                rows.append(("BACKWARD", candidate, "OpenAlex"))

    cursor = "*"
    for _ in range(max_pages):
        data = get_json(
            f"{OPENALEX}/works",
            params={
                "filter": f"cites:{work['id'].rsplit('/', 1)[-1]}",
                "per-page": 200,
                "cursor": cursor,
            },
        )
        if not data:
            break
        for item in data.get("results", []) or []:
            candidate = extract_doi(item.get("doi", ""))
            if candidate and candidate != doi:
                rows.append(("FORWARD", candidate, "OpenAlex"))
        cursor = data.get("meta", {}).get("next_cursor")
        if not cursor or not data.get("results"):
            break
    return rows, ""


def crossref_collect(doi: str):
    data = get_json(f"{CROSSREF}/works/{doi}")
    if not data or "message" not in data:
        return [], "Crossref DOI lookup failed"

    rows = []
    for ref in data["message"].get("reference", []) or []:
        candidate = extract_doi(ref.get("DOI", ""))
        if candidate and candidate != doi:
            rows.append(("BACKWARD", candidate, "Crossref"))
    return rows, ""


def metadata_crossref(doi: str):
    data = get_json(f"{CROSSREF}/works/{doi}")
    if not data or "message" not in data:
        return {}
    item = data["message"]
    authors = "; ".join(
        " ".join(filter(None, [a.get("given", ""), a.get("family", "")])).strip()
        for a in item.get("author", []) or []
    )
    date_parts = item.get("published-print", {}).get("date-parts") or item.get("published", {}).get("date-parts") or []
    year = str(date_parts[0][0]) if date_parts and date_parts[0] else ""
    return {
        "title": (item.get("title") or [""])[0],
        "authors": authors,
        "year": year,
        "venue": (item.get("container-title") or [""])[0],
    }


def build_existing_indexes(paths):
    dois, titles = set(), set()
    for path in paths:
        if not path.exists():
            continue
        for row in read_csv(path):
            d = norm(row.get("doi", ""))
            t = norm_title(row.get("title", ""))
            if d:
                dois.add(d)
            if t:
                titles.add(t)
    return dois, titles


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Multi-source citation snowballing collector; ACM remains the primary database."
    )
    parser.add_argument("--seed", action="append", help="Only process this record_id; repeat for multiple seeds")
    parser.add_argument("--limit", type=int, default=0, help="Process only the first N selected seeds")
    parser.add_argument("--validate-existing", action="store_true", help="Validate the existing snowballing CSV without calling citation APIs")
    parser.add_argument("--output", help="Override the configured output CSV path; relative paths are resolved from the repository root")
    args = parser.parse_args()

    cfg = load_config()
    seed_path = ROOT / cfg["seed_csv"]
    output_path = (ROOT / args.output) if args.output else (ROOT / cfg["output_csv"])
    seeds = read_csv(seed_path)

    if args.seed:
        wanted = set(args.seed)
        seeds = [s for s in seeds if s.get("record_id") in wanted]
    if args.limit:
        seeds = seeds[:args.limit]

    existing_dois, existing_titles = build_existing_indexes([
        ROOT / cfg["all_records_csv"],
        ROOT / cfg["screened_csv"],
        ROOT / cfg["included_csv"],
    ])

    if args.validate_existing:
        if not output_path.exists():
            print(f"Existing snowballing CSV not found: {output_path}")
            return 1

        rows = read_csv(output_path)
        unique = {}
        for row in rows:
            doi = norm(row.get("doi", ""))
            if not doi:
                continue
            key = (row.get("seed_record_id", ""), row.get("direction", ""), doi)
            unique.setdefault(key, row)

        global_candidates = {}
        for row in unique.values():
            doi = norm(row.get("doi", ""))
            if doi:
                global_candidates.setdefault(doi, row)

        already_primary = 0
        for doi, row in global_candidates.items():
            title = row.get("title", "")
            if doi in existing_dois or norm_title(title) in existing_titles:
                already_primary += 1

        print("\n========================================")
        print("EXISTING SNOWBALLING CSV VALIDATION")
        print("========================================")
        print(f"CSV rows: {len(rows)}")
        print(f"Rows after per-seed/direction DOI deduplication: {len(unique)}")
        print(f"Global unique candidates after DOI deduplication: {len(global_candidates)}")
        print(f"Already matched to primary corpus: {already_primary}")
        print(f"New snowballing candidates requiring V1 screening: {len(global_candidates) - already_primary}")
        return 0

    max_pages = int(cfg.get("openalex_max_pages", 5))
    raw = []
    errors = {}

    for seed in seeds:
        seed_id = seed.get("record_id", "")
        doi = norm(seed.get("doi", ""))
        print(f"\n{seed_id}: {seed.get('title')}")
        if not doi:
            errors[seed_id] = "missing DOI"
            print("  DOI missing; skipped")
            continue

        collected = []
        oc = oc_collect(doi)
        collected.extend(oc)
        print(
            f"  OpenCitations: backward={sum(x[0]=='BACKWARD' for x in oc)}, "
            f"forward={sum(x[0]=='FORWARD' for x in oc)}"
        )

        oa, oa_error = openalex_collect(doi, max_pages)
        collected.extend(oa)
        print(
            f"  OpenAlex:      backward={sum(x[0]=='BACKWARD' for x in oa)}, "
            f"forward={sum(x[0]=='FORWARD' for x in oa)}"
        )

        cr, cr_error = crossref_collect(doi)
        collected.extend(cr)
        print(f"  Crossref:      backward={sum(x[0]=='BACKWARD' for x in cr)}, forward=0")

        if not collected:
            errors[seed_id] = "; ".join(x for x in [oa_error, cr_error, "no citation rows"] if x)
        for direction, candidate, source in collected:
            raw.append({
                "seed_record_id": seed_id,
                "seed_title": seed.get("title", ""),
                "direction": direction,
                "doi": candidate,
                "source": source,
            })
        time.sleep(float(cfg.get("request_delay_seconds", 0.5)))

    unique = {}
    for row in raw:
        key = (row["seed_record_id"], row["direction"], row["doi"])
        if key not in unique:
            unique[key] = row
        else:
            sources = set(unique[key]["source"].split(";"))
            sources.add(row["source"])
            unique[key]["source"] = ";".join(sorted(sources))

    metadata = {}
    for row in unique.values():
        doi = row["doi"]
        if doi not in metadata:
            metadata[doi] = metadata_crossref(doi)
            time.sleep(float(cfg.get("request_delay_seconds", 0.5)))

    fields = [
        "seed_record_id", "seed_title", "direction", "title", "authors", "year",
        "venue", "doi", "url", "source", "already_in_primary_csv",
        "already_in_snowball_csv", "collection_status"
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in unique.values():
            d = row["doi"]
            m = metadata.get(d, {})
            title = m.get("title", "")
            writer.writerow({
                **row,
                "title": title,
                "authors": m.get("authors", ""),
                "year": m.get("year", ""),
                "venue": m.get("venue", ""),
                "url": "https://doi.org/" + d,
                "already_in_primary_csv": "YES" if d in existing_dois or norm_title(title) in existing_titles else "NO",
                "already_in_snowball_csv": "NO",
                "collection_status": "COLLECTED" if title else "COLLECTED_METADATA_MISSING",
            })

    print("\n========================================")
    print("MULTI-SOURCE CITATION SNOWBALLING COMPLETE")
    print("========================================")
    global_candidates = {}
    for row in unique.values():
        doi = norm(row["doi"])
        if doi:
            global_candidates.setdefault(doi, row)

    already_primary = 0
    for doi, row in global_candidates.items():
        title = metadata.get(doi, {}).get("title", "")
        if doi in existing_dois or norm_title(title) in existing_titles:
            already_primary += 1

    new_candidates = len(global_candidates) - already_primary

    print(f"Seeds processed: {len(seeds)}")
    print(f"Collected citation rows after per-seed/direction DOI deduplication: {len(unique)}")
    print(f"Global unique candidates after DOI deduplication: {len(global_candidates)}")
    print(f"Already matched to primary corpus: {already_primary}")
    print(f"New snowballing candidates requiring V1 screening: {new_candidates}")
    print(f"Metadata matched: {sum(1 for row in unique.values() if metadata.get(row['doi'], {}).get('title'))}")
    print(f"Output: {output_path}")
    print(f"Seeds with collection issues: {len(errors)}")
    for seed_id, msg in errors.items():
        print(f"  {seed_id}: {msg}")
    print("\nNo screening decisions were changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
