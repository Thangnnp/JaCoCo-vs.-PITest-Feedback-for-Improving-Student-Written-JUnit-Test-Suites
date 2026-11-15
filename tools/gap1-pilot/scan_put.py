#!/usr/bin/env python3
"""Tìm chương trình kiểm thử (PUT) mà cả hai loại phản hồi đều còn điều để báo trên bộ test baseline.

Tiêu chí (công khai, áp dụng như nhau cho mọi bài):
  (1) bài AC biên dịch được, không gọi System.exit;
  (2) chạy qua Judge.run (Judge.java của bộ công cụ, mọi đầu vào trong một JVM) cho output giống hệt PUT hiện tại
      chạy như tiến trình, trên toàn bộ tập đầu vào tham chiếu đã khoá;
  (3) với bộ baseline (SampleTest), JaCoCo còn ít nhất 1 nhánh chưa phủ VÀ PITest còn ít nhất 1 mutant SURVIVED;
  (4) ít nhất 1 nhánh chưa phủ ở baseline được bộ test tham chiếu (mọi đầu vào tham chiếu, expected = oracle) phủ;
  (5) bộ test tham chiếu diệt được ít nhất 1 mutant sống sót ở baseline.
Ghi thêm số nhánh/mutant trong báo cáo baseline mà tập tham chiếu cũng chưa phủ/diệt được ("chưa phủ/diệt được bằng
tập tham chiếu"). Con số này KHÔNG có nghĩa là nhánh không đạt được hay mutant tương đương: tập tham chiếu hữu hạn,
nên một mục chưa phủ/diệt được có thể vẫn phủ/diệt được bằng đầu vào khác. Chỉ kết luận "không đạt được" hoặc
"tương đương" cho từng mục cụ thể khi có một kiểm tra riêng, có căn cứ (lập luận trên mã, ghi rõ người kiểm và lý do).
Bản trước của tiêu chí (4) đòi tập tham chiếu phủ 100% chương trình; không ứng viên nào trong 30 bài AC của p02263 đạt,
vì sau Sample hầu như luôn còn nhánh mà tập tham chiếu chưa phủ được.
Duyệt các bài AC theo thứ tự ngẫu nhiên cố định (seed), dừng ở ứng viên đầu tiên đạt cả ba.
  python scan_put.py --subset SUBSET --frozen frozen --lib lib --pid p02263 --baseline SampleTest.java --out scan --max 20
"""
import argparse, json, random, re, subprocess, sys, shutil
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wa_pilot import ENV, judge_equivalence, run_prog, norm_out  # noqa: E402


def mutants(d):
    """{(lớp, phương thức, dòng, mutator, chỉ số): trạng thái} từ mutations.xml của feedback.py."""
    f = Path(d) / "pit" / "mutations.xml"
    if not f.exists():
        return {}
    import xml.etree.ElementTree as ET
    res = {}
    for m in ET.parse(f).getroot().findall("mutation"):
        key = (m.findtext("mutatedClass"), m.findtext("mutatedMethod"), m.findtext("methodDescription"),
               m.findtext("lineNumber"), m.findtext("mutator"), m.findtext("indexes") or m.findtext("index"))
        res[key] = m.get("status")
    return res


def line_mb(d):
    """{dòng: số nhánh chưa phủ} từ jacoco.xml của feedback.py."""
    import xml.etree.ElementTree as ET
    f = Path(d) / "jacoco.xml"
    if not f.exists():
        return {}
    return {int(l.get("nr")): int(l.get("mb")) for l in ET.parse(f).getroot().iter("line") if int(l.get("mb"))}


def make_ref_test(path, inputs, outputs):
    """Bộ test tham chiếu: mỗi đầu vào tham chiếu một test, expected = oracle."""
    def lit(x):
        return '"' + x.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'
    body = "".join(f"    @Test void r{i:03d}() {{ assertEquals({lit(o)}, Judge.run({lit(s)})); }}\n"
                   for i, (s, o) in enumerate(zip(inputs, outputs)))
    path.write_text("package codenet;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\n"
                    "import org.junit.jupiter.api.Test;\n\nclass RefTest {\n" + body + "}\n", encoding="utf-8")


