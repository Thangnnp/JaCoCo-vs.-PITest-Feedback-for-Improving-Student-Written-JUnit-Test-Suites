#!/usr/bin/env python3
"""Chấm MỘT phiên của sinh viên cho GAP 1 bằng cách CHẠY CHÍNH BỘ JUNIT của sinh viên.

Một test là HỢP LỆ khi pass trên chương trình được kiểm thử (PUT) ở cả hai lần chạy. Test fail trên PUT
(expected output sai, assertion sai) hoặc lúc pass lúc fail bị loại và được ghi lý do.
Một bài WA bị PHÁT HIỆN (thước đo chính) khi có ít nhất một test hợp lệ FAIL do assertion trên bài WA đó,
ở cả hai lần chạy. Thước đo phụ tính thêm trường hợp test ERROR (bài WA ném ngoại lệ trong test).
Quá thời gian, JVM dừng (System.exit) hoặc kết quả hai lần chạy khác nhau: KHÔNG tính là phát hiện,
bài WA vẫn nằm trong mẫu số. Mẫu số là danh sách WA cố định trong manifest (trạng thái "đánh giá").
Không có đầu vào nào được tự thêm vào bộ test: bộ test được chấm đúng như sinh viên nộp.

Đối chiếu AC độc lập (--ac-list, file JSON của pick_ac.py): pass trên PUT chưa đủ để coi test đúng với đề.
Test hợp lệ còn được chạy trên K bài AC của tác giả khác; test không PASS trên ít nhất một bài là test "bất đồng AC".
Mặc định test bất đồng bị loại tạm khỏi phân tích chính, chờ hai thành viên đối chiếu với đề bài và người thứ ba
quyết khi hai người không thống nhất; quyết định ghi vào --review (CSV: suite_sha256,test,quyet_dinh=giu|loai,...).
Thước đo độ nhạy WADR_giu_bat_dong tính lại khi GIỮ mọi test bất đồng.

  python junit_eval.py --subset SUBSET --pid p03546 --put s575130508 \
      --manifest results/p03546_heldout_manifest.csv \
      --suite before=path/Before.java --suite after=path/After.java --out session_out \
      [--junit-api lib/junit-jupiter-api.jar:lib/opentest4j.jar:lib/apiguardian-api.jar]
      [--ac-list frozen/ac_check/p03546.json] [--review review_p03546.csv]

Lớp test phải nằm trong package codenet và gọi Judge.run(String). Khi không có --junit-api, script dùng
bản thay thế tối giản của JUnit 5 API (tools/junit_shim) để chạy thử.
"""
import argparse, base64, concurrent.futures as cf, csv, hashlib, json, os, re, shutil, subprocess, sys, threading, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wa_pilot import ENV, inputs_from_junit, norm_in  # noqa: E402
from validators import validate  # noqa: E402

JAVA_FLAGS = ["-Xss64m", "-Xmx256m", "-XX:TieredStopAtLevel=1", "-XX:+UseSerialGC"]


def sh(cmd, **kw):
    return subprocess.run(cmd, env=ENV, capture_output=True, text=True, **kw)


def javac(srcs, out, cp=None):
    out.mkdir(parents=True, exist_ok=True)
    cmd = ["javac", "-nowarn", "-encoding", "UTF-8", "-proc:none", "-d", str(out)]
    if cp:
        cmd += ["-cp", cp]
    r = sh(cmd + [str(s) for s in srcs])
    return r.returncode == 0, r.stderr.strip()[:500]


def with_package(src: str) -> str:
    body = re.sub(r"^\s*package\s+[\w.]+\s*;\s*", "", src, count=1, flags=re.M)
    return "package codenet;\n\n" + body


