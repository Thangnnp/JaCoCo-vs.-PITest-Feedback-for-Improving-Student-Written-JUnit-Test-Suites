#!/usr/bin/env python3
"""Sinh đầu vào bổ sung do nhóm nghiên cứu viết (kiểm tra độ nhạy của thước đo, KHÔNG phải dữ liệu sinh viên).
Mỗi bài: các đầu vào biên viết tay + đầu vào ngẫu nhiên trong ràng buộc của đề (seed cố định).
  python gen_extra.py --out extra --n-random 8 --seed 2026
"""
import argparse, random
from pathlib import Path


def rpn(r, n_ops):
    # biểu thức RPN hợp lệ, giá trị trên stack trong [-1e9, 1e9]
    while True:
        toks, st = [], []
        need = n_ops
        while need or len(st) != 1:
            if len(st) >= 2 and (need == 0 or r.random() < 0.45):
                b, a = st.pop(), st.pop(); op = r.choice("+-*")
                v = a + b if op == "+" else a - b if op == "-" else a * b
                st.append(v); toks.append(op)
                if len(toks) > 0 and op and len(st) == 1 and need == 0:
                    pass
            else:
                if need == 0:
                    break
                x = r.choice([r.randint(1, 9), r.randint(1, 999999)])
                st.append(x); toks.append(str(x)); need -= 1 if len(toks) > 1 else 0
            if any(abs(v) > 10**9 for v in st):
                break
        if len(st) == 1 and abs(st[0]) <= 10**9 and toks.count("+") + toks.count("-") + toks.count("*") >= 1:
            return " ".join(toks) + "\n"


