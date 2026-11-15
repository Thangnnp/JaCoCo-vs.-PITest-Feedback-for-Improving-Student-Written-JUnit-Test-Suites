#!/usr/bin/env python3
"""Khoá dữ liệu đánh giá trước nghiên cứu chính.
 1. Tập WA đánh giá: chép pXXXXX_heldout_manifest.csv vào thư mục khoá, ghi SHA-256 của từng file.
 2. Tập đầu vào tham chiếu CỐ ĐỊNH (chỉ dùng cho phân tích mô tả nhóm hành vi, không dùng để chấm phiên):
    Sample Input + đầu vào do nhóm nghiên cứu viết, đã qua kiểm ràng buộc, theo đúng thứ tự wa_pilot.py dùng.
  python freeze.py --subset SUBSET --results RESULTS --extra EXTRA --out frozen --problems p02263 ...
"""
import argparse, csv, hashlib, json, shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from desc_rules import extract_samples  # noqa: E402
from validators import validate  # noqa: E402
from wa_pilot import norm_in  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--subset", required=True); ap.add_argument("--results", required=True)
ap.add_argument("--extra", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--problems", nargs="+", required=True)
a = ap.parse_args()
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
index = {"problems": {}}
for pid in a.problems:
    rep = json.loads((Path(a.results) / f"{pid}_report.json").read_text(encoding="utf-8"))
    man = Path(a.results) / f"{pid}_heldout_manifest.csv"
    shutil.copy(man, out / man.name)
    rows = list(csv.DictReader(open(man, encoding="utf-8")))
    page = (Path(a.subset) / "problem_descriptions" / f"{pid}.html").read_text(encoding="utf-8", errors="replace")
    inputs = [norm_in(s) for s, _ in extract_samples(page)]
    for f in sorted((Path(a.extra) / pid).glob("*.in")):
        e = norm_in(f.read_text(encoding="utf-8"))
        if e not in inputs and not validate(pid, e):
            inputs.append(e)
    assert len(inputs) == rep["oracle"]["dau_vao_hop_le"], (pid, len(inputs), rep["oracle"]["dau_vao_hop_le"])
    d = out / "reference_inputs" / pid; d.mkdir(parents=True, exist_ok=True)
    for i, s in enumerate(inputs):
        (d / f"{i:03d}.in").write_text(s, encoding="utf-8")
    index["problems"][pid] = {
        "put": rep["chuong_trinh_kiem_thu"]["submission"],
        "WA_danh_gia": sum(1 for r in rows if r["trang_thai"] == "đánh giá"),
        "manifest_sha256": hashlib.sha256(man.read_bytes()).hexdigest(),
        "reference_inputs": len(inputs),
        "reference_inputs_sha256": hashlib.sha256("".join(inputs).encode()).hexdigest(),
        "nhom_hanh_vi_tren_tap_tham_chieu": rep["nhom_hanh_vi_WA"]}
(out / "frozen_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({p: (v["WA_danh_gia"], v["reference_inputs"]) for p, v in index["problems"].items()}))