def prepare_harness(work: Path, api_cp: str):
    """Biên dịch HarnessRunner, Judge chấm (EvalJudge) và (nếu cần) bản thay thế JUnit API."""
    ver = hashlib.sha256(b"".join((HERE / f).read_bytes() for f in ("junit_shim/HarnessRunner.java", "EvalJudge.java"))).hexdigest()[:8]
    h = work / (("_harness_junit_" if api_cp else "_harness_shim_") + ver)  # mã harness đổi thì biên dịch lại
    if (h / "ok").exists():
        return h
    if not api_cp:
        shim_src = list((HERE / "junit_shim" / "org").rglob("*.java"))
        ok, err = javac(shim_src, h / "api")
        if not ok:
            raise SystemExit("Không biên dịch được bản thay thế JUnit: " + err)
    cp = api_cp or str(h / "api")
    ok, err = javac([HERE / "junit_shim" / "HarnessRunner.java"], h / "runner", cp)
    if not ok:
        raise SystemExit("Không biên dịch được HarnessRunner: " + err)
    jd = h / "judge_src" / "codenet"; jd.mkdir(parents=True, exist_ok=True)
    shutil.copy(HERE / "EvalJudge.java", jd / "Judge.java")
    ok, err = javac([jd / "Judge.java"], h / "judge")
    if not ok:
        raise SystemExit("Không biên dịch được EvalJudge: " + err)
    (h / "ok").write_text("ok")
    return h


def compile_program(src: str, out: Path):
    """Biên dịch một bài nộp thành codenet.Main trong thư mục riêng (dùng chung giữa các phiên)."""
    if (out / "codenet" / "Main.class").exists():
        return True, ""
    d = out.parent / (out.name + "_src") / "codenet"; d.mkdir(parents=True, exist_ok=True)
    (d / "Main.java").write_text(with_package(src), encoding="utf-8")
    return javac([d / "Main.java"], out)


