#!/usr/bin/env python3
"""Trích tập con CodeNet cho pilot GAP 1 (chỉ dùng thư viện chuẩn Python 3.9+).

Chạy trên máy đã tải CodeNet:
  python codenet_subset.py --codenet Project_CodeNet.tar.gz --out codenet_pilot_subset.zip
  python codenet_subset.py --codenet D:/data/Project_CodeNet --out codenet_pilot_subset.zip   (thư mục đã giải nén)

Kết quả là một file zip nhỏ (vài MB) gồm:
  candidates.csv          mọi bài, kèm lý do đạt / không đạt tiêu chí chọn bài
  selected.csv            các bài được chọn ngẫu nhiên (seed cố định) trong số bài đạt
  metadata/pXXXXX.csv     dòng metadata của các submission Java được trích
  problem_descriptions/   mô tả bài đã chọn
  data/pXXXXX/AC/*.java   submission Java Accepted (tối đa --max-ac, lấy ngẫu nhiên theo seed)
  data/pXXXXX/WA/*.java   submission Java Wrong Answer (tối đa --max-wa, lấy ngẫu nhiên theo seed)
Với file tar.gz, script đọc tuần tự hai lượt (không cần giải nén 8 GB ra đĩa), mỗi lượt có thể mất vài chục phút.
"""
import argparse, csv, io, os, random, re, statistics, sys, tarfile, time, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from desc_rules import extract_samples, special_judge_reason  # noqa: E402

RE_META = re.compile(r"(?:^|/)metadata/(p\d{5}|problem_list)\.csv$")
RE_DESC = re.compile(r"(?:^|/)problem_descriptions/(p\d{5})\.html$")
RE_JAVA = re.compile(r"(?:^|/)data/(p\d{5})/Java/(s\d{9})\.java$")


def iter_members(src, want):
    """Duyệt (tên, bytes) của các file mà want(tên) trả về True. Hỗ trợ thư mục và tar.gz."""
    src = Path(src)
    if src.is_dir():
        for root, _dirs, files in os.walk(src):
            for fn in files:
                p = Path(root) / fn
                name = p.relative_to(src).as_posix()
                r = want(name)
                if r == "STOP":
                    return
                if r:
                    yield name, p.read_bytes()
        return
    t0, n = time.time(), 0
    with tarfile.open(src, mode="r|*") as tf:
        for m in tf:
            n += 1
            if n % 500000 == 0:
                print(f"  ... đã đọc {n:,} mục trong {time.time() - t0:,.0f} giây", flush=True)
            if not m.isfile():
                continue
            r = want(m.name)
            if r == "STOP":
                return
            if r:
                yield m.name, tf.extractfile(m).read()


def median(xs):
    return statistics.median(xs) if xs else None


