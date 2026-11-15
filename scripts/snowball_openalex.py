import csv
import os
import re
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote

import requests

REPO_ROOT = Path(__file__).resolve().parents[1]
SLR_DIR = REPO_ROOT / "Ngo Minh Tien" / "SLR"
SEED_CSV = SLR_DIR / "03_final_included.csv"
OUT_CSV = SLR_DIR / "snowballing-candidates.csv"

BASE = "https://dl.acm.org"
TIMEOUT = 30
SLEEP = 0.4

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/154 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
})


def normalize_doi(value):
    if not value:
        return ""
    value = value.strip()
    value = re.sub(r"^https?://doi.org/", "", value, flags=re.I)
    value = re.sub(r"^https?://dl.acm.org/doi/", "", value, flags=re.I)
    value = re.sub(r"^doi:\\s*", "", value, flags=re.I)
    return value.strip().lower()


def get(url):
    for attempt in range(5):
        response = SESSION.get(url, timeout=TIMEOUT)
        if response.status_code in (429, 503):
            wait = min(30, 2 ** attempt)
            print(f"  HTTP {response.status_code}; waiting {wait}s...")
            time.sleep(wait)
            continue
        response.raise_for_status()
        return response
    raise RuntimeError(f"ACM request failed: {url}")


class ACMParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dois = set()
        self.cited_by_ajax = None

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        href = d.get("href", "")
        ajax = d.get("data-ajaxurl", "")

        if ajax.startswith("/action/ajaxShowCitedBy"):
            self.cited_by_ajax = ajax

        if "/doi/" in href:
            marker = href.find("/doi/")
            value = href[marker + 5:]
            value = re.split(r'[?#"<>\s]', value, maxsplit=1)[0]
            if value.startswith("10."):
                self.dois.add(normalize_doi(value))


def fetch_seed_page(doi):
    url = BASE + "/doi/" + quote(doi, safe="")
    return get(url)


def fetch_backward(doi):
    response = fetch_seed_page(doi)
    parser = ACMParser()
    parser.feed(response.text)
    return parser.dois, parser.cited_by_ajax


def fetch_forward(ajax_path):
    if not ajax_path:
        return set()

    response = get(BASE + ajax_path)
    parser = ACMParser()
    parser.feed(response.text)
    return parser.dois


def extract_metadata(doi):
    response = fetch_seed_page(doi)
    text = response.text

    def meta(name):
        pattern = '<meta name="' + re.escape(name) + '" content="([^"]*)"'
        match = re.search(pattern, text, re.I)
        return match.group(1).strip() if match else ""

    authors = []
    for match in re.finditer(
        r'<meta name="citation_author" content="([^"]*)"',
        text,
        re.I,
    ):
        authors.append(match.group(1).strip())

    return {
        "title": meta("citation_title"),
        "authors": "; ".join(authors),
        "year": meta("citation_publication_date")[:4],
        "venue": meta("citation_conference_title") or meta("citation_journal_title"),
        "doi": doi,
        "url": BASE + "/doi/" + quote(doi, safe=""),
    }


def main():
    if not SEED_CSV.exists():
        raise FileNotFoundError(SEED_CSV)

    with SEED_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        seeds = list(csv.DictReader(f))

    print(f"Seeds: {len(seeds)}")

    candidates = {}
    unresolved = []

    for i, seed in enumerate(seeds, 1):
        seed_id = seed.get("record_id", "")
        seed_title = seed.get("title", "")
        doi = normalize_doi(seed.get("doi", ""))

        print(f"[{i}/{len(seeds)}] {seed_id}: {seed_title}")

        if not doi:
            unresolved.append((seed_id, "missing DOI"))
            continue

        try:
            backward, ajax = fetch_backward(doi)
            backward.discard(doi)
            print(f"  ACM backward references: {len(backward)}")
        except Exception as e:
            print(f"  ACM backward failed: {e}")
            backward, ajax = set(), None

        try:
            forward = fetch_forward(ajax)
            forward.discard(doi)
            print(f"  ACM forward citations: {len(forward)}")
        except Exception as e:
            print(f"  ACM forward failed: {e}")
            forward = set()

        for direction, dois in (("backward", backward), ("forward", forward)):
            for candidate_doi in sorted(dois):
                key = (direction, candidate_doi)
                if key not in candidates:
                    candidates[key] = {
                        "seed_record_id": seed_id,
                        "seed_title": seed_title,
                        "direction": direction,
                        "doi": candidate_doi,
                    }

        time.sleep(SLEEP)

    print()
    print(f"Unique ACM citation candidates: {len(candidates)}")
    print("Fetching ACM metadata...")

    rows = []
    for n, row in enumerate(candidates.values(), 1):
        try:
            metadata = extract_metadata(row["doi"])
        except Exception as e:
            print(f"  metadata failed [{n}/{len(candidates)}] {row['doi']}: {e}")
            metadata = {
                "title": "",
                "authors": "",
                "year": "",
                "venue": "",
                "doi": row["doi"],
                "url": BASE + "/doi/" + quote(row["doi"], safe=""),
            }

        row.update(metadata)
        row["source"] = "ACM Digital Library"
        rows.append(row)

        if n % 50 == 0:
            print(f"  metadata: {n}/{len(candidates)}")
        time.sleep(SLEEP)

    fields = [
        "seed_record_id",
        "seed_title",
        "direction",
        "title",
        "authors",
        "year",
        "venue",
        "doi",
        "url",
        "source",
    ]

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print()
    print(f"Unique ACM candidates written: {len(rows)}")
    print(f"Output: {OUT_CSV}")

    if unresolved:
        print("Unresolved seeds:")
        for item in unresolved:
            print("  ", item)


if __name__ == "__main__":
    main()