def compile_plain(src, d):
    d.mkdir(parents=True, exist_ok=True)
    (d / "Main.java").write_text(src, encoding="utf-8")
    return subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-d", str(d), str(d / "Main.java")],
                          env=ENV, capture_output=True).returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subset", required=True); ap.add_argument("--frozen", required=True)
    ap.add_argument("--lib", required=True); ap.add_argument("--pid", required=True)
    ap.add_argument("--baseline", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--max", type=int, default=20); ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--quick", action="store_true",
                    help="sàng lọc nhanh: chỉ xét điều kiện 1–3, đếm số ứng viên đạt (chưa cần tập tham chiếu đầy đủ)")
    a = ap.parse_args()
    sub, out = Path(a.subset), Path(a.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    idx = json.loads((Path(a.frozen) / "frozen_index.json").read_text(encoding="utf-8"))["problems"][a.pid]
    ref = [f.read_text(encoding="utf-8") for f in sorted((Path(a.frozen) / "reference_inputs" / a.pid).glob("*.in"))]
    cur = (sub / "data" / a.pid / "AC" / f"{idx['put']}.java").read_text(encoding="utf-8", errors="replace")
    cdir = out / "_cur"
    compile_plain(cur, cdir)
    oracle = [run_prog(str(cdir), s, 8)["out"] for s in ref]
    ref_test = out / "RefTest.java"
    make_ref_test(ref_test, ref, oracle)
    cands = sorted(p.stem for p in (sub / "data" / a.pid / "AC").glob("*.java"))
    random.Random(f"{a.seed}-{a.pid}-put").shuffle(cands)
    log = []
    for sid in cands[:a.max]:
        src = (sub / "data" / a.pid / "AC" / f"{sid}.java").read_text(encoding="utf-8", errors="replace")
        rec = {"submission": sid}
        if re.search(r"System\s*\.\s*exit", src):
            rec["ket_qua"] = "có System.exit"; log.append(rec); continue
        same, tot, note = judge_equivalence(src, ref, oracle, out, HERE / "Judge.java")
        if same != tot:
            rec["ket_qua"] = f"Judge.run lệch {same}/{tot}"; log.append(rec); continue
        fb = {}
        for tool in ("jacoco", "pitest"):
            r = subprocess.run([sys.executable, str(HERE / "feedback.py"), "--tool", tool, "--lib", a.lib, "--subset", a.subset,
                                "--pid", a.pid, "--put", sid, "--test", a.baseline, "--out", str(out / sid / tool)],
                               env=ENV, capture_output=True, text=True)
            fb[tool] = json.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else {"loi": r.stderr[-300:]}
        j, p = fb["jacoco"], fb["pitest"]
        base_ok = j.get("dong_con_nhanh_chua_phu", 0) >= 1 and p.get("trang_thai", {}).get("SURVIVED", 0) >= 1
        if a.quick:
            rec["ket_qua"] = "ĐẠT 1–3" if base_ok else "phản hồi rỗng ở " + (
                "JaCoCo" if j.get("dong_con_nhanh_chua_phu", 0) < 1 else "PITest")
            log.append(rec)
            if sum(1 for r in log if r["ket_qua"] == "ĐẠT 1–3") >= 3:
                break
            continue
        if base_ok:  # (4), (5): chạy bộ test tham chiếu
            for tool in ("jacoco", "pitest"):
                r = subprocess.run([sys.executable, str(HERE / "feedback.py"), "--tool", tool, "--lib", a.lib, "--subset",
                                    a.subset, "--pid", a.pid, "--put", sid, "--test", str(ref_test), "--out",
                                    str(out / sid / f"ref_{tool}")], env=ENV, capture_output=True, text=True)
                fb["ref_" + tool] = json.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else {"loi": r.stderr[-300:]}
            rj = fb["ref_jacoco"]
            mb0, mb1 = line_mb(out / sid / "jacoco"), line_mb(out / sid / "ref_jacoco")
            phu_duoc = sum(max(0, mb0[n] - mb1.get(n, 0)) for n in mb0)
            chua_phu = sum(mb0.values()) - phu_duoc
            surv = {m for m, st in mutants(out / sid / "pitest").items() if st == "SURVIVED"}
            ref_m = mutants(out / sid / "ref_pitest")
            diet_duoc = sum(1 for m in surv if ref_m.get(m) in ("KILLED", "TIMED_OUT", "MEMORY_ERROR", "RUN_ERROR"))
            rec.update({"tham_chieu_nhanh": f"{rj.get('branch_covered')}/{rj.get('branch_total')}",
                        "nhanh_bao_cao_tham_chieu_phu_duoc": phu_duoc,
                        "nhanh_bao_cao_chua_phu_bang_tham_chieu": chua_phu,
                        "mutant_song_sot_tham_chieu_diet_duoc": diet_duoc,
                        "mutant_song_sot_chua_diet_bang_tham_chieu": len(surv) - diet_duoc})
        rec.update({"nhanh": f"{j.get('branch_covered')}/{j.get('branch_total')}",
                    "mutant_song_sot": p.get("trang_thai", {}).get("SURVIVED", 0),
                    "mutant": f"{p.get('mutants_killed')}/{p.get('mutants_total')}"})
        if not base_ok:
            rec["ket_qua"] = "phản hồi rỗng ở " + ("JaCoCo" if j.get("dong_con_nhanh_chua_phu", 0) < 1 else "PITest")
        elif phu_duoc < 1:
            rec["ket_qua"] = "mọi nhánh JaCoCo báo đều chưa phủ được bằng tập tham chiếu"
        elif diet_duoc < 1:
            rec["ket_qua"] = "mọi mutant sống sót đều chưa diệt được bằng tập tham chiếu"
        else:
            rec["ket_qua"] = "ĐẠT"
        ok = rec["ket_qua"] == "ĐẠT"
        log.append(rec)
        if ok:
            break
    res = {"problem_id": a.pid, "put_hien_tai": idx["put"], "so_ung_vien_da_xet": len(log),
           "put_dat": next((r["submission"] for r in log if r["ket_qua"] == "ĐẠT"), None),
           "so_dat_1_3": sum(1 for r in log if r["ket_qua"] == "ĐẠT 1–3"), "nhat_ky": log}
    (out / f"{a.pid}_scan.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("problem_id", "so_ung_vien_da_xet", "put_dat", "so_dat_1_3")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