def to_int(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--codenet", required=True, help="Project_CodeNet.tar.gz hoặc thư mục Project_CodeNet")
    ap.add_argument("--out", default="codenet_pilot_subset.zip")
    ap.add_argument("--n", type=int, default=15, help="số bài chọn (12 chính + 3 dự phòng)")
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--min-ac", type=int, default=30)
    ap.add_argument("--min-wa", type=int, default=30)
    ap.add_argument("--max-ac", type=int, default=100)
    ap.add_argument("--max-wa", type=int, default=400)
    ap.add_argument("--max-median-code", type=int, default=2000, help="byte, trung vị code_size của bài AC")
    ap.add_argument("--max-median-cpu", type=int, default=1000, help="ms, trung vị cpu_time của bài AC")
    a = ap.parse_args(argv)

    print("Lượt 1: đọc metadata và mô tả bài ...", flush=True)
    meta_rows, problem_list, descs = {}, {}, {}

    def want1(name):
        return bool(RE_META.search(name) or RE_DESC.search(name))

    for name, data in iter_members(a.codenet, want1):
        text = data.decode("utf-8", errors="replace")
        m = RE_META.search(name)
        if m:
            rows = list(csv.DictReader(io.StringIO(text)))
            if m.group(1) == "problem_list":
                problem_list = {r["id"]: r for r in rows}
            else:
                meta_rows[m.group(1)] = [r for r in rows if r.get("language") == "Java"]
        else:
            descs[RE_DESC.search(name).group(1)] = text
    if not meta_rows:
        raise SystemExit("Không đọc được metadata/pXXXXX.csv. Kiểm tra lại đường dẫn --codenet.")
    print(f"  metadata: {len(meta_rows)} bài; mô tả: {len(descs)} bài", flush=True)

    cand = []
    for pid in sorted(meta_rows):
        rows = meta_rows[pid]
        ac = [r for r in rows if r["status"] == "Accepted"]
        wa = [r for r in rows if r["status"] == "Wrong Answer"]
        page = descs.get(pid, "")
        samples = extract_samples(page) if page else []
        sj = special_judge_reason(page) if page else ""
        med_code = median([v for v in (to_int(r["code_size"]) for r in ac) if v is not None])
        med_cpu = median([v for v in (to_int(r["cpu_time"]) for r in ac) if v is not None and v >= 0])
        reasons = []
        if not page:
            reasons.append("không có mô tả")
        if page and not samples:
            reasons.append("không có Sample Input/Output")
        if sj:
            reasons.append(f"không có đáp án duy nhất ({sj})")
        if len(ac) < a.min_ac:
            reasons.append(f"Java AC < {a.min_ac}")
        if len(wa) < a.min_wa:
            reasons.append(f"Java WA < {a.min_wa}")
        if med_code is None or med_code > a.max_median_code:
            reasons.append(f"trung vị code AC > {a.max_median_code} byte")
        if med_cpu is None or med_cpu > a.max_median_cpu:
            reasons.append(f"trung vị CPU AC > {a.max_median_cpu} ms")
        pl = problem_list.get(pid, {})
        cand.append({"problem_id": pid, "dataset": pl.get("dataset", ""), "name": pl.get("name", ""),
                     "java_ac": len(ac), "java_wa": len(wa), "samples": len(samples),
                     "median_ac_code_size": med_code, "median_ac_cpu_ms": med_cpu,
                     "eligible": "yes" if not reasons else "no", "reasons": "; ".join(reasons)})
    eligible = [c["problem_id"] for c in cand if c["eligible"] == "yes"]
    rng = random.Random(a.seed)
    chosen = rng.sample(eligible, min(a.n, len(eligible)))
    print(f"  bài đạt tiêu chí: {len(eligible)}; chọn ngẫu nhiên {len(chosen)} (seed {a.seed}): {', '.join(chosen)}")

    need = {}
    for pid in chosen:
        rows = meta_rows[pid]
        for status, cap in (("Accepted", a.max_ac), ("Wrong Answer", a.max_wa)):
            sids = sorted(r["submission_id"] for r in rows if r["status"] == status)
            r2 = random.Random(f"{a.seed}-{pid}-{status}")
            for sid in (r2.sample(sids, cap) if len(sids) > cap else sids):
                need[(pid, sid)] = "AC" if status == "Accepted" else "WA"
    print(f"Lượt 2: trích {len(need)} file Java ...", flush=True)
    remaining = set(need)
    got = {}

    def want2(name):
        if not remaining:
            return "STOP"
        m = RE_JAVA.search(name)
        return bool(m and (m.group(1), m.group(2)) in remaining)

    for name, data in iter_members(a.codenet, want2):
        m = RE_JAVA.search(name)
        key = (m.group(1), m.group(2))
        got[key] = data
        remaining.discard(key)
    print(f"  đã trích {len(got)}/{len(need)} file", flush=True)

    with zipfile.ZipFile(a.out, "w", zipfile.ZIP_DEFLATED) as z:
        def put_csv(path, rows, fields):
            buf = io.StringIO()
            w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
            z.writestr(path, buf.getvalue())
        put_csv("candidates.csv", cand, list(cand[0].keys()))
        by_id = {c["problem_id"]: c for c in cand}
        put_csv("selected.csv", [dict(by_id[p], order=i + 1) for i, p in enumerate(chosen)],
                list(cand[0].keys()) + ["order"])
        for pid in chosen:
            rows = [r for r in meta_rows[pid] if (pid, r["submission_id"]) in need]
            if rows:
                put_csv(f"metadata/{pid}.csv", rows, list(rows[0].keys()))
            if pid in descs:
                z.writestr(f"problem_descriptions/{pid}.html", descs[pid])
        for (pid, sid), data in sorted(got.items()):
            z.writestr(f"data/{pid}/{need[(pid, sid)]}/{sid}.java", data)
        z.writestr("README.txt", f"Tạo bởi codenet_subset.py, seed={a.seed}, tham số={vars(a)}\n")
    print(f"Xong: {a.out} ({os.path.getsize(a.out) / 1e6:.1f} MB). Gửi file này lên để chạy pilot.")


if __name__ == "__main__":
    main()
