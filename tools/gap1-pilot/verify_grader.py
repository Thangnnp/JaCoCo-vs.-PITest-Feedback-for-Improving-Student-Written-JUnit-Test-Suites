#!/usr/bin/env python3
"""Kiểm chứng bộ chấm (junit_eval.py + pick_ac.py) trên một bài giả lập trước khi tuyển mẫu chính.

Bài giả lập pFIX01. Đề: dòng 1 là N (1 ≤ N ≤ 10), dòng 2 là N số nguyên a_i (−100 ≤ a_i ≤ 100).
In giá trị lớn nhất M và MỘT chỉ số i (đánh từ 1) sao cho a_i = M; nếu có nhiều chỉ số, in chỉ số nào cũng được.
Ý "chỉ số nào cũng được" là cố ý: PUT in chỉ số đầu tiên, một bài AC khác in chỉ số cuối cùng, nên một test
chốt chỉ số khi có giá trị trùng thì pass trên PUT nhưng sai so với đề.

Script dựng: 8 bài AC (5 đạt tiêu chí đối chiếu + 3 bài phải bị loại), 10 bài WA mỗi bài một kiểu lỗi/hành vi,
6 bộ JUnit, mỗi bộ một tình huống. Với mỗi bộ, KỲ VỌNG được ghi trước (EXPECT) rồi so với kết quả thật.
Kết quả ghi vào grader_check/report.md và report.json; trả mã lỗi 1 nếu có bất kỳ chỗ nào lệch kỳ vọng.

  python verify_grader.py --out grader_check [--junit-api lib/junit-platform-console-standalone-1.10.2.jar]
"""
import argparse, csv, hashlib, json, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pick_ac, junit_eval  # noqa: E402

PID = "pFIX01"
READ = "java.util.Scanner sc = new java.util.Scanner(System.in); int n = sc.nextInt(); int[] a = new int[n];\n" \
       "        for (int i = 0; i < n; i++) a[i] = sc.nextInt();\n"

