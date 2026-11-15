#!/usr/bin/env python3
"""Sinh bộ JUnit baseline gồm đúng các cặp Sample Input/Output của đề (mỗi cặp một @Test).
  python make_sample_suite.py --subset SUBSET --pid p03546 --out SampleTest.java
"""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from desc_rules import extract_samples  # noqa: E402


def java_text_block(s: str) -> str:
    s = s.replace("\\", "\\\\").replace('"""', '\\"""')
    body = "".join("            " + l + "\n" for l in s.split("\n"))
    return '"""\n' + body + '            """'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subset", required=True); ap.add_argument("--pid", required=True)
    ap.add_argument("--out", required=True); ap.add_argument("--class-name", default="SampleTest")
    a = ap.parse_args()
    page = (Path(a.subset) / "problem_descriptions" / f"{a.pid}.html").read_text(encoding="utf-8", errors="replace")
    tests = []
    for i, (si, so) in enumerate(extract_samples(page), 1):
        si = si.lstrip("\n"); si = si if si.endswith("\n") else si + "\n"
        so = so.lstrip("\n").rstrip("\n")
        tests.append(f"""    @Test
    void sample{i}() {{
        assertEquals({java_text_block(so).rstrip()}.strip(), Judge.run({java_text_block(si.rstrip(chr(10)))}));
    }}
""")
    src = f"""package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của {a.pid}: các cặp Sample Input/Output của đề. */
class {a.class_name} {{
{chr(10).join(tests)}}}
"""
    Path(a.out).write_text(src, encoding="utf-8")
    print("đã ghi", a.out, len(tests), "test")


if __name__ == "__main__":
    main()
