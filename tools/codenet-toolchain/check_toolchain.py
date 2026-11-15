#!/usr/bin/env python3
"""
Kiểm tra bộ công cụ thực nghiệm (bản tương đương test_api.py cho RQ của nhóm — không dùng API LLM).

Đóng gói một submission CodeNet thành dự án Maven + JUnit 5, chạy JaCoCo và PITest, rồi in ra
đúng hai loại phản hồi mà sinh viên sẽ nhận trong thực nghiệm:
  - JaCoCo : branch coverage + danh sách nhánh chưa phủ (theo dòng)
  - PITest : mutation score + danh sách mutant sống sót (theo dòng)

Cách dùng (Python 3.9+, JDK 17+, Maven 3.8+):
  python check_toolchain.py env
  python check_toolchain.py new --submission demo/Main.java --problem p02546 \
         --descriptions <đường dẫn problem_descriptions.tar.gz hoặc thư mục> --out projects/p02546_demo
  python check_toolchain.py run --project projects/p02546_demo
  python check_toolchain.py summarize --project projects/p02546_demo      # chỉ đọc lại báo cáo

Kết quả của `run`: <project>/feedback/summary.json, feedback_jacoco.md, feedback_pit.md
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tarfile
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "template"
DETECTED = {"KILLED", "TIMED_OUT", "MEMORY_ERROR", "RUN_ERROR"}   # PIT tính là "detected"


# --------------------------------------------------------------------------- tiện ích
def find_mvn() -> str | None:
    return shutil.which("mvn") or shutil.which("mvn.cmd")


def run_cmd(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       shell=(sys.platform == "win32" and cmd[0].endswith(".cmd")))
    return p.returncode, (p.stdout or "") + (p.stderr or "")


# --------------------------------------------------------------------------- env
def cmd_env(_args) -> int:
    ok = True
    java = shutil.which("java")
    if not java:
        print("[X] Không thấy java. Cài JDK 17+ và thêm vào PATH.")
        ok = False
    else:
        _, out = run_cmd([java, "-version"])
        m = re.search(r'version "(\d+)', out)
        ver = int(m.group(1)) if m else 0
        vline = next((l for l in out.splitlines() if 'version' in l and not l.startswith('Picked up')), '?')
        print(f"[{'OK' if ver >= 17 else 'X'}] java: {vline}")
        ok &= ver >= 17
    mvn = find_mvn()
    if not mvn:
        print("[X] Không thấy Maven (mvn). Cài Maven 3.8+ và thêm vào PATH.")
        ok = False
    else:
        _, out = run_cmd([mvn, "-v"])
        mline = next((l for l in out.splitlines() if l.startswith('Apache Maven')), '?')
        print(f"[OK] maven: {mline}")
    return 0 if ok else 1


# --------------------------------------------------------------------------- new
def read_description(desc: Path, problem: str) -> str:
    name = f"{problem}.html"
    if desc.is_dir():
        for cand in (desc / name, desc / "problem_descriptions" / name):
            if cand.exists():
                return cand.read_text(encoding="utf-8", errors="replace")
    elif desc.suffixes[-2:] == [".tar", ".gz"] or desc.suffix == ".tgz":
        with tarfile.open(desc) as tf:
            for m in tf.getmembers():
                if m.name.endswith("/" + name) or m.name == name:
                    return tf.extractfile(m).read().decode("utf-8", errors="replace")
    raise SystemExit(f"Không tìm thấy mô tả {name} trong {desc}")


def extract_samples(page: str) -> list[tuple[str, str]]:
    """Lấy cặp (Sample Input k, Sample Output k) từ HTML mô tả bài (AIZU và AtCoder bản tiếng Anh)."""
    def grab(kind):
        found = {}
        for m in re.finditer(rf"Sample {kind}\s*(\d*)\s*</h\d>\s*(?:<[^>]+>\s*)*?<pre[^>]*>(.*?)</pre>",
                             page, flags=re.I | re.S):
            k = m.group(1) or "1"
            if k not in found:
                found[k] = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        return found
    ins, outs = grab("Input"), grab("Output")
    return [(ins[k], outs[k]) for k in sorted(ins, key=int) if k in outs]


def java_literal(s: str) -> str:
    s = s.replace("\r\n", "\n")
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t") + '"'


RISKS = [
    (r"System\.exit\s*\(", "gọi System.exit → JUnit/PIT bị dừng giữa chừng; nên loại submission này"),
    (r"static\s+[\w<>\[\], ]+\s+\w+\s*=\s*new\s+(Scanner|BufferedReader|InputStreamReader|FastReader|FastScanner)\b",
     "đọc System.in qua biến static → test thứ hai đọc phải stream cũ; nên loại hoặc sửa thành biến cục bộ"),
    (r"\bThread\b|\bExecutorService\b", "dùng thread → dễ timeout/flaky khi chạy PIT"),
    (r"new\s+File(Reader|InputStream)?\s*\(", "đọc file thay vì stdin"),
]


def cmd_new(args) -> int:
    src = Path(args.submission).read_text(encoding="utf-8", errors="replace")
    if not re.search(r"\bclass\s+Main\b", src):
        raise SystemExit("Submission không có class Main (CodeNet Java thường dùng Main) — kiểm tra lại file.")
    warnings = [msg for pat, msg in RISKS if re.search(pat, src)]
    src = re.sub(r"^\s*package\s+[\w.]+\s*;\s*", "", src, flags=re.M)
    out = Path(args.out)
    if out.exists() and any(out.iterdir()) and not args.force:
        raise SystemExit(f"{out} đã có nội dung (thêm --force để ghi đè).")
    main_dir, test_dir = out / "src/main/java/codenet", out / "src/test/java/codenet"
    main_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)
    artifact = re.sub(r"[^A-Za-z0-9_.-]", "_", out.name)
    (out / "pom.xml").write_text((TEMPLATE / "pom.xml").read_text(encoding="utf-8").replace("__ARTIFACT__", artifact),
                                 encoding="utf-8")
    (main_dir / "Main.java").write_text("package codenet;\n\n" + src, encoding="utf-8")
    shutil.copy(TEMPLATE / "Judge.java", test_dir / "Judge.java")

    samples = []
    if args.descriptions:
        samples = extract_samples(read_description(Path(args.descriptions), args.problem))
    lines = ["package codenet;", "", "import static org.junit.jupiter.api.Assertions.assertEquals;", "",
             "import org.junit.jupiter.api.Test;", "",
             "/** Test mẫu lấy từ Sample Input/Output của đề — CHỈ để kiểm tra bộ công cụ,",
             " *  KHÔNG phải bộ test baseline của sinh viên (baseline do sinh viên tự viết). */",
             "class SampleSmokeTest {"]
    for i, (inp, exp) in enumerate(samples, 1):
        lines += ["    @Test", f"    void sample{i}() {{",
                  f"        assertEquals(Judge.normalize({java_literal(exp)}), Judge.run({java_literal(inp)}));",
                  "    }", ""]
    if not samples:
        lines += ["    @Test", "    void placeholder() {", "        // Không lấy được sample từ đề: viết test tay ở đây.",
                  "        Judge.run(\"\");", "    }"]
    lines.append("}")
    (test_dir / "SampleSmokeTest.java").write_text("\n".join(lines) + "\n", encoding="utf-8")
    meta = {"problem": args.problem, "submission": str(Path(args.submission).name),
            "samples": len(samples), "warnings": warnings}
    (out / "codenet.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Tạo {out}  (bài {args.problem}, {len(samples)} test mẫu)")
    for w in warnings:
        print(f"[!] Cảnh báo: {w}")
    return 0


# --------------------------------------------------------------------------- summarize
def source_lines(project: Path) -> list[str]:
    f = project / "src/main/java/codenet/Main.java"
    return f.read_text(encoding="utf-8", errors="replace").splitlines() if f.exists() else []


def parse_jacoco(xml_path: Path) -> dict:
    root = ET.parse(xml_path).getroot()
    covered = missed = 0
    lines = []
    for pkg in root.iter("package"):
        for sf in pkg.iter("sourcefile"):
            if sf.get("name") != "Main.java":
                continue
            for c in sf.findall("counter"):
                if c.get("type") == "BRANCH":
                    covered += int(c.get("covered"))
                    missed += int(c.get("missed"))
            for ln in sf.findall("line"):
                mb, cb = int(ln.get("mb")), int(ln.get("cb"))
                if mb > 0:
                    lines.append({"line": int(ln.get("nr")), "missed_branches": mb, "covered_branches": cb})
    total = covered + missed
    return {"branch_covered": covered, "branch_total": total,
            "branch_coverage": round(covered / total, 4) if total else None, "uncovered": lines}


def parse_pit(xml_path: Path) -> dict:
    root = ET.parse(xml_path).getroot()
    muts = []
    for m in root.iter("mutation"):
        muts.append({"status": m.get("status"),
                     "line": int(m.findtext("lineNumber") or 0),
                     "method": m.findtext("mutatedMethod"),
                     "mutator": (m.findtext("mutator") or "").split(".")[-1],
                     "description": m.findtext("description") or ""})
    total = len(muts)
    detected = sum(m["status"] in DETECTED for m in muts)
    no_cov = sum(m["status"] == "NO_COVERAGE" for m in muts)
    survived = [m for m in muts if m["status"] in ("SURVIVED", "NO_COVERAGE")]
    return {"mutants_total": total, "mutants_detected": detected, "no_coverage": no_cov,
            "mutation_score": round(detected / total, 4) if total else None,
            "test_strength": round(detected / (total - no_cov), 4) if total - no_cov else None,
            "surviving": sorted(survived, key=lambda m: (m["line"], m["mutator"]))}


def cmd_summarize(args) -> int:
    project = Path(args.project)
    jx = project / "target/site/jacoco/jacoco.xml"
    px = project / "target/pit-reports/mutations.xml"
    src = source_lines(project)
    fb = project / "feedback"
    fb.mkdir(exist_ok=True)
    summary = {"project": project.name}
    code_at = (lambda n: src[n - 1].strip() if 0 < n <= len(src) else "")

    if jx.exists():
        j = parse_jacoco(jx)
        summary["jacoco"] = {k: v for k, v in j.items() if k != "uncovered"}
        rows = [f"| {u['line']} | {u['missed_branches']} / {u['missed_branches'] + u['covered_branches']} | `{code_at(u['line'])}` |"
                for u in j["uncovered"]]
        (fb / "feedback_jacoco.md").write_text(
            "# Phản hồi JaCoCo — nhánh chưa được phủ\n\n"
            f"Branch coverage: **{j['branch_covered']}/{j['branch_total']}**"
            f" ({(j['branch_coverage'] or 0) * 100:.1f}%)\n\n"
            "| Dòng | Nhánh chưa phủ / tổng nhánh | Mã nguồn |\n| ---: | :-: | :--- |\n" + "\n".join(rows) + "\n",
            encoding="utf-8")
    else:
        print(f"[!] Chưa có {jx} (chạy `run` trước).")
    if px.exists():
        p = parse_pit(px)
        summary["pit"] = {k: v for k, v in p.items() if k != "surviving"}
        rows = [f"| {m['line']} | {m['status']} | {m['description']} | `{code_at(m['line'])}` |" for m in p["surviving"]]
        (fb / "feedback_pit.md").write_text(
            "# Phản hồi PITest — mutant sống sót\n\n"
            f"Mutation score: **{p['mutants_detected']}/{p['mutants_total']}**"
            f" ({(p['mutation_score'] or 0) * 100:.1f}%)\n\n"
            "| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |\n| ---: | :-: | :--- | :--- |\n" + "\n".join(rows) + "\n",
            encoding="utf-8")
    else:
        print(f"[!] Chưa có {px} (chạy `run` không kèm --skip-pit).")
    (fb / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if ("jacoco" in summary) else 1


# --------------------------------------------------------------------------- run
def cmd_run(args) -> int:
    project = Path(args.project)
    mvn = find_mvn()
    if not mvn:
        raise SystemExit("Không thấy Maven. Chạy `python check_toolchain.py env` để kiểm tra.")
    goals = ["-B", "-q", "clean", "test"]
    if not args.skip_pit:
        goals.append("org.pitest:pitest-maven:mutationCoverage")
    print(f"[..] {Path(mvn).name} {' '.join(goals)}   (lần đầu Maven tải thư viện, có thể mất vài phút)")
    code, out = run_cmd([mvn, *goals], cwd=project)
    (project / "feedback").mkdir(exist_ok=True)
    (project / "feedback" / "maven.log").write_text(out, encoding="utf-8")
    if code != 0:
        print(out[-3000:])
        print("[X] Maven thất bại — xem feedback/maven.log. Lỗi thường gặp: test mẫu FAIL (PIT yêu cầu "
              "mọi test xanh), không tải được thư viện (mạng), sai phiên bản JDK.")
        return 1
    print("[OK] Maven chạy xong")
    return cmd_summarize(args)


def main(argv=None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("env")
    n = sub.add_parser("new")
    n.add_argument("--submission", required=True)
    n.add_argument("--problem", required=True, help="mã bài, vd p02546")
    n.add_argument("--descriptions", help="problem_descriptions.tar.gz hoặc thư mục giải nén (để lấy test mẫu)")
    n.add_argument("--out", required=True)
    n.add_argument("--force", action="store_true")
    r = sub.add_parser("run")
    r.add_argument("--project", required=True)
    r.add_argument("--skip-pit", action="store_true")
    s = sub.add_parser("summarize")
    s.add_argument("--project", required=True)
    args = ap.parse_args(argv)
    return {"env": cmd_env, "new": cmd_new, "run": cmd_run, "summarize": cmd_summarize}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