# ----------------------------------------------------------------------------- chương trình
# (mã, user_id, nguồn). PUT = s_put. Ba bài cuối phải bị pick_ac loại.
AC = {
    "s_put": ("u01", "public class Main { public static void main(String[] x) {\n        " + READ +
              "        int b = 0; for (int i = 1; i < n; i++) if (a[i] > a[b]) b = i;\n"
              "        System.out.println(a[b] + \" \" + (b + 1)); } }\n"),
    # chỉ số CUỐI khi trùng (đề cho phép)
    "s_ac_last": ("u02", "import java.io.*; import java.util.*;\npublic class Main { public static void main(String[] x) throws IOException {\n"
                  "        BufferedReader r = new BufferedReader(new InputStreamReader(System.in)); int n = Integer.parseInt(r.readLine().trim());\n"
                  "        StringTokenizer t = new StringTokenizer(r.readLine()); int[] a = new int[n]; for (int i = 0; i < n; i++) a[i] = Integer.parseInt(t.nextToken());\n"
                  "        int b = 0; for (int i = 1; i < n; i++) if (a[i] >= a[b]) b = i;\n"
                  "        System.out.println(a[b] + \" \" + (b + 1)); } }\n"),
    # lớp Main không public, PrintWriter có flush
    "s_ac_nonpub": ("u03", "import java.io.*;\nclass Main { public static void main(String[] x) {\n        " + READ +
                    "        PrintWriter w = new PrintWriter(System.out); int b = 0; for (int i = n - 1; i >= 0; i--) if (a[i] >= a[b]) b = i;\n"
                    "        w.println(a[b] + \" \" + (b + 1)); w.flush(); } }\n"),
    # tính trong luồng riêng không phải daemon
    "s_ac_thread": ("u04", "public class Main { public static void main(String[] x) { new Thread(() -> {\n        " + READ +
                    "        int b = 0; for (int i = 1; i < n; i++) if (a[i] > a[b]) b = i;\n"
                    "        System.out.println(a[b] + \" \" + (b + 1)); }).start(); } }\n"),
    "s_ac_stream": ("u05", "import java.util.stream.*;\npublic class Main { public static void main(String[] x) {\n        " + READ +
                    "        int m = IntStream.of(a).max().getAsInt(); int b = IntStream.range(0, n).filter(i -> a[i] == m).findFirst().getAsInt();\n"
                    "        System.out.println(m + \" \" + (b + 1)); } }\n"),
    # phải bị loại: cùng tác giả với PUT
    "s_ac_sameuser": ("u01", "public class Main { public static void main(String[] x) {\n        " + READ +
                      "        int b = 0; for (int i = 0; i < n; i++) if (a[i] > a[b]) b = i;\n"
                      "        System.out.println(a[b] + \" \" + (b + 1)); } }\n"),
    # phải bị loại: gọi System.exit
    "s_ac_exit": ("u06", "public class Main { public static void main(String[] x) {\n        " + READ +
                  "        int b = 0; for (int i = 1; i < n; i++) if (a[i] > a[b]) b = i;\n"
                  "        System.out.println(a[b] + \" \" + (b + 1)); System.exit(0); } }\n"),
    # phải bị loại: nhãn AC nhưng khác PUT trên đầu vào tham chiếu (in chỉ số đánh từ 0)
    "s_ac_mislabel": ("u07", "public class Main { public static void main(String[] x) {\n        " + READ +
                      "        int b = 0; for (int i = 1; i < n; i++) if (a[i] > a[b]) b = i;\n"
                      "        System.out.println(a[b] + \" \" + b); } }\n"),
}
WA = {
    "w_neg": "khởi tạo max = 0: sai khi mọi số âm",
    "w_last": "bỏ sót phần tử cuối (off-by-one)",
    "w_throw1": "ném ArrayIndexOutOfBounds khi N = 1",
    "w_loop": "lặp vô hạn khi hai số liền kề bằng nhau",
    "w_exit": "gọi System.exit(0) trước khi in khi N = 1",
    "w_static": "biến static đếm số lần gọi main: đúng nếu mỗi lần chạy là một tiến trình mới",
    "w_thread": "tính trong luồng riêng, in chỉ số đánh từ 0",
    "w_noflush": "logic đúng nhưng PrintWriter không flush: không in gì",
    "w_nonpub": "lớp Main không public, N chẵn thì in giá trị nhỏ nhất",
    "w_tie": "in chỉ số cuối khi trùng (đề cho phép) và đúng ở mọi chỗ khác",
}
LOOP_BEST = "        int b = 0; for (int i = 1; i < n; i++) if (a[i] > a[b]) b = i;\n"
WA_SRC = {
    "w_neg": "public class Main { public static void main(String[] x) {\n        " + READ +
             "        int m = 0, b = -1; for (int i = 0; i < n; i++) if (a[i] > m) { m = a[i]; b = i; }\n"
             "        System.out.println(m + \" \" + (b + 1)); } }\n",
    "w_last": "public class Main { public static void main(String[] x) {\n        " + READ +
              "        int b = 0; for (int i = 1; i < n - 1; i++) if (a[i] > a[b]) b = i;\n"
              "        System.out.println(a[b] + \" \" + (b + 1)); } }\n",
    "w_throw1": "public class Main { public static void main(String[] x) {\n        " + READ +
                "        int b = a[1] > a[0] ? 1 : 0; for (int i = 2; i < n; i++) if (a[i] > a[b]) b = i;\n"
                "        System.out.println(a[b] + \" \" + (b + 1)); } }\n",
    "w_loop": "public class Main { public static void main(String[] x) {\n        " + READ +
              "        int b = 0, i = 1; while (i < n) { if (a[i] == a[i - 1]) continue; if (a[i] > a[b]) b = i; i++; }\n"
              "        System.out.println(a[b] + \" \" + (b + 1)); } }\n",
    "w_exit": "public class Main { public static void main(String[] x) {\n        " + READ +
              "        if (n == 1) System.exit(0);\n" + LOOP_BEST +
              "        System.out.println(a[b] + \" \" + (b + 1)); } }\n",
    "w_static": "public class Main { static int calls = 0; public static void main(String[] x) {\n        " + READ +
                LOOP_BEST + "        calls++; System.out.println(a[b] + \" \" + (b + calls)); } }\n",
    "w_thread": "public class Main { public static void main(String[] x) { new Thread(() -> {\n        " + READ +
                LOOP_BEST + "        System.out.println(a[b] + \" \" + b); }).start(); } }\n",
    "w_noflush": "import java.io.*;\npublic class Main { public static void main(String[] x) {\n        " + READ +
                 "        PrintWriter w = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));\n" + LOOP_BEST +
                 "        w.println(a[b] + \" \" + (b + 1)); } }\n",
    "w_nonpub": "class Main { public static void main(String[] x) {\n        " + READ +
                "        int b = 0; for (int i = 1; i < n; i++) if (n % 2 == 0 ? a[i] < a[b] : a[i] > a[b]) b = i;\n"
                "        System.out.println(a[b] + \" \" + (b + 1)); } }\n",
    "w_tie": "public class Main { public static void main(String[] x) {\n        " + READ +
             "        int b = 0; for (int i = 1; i < n; i++) if (a[i] >= a[b]) b = i;\n"
             "        System.out.println(a[b] + \" \" + (b + 1)); } }\n",
}
REF_INPUTS = ["3\n1 2 3\n", "1\n-7\n", "4\n5 -1 0 2\n", "5\n-3 -8 -1 -9 -2\n", "2\n100 -100\n", "10\n1 2 3 4 5 6 7 8 9 10\n"]

