#!/usr/bin/env python3
"""Tạo phản hồi cho sinh viên đúng như trong môi trường của sinh viên: chương trình PUT (package codenet),
Judge.java của bộ công cụ nhóm (gọi thẳng Main.main), bộ JUnit 5 của sinh viên, JUnit 5 thật.

  --tool jacoco : chạy test với JaCoCo agent, xuất bảng "nhánh chưa phủ" (feedback_jacoco.md) + HTML/XML
  --tool pitest : chạy PITest (mutator mặc định), xuất bảng "mutant sống sót" (feedback_pitest.md) + HTML/XML

  python feedback.py --tool jacoco --lib lib --subset SUBSET --pid p03546 --put s575130508 \
      --test ex/p03546/SampleTest.java --out ex/p03546/fb_jacoco_before
"""
import argparse, json, os, re, shutil, subprocess, sys, xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wa_pilot import ENV  # noqa: E402

JUNIT = "junit-platform-console-standalone-1.10.2.jar"
PIT = ["pitest-1.16.1.jar", "pitest-entry-1.16.1.jar", "pitest-command-line-1.16.1.jar", "pitest-junit5-plugin-1.2.1.jar",
       "commons-text-1.10.0.jar", "commons-lang3-3.12.0.jar"]


def with_package(src):
    return "package codenet;\n\n" + re.sub(r"^\s*package\s+[\w.]+\s*;\s*", "", src, count=1, flags=re.M)


