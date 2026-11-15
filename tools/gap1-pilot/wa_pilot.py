#!/usr/bin/env python3
"""Pilot phép đo Wrong Answer (WA) cho GAP 1.

Với mỗi bài trong tập con CodeNet (tạo bởi codenet_subset.py), script trả lời các câu hỏi pilot:
  1. Áp dụng cùng đầu vào lên các bài nộp khác cấu trúc: mỗi bài nộp chạy như chương trình độc lập
     (`java Main`, đầu vào qua stdin, so stdout), không sửa mã. Bài nộp có `package` hoặc lớp chính
     khác `Main` bị loại và được đếm. Riêng chương trình sinh viên kiểm thử phải chạy qua Judge.run
     (thêm `package codenet;`), nên script kiểm tra Judge.run cho đúng output như chạy tiến trình.
  2. Đầu ra đúng (oracle): chạy đầu vào trên nhóm bài AC; oracle là output chung của ít nhất 90%
     bài AC chạy thành công (tối thiểu 5 bài). Với Sample Input, oracle được đối chiếu với Sample Output.
  3. Tập WA đánh giá được cố định trước bằng manifest SHA-256 và không đưa cho sinh viên.
  4. Loại mã trùng (chuẩn hoá mã giống hệt), lỗi biên dịch, bài không tất định; TLE, lỗi môi trường
     (hết bộ nhớ, tràn stack, JVM lỗi) không tính là phát hiện.
  5. Tỉ lệ phát hiện được báo cáo ở cấp bài nộp WA và ở cấp nhóm hành vi (bài WA cho cùng output trên
     toàn bộ đầu vào hợp lệ được xem là cùng một dạng lỗi).

Cách chạy:
  python wa_pilot.py --subset <thư mục giải nén codenet_pilot_subset.zip> --out results \
      [--extra <thư mục chứa pXXXXX/*.in hoặc pXXXXX/*.java (JUnit)>]
"""
import argparse, base64, concurrent.futures as cf, csv, hashlib, json, os, random, re, shutil, statistics
import subprocess, sys, tempfile, time
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from desc_rules import extract_samples, special_judge_reason  # noqa: E402
from validators import validate  # noqa: E402

ENV = {k: v for k, v in os.environ.items() if k not in ("JAVA_TOOL_OPTIONS", "_JAVA_OPTIONS", "JDK_JAVA_OPTIONS")}
JAVA_FLAGS = ["-Xss64m", "-Xmx256m", "-XX:TieredStopAtLevel=1", "-XX:+UseSerialGC", "-Xshare:auto"]
# Lỗi hạ tầng: JVM không khởi động được. StackOverflowError / OutOfMemoryError trong lúc chạy là lỗi của
# chính chương trình (bài AC chạy được cùng đầu vào với cùng giới hạn), nên tính là RE, không phải ENV.
ENV_ERR = re.compile(r"Could not reserve|Error occurred during initialization|"
                     r"Could not create the Java Virtual Machine|There is insufficient memory|hs_err_pid")


# ----------------------------------------------------------------------------- chuẩn hoá
def norm_out(s: str) -> str:
    """Giống Judge.normalize của bộ công cụ nhóm: bỏ \\r, khoảng trắng cuối dòng, dòng trống cuối."""
    lines = s.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return re.sub(r"\n+$", "", "\n".join(l.rstrip() for l in lines))