# ----------------------------------------------------------------------------- bộ test
HEAD = "package codenet;\n\nimport static org.junit.jupiter.api.Assertions.*;\nimport org.junit.jupiter.api.Test;\n\n"
TOGGLE = ("    // đổi trạng thái một tệp mỗi lần gọi: lần chạy thứ nhất trả true, lần thứ hai false, ...\n"
          "    static boolean toggle(String tag) { try { java.nio.file.Path f = java.nio.file.Paths.get(System.getProperty(\"judge.main.dir\"), \"toggle_\" + tag);\n"
          "        if (java.nio.file.Files.exists(f)) { java.nio.file.Files.delete(f); return false; }\n"
          "        java.nio.file.Files.createFile(f); return true; } catch (java.io.IOException e) { throw new RuntimeException(e); } }\n")
SUITES = {
    "S1_assertion_manh": HEAD + "class StrongTest {\n"
    "    @Test void t00_lienKeBang() { assertEquals(\"5 3\", Judge.run(\"3\\n2 2 5\")); }\n"
    "    @Test void t01_moiSoAm() { assertEquals(\"-3 2\", Judge.run(\"3\\n-5 -3 -9\")); }\n"
    "    @Test void t02_lonNhatOCuoi() { assertEquals(\"9 4\", Judge.run(\"4\\n1 2 3 9\")); }\n"
    "    @Test void t03_motPhanTu() { assertEquals(\"7 1\", Judge.run(\"1\\n7\")); }\n"
    "    @Test void t04_nChan() { assertEquals(\"8 2\", Judge.run(\"2\\n4 8\")); }\n"
    "    @Test void t05_goiHaiLan() { assertEquals(\"5 2\", Judge.run(\"2\\n1 5\")); assertEquals(\"5 2\", Judge.run(\"2\\n1 5\")); }\n"
    "}\n",
    "S2_assertion_yeu": HEAD + "class WeakTest {\n"
    "    @Test void y01() { assertNotNull(Judge.run(\"3\\n-5 -3 -9\")); }\n"
    "    @Test void y02() { assertFalse(Judge.run(\"4\\n1 2 3 9\").isEmpty()); }\n"
    "    @Test void y03() { assertTrue(Judge.run(\"1\\n7\").length() > 0); }\n"
    "}\n",
    "S3_expected_sai": HEAD + "class WrongExpectedTest {\n"
    "    @Test void e01_dung() { assertEquals(\"7 1\", Judge.run(\"1\\n7\")); }\n"
    "    @Test void e02_sai() { assertEquals(\"4 1\", Judge.run(\"2\\n4 8\")); }\n"
    "    @Test void e03_dung() { assertEquals(\"-3 2\", Judge.run(\"3\\n-5 -3 -9\")); }\n"
    "}\n",
    "S4_assertThrows_ngoai_le": HEAD + "class ThrowsTest {\n"
    "    @Test void x01_nemKhiRong() { assertThrows(RuntimeException.class, () -> Judge.run(\"\")); }\n"
    "    @Test void x02_nemKhiHopLe() { assertThrows(RuntimeException.class, () -> Judge.run(\"1\\n7\")); }\n"
    "    @Test void x03_batNgoaiLe() { try { assertEquals(\"7 1\", Judge.run(\"1\\n7\")); }\n"
    "        catch (RuntimeException e) { fail(\"chương trình ném ngoại lệ: \" + e); } }\n"
    "    @Test void x04_khongBat() { assertEquals(\"7 1\", Judge.run(\"1\\n7\")); }\n"
    "}\n",
    "S5_flaky_ro_trang_thai": HEAD + "class FlakyTest {\n" + TOGGLE +
    "    static int dem = 0;\n"
    "    @Test void f01_flakyTrenPUT() { assertEquals(\"9 4\", Judge.run(\"4\\n1 2 3 9\")); if (toggle(\"f01\")) fail(\"flaky\"); }\n"
    "    @Test void f02_flakyKhiSai() { String o = Judge.run(\"3\\n-5 -3 -9\"); if (!o.equals(\"-3 2\") && toggle(\"f02\")) fail(\"sai: \" + o); }\n"
    "    @Test void f03_ghiStatic() { dem++; assertEquals(\"7 1\", Judge.run(\"1\\n7\")); }\n"
    "    @Test void f04_docStatic() { assertEquals(1, dem); }\n"
    "}\n",
    "S6_bat_dong_AC": HEAD + "class TieTest {\n"
    "    @Test void d01_trungChotChiSo() { assertEquals(\"5 1\", Judge.run(\"3\\n5 1 5\")); }\n"
    "    @Test void d02_binhThuong() { assertEquals(\"8 2\", Judge.run(\"2\\n4 8\")); }\n"
    "}\n",
}

