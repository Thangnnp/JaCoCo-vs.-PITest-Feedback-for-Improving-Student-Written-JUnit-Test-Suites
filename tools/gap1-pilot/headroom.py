#!/usr/bin/env python3
"""Độ nhạy của thước đo: tỉ lệ phát hiện WA khi thêm k đầu vào bổ sung (chọn ngẫu nhiên từ tập đầu vào
do nhóm nghiên cứu viết) vào bộ đầu vào sample. Đọc pXXXXX_wa_runs.csv của wa_pilot.py.
  python headroom.py results --ks 1 2 3 5 --draws 2000 --seed 2026
"""
import argparse, csv, random, statistics
from collections import defaultdict
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("results"); ap.add_argument("--ks", type=int, nargs="*", default=[1, 2, 3, 5])
ap.add_argument("--draws", type=int, default=2000); ap.add_argument("--seed", type=int, default=2026)
ap.add_argument("--problems", nargs="*")
a = ap.parse_args()
print("| Bài | WA | Sample | " + " | ".join(f"+{k} đầu vào (TB [P10–P90])" for k in a.ks) + " | + toàn bộ |")
print("|---|---|---|" + "---|" * len(a.ks) + "---|")
for f in sorted(Path(a.results).glob("p*_wa_runs.csv")):
    pid = f.name[:6]
    if a.problems and pid not in a.problems:
        continue
    det, origin = defaultdict(set), {}
    was = set()
    for r in csv.DictReader(open(f, encoding="utf-8")):
        i = int(r["input_index"]); origin[i] = r["input_origin"]; was.add(r["submission_id"])
        if r["status"] == "MISMATCH":
            det[i].add(r["submission_id"])
    n = len(was)
    samp = [i for i in origin if origin[i] == "sample"]
    extra = [i for i in origin if origin[i] == "extra"]
    base = set().union(*(det[i] for i in samp)) if samp else set()
    rng = random.Random(f"{a.seed}-{pid}")
    cells = []
    for k in a.ks:
        if k > len(extra):
            cells.append("—"); continue
        vals = []
        for _ in range(a.draws):
            s = base.union(*(det[i] for i in rng.sample(extra, k)))
            vals.append(len(s) / n)
        vals.sort()
        cells.append(f"{statistics.mean(vals):.2f} [{vals[int(.1*len(vals))]:.2f}–{vals[int(.9*len(vals))-1]:.2f}]")
    full = base.union(*(det[i] for i in extra)) if extra else base
    print(f"| {pid} | {n} | {len(base)/n:.2f} | " + " | ".join(cells) + f" | {len(full)/n:.2f} ({len(extra)}) |")