def norm_in(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n").lstrip("\n")
    return s if s.endswith("\n") else s + "\n"


def strip_comments(src: str) -> str:
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if src.startswith('"""', i):  # text block: giữ nguyên tới dấu """ đóng
            j = src.find('"""', i + 3)
            j = n if j < 0 else j + 3
            out.append(src[i:j]); i = j
            continue
        if c in "\"'":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append(src[i:j + 1]); i = j + 1
        elif src.startswith("//", i):
            j = src.find("\n", i); i = n if j < 0 else j
        elif src.startswith("/*", i):
            j = src.find("*/", i + 2); i = n if j < 0 else j + 2
        else:
            out.append(c); i += 1
    return "".join(out)


TOKEN = re.compile(r'"(?:[^"\\\n]|\\.)*"|\'(?:[^\'\\\n]|\\.)*\'|[A-Za-z_$][\w$]*|\d[\w.]*|\S')


def src_tokens(src: str):
    return TOKEN.findall(strip_comments(src))


def norm_src(src: str) -> str:
    """Chuỗi token cách nhau 1 dấu cách: hai bài chỉ khác khoảng trắng / chú thích cho cùng kết quả."""
    return " ".join(src_tokens(src))


def shingles(src: str, k: int = 5) -> set:
    tok = src_tokens(src)
    return {tuple(tok[i:i + k]) for i in range(max(1, len(tok) - k + 1))}


def structure_issue(src: str) -> str:
    s = strip_comments(src)
    if re.search(r"^\s*package\s+[\w.]+\s*;", s, re.M):
        return "có khai báo package"
    if not re.search(r"\bclass\s+Main\b", s):
        return "lớp chính không phải Main"
    if not re.search(r"static\s+(?:public\s+)?void\s+main\s*\(|public\s+static\s+void\s+main\s*\(", s):
        return "không có hàm main"
    return ""


# ----------------------------------------------------------------------------- biên dịch, chạy
def compile_batch(jobs, workdir: Path):
    """jobs: list (src_path, out_dir). Trả về dict src_path -> '' (OK) hoặc thông báo lỗi."""
    tooldir = workdir / "_tools"
    if not (tooldir / "BatchCompile.class").exists():
        tooldir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["javac", "-d", str(tooldir), str(HERE / "BatchCompile.java")], check=True, env=ENV,
                       capture_output=True)
    p = subprocess.run(["java", "-cp", str(tooldir), "BatchCompile"], env=ENV, capture_output=True, text=True,
                       input="".join(f"{s}\t{o}\n" for s, o in jobs))
    res = {}
    for line in p.stdout.splitlines():
        parts = line.split("\t")
        if parts[0] == "OK":
            res[parts[1]] = ""
        elif parts[0] == "CE":
            res[parts[1]] = parts[2] if len(parts) > 2 else "lỗi biên dịch"
    for s, _ in jobs:
        res.setdefault(s, "không biên dịch được (BatchCompile không trả kết quả)")
    return res


def run_once(classdir: str, inp: str, timeout: float):
    t0 = time.time()
    try:
        p = subprocess.run(["java", *JAVA_FLAGS, "-cp", classdir, "Main"], input=inp.encode("utf-8"),
                           capture_output=True, timeout=timeout, env=ENV)
    except subprocess.TimeoutExpired:
        return {"status": "TLE", "out": None, "sec": round(time.time() - t0, 3)}
    err = p.stderr.decode("utf-8", errors="replace")
    out = norm_out(p.stdout.decode("utf-8", errors="replace"))
    if ENV_ERR.search(err):
        status = "ENV"
    elif p.returncode != 0:
        status = "RE"
    else:
        status = "OK"
    return {"status": status, "out": out, "sec": round(time.time() - t0, 3), "rc": p.returncode}


def run_prog(classdir, inp, timeout):
    r = run_once(classdir, inp, timeout)
    if r["status"] == "ENV":  # lỗi môi trường: chạy lại một lần
        r2 = run_once(classdir, inp, timeout)
        if r2["status"] != "ENV":
            r = r2
    return r


# ----------------------------------------------------------------------------- đầu vào
JAVA_STR = r'"(?:[^"\\\n]|\\.)*"'
TEXT_BLOCK = r'"""[ \t]*\n(.*?)"""'


def unescape_java(lit: str) -> str:
    body = lit[1:-1]
    return bytes(body, "utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8")