# ----------------------------------------------------------------------------- kỳ vọng
# Mỗi bộ: test hợp lệ, test bị loại (lý do), test bất đồng AC, và với từng WA (chính, phụ, giữ bất đồng).
# P = phát hiện, K = không, U = không ổn định. Thước đo phụ (assertion hoặc ngoại lệ) ghi theo tiền tố.
EXPECT = {
    "S1_assertion_manh": {
        "hop_le": ["t00_lienKeBang", "t01_moiSoAm", "t02_lonNhatOCuoi", "t03_motPhanTu", "t04_nChan", "t05_goiHaiLan"],
        "bi_loai": {}, "bat_dong": [],
        "wa": {"w_neg": "PPP", "w_last": "PPP", "w_throw1": "KPK", "w_loop": "KKK", "w_exit": "KKK", "w_static": "KKK",
               "w_thread": "PPP", "w_noflush": "PPP", "w_nonpub": "PPP", "w_tie": "KKK"}},
    "S2_assertion_yeu": {
        "hop_le": ["y01", "y02", "y03"], "bi_loai": {}, "bat_dong": [],
        "wa": {"w_neg": "KKK", "w_last": "KKK", "w_throw1": "KPK", "w_loop": "KKK", "w_exit": "KKK", "w_static": "KKK",
               "w_thread": "KKK", "w_noflush": "PPP", "w_nonpub": "KKK", "w_tie": "KKK"}},
    "S3_expected_sai": {
        "hop_le": ["e01_dung", "e03_dung"], "bi_loai": {"e02_sai": "FAIL trên PUT"}, "bat_dong": [],
        "wa": {"w_neg": "PPP", "w_last": "KKK", "w_throw1": "KPK", "w_loop": "KKK", "w_exit": "KKK", "w_static": "KKK",
               "w_thread": "PPP", "w_noflush": "PPP", "w_nonpub": "KKK", "w_tie": "KKK"}},
    "S4_assertThrows_ngoai_le": {
        "hop_le": ["x03_batNgoaiLe", "x04_khongBat"],
        "bi_loai": {"x01_nemKhiRong": "ngoài ràng buộc", "x02_nemKhiHopLe": "FAIL trên PUT"}, "bat_dong": [],
        "wa": {"w_neg": "KKK", "w_last": "KKK", "w_throw1": "PPP", "w_loop": "KKK", "w_exit": "KKK", "w_static": "KKK",
               "w_thread": "PPP", "w_noflush": "PPP", "w_nonpub": "KKK", "w_tie": "KKK"}},
    "S5_flaky_ro_trang_thai": {
        "hop_le": ["f02_flakyKhiSai", "f03_ghiStatic"],
        "bi_loai": {"f01_flakyTrenPUT": "lúc pass lúc fail", "f04_docStatic": "phụ thuộc thứ tự"},
        "bat_dong": [],
        "wa": {"w_neg": "UUU", "w_last": "KKK", "w_throw1": "KPK", "w_loop": "KKK", "w_exit": "KKK", "w_static": "KKK",
               "w_thread": "PPP", "w_noflush": "PPP", "w_nonpub": "KKK", "w_tie": "KKK"}},
    "S6_bat_dong_AC": {
        "hop_le": ["d02_binhThuong"], "bi_loai": {}, "bat_dong": ["d01_trungChotChiSo"],
        "wa": {"w_neg": "KKK", "w_last": "PPP", "w_throw1": "KKK", "w_loop": "KKK", "w_exit": "KKK", "w_static": "KKK",
               "w_thread": "PPP", "w_noflush": "PPP", "w_nonpub": "PPP", "w_tie": "KKP"}},
}
EXPECT_AC = ["s_ac_last", "s_ac_nonpub", "s_ac_stream", "s_ac_thread"]  # đúng bốn bài, thứ tự không quan trọng