def gen(pid, r, k):
    out = []
    if pid == "p02263":
        out += ["1 2 -\n", "3 4 * 5 -\n", "999999 999 *\n", "1 2 3 4 + - *\n", "10 20 - 30 -\n"]
        out += [rpn(r, r.randint(2, 30)) for _ in range(k)]
    elif pid == "p02917":
        out += ["2\n0\n", "2\n100000\n", "3\n5 1\n", "3\n1 5\n", "5\n3 1 4 1 5\n"]
        for _ in range(k):
            n = r.randint(2, 100); out.append(f"{n}\n" + " ".join(str(r.randint(0, 10**5)) for _ in range(n - 1)) + "\n")
    elif pid == "p03378":
        out += ["2 1 1\n2\n", "5 1 2\n1\n", "5 1 2\n4\n", "10 4 5\n1 2 3 4\n", "100 1 99\n100\n"]
        for _ in range(k):
            n = r.randint(2, 100); x = r.randint(1, n - 1)
            pool = [i for i in range(1, n + 1) if i != x]
            a = sorted(r.sample(pool, r.randint(1, len(pool))))
            out.append(f"{n} {len(a)} {x}\n" + " ".join(map(str, a)) + "\n")
    elif pid == "p03416":
        out += ["10000 10000\n", "10001 10001\n", "99999 99999\n", "10000 99999\n", "12321 12321\n", "12320 12322\n"]
        for _ in range(k):
            a = r.randint(10000, 99999); out.append(f"{a} {r.randint(a, 99999)}\n")
    elif pid == "p03813":
        out += ["1\n", "1199\n", "1200\n", "1201\n", "3000\n"]
        out += [f"{r.randint(1, 3000)}\n" for _ in range(k)]
    elif pid == "p01137":
        out += ["1\n0\n", "2\n0\n", "1000000\n0\n", "27\n28\n64\n0\n", "999999\n0\n"]
        for _ in range(k):
            out.append("".join(f"{r.randint(1, 10**6)}\n" for _ in range(r.randint(1, 5))) + "0\n")
    elif pid == "p02699":
        out += ["1 1\n", "100 100\n", "100 99\n", "99 100\n", "1 100\n", "100 1\n"]
        out += [f"{r.randint(1, 100)} {r.randint(1, 100)}\n" for _ in range(k)]
    elif pid == "p03681":
        out += ["1 1\n", "1 2\n", "2 1\n", "1 3\n", "100000 100000\n", "100000 99999\n", "99999 100000\n"]
        for _ in range(k):
            n = r.randint(1, 10**5); out.append(f"{n} {max(1, min(10**5, n + r.choice([-1, 0, 1, 5])))}\n")
    elif pid == "p03731":
        out += ["1 1\n0\n", "1 1000000000\n0\n", "2 10\n0 10\n", "2 10\n0 5\n", "3 1000000000\n0 1000000000 2000000000\n"]
        for _ in range(k):
            n = r.randint(1, 50); T = r.choice([r.randint(1, 10), r.randint(1, 10**9)])
            t = sorted(r.sample(range(1, 10**9), n - 1)); out.append(f"{n} {T}\n" + " ".join(map(str, [0] + t)) + "\n")
    elif pid == "p03546":
        def cm(rr):
            return [[0 if i == j else rr.randint(1, 1000) for j in range(10)] for i in range(10)]
        def wall(h, w, rr, pneg=0.3):
            g = [[-1 if rr.random() < pneg else rr.randint(0, 9) for _ in range(w)] for _ in range(h)]
            if all(v == -1 for row in g for v in row):
                g[0][0] = rr.randint(0, 9)
            return g
        def fmt(c, g):
            return f"{len(g)} {len(g[0])}\n" + "".join(" ".join(map(str, row)) + "\n" for row in c + g)
        c1 = [[0 if i == j else 1000 for j in range(10)] for i in range(10)]
        out.append(fmt(c1, [[1]])); out.append(fmt(c1, [[-1, 5]]))
        c2 = [[0 if i == j else 1000 for j in range(10)] for i in range(10)]
        for i in range(10):
            c2[i][(i + 1) % 10] = 1  # đường đi vòng qua nhiều chữ số rẻ hơn đi thẳng
        out.append(fmt(c2, [[2, 0, 9]]))
        for _ in range(k):
            h, w = r.randint(1, 20), r.randint(1, 20); out.append(fmt(cm(r), wall(h, w, r)))
    elif pid == "p03196":
        out += ["1 1\n", "1 1000000000000\n", "1000000000000 1\n", "2 1000000000000\n", "3 24\n",
                "2 999999999989\n", "40 1099511627776\n"]
        for _ in range(k):
            out.append(f"{r.choice([r.randint(1, 5), r.randint(1, 10**12)])} {r.randint(1, 10**12)}\n")
    elif pid == "p03351":
        out += ["1 1 1 1\n", "1 100 100 1\n", "1 50 100 49\n", "1 50 100 50\n", "50 1 100 49\n", "100 50 1 50\n"]
        out += [" ".join(str(r.randint(1, 100)) for _ in range(4)) + "\n" for _ in range(k)]
    elif pid == "p03633":
        out += ["1\n1000000000000000000\n", "2\n1000000000000000000\n1000000000000000000\n", "3\n4\n6\n8\n"]
        for _ in range(k):
            ps = [2, 3, 5, 7, 11, 13]
            n = r.randint(1, 6)
            out.append(f"{n}\n" + "".join(f"{r.choice(ps) ** r.randint(1, 3)}\n" for _ in range(n)))
    elif pid == "p03253":
        out += ["1 1\n", "1 1000000000\n", "100000 1\n", "100000 1000000000\n", "3 8\n", "5 999999937\n",
                "100000 536870912\n"]
        for _ in range(k):
            out.append(f"{r.choice([r.randint(1, 10), r.randint(1, 10**5)])} {r.choice([r.randint(1, 1000), r.randint(1, 10**9)])}\n")
    elif pid == "p02729":
        out += ["2 0\n", "0 2\n", "1 1\n", "100 100\n", "0 100\n", "100 0\n", "1 0\n".replace("1 0", "2 1")]
        for _ in range(k):
            n = r.randint(0, 100); m = r.randint(max(0, 2 - n), 100); out.append(f"{n} {m}\n")
    elif pid == "p00003":
        out += ["1\n3 4 5\n", "1\n5 3 4\n", "1\n1 1 1\n", "1\n1000 1000 1000\n", "2\n6 8 10\n10 6 8\n",
                "1\n600 800 1000\n"]
        for _ in range(k):
            n = r.randint(1, 8); rows = []
            for _ in range(n):
                if r.random() < 0.4:
                    a, b, c = r.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)])
                    t = r.randint(1, 1000 // c); tri = [a * t, b * t, c * t]; r.shuffle(tri)
                else:
                    tri = [r.randint(1, 1000) for _ in range(3)]
                rows.append(" ".join(map(str, tri)))
            out.append(f"{n}\n" + "\n".join(rows) + "\n")
    elif pid == "p00144":
        def net(n, dens):
            lines = []
            for i in range(1, n + 1):
                ts = [j for j in range(1, n + 1) if j != i and r.random() < dens]
                lines.append(f"{i} {len(ts)}" + "".join(f" {t}" for t in ts))
            return lines
        out.append("2\n1 1 2\n2 0\n2\n1 2 2\n2 1 5\n")
        out.append("3\n1 1 2\n2 1 3\n3 0\n3\n1 3 3\n1 3 2\n1 3 0\n")
        out.append("2\n1 1 2\n2 1 1\n1\n1 2 1\n")
        for _ in range(k):
            n = r.randint(2, 30); lines = net(n, r.choice([0.05, 0.15, 0.4])); pk = []
            for _ in range(r.randint(1, 8)):
                a = r.randint(1, n); b = r.choice([x for x in range(1, n + 1) if x != a])
                pk.append(f"{a} {b} {r.choice([0, 1, 2, 3, r.randint(0, 10000)])}")
            out.append(f"{n}\n" + "\n".join(lines) + f"\n{len(pk)}\n" + "\n".join(pk) + "\n")
    elif pid == "p02240":
        out.append("2 0\n1\n0 1\n")
        out.append("2 1\n0 1\n2\n0 1\n1 0\n")
        out.append("3 1\n0 0\n2\n0 0\n1 2\n")
        out.append("5 4\n0 1\n1 2\n2 3\n3 4\n2\n0 4\n4 0\n")
        for _ in range(k):
            n = r.randint(2, 50); m = r.randint(0, 60)
            es = [f"{r.randrange(n)} {r.randrange(n)}" for _ in range(m)]
            qs = [f"{r.randrange(n)} {r.randrange(n)}" for _ in range(r.randint(1, 10))]
            out.append(f"{n} {m}\n" + "".join(e + "\n" for e in es) + f"{len(qs)}\n" + "".join(q + "\n" for q in qs))
    elif pid == "p03712":
        out += ["1 1\na\n", "1 5\nabcde\n", "3 1\na\nb\nc\n"]
        for _ in range(k):
            h, w = r.randint(1, 8), r.randint(1, 8)
            out.append(f"{h} {w}\n" + "".join("".join(r.choice("abcxyz") for _ in range(w)) + "\n" for _ in range(h)))
    elif pid == "p02832":
        out += ["1\n1\n", "1\n2\n".replace("1\n2", "2\n2 2"), "3\n1 2 3\n", "3\n3 2 1\n", "5\n2 3 1 2 3\n", "4\n2 2 2 2\n"]
        for _ in range(k):
            n = r.randint(1, 30); out.append(f"{n}\n" + " ".join(str(r.randint(1, min(n, r.choice([3, n])))) for _ in range(n)) + "\n")
    elif pid == "p01125":
        def ds(rr):
            x, y = 10, 10; path = set(); cmds = []
            for _ in range(rr.randint(1, 6)):
                d = rr.choice("NESW"); lim = {"N": 20 - y, "S": y, "E": 20 - x, "W": x}[d]
                if lim == 0:
                    continue
                l = rr.randint(1, lim); cmds.append(f"{d} {l}")
                for _ in range(l):
                    x += {"E": 1, "W": -1}.get(d, 0); y += {"N": 1, "S": -1}.get(d, 0); path.add((x, y))
            if not cmds:
                cmds = ["N 1"]; path = {(10, 11)}
            cells = [(a, b) for a in range(21) for b in range(21) if (a, b) != (10, 10)]
            g = set(rr.sample(sorted(path - {(10, 10)}), min(len(path - {(10, 10)}), rr.randint(1, 3))))
            if rr.random() < 0.5:
                g.add(rr.choice(cells))
            g = sorted(g)[:20]
            return f"{len(g)}\n" + "".join(f"{a} {b}\n" for a, b in g) + f"{len(cmds)}\n" + "".join(c + "\n" for c in cmds)
        out += ["1\n10 12\n1\nN 1\n0\n", "1\n0 0\n2\nW 10\nS 10\n0\n", "1\n20 20\n2\nE 10\nN 10\n0\n"]
        for _ in range(k):
            out.append("".join(ds(r) for _ in range(r.randint(1, 3))) + "0\n")
    elif pid == "p03274":
        out += ["1 1\n0\n", "1 1\n-100000000\n", "2 2\n-100000000 100000000\n", "3 2\n-5 -3 -1\n", "3 2\n1 3 5\n",
                "4 2\n-10 -1 2 20\n"]
        for _ in range(k):
            n = r.randint(1, 15); xs = sorted(r.sample(range(-10**8, 10**8 + 1), n)) if r.random() < 0.5 else sorted(r.sample(range(-30, 31), n))
            out.append(f"{n} {r.randint(1, n)}\n" + " ".join(map(str, xs)) + "\n")
    elif pid == "p00013":
        out += ["1\n0\n", "1\n2\n3\n0\n0\n0\n", "10\n0\n9\n0\n", "5\n"]
        for _ in range(k):
            cars = list(range(1, 11)); r.shuffle(cars); st = []; seq = []
            for c in cars[:r.randint(1, 10)]:
                seq.append(c); st.append(c)
                while st and r.random() < 0.4:
                    seq.append(0); st.pop()
            while st and r.random() < 0.7:
                seq.append(0); st.pop()
            out.append("".join(f"{x}\n" for x in seq))
    elif pid == "p04005":
        out += ["2 2 2\n", "2 3 4\n", "3 3 3\n", "1000000000 1000000000 1000000000\n", "999999999 999999999 999999999\n",
                "2 2 1000000000\n", "1000000000 3 5\n"]
        for _ in range(k):
            out.append(" ".join(str(r.choice([r.randint(2, 10), r.randint(2, 10**9)])) for _ in range(3)) + "\n")
    elif pid == "p03986":
        out += ["ST\n", "TS\n", "SSTT\n", "TTSS\n", "STST\n", "TSTS\n"]
        for _ in range(k):
            n = r.choice([r.randint(1, 6), r.randint(1, 50)]); x = list("S" * n + "T" * n); r.shuffle(x)
            out.append("".join(x) + "\n")
    elif pid == "p02909":
        out += ["Sunny\n", "Cloudy\n", "Rainy\n"]
    elif pid == "p03126":
        out += ["1 1\n1 1\n", "1 30\n1 30\n", "2 3\n3 1 2 3\n3 3 2 1\n", "2 2\n1 1\n1 2\n",
                "3 5\n5 1 2 3 4 5\n5 5 4 3 2 1\n1 5\n", "30 1\n" + "1 1\n" * 30]
        for _ in range(k):
            n, m = r.randint(1, 6), r.randint(1, 8)
            rows = []
            for _ in range(n):
                kk = r.randint(1, m); rows.append(f"{kk} " + " ".join(map(str, r.sample(range(1, m + 1), kk))))
            out.append(f"{n} {m}\n" + "\n".join(rows) + "\n")
    elif pid == "p02681":
        out += ["a\nab\n", "a\nba\n", "abc\nabcd\n", "abc\nabdd\n", "zzzzzzzzzz\nzzzzzzzzzzz\n", "ab\nbab\n"]
        for _ in range(k):
            n = r.randint(1, 10); a = "".join(r.choice("ab") for _ in range(n))
            b = a + r.choice("ab") if r.random() < 0.5 else "".join(r.choice("ab") for _ in range(n + 1))
            out.append(f"{a}\n{b}\n")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="extra"); ap.add_argument("--n-random", type=int, default=8)
    ap.add_argument("--seed", type=int, default=2026); ap.add_argument("--problems", nargs="*")
    a = ap.parse_args()
    pids = a.problems or ["p02263", "p02917", "p03378", "p03416", "p03813", "p01137", "p02699", "p03681",
                          "p03731", "p03546", "p03196", "p03351"]
    for pid in pids:
        r = random.Random(f"{a.seed}-{pid}")
        d = Path(a.out) / pid; d.mkdir(parents=True, exist_ok=True)
        for i, s in enumerate(gen(pid, r, a.n_random)):
            (d / f"x{i:02d}.in").write_text(s, encoding="utf-8")
        print(pid, len(list(d.glob('*.in'))))


if __name__ == "__main__":
    main()