def text_block_value(raw: str) -> str:
    """Giá trị của text block Java (JLS 3.10.6): bỏ thụt lề chung (tính cả dòng chứa dấu đóng),
    bỏ khoảng trắng cuối dòng, rồi xử lý escape. raw là phần giữa dòng mở và dấu \"\"\" đóng."""
    lines = raw.split("\n")
    sig = [l for l in lines[:-1] if l.strip()] + [lines[-1]]  # dòng cuối = phần trước dấu đóng
    ind = min((len(l) - len(l.lstrip(" \t")) for l in sig), default=0)
    out = [l[ind:].rstrip(" \t") for l in lines]
    val = "\n".join(out)
    return bytes(val, "utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8")


def inputs_from_junit(text: str):
    """Lấy đối số chuỗi của Judge.run(...) (chuỗi thường, text block, hoặc nối bằng +).
    Bỏ chú thích trước khi tìm, nên lời gọi nằm trong // hoặc /* */ không được tính."""
    text = strip_comments(text)
    res = []
    for m in re.finditer(r"Judge\.run\s*\(", text):
        i, depth, j = m.end(), 1, m.end()
        while j < len(text) and depth:
            if text[j] == '"':
                if text.startswith('"""', j):
                    k = text.find('"""', j + 3); j = k + 3; continue
                k = j + 1
                while k < len(text) and text[k] != '"':
                    k += 2 if text[k] == "\\" else 1
                j = k + 1; continue
            depth += {"(": 1, ")": -1}.get(text[j], 0); j += 1
        arg = text[i:j - 1]
        parts = []
        for tb in re.finditer(TEXT_BLOCK, arg, re.S):
            parts.append(("tb", tb.start(), text_block_value(tb.group(1))))
        for s in re.finditer(JAVA_STR, re.sub(TEXT_BLOCK, lambda x: " " * len(x.group(0)), arg, flags=re.S)):
            parts.append(("s", s.start(), unescape_java(s.group(0))))
        rest = re.sub(TEXT_BLOCK, "", arg, flags=re.S)
        rest = re.sub(JAVA_STR, "", rest).replace("+", "").strip()
        if rest:  # có biến hoặc lời gọi hàm: không trích tĩnh được
            res.append(None)
            continue
        res.append("".join(p[2] for p in sorted(parts, key=lambda x: x[1])))
    return res


def load_extra_inputs(extra_dir: Path, pid: str):
    out, skipped = [], 0
    d = extra_dir / pid if extra_dir else None
    if not d or not d.is_dir():
        return out, skipped
    for f in sorted(d.iterdir()):
        if f.suffix == ".in":
            out.append(f.read_text(encoding="utf-8"))
        elif f.suffix == ".java":
            for s in inputs_from_junit(f.read_text(encoding="utf-8")):
                if s is None:
                    skipped += 1
                else:
                    out.append(s)
    return out, skipped


# ----------------------------------------------------------------------------- Judge.run
JUDGE_CHECK = r'''package codenet;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.Base64;
public class JudgeCheck {
    public static void main(String[] a) throws Exception {
        java.io.PrintStream real = System.out;
        for (int i = 0; i < a.length; i++) {
            String in = new String(Files.readAllBytes(Paths.get(a[i])), StandardCharsets.UTF_8);
            String out;
            try { out = Judge.run(in); } catch (Throwable t) { out = "<<EXCEPTION " + t + ">>"; }
            real.println("=== " + i + " " + Base64.getEncoder().encodeToString(out.getBytes(StandardCharsets.UTF_8)));
            real.flush();
        }
    }
}
'''