def build(out: Path):
    sub = out / "subset"
    for k in ("AC", "WA"):
        (sub / "data" / PID / k).mkdir(parents=True, exist_ok=True)
    (sub / "metadata").mkdir(parents=True, exist_ok=True)
    rows = []
    for sid, (uid, src) in AC.items():
        (sub / "data" / PID / "AC" / f"{sid}.java").write_text(src, encoding="utf-8"); rows.append((sid, uid, "Accepted"))
    for i, (sid, src) in enumerate(WA_SRC.items()):
        (sub / "data" / PID / "WA" / f"{sid}.java").write_text(src, encoding="utf-8"); rows.append((sid, f"u1{i:02d}", "Wrong Answer"))
    with open(sub / "metadata" / f"{PID}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["submission_id", "problem_id", "user_id", "status"])
        for sid, uid, st in rows:
            w.writerow([sid, PID, uid, st])
    fr = out / "frozen"; (fr / "reference_inputs" / PID).mkdir(parents=True, exist_ok=True)
    for i, s in enumerate(REF_INPUTS):
        (fr / "reference_inputs" / PID / f"r{i:02d}.in").write_text(s, encoding="utf-8")
    (fr / "frozen_index.json").write_text(json.dumps({"problems": {PID: {"put": "s_put"}}}), encoding="utf-8")
    man = out / f"{PID}_heldout_manifest.csv"
    with open(man, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["submission_id", "trang_thai"])
        for sid in WA_SRC:
            w.writerow([sid, "đánh giá"])
    tests = out / "tests"; tests.mkdir(exist_ok=True)
    for name, src in SUITES.items():
        (tests / f"{name}.java").write_text(src, encoding="utf-8")
    return sub, fr, man, tests


def code(s):
    return {"phat_hien": "P", "khong": "K", "khong_on_dinh": "U"}.get(s.split(" ")[0], "?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--junit-api", default="")
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    sub, fr, man, tests = build(out)
    ac = pick_ac.main(["--subset", str(sub), "--frozen", str(fr), "--pid", PID, "--k", "4", "--out", str(fr / "ac_check" / f"{PID}.json")])
    checks = [("pick_ac chọn đúng 4 bài AC độc lập", sorted(ac["ac_doi_chieu"]) == EXPECT_AC,
               f"chọn {sorted(ac['ac_doi_chieu'])}; loại: " + "; ".join(f"{r['submission']} ({r['ket_qua']})"
                                                               for r in ac["nhat_ky"] if r["ket_qua"] != "CHỌN"))]
    rows = []
    for name in SUITES:
        so = out / "runs" / name
        junit_eval.main(["--subset", str(sub), "--pid", PID, "--put", "s_put", "--manifest", str(man),
                         "--suite", f"s={tests / f'{name}.java'}", "--out", str(so), "--cache", str(out / "_cache"),
                         "--ac-list", str(fr / "ac_check" / f"{PID}.json"), "--workers", "4", "--timeout", "3"]
                        + (["--junit-api", a.junit_api] if a.junit_api else []))
        rep = json.loads((so / "summary.json").read_text(encoding="utf-8"))["bo_test"]["s"]
        per = {r["submission_id"]: r for r in csv.DictReader(open(so / "per_wa.csv", encoding="utf-8"))}
        exp = EXPECT[name]
        bi_loai = {x["test"]: x["ly_do"] for x in rep["test_khong_hop_le"]}
        bat_dong = [x["test"] for x in rep["test_bat_dong_AC"]]
        ok_valid = sorted(rep["ten_test_hop_le"]) == sorted(exp["hop_le"])
        ok_loai = set(bi_loai) == set(exp["bi_loai"]) and all(exp["bi_loai"][t] in bi_loai[t] for t in exp["bi_loai"])
        ok_bd = sorted(bat_dong) == sorted(exp["bat_dong"])
        checks.append((f"{name}: test hợp lệ = {exp['hop_le']}", ok_valid, f"thực tế {sorted(rep['ten_test_hop_le'])}"))
        checks.append((f"{name}: test bị loại và lý do", ok_loai, json.dumps(bi_loai, ensure_ascii=False)))
        checks.append((f"{name}: test bất đồng AC", ok_bd, json.dumps(rep["test_bat_dong_AC"], ensure_ascii=False)))
        for sid, e in exp["wa"].items():
            g = code(per[sid]["s_chinh"]) + code(per[sid]["s_phu"]) + code(per[sid]["s_giu_bat_dong"])
            rows.append((name, sid, e, g, per[sid]["s_phu"]))
            checks.append((f"{name} / {sid} (chính, phụ, giữ bất đồng) = {e}", g == e, f"thực tế {g} [{per[sid]['s_phu']}]"))
    # ghi đè bằng quyết định của người duyệt: giữ d01 thì w_tie phải được tính ở thước đo chính
    s6 = tests / "S6_bat_dong_AC.java"
    sha = hashlib.sha256(s6.read_text(encoding="utf-8").encode()).hexdigest()
    rv = out / "review.csv"
    rv.write_text("suite_sha256,test,quyet_dinh,nguoi_duyet_1,nguoi_duyet_2,nguoi_quyet\n"
                  f"{sha},d01_trungChotChiSo,giữ,A,B,\n", encoding="utf-8")
    so = out / "runs" / "S6_review_giu"
    junit_eval.main(["--subset", str(sub), "--pid", PID, "--put", "s_put", "--manifest", str(man), "--suite", f"s={s6}",
                     "--out", str(so), "--cache", str(out / "_cache"), "--ac-list", str(fr / "ac_check" / f"{PID}.json"),
                     "--review", str(rv), "--workers", "4", "--timeout", "3"] + (["--junit-api", a.junit_api] if a.junit_api else []))
    per = {r["submission_id"]: r for r in csv.DictReader(open(so / "per_wa.csv", encoding="utf-8"))}
    checks.append(("S6 với file duyệt ghi 'giu' cho d01: w_tie được tính ở thước đo chính",
                   code(per["w_tie"]["s_chinh"]) == "P", per["w_tie"]["s_chinh"]))
    n_ok = sum(1 for _, ok, _ in checks if ok)
    md = [f"# Kiểm chứng bộ chấm trên bài giả lập {PID}", "",
          f"JUnit API: {a.junit_api or 'junit_shim'}. Kết quả: **{n_ok}/{len(checks)}** kiểm tra khớp kỳ vọng.", "",
          "## Bài WA giả lập", "", "| Bài | Hành vi |", "| --- | --- |"] + [f"| {k} | {v} |" for k, v in WA.items()] + [
          "", "## Kiểm tra", "", "| Kiểm tra | Khớp | Chi tiết |", "| --- | :-: | --- |"] + [
          f"| {c} | {'có' if ok else 'KHÔNG'} | {d.replace('|', '/')} |" for c, ok, d in checks]
    (out / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "report.json").write_text(json.dumps({"khop": n_ok, "tong": len(checks),
                                                 "kiem_tra": [{"kiem_tra": c, "khop": ok, "chi_tiet": d} for c, ok, d in checks]},
                                                ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n== {n_ok}/{len(checks)} khớp kỳ vọng ==")
    for c, ok, d in checks:
        if not ok:
            print("LỆCH:", c, "|", d)
    sys.exit(0 if n_ok == len(checks) else 1)


if __name__ == "__main__":
    main()
