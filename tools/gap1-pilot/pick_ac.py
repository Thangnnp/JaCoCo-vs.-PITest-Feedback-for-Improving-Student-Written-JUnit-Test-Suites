#!/usr/bin/env python3
"""Chọn các bài AC ĐỘC LẬP dùng để đối chiếu bộ test của sinh viên (kiểm chứng bộ chấm, §5.9).

Một test pass trên PUT chưa chắc đúng với đề: PUT có thể có một lựa chọn riêng mà đề không bắt buộc
(vd. đề chấp nhận nhiều output, PUT in một trong số đó). Vì vậy mỗi bộ test còn được chạy trên K bài AC khác.

Tiêu chí chọn (công khai, áp dụng như nhau cho mọi bài), duyệt bài AC theo thứ tự ngẫu nhiên cố định (seed):
  (1) khác submission với PUT, và user_id (trong metadata CodeNet) khác PUT và khác các bài đã chọn
      (khác tác giả, để lựa chọn cài đặt không trùng nhau);
  (2) không gọi System.exit;
  (3) biên dịch được, chạy như tiến trình cho output giống PUT (sau chuẩn hoá) trên MỌI đầu vào tham chiếu đã khoá,
      mỗi lần chạy không quá --limit giây (mặc định 4, bằng giới hạn mỗi test của junit_eval.py), để test không bị
      coi là bất đồng chỉ vì bài AC chạy chậm.
Dừng khi đủ K bài. Kết quả ghi vào JSON và được khoá (SHA-256) cùng manifest trước khi tuyển mẫu chính.

  python pick_ac.py --subset SUBSET --frozen frozen --pid p03274 --k 4 --out frozen/ac_check/p03274.json
"""
import argparse, csv, hashlib, json, random, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wa_pilot import ENV, run_prog, strip_comments  # noqa: E402


def compile_plain(src, d):
    d.mkdir(parents=True, exist_ok=True)
    body = re.sub(r"^\s*package\s+[\w.]+\s*;\s*", "", src, count=1, flags=re.M)
    (d / "Main.java").write_text(body, encoding="utf-8")
    return subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-d", str(d), str(d / "Main.java")],
                          env=ENV, capture_output=True).returncode == 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--subset", required=True); ap.add_argument("--frozen", required=True)
    ap.add_argument("--pid", required=True); ap.add_argument("--put", default=None, help="mặc định: PUT trong frozen_index.json")
    ap.add_argument("--k", type=int, default=4); ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--max", type=int, default=60, help="số ứng viên tối đa được xét")
    ap.add_argument("--limit", type=float, default=4.0, help="giây tối đa mỗi lần chạy của bài AC đối chiếu")
    ap.add_argument("--out", required=True); ap.add_argument("--work", default=None)
    a = ap.parse_args(argv)
    sub, frozen = Path(a.subset), Path(a.frozen)
    put = a.put or json.loads((frozen / "frozen_index.json").read_text(encoding="utf-8"))["problems"][a.pid]["put"]
    meta = {r["submission_id"]: r for r in csv.DictReader(open(sub / "metadata" / f"{a.pid}.csv", encoding="utf-8"))}
    ref_files = sorted((frozen / "reference_inputs" / a.pid).glob("*.in"))
    ref = [f.read_text(encoding="utf-8") for f in ref_files]
    work = Path(a.work or Path(a.out).with_suffix("")).resolve() / "_work"
    acdir = sub / "data" / a.pid / "AC"
    put_src = (acdir / f"{put}.java").read_text(encoding="utf-8", errors="replace")
    if not compile_plain(put_src, work / put):
        raise SystemExit("PUT không biên dịch được")
    put_out = [run_prog(str(work / put), s, 8) for s in ref]
    cands = sorted(p.stem for p in acdir.glob("*.java") if p.stem != put)
    random.Random(f"{a.seed}-{a.pid}-ac-check").shuffle(cands)
    users = {meta.get(put, {}).get("user_id")}
    chosen, log = [], []
    for sid in cands[:a.max]:
        if len(chosen) >= a.k:
            break
        uid = meta.get(sid, {}).get("user_id")
        rec = {"submission": sid, "user_id": uid}
        src = (acdir / f"{sid}.java").read_text(encoding="utf-8", errors="replace")
        if not uid or uid in users:
            rec["ket_qua"] = "trùng tác giả với PUT hoặc bài đã chọn" if uid else "thiếu user_id"
        elif re.search(r"System\s*\.\s*exit", strip_comments(src)):
            rec["ket_qua"] = "có System.exit"
        elif not compile_plain(src, work / sid):
            rec["ket_qua"] = "không biên dịch được"
        else:
            runs = [run_prog(str(work / sid), s, 8) for s in ref]
            diff = [ref_files[i].name for i, r in enumerate(runs) if r["status"] != "OK" or r["out"] != put_out[i]["out"]]
            slow = max((r["sec"] for r in runs), default=0)
            if not diff and slow > a.limit:
                rec["ket_qua"] = f"chạy chậm: {slow:.1f} giây > {a.limit:g}"
            elif diff:
                rec["ket_qua"] = f"khác PUT trên {len(diff)}/{len(ref)} đầu vào tham chiếu"; rec["vi_du"] = diff[:3]
            else:
                rec["ket_qua"] = "CHỌN"; chosen.append(sid); users.add(uid)
        log.append(rec)
    res = {"problem_id": a.pid, "put": put, "put_user_id": meta.get(put, {}).get("user_id"), "k": a.k, "seed": a.seed,
           "so_dau_vao_tham_chieu": len(ref), "ac_doi_chieu": chosen, "du_k": len(chosen) >= a.k,
           "sha256_nguon": {s: hashlib.sha256((acdir / f"{s}.java").read_bytes()).hexdigest() for s in chosen},
           "nhat_ky": log}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("problem_id", "put", "ac_doi_chieu", "du_k")}, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main()