def run_suite(h: Path, api_cp: str, test_cls_dir: Path, test_class: str, main_dir: Path, timeout: float, log=None,
              start=0, stop=None):
    """Chạy các @Test có chỉ số trong [start, stop) (mặc định: tất cả), trả về list (tên, trạng thái, thông báo).
    Trạng thái: PASS, FAIL, ERROR, TIMEOUT, EXIT."""
    cp = os.pathsep.join([str(h / "runner"), api_cp or str(h / "api"), str(h / "judge"), str(test_cls_dir)])
    results, total = [], None
    while True:
        props = [f"-Djudge.main.dir={main_dir}"] + ([f"-Djudge.log={log}"] if log else [])
        p = subprocess.Popen(["java", *JAVA_FLAGS, *props, "-cp", cp, "HarnessRunner",
                              test_class, str(start)] + ([str(stop)] if stop is not None else []), env=ENV, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                             text=True, encoding="utf-8", errors="replace")
        lines, cur = [], {"name": None, "t": time.time()}

        def reader():
            for line in p.stdout:
                line = line.rstrip("\n")
                lines.append(line)
                if line.startswith("START "):
                    cur["name"] = line.split(" ", 2)[2]; cur["t"] = time.time()
                elif line.startswith("RESULT "):
                    cur["name"] = None; cur["t"] = time.time()
        th = threading.Thread(target=reader, daemon=True); th.start()
        t0 = time.time(); timed_out = False
        while p.poll() is None:
            time.sleep(0.02)
            limit = timeout if cur["name"] else timeout + 10  # khởi động JVM, @BeforeAll
            if time.time() - cur["t"] > limit or time.time() - t0 > timeout * 50 + 30:
                p.kill(); timed_out = True; break
        p.wait(); th.join(timeout=2)
        last_start = None
        for line in lines:
            if line.startswith("COUNT "):
                total = int(line.split()[1])
            elif line.startswith("START "):
                _, i, name = line.split(" ", 2); last_start = (int(i), name)
            elif line.startswith("RESULT "):
                parts = line.split(" ", 4)
                results.append((parts[2], parts[3], parts[4] if len(parts) > 4 else ""))
                last_start = None
        if "DONE" in lines:
            return results, total
        if total is None:  # không khởi động được (thiếu lớp, lỗi @BeforeAll...)
            return results + [("<class>", "ERROR", "không chạy được lớp test")], 0
        if last_start is None:  # dừng ngoài một test
            return results, total
        results.append((last_start[1], "TIMEOUT" if timed_out else "EXIT", ""))
        start = last_start[0] + 1
        if start >= (total if stop is None else min(stop, total)):
            return results, total


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--subset", required=True)
    ap.add_argument("--pid", required=True)
    ap.add_argument("--put", required=True, help="mã bài AC dùng làm chương trình sinh viên kiểm thử")
    ap.add_argument("--manifest", required=True, help="pXXXXX_heldout_manifest.csv đã khoá")
    ap.add_argument("--suite", action="append", required=True, help="nhãn=đường_dẫn_lớp_test.java (vd before=..., after=...)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--junit-api", default="", help="classpath của junit-jupiter-api, opentest4j, apiguardian")
    ap.add_argument("--timeout", type=float, default=4.0, help="giây cho mỗi test")
    ap.add_argument("--workers", type=int, default=max(2, os.cpu_count() or 2))
    ap.add_argument("--cache", default=None, help="thư mục lưu bản biên dịch của bài nộp (dùng chung giữa các phiên)")
    ap.add_argument("--ac-list", default=None, help="JSON của pick_ac.py: các bài AC độc lập để đối chiếu test")
    ap.add_argument("--review", default=None, help="CSV quyết định của người duyệt cho test bất đồng AC")
    a = ap.parse_args(argv)

    sub, out = Path(a.subset), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    cache = Path(a.cache) if a.cache else out / "_cache"
    h = prepare_harness(cache, a.junit_api)

    wa_ids = [r["submission_id"] for r in csv.DictReader(open(a.manifest, encoding="utf-8")) if r["trang_thai"] == "đánh giá"]
    man_sha = hashlib.sha256(Path(a.manifest).read_bytes()).hexdigest()

    put_dir = cache / a.pid / "AC" / a.put
    ok, err = compile_program((sub / "data" / a.pid / "AC" / f"{a.put}.java").read_text(encoding="utf-8", errors="replace"), put_dir)
    if not ok:
        raise SystemExit("PUT không biên dịch được: " + err)

    ac_ids, ac_dirs = [], {}
    if a.ac_list:
        acj = json.loads(Path(a.ac_list).read_text(encoding="utf-8"))
        if acj.get("put") != a.put:
            raise SystemExit("--ac-list được chọn cho PUT khác")
        for sid in acj["ac_doi_chieu"]:
            d = cache / a.pid / "AC" / sid
            ok, err = compile_program((sub / "data" / a.pid / "AC" / f"{sid}.java").read_text(encoding="utf-8", errors="replace"), d)
            if not ok:
                raise SystemExit(f"AC đối chiếu {sid} không biên dịch được: " + err)
            ac_ids.append(sid); ac_dirs[sid] = d
    review = {}
    if a.review and Path(a.review).exists():
        for r in csv.DictReader(open(a.review, encoding="utf-8")):
            q = r["quyet_dinh"].strip().lower()
            q = {"giữ": "giu", "loại": "loai"}.get(q, q)
            if q not in ("giu", "loai"):
                raise SystemExit(f"--review: quyet_dinh phải là giu hoặc loai, gặp {r['quyet_dinh']!r}")
            review[(r["suite_sha256"], r["test"])] = q

    def comp_wa(sid):
        d = cache / a.pid / "WA" / sid
        ok, _ = compile_program((sub / "data" / a.pid / "WA" / f"{sid}.java").read_text(encoding="utf-8", errors="replace"), d)
        return sid, ok
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        compiled = dict(ex.map(comp_wa, wa_ids))

    summary = {"problem_id": a.pid, "put": a.put, "manifest_sha256": man_sha, "WA_mau_so": len(wa_ids),
               "junit_api": a.junit_api or "junit_shim (bản thay thế tối giản)", "timeout_giay_moi_test": a.timeout,
               "ac_doi_chieu": ac_ids, "bo_test": {}}
    per_wa = {sid: {} for sid in wa_ids}
    for spec in a.suite:
        label, path = spec.split("=", 1)
        text = Path(path).read_text(encoding="utf-8")
        m = re.search(r"\bclass\s+(\w+)", text)
        cls = "codenet." + m.group(1)
        tdir = out / f"_test_{label}"
        shutil.rmtree(tdir, ignore_errors=True)
        sdir = tdir / "src" / "codenet"; sdir.mkdir(parents=True)
        (sdir / f"{m.group(1)}.java").write_text(with_package(text), encoding="utf-8")
        cp = os.pathsep.join([a.junit_api or str(h / "api"), str(h / "judge")])
        ok, err = javac([sdir / f"{m.group(1)}.java"], tdir / "cls", cp)
        rep = {"file": str(path), "sha256": hashlib.sha256(text.encode()).hexdigest()}
        if not ok:
            rep.update({"bien_dich": "lỗi", "loi": err, "fail_type": "method"})
            summary["bo_test"][label] = rep
            continue
        # chạy trên PUT hai lần; lần 1 ghi lại mọi đầu vào thực tế truyền vào Judge.run
        logf = tdir / "inputs.log"
        r1, n_tests = run_suite(h, a.junit_api, tdir / "cls", cls, put_dir, a.timeout, log=logf)
        r2, _ = run_suite(h, a.junit_api, tdir / "cls", cls, put_dir, a.timeout)
        s1, s2 = dict((n, s) for n, s, _ in r1), dict((n, s) for n, s, _ in r2)
        msg1 = dict((n, mm) for n, _, mm in r1)
        valid, invalid = [], []
        for name in sorted(set(s1) | set(s2)):
            if s1.get(name) == "PASS" and s2.get(name) == "PASS":
                valid.append(name)
            else:
                why = "lúc pass lúc fail trên PUT" if "PASS" in (s1.get(name), s2.get(name)) else \
                      f"{s1.get(name)} trên PUT: {msg1.get(name, '')}"
                invalid.append({"test": name, "ly_do": why,
                                "fail_type": {"TIMEOUT": "timeout", "EXIT": "harness"}.get(s1.get(name), "method")})
        # chạy riêng từng test trên PUT (mỗi test một JVM mới): test chỉ pass nhờ trạng thái do test trước để lại
        # (biến static của lớp test, tệp...) bị loại. Lý do: khi bài WA làm JVM dừng (System.exit, quá thời gian),
        # bộ chấm chạy tiếp các test sau trong JVM mới, nên test phụ thuộc thứ tự có thể fail mà không do bài WA.
        idx = {name: i for i, name in enumerate(sorted(set(s1) | set(s2)))}
        alone = {}
        for name in valid:
            rr, _ = run_suite(h, a.junit_api, tdir / "cls", cls, put_dir, a.timeout, start=idx[name], stop=idx[name] + 1)
            alone[name] = rr[0][1] if rr and rr[0][0] == name else "không chạy"
        for name in [t for t in valid if alone[t] != "PASS"]:
            invalid.append({"test": name, "ly_do": f"phụ thuộc thứ tự: {alone[name]} khi chạy riêng trên PUT",
                            "fail_type": "method"})
        valid = [t for t in valid if alone[t] == "PASS"]
        # kích thước bộ test = số đầu vào độc lập mà các test HỢP LỆ thực sự truyền vào Judge.run
        used = {}
        if logf.exists():
            for line in logf.read_text(encoding="utf-8").splitlines():
                name, b64 = line.split("\t", 1)
                used.setdefault(name, set()).add(norm_in(base64.b64decode(b64).decode("utf-8")))
        # test dùng đầu vào ngoài ràng buộc của đề: loại khỏi phép chấm (bài WA có thể sai ở đó mà vẫn đúng
        # trong phạm vi đề), ghi fail_type parse
        oor_tests = [t for t in valid if any(validate(a.pid, x) for x in used.get(t, ()))]
        for t in oor_tests:
            invalid.append({"test": t, "ly_do": "dùng đầu vào ngoài ràng buộc của đề", "fail_type": "parse"})
        oor = sorted({x for t in valid for x in used.get(t, ()) if validate(a.pid, x)})
        valid = [t for t in valid if t not in oor_tests]
        # đối chiếu với các bài AC độc lập: test hợp lệ trên PUT nhưng không PASS trên ít nhất một AC khác
        bat_dong = {}
        for ac in ac_ids:
            rr, _ = run_suite(h, a.junit_api, tdir / "cls", cls, ac_dirs[ac], a.timeout)
            st_ac = {n: s for n, s, _ in rr}
            for t in valid:
                if st_ac.get(t) != "PASS":
                    bat_dong.setdefault(t, []).append(f"{ac}:{st_ac.get(t, 'không chạy')}")
        quyet = {t: review.get((rep["sha256"], t), "chua_duyet") for t in bat_dong}
        valid_all = valid  # phân tích độ nhạy: giữ mọi test bất đồng
        valid = [t for t in valid if t not in bat_dong or quyet[t] == "giu"]
        distinct = sorted(set().union(*(used.get(t, set()) for t in valid))) if valid else []
        rep.update({"test_bat_dong_AC": [{"test": t, "ac_khong_pass": v, "quyet_dinh": quyet[t]}
                                         for t, v in sorted(bat_dong.items())],
                    "test_hop_le_khi_giu_bat_dong": len(valid_all)})
        rep.update({"bien_dich": "ok", "so_test": n_tests, "test_hop_le": len(valid), "ten_test_hop_le": valid,
                    "test_khong_hop_le": invalid,
                    "dau_vao_doc_lap": len(distinct), "dau_vao_ngoai_rang_buoc": len(oor),
                    "loi_goi_Judge_run_trong_ma_nguon_sau_bo_chu_thich": len(inputs_from_junit(text))})

        def eval_wa(sid):
            if not compiled.get(sid):
                return sid, "WA_khong_bien_dich", "WA_khong_bien_dich", "WA_khong_bien_dich"
            wd = cache / a.pid / "WA" / sid
            outs = []
            for _ in range(2):
                res, _n = run_suite(h, a.junit_api, tdir / "cls", cls, wd, a.timeout)
                st_all = {n: s for n, s, _ in res if n in valid_all}
                st = {n: s for n, s in st_all.items() if n in valid}
                prim = any(s == "FAIL" for s in st.values())
                sec = any(s in ("FAIL", "ERROR") for s in st.values())
                prim_all = any(s == "FAIL" for s in st_all.values())
                kinds = ",".join(sorted({s for s in st.values() if s != "PASS"}))
                outs.append((prim, sec, prim_all, kinds))
            on_dinh_all = outs[0][2] == outs[1][2]
            sens = ("phat_hien" if outs[0][2] else "khong") if on_dinh_all else "khong_on_dinh"
            if outs[0][:2] != outs[1][:2]:
                return sid, "khong_on_dinh", "khong_on_dinh", sens
            p, s, _pa, k = outs[0]
            return sid, ("phat_hien" if p else "khong"), ("phat_hien" if s else "khong") + (f" [{k}]" if k else ""), sens
        with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
            res = list(ex.map(eval_wa, wa_ids))
        n = len(wa_ids)
        prim = sum(1 for _, p, _, _ in res if p == "phat_hien")
        sec = sum(1 for _, _, s, _ in res if s.startswith("phat_hien"))
        sens = sum(1 for _, _, _, x in res if x == "phat_hien")
        unstable = sum(1 for _, p, _, _ in res if p == "khong_on_dinh")
        for sid, p, s, x in res:
            per_wa[sid][label] = (p, s, x)
        rep.update({"WA_phat_hien_assertion": prim, "WADR": round(prim / n, 4) if n else None,
                    "WADR_giu_bat_dong": round(sens / n, 4) if n else None,
                    "WA_phat_hien_assertion_hoac_ngoai_le": sec, "WADR_phu": round(sec / n, 4) if n else None,
                    "WA_khong_on_dinh": unstable,
                    "WA_co_TIMEOUT_hoac_EXIT": sum(1 for _, _, s, _ in res if "TIMEOUT" in s or "EXIT" in s)})
        summary["bo_test"][label] = rep
    labels = [s.split("=", 1)[0] for s in a.suite]
    if "before" in summary["bo_test"] and "after" in summary["bo_test"] and \
            summary["bo_test"]["before"].get("WADR") is not None and summary["bo_test"]["after"].get("WADR") is not None:
        b, af = summary["bo_test"]["before"], summary["bo_test"]["after"]
        summary["delta_WADR"] = round(af["WADR"] - b["WADR"], 4)
        summary["delta_WADR_phu"] = round(af["WADR_phu"] - b["WADR_phu"], 4)
        summary["delta_WADR_giu_bat_dong"] = round(af["WADR_giu_bat_dong"] - b["WADR_giu_bat_dong"], 4)
        summary["cham_tran_sau_phan_hoi_0_95"] = af["WADR"] >= 0.95
    with open(out / "per_wa.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["submission_id"] + [f"{l}_{k}" for l in labels for k in ("chinh", "phu", "giu_bat_dong")])
        for sid in wa_ids:
            w.writerow([sid] + [x for l in labels for x in per_wa[sid].get(l, ("", "", ""))])
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "bo_test"}, ensure_ascii=False))
    for l, r in summary["bo_test"].items():
        print(l, {k: r.get(k) for k in ("so_test", "test_hop_le", "dau_vao_doc_lap", "WADR", "WADR_phu", "WADR_giu_bat_dong", "WA_khong_on_dinh")})


if __name__ == "__main__":
    main()