def build(a, lib, out):
    proj = out / "proj"
    shutil.rmtree(proj, ignore_errors=True)
    src = proj / "src" / "codenet"; src.mkdir(parents=True)
    (src / "Main.java").write_text(with_package((Path(a.subset) / "data" / a.pid / "AC" / f"{a.put}.java")
                                                .read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
    shutil.copy(HERE / "Judge.java", src / "Judge.java")
    ttext = Path(a.test).read_text(encoding="utf-8")
    tname = re.search(r"\bclass\s+(\w+)", ttext).group(1)
    tsrc = proj / "test" / "codenet"; tsrc.mkdir(parents=True)
    (tsrc / f"{tname}.java").write_text(with_package(ttext), encoding="utf-8")
    cls = proj / "classes"; tcls = proj / "test-classes"
    r = subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-g", "-d", str(cls), str(src / "Main.java"),
                        str(src / "Judge.java")], env=ENV, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("Không biên dịch được chương trình: " + r.stderr[:500])
    r = subprocess.run(["javac", "-nowarn", "-encoding", "UTF-8", "-g", "-d", str(tcls), "-cp",
                        os.pathsep.join([str(cls), str(lib / JUNIT)]), str(tsrc / f"{tname}.java")],
                       env=ENV, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("Không biên dịch được bộ test: " + r.stderr[:500])
    return proj, cls, tcls, "codenet." + tname


def code_line(src_lines, n):
    return src_lines[n - 1].strip().replace("|", "\\|") if 0 < n <= len(src_lines) else ""


def jacoco(a, lib, out, proj, cls, tcls, tclass):
    exec_f = out / "jacoco.exec"
    agent = f"-javaagent:{lib / 'jacocoagent.jar'}=destfile={exec_f},includes=codenet.Main*"
    r = subprocess.run(["java", agent, "-jar", str(lib / JUNIT), "execute", "--disable-banner", "--details=tree",
                        "-cp", os.pathsep.join([str(cls), str(tcls)]), "--select-class", tclass],
                       env=ENV, capture_output=True, text=True, timeout=600)
    (out / "junit_output.txt").write_text(r.stdout, encoding="utf-8")
    main_only = out / "main_only"; (main_only / "codenet").mkdir(parents=True, exist_ok=True)
    for f in (cls / "codenet").glob("Main*.class"):
        shutil.copy(f, main_only / "codenet" / f.name)
    subprocess.run(["java", "-jar", str(lib / "jacococli.jar"), "report", str(exec_f), "--classfiles", str(main_only),
                    "--sourcefiles", str(proj / "src"), "--xml", str(out / "jacoco.xml"), "--html", str(out / "html")],
                   env=ENV, capture_output=True, text=True, check=True)
    root = ET.parse(out / "jacoco.xml").getroot()
    lines = (proj / "src" / "codenet" / "Main.java").read_text(encoding="utf-8").split("\n")
    rows, cov, tot, missed_lines = [], 0, 0, 0
    for sf in root.iter("sourcefile"):
        for ln in sf.iter("line"):
            mb, cb = int(ln.get("mb")), int(ln.get("cb"))
            if int(ln.get("mi")) > 0:
                missed_lines += 1
            tot += mb + cb; cov += cb
            if mb:
                n = int(ln.get("nr")); rows.append(f"| {n} | {mb} / {mb + cb} | `{code_line(lines, n)}` |")
    md = [f"# Phản hồi JaCoCo: nhánh chưa được phủ ({a.pid})", "",
          f"Branch coverage: **{cov}/{tot}** ({100 * cov / tot:.1f}%)" if tot else "Chương trình không có nhánh.", ""]
    md += (["| Dòng | Nhánh chưa phủ / tổng nhánh | Mã nguồn |", "| ---: | :-: | :--- |"] + rows) if rows \
        else ["Không còn nhánh nào chưa được phủ."]
    (out / "feedback_jacoco.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    tests_ok = re.search(r"(\d+) tests successful", r.stdout); tests_fail = re.search(r"(\d+) tests failed", r.stdout)
    return {"branch_covered": cov, "branch_total": tot, "branch_coverage": round(cov / tot, 4) if tot else None,
            "dong_con_nhanh_chua_phu": len(rows), "dong_con_lenh_chua_chay": missed_lines,
            "junit_tests_successful": int(tests_ok.group(1)) if tests_ok else None,
            "junit_tests_failed": int(tests_fail.group(1)) if tests_fail else None}


def pitest(a, lib, out, proj, cls, tcls, tclass):
    rep = out / "pit"
    cp = os.pathsep.join([str(lib / j) for j in PIT] + [str(lib / JUNIT)])
    r = subprocess.run(["java", "-cp", cp, "org.pitest.mutationtest.commandline.MutationCoverageReport",
                        "--classPath", ",".join([str(cls), str(tcls)]),  # PITest tách bằng dấu phẩy
                        "--mutableCodePaths", str(cls),
                        "--targetClasses", "codenet.Main*", "--targetTests", tclass,
                        "--sourceDirs", str(proj / "src"), "--reportDir", str(rep),
                        "--outputFormats", "XML,HTML", "--timestampedReports=false", "--threads", "2"],
                       env=ENV, capture_output=True, text=True, timeout=1800)
    (out / "pit_log.txt").write_text(r.stdout + "\n" + r.stderr, encoding="utf-8")
    if not (rep / "mutations.xml").exists():
        raise SystemExit("PITest không tạo được báo cáo, xem pit_log.txt")
    root = ET.parse(rep / "mutations.xml").getroot()
    lines = (proj / "src" / "codenet" / "Main.java").read_text(encoding="utf-8").split("\n")
    muts = root.findall("mutation")
    killed = sum(1 for m in muts if m.get("detected") == "true")
    rows, st = [], {}
    for m in muts:
        s = m.get("status"); st[s] = st.get(s, 0) + 1
        if s in ("SURVIVED", "NO_COVERAGE"):
            n = int(m.findtext("lineNumber"))
            rows.append((n, s, m.findtext("description"), code_line(lines, n)))
    rows.sort()
    md = [f"# Phản hồi PITest: mutant sống sót ({a.pid})", "",
          f"Mutation score: **{killed}/{len(muts)}** ({100 * killed / len(muts):.1f}%)" if muts else "Không sinh được mutant.", ""]
    md += (["| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |", "| ---: | :-: | :--- | :--- |"] +
           [f"| {n} | {s} | {d} | `{c}` |" for n, s, d, c in rows]) if rows else ["Không còn mutant nào sống sót."]
    (out / "feedback_pitest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return {"mutants_total": len(muts), "mutants_killed": killed,
            "mutation_score": round(killed / len(muts), 4) if muts else None, "trang_thai": st,
            "mutant_song_sot_hoac_khong_phu": len(rows)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tool", choices=["jacoco", "pitest"], required=True)
    ap.add_argument("--lib", required=True); ap.add_argument("--subset", required=True)
    ap.add_argument("--pid", required=True); ap.add_argument("--put", required=True)
    ap.add_argument("--test", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    lib, out = Path(a.lib).resolve(), Path(a.out).resolve()
    shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    proj, cls, tcls, tclass = build(a, lib, out)
    res = (jacoco if a.tool == "jacoco" else pitest)(a, lib, out, proj, cls, tcls, tclass)
    res = {"problem_id": a.pid, "put": a.put, "tool": a.tool, "test": a.test, **res}
    (out / "summary.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