def judge_equivalence(src: str, inputs, proc_outputs, workdir: Path, judge_java: Path):
    """Chạy chương trình qua Judge.run (thêm package codenet, mọi đầu vào trong MỘT JVM như JUnit)
    và so với output khi chạy tiến trình độc lập. Trả về (số khớp, tổng, mô tả lệch)."""
    d = Path(tempfile.mkdtemp(dir=workdir))
    pkg = d / "src" / "codenet"; pkg.mkdir(parents=True)
    body = re.sub(r"^\s*package\s+[\w.]+\s*;\s*", "", src, flags=re.M)
    (pkg / "Main.java").write_text("package codenet;\n\n" + body, encoding="utf-8")
    shutil.copy(judge_java, pkg / "Judge.java")
    (pkg / "JudgeCheck.java").write_text(JUDGE_CHECK, encoding="utf-8")
    cls = d / "classes"
    c = subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-d", str(cls), *map(str, pkg.glob("*.java"))],
                       env=ENV, capture_output=True, text=True)
    if c.returncode:
        return 0, len(inputs), "không biên dịch được khi thêm package codenet"
    files = []
    for i, s in enumerate(inputs):
        f = d / f"in{i}.txt"; f.write_text(s, encoding="utf-8"); files.append(str(f))
    try:
        p = subprocess.run(["java", *JAVA_FLAGS, "-cp", str(cls), "codenet.JudgeCheck", *files], env=ENV,
                           capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return 0, len(inputs), "Judge.run quá thời gian"
    got = {}
    for line in p.stdout.splitlines():
        m = re.match(r"=== (\d+) (\S*)$", line)
        if m:
            got[int(m.group(1))] = base64.b64decode(m.group(2)).decode("utf-8")
    same, diffs = 0, []
    for i, exp in enumerate(proc_outputs):
        if got.get(i) == exp:
            same += 1
        else:
            diffs.append(i)
    note = "" if not diffs else f"lệch ở đầu vào {diffs[:5]} (JVM dừng sớm hoặc trạng thái static giữa các lần gọi)"
    return same, len(inputs), note


# ----------------------------------------------------------------------------- một bài
def analyse_problem(pid, sub: Path, out: Path, extra_dir, a, judge_java):
    t0 = time.time()
    work = out / "_work" / pid
    work.mkdir(parents=True, exist_ok=True)
    rep = {"problem_id": pid}
    page = (sub / "problem_descriptions" / f"{pid}.html").read_text(encoding="utf-8", errors="replace")
    samples = extract_samples(page)
    rep["special_judge_phrase"] = special_judge_reason(page)

    # --- 1. đọc, kiểm cấu trúc, loại trùng
    subs = {}
    for kind in ("AC", "WA"):
        for f in sorted((sub / "data" / pid / kind).glob("*.java")):
            subs[f.stem] = {"kind": kind, "path": f, "src": f.read_text(encoding="utf-8", errors="replace")}
    cnt = Counter()
    for sid, s in subs.items():
        cnt[f"{s['kind']}_tong"] += 1
        s["issue"] = structure_issue(s["src"])
        if s["issue"]:
            cnt[f"{s['kind']}_loai_cau_truc"] += 1
    groups = defaultdict(list)
    for sid, s in subs.items():
        if not s["issue"]:
            groups[(s["kind"], hashlib.sha256(norm_src(s["src"]).encode()).hexdigest())].append(sid)
    uniq = []
    for (kind, _h), sids in groups.items():
        sids.sort()
        uniq.append(sids[0])
        for d in sids[1:]:
            subs[d]["issue"] = f"trùng mã với {sids[0]}"
            cnt[f"{kind}_trung_ma"] += 1
    # gần trùng (chỉ báo cáo): Jaccard 5-gram token >= 0.9 giữa các bài WA còn lại
    wa_u = [s for s in uniq if subs[s]["kind"] == "WA"]
    sh = {s: shingles(subs[s]["src"]) for s in wa_u}
    near = 0
    for i in range(len(wa_u)):
        for j in range(i + 1, len(wa_u)):
            A, B = sh[wa_u[i]], sh[wa_u[j]]
            if A and B and len(A & B) / len(A | B) >= 0.9:
                near += 1
    rep["cap_WA_gan_trung_jaccard_0_9"] = near

    # --- 2. biên dịch
    # CodeNet lưu file theo tên sXXXXXXXXX.java; Java yêu cầu lớp public Main nằm trong Main.java,
    # nên chép nguyên văn nội dung sang <thư mục riêng>/Main.java (không sửa mã).
    jobs = []
    for s in uniq:
        sd = work / "src" / s
        sd.mkdir(parents=True, exist_ok=True)
        (sd / "Main.java").write_text(subs[s]["src"], encoding="utf-8")
        subs[s]["main_path"] = sd / "Main.java"
        jobs.append((str(sd / "Main.java"), str(work / "cls" / s)))
    ce = compile_batch(jobs, out / "_work")
    for s in uniq:
        msg = ce[str(subs[s]["main_path"])]
        if msg:
            subs[s]["issue"] = "lỗi biên dịch: " + msg[:120]
            cnt[f"{subs[s]['kind']}_loi_bien_dich"] += 1
    ok = [s for s in uniq if not subs[s]["issue"]]
    ac_ok = sorted(s for s in ok if subs[s]["kind"] == "AC")
    wa_ok = sorted(s for s in ok if subs[s]["kind"] == "WA")

    # --- 3. tập đầu vào
    extra, skipped = load_extra_inputs(extra_dir, pid)
    inputs, origin = [], []
    for i, (si, _so) in enumerate(samples):
        inputs.append(norm_in(si)); origin.append("sample")
    out_of_range = []
    for e in extra:
        e = norm_in(e)
        if e in inputs:
            continue
        why = validate(pid, e)
        if why:  # ngoài ràng buộc của đề: không dùng, kể cả khi các bài AC cho cùng output
            out_of_range.append(why); continue
        inputs.append(e); origin.append("extra")
    rep["dau_vao"] = {"sample": origin.count("sample"), "extra": origin.count("extra"),
                      "junit_khong_trich_duoc": skipped, "ngoai_rang_buoc": len(out_of_range),
                      "co_validator": validate(pid, inputs[0]) is not None if inputs else False}

    def par_map(fn, items):
        with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
            return list(ex.map(fn, items))

    # --- 4. oracle từ nhóm AC
    rng = random.Random(f"{a.seed}-{pid}")
    ac_shuffled = ac_ok[:]; rng.shuffle(ac_shuffled)
    pool = ac_shuffled[:a.oracle_pool]
    put_candidates = ac_shuffled[a.oracle_pool:] or ac_shuffled[:]
    cls = lambda s: str(work / "cls" / s)
    ac_runs = {}
    pairs = [(s, i) for s in pool for i in range(len(inputs))]
    res = par_map(lambda p: run_prog(cls(p[0]), inputs[p[1]], a.timeout), pairs)
    res2 = par_map(lambda p: run_prog(cls(p[0]), inputs[p[1]], a.timeout), pairs)  # lần 2: kiểm tất định
    nondet_ac = set()
    for (s, i), r1, r2 in zip(pairs, res, res2):
        ac_runs[(s, i)] = r1
        if r1["status"] == "OK" and r2["status"] == "OK" and r1["out"] != r2["out"]:
            nondet_ac.add(s)
    oracle, oracle_info = {}, []
    for i, inp in enumerate(inputs):
        outs = [ac_runs[(s, i)]["out"] for s in pool if s not in nondet_ac and ac_runs[(s, i)]["status"] == "OK"]
        info = {"input": i, "origin": origin[i], "ac_thanh_cong": len(outs)}
        if outs:
            mode, k = Counter(outs).most_common(1)[0]
            info["ty_le_dong_thuan"] = round(k / len(outs), 3)
            if len(outs) >= a.min_oracle and k / len(outs) >= a.agree:
                oracle[i] = mode
        if origin[i] == "sample":
            exp = norm_out(samples[i][1].lstrip("\n"))  # HTML của AIZU có dòng trống đầu trong <pre>
            info["khop_sample_output"] = (oracle.get(i) == exp) if i in oracle else None
            if i in oracle and oracle[i] != exp:  # oracle sai so với đề: không dùng đầu vào này
                oracle.pop(i)
        info["hop_le"] = i in oracle
        oracle_info.append(info)
    valid = sorted(oracle)
    rep["oracle"] = {"ac_bien_dich_duoc": len(ac_ok), "ac_trong_nhom_oracle": len(pool),
                     "ac_khong_tat_dinh": len(nondet_ac), "dau_vao_hop_le": len(valid),
                     "dau_vao_bi_loai": len(inputs) - len(valid),
                     "sample_khop_oracle": sum(1 for x in oracle_info if x.get("khop_sample_output") is True),
                     "sample_tong": origin.count("sample"), "chi_tiet": oracle_info}

    # --- 5. chương trình sinh viên kiểm thử (PUT): AC khớp oracle mọi đầu vào hợp lệ, tất định,
    #        và Judge.run cho cùng output như chạy tiến trình
    put, put_log = None, []
    for s in put_candidates[:a.put_tries]:
        r = [run_prog(cls(s), inputs[i], a.timeout) for i in valid]
        if any(x["status"] != "OK" or x["out"] != oracle[i] for x, i in zip(r, valid)):
            put_log.append({"submission": s, "ket_qua": "lệch oracle"}); continue
        same, tot, note = judge_equivalence(subs[s]["src"], [inputs[i] for i in valid], [oracle[i] for i in valid],
                                            work, judge_java)
        put_log.append({"submission": s, "judge_khop": f"{same}/{tot}", "ghi_chu": note})
        if tot and same == tot:
            put = s; break
    rep["chuong_trinh_kiem_thu"] = {"submission": put, "cac_lan_thu": put_log}

    # --- 6. chạy WA trên đầu vào hợp lệ, mỗi cặp hai lần để kiểm tra tất định
    pairs = [(w, i) for w in wa_ok for i in valid]
    res1 = par_map(lambda p: run_prog(cls(p[0]), inputs[p[1]], a.timeout), pairs)
    res2 = par_map(lambda p: run_prog(cls(p[0]), inputs[p[1]], a.timeout), pairs)

    def classify(r, i):
        return ("MATCH" if r["out"] == oracle[i] else "MISMATCH") if r["status"] == "OK" else r["status"]

    wa_runs, nondet_wa, slow = {}, set(), []
    for (w, i), r1, r2 in zip(pairs, res1, res2):
        s1, s2 = classify(r1, i), classify(r2, i)
        if s1 == s2 and (s1 != "MISMATCH" or r1["out"] == r2["out"]):
            wa_runs[(w, i)] = {"status": s1, "out": r1["out"]}
        elif "TLE" in (s1, s2):
            slow.append((w, i))  # một lần quá giờ, một lần không: chạy lại với thời gian gấp 3
        else:
            nondet_wa.add(w)
            wa_runs[(w, i)] = {"status": s1, "out": r1["out"]}
    res3 = par_map(lambda p: run_prog(cls(p[0]), inputs[p[1]], a.timeout * 3), slow)
    for (w, i), r in zip(slow, res3):
        wa_runs[(w, i)] = {"status": classify(r, i), "out": r["out"]}
    cnt["WA_cap_chay_lai_do_TLE"] = len(slow)
    for w in nondet_wa:
        subs[w]["issue"] = "không tất định"
    cnt["WA_khong_tat_dinh"] = len(nondet_wa)
    wa_eval = [w for w in wa_ok if w not in nondet_wa]
    st_count = Counter(wa_runs[(w, i)]["status"] for w in wa_eval for i in valid)
    rep["ket_qua_chay_WA"] = dict(st_count)

    # --- 7. tỉ lệ phát hiện: bộ "ban đầu" (sample) và bộ "ban đầu + bổ sung"
    def detected(w, idx, with_re=False):
        ok_st = {"MISMATCH", "RE"} if with_re else {"MISMATCH"}
        return any(wa_runs[(w, i)]["status"] in ok_st for i in idx)

    sets = {"sample": [i for i in valid if origin[i] == "sample"], "sample+extra": valid}
    sig = {w: tuple((wa_runs[(w, i)]["status"], wa_runs[(w, i)]["out"]) for i in valid) for w in wa_eval}
    classes = defaultdict(list)
    for w in wa_eval:
        classes[sig[w]].append(w)
    rep["WA_danh_gia"] = len(wa_eval)
    rep["nhom_hanh_vi_WA"] = len(classes)
    det = {}
    for name, idx in sets.items():
        d1 = sum(detected(w, idx) for w in wa_eval)
        d2 = sum(detected(w, idx, True) for w in wa_eval)
        dc = sum(detected(ws[0], idx) for ws in classes.values())
        det[name] = {"so_dau_vao_doc_lap": len(idx), "phat_hien_MISMATCH": d1, "phat_hien_MISMATCH_hoac_RE": d2,
                     "ty_le": round(d1 / len(wa_eval), 3) if wa_eval else None,
                     "nhom_hanh_vi_phat_hien": dc,
                     "ty_le_nhom": round(dc / len(classes), 3) if classes else None}
    rep["phat_hien"] = det
    rep["dem"] = dict(cnt)

    # --- 8. manifest tập WA giữ kín
    with open(out / f"{pid}_heldout_manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["submission_id", "sha256", "trang_thai"])
        for sid, s in sorted(subs.items()):
            if s["kind"] == "WA":
                w.writerow([sid, hashlib.sha256(s["src"].encode()).hexdigest(),
                            "đánh giá" if sid in wa_eval else s["issue"] or "loại"])
    with open(out / f"{pid}_wa_runs.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["submission_id", "input_index", "input_origin", "status"])
        for wv in wa_eval:
            for i in valid:
                w.writerow([wv, i, origin[i], wa_runs[(wv, i)]["status"]])
    rep["thoi_gian_giay"] = round(time.time() - t0, 1)
    (out / f"{pid}_report.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--subset", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--extra", default=None)
    ap.add_argument("--judge", default=str(HERE / "Judge.java"), help="Judge.java của bộ công cụ nhóm")
    ap.add_argument("--problems", nargs="*")
    ap.add_argument("--timeout", type=float, default=4.0)
    ap.add_argument("--oracle-pool", type=int, default=20)
    ap.add_argument("--min-oracle", type=int, default=5)
    ap.add_argument("--agree", type=float, default=0.9)
    ap.add_argument("--put-tries", type=int, default=10)
    ap.add_argument("--workers", type=int, default=max(2, os.cpu_count() or 2))
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args(argv)
    sub, out = Path(a.subset), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    extra = Path(a.extra) if a.extra else None
    pids = a.problems or [r["problem_id"] for r in csv.DictReader(open(sub / "selected.csv", encoding="utf-8"))]
    reps = []
    for pid in pids:
        print(f"[{pid}] đang chạy ...", flush=True)
        r = analyse_problem(pid, sub, out, extra, a, Path(a.judge))
        reps.append(r)
        d = r["phat_hien"]
        print(f"[{pid}] WA đánh giá {r['WA_danh_gia']}, nhóm hành vi {r['nhom_hanh_vi_WA']}, "
              f"phát hiện sample {d['sample']['ty_le']} → sample+extra {d['sample+extra']['ty_le']} "
              f"({r['thoi_gian_giay']} giây)", flush=True)
    (out / "summary.json").write_text(json.dumps(reps, ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.rmtree(out / "_work", ignore_errors=True)


if __name__ == "__main__":
    main()
