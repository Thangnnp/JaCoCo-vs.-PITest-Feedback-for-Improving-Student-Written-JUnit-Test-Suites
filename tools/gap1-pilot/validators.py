#!/usr/bin/env python3
"""Kiểm tra đầu vào có nằm trong ràng buộc của đề hay không (viết tay theo mục Constraints/Input của từng bài).
Đồng thuận của bài AC không đủ: bài AC có thể cho cùng output trên đầu vào ngoài ràng buộc.
validate(pid, text) -> "" nếu hợp lệ, hoặc lý do vi phạm. Bài chưa có validator: trả None (không kiểm)."""


def _ints(s):
    return [int(x) for x in s.split()]


def _rpn(s):
    t = s.split()
    nopd = sum(1 for x in t if x not in "+-*")
    nop = len(t) - nopd
    if not (2 <= nopd <= 100 and 1 <= nop <= 99):
        return "số toán hạng/toán tử ngoài ràng buộc"
    st = []
    for x in t:
        if x in "+-*":
            if len(st) < 2:
                return "biểu thức RPN không hợp lệ"
            b, a = st.pop(), st.pop()
            st.append(a + b if x == "+" else a - b if x == "-" else a * b)
        else:
            if not x.isdigit() or not (1 <= int(x) < 10**6):
                return "toán hạng ngoài [1, 10^6)"
            st.append(int(x))
        if abs(st[-1]) > 10**9:
            return "giá trị trên stack vượt 10^9"
    return "" if len(st) == 1 else "biểu thức RPN không hợp lệ"


def _p02917(s):
    v = _ints(s); n = v[0]; b = v[1:]
    return "" if 2 <= n <= 100 and len(b) == n - 1 and all(0 <= x <= 10**5 for x in b) else "ngoài ràng buộc"


def _p03378(s):
    v = _ints(s); n, m, x = v[:3]; a = v[3:]
    if not (1 <= n <= 100 and 1 <= m <= 100 and 1 <= x <= n - 1 and len(a) == m):
        return "N, M, X ngoài ràng buộc"
    if any(not (1 <= a[i] <= n) for i in range(m)) or any(a[i] >= a[i + 1] for i in range(m - 1)):
        return "A không tăng ngặt trong [1, N]"
    if x in a or 0 in a or n in a:
        return "có trạm thu phí ở ô 0, X hoặc N"
    return ""


def _p03416(s):
    a, b = _ints(s)
    return "" if 10000 <= a <= b <= 99999 else "ngoài ràng buộc"


def _p03813(s):
    v = _ints(s)
    return "" if len(v) == 1 and 1 <= v[0] <= 3000 else "ngoài ràng buộc"


def _p01137(s):
    v = _ints(s)
    if not v or v[-1] != 0 or any(x <= 0 or x > 10**6 for x in v[:-1]) or len(v) < 2:
        return "e ngoài (0, 10^6] hoặc thiếu dòng kết thúc 0"
    return ""


def _p02699(s):
    v = _ints(s)
    return "" if len(v) == 2 and all(1 <= x <= 100 for x in v) else "ngoài ràng buộc"


def _p03681(s):
    v = _ints(s)
    return "" if len(v) == 2 and all(1 <= x <= 10**5 for x in v) else "ngoài ràng buộc"


def _p03731(s):
    v = _ints(s); n, T = v[:2]; t = v[2:]
    if not (1 <= n <= 200000 and 1 <= T <= 10**9 and len(t) == n and t[0] == 0):
        return "N, T hoặc t_1 ngoài ràng buộc"
    if any(t[i] >= t[i + 1] for i in range(n - 1)) or t[-1] > 10**9:
        return "t không tăng ngặt hoặc vượt 10^9"
    return ""


def _p03546(s):
    v = _ints(s); h, w = v[:2]; c = v[2:102]; a = v[102:]
    if not (1 <= h <= 200 and 1 <= w <= 200 and len(c) == 100 and len(a) == h * w):
        return "kích thước ngoài ràng buộc"
    for i in range(10):
        for j in range(10):
            x = c[i * 10 + j]
            if (i == j and x != 0) or (i != j and not 1 <= x <= 1000):
                return "c ngoài ràng buộc"
    if any(not -1 <= x <= 9 for x in a) or all(x == -1 for x in a):
        return "A ngoài ràng buộc hoặc không có chữ số"
    return ""


def _p03196(s):
    v = _ints(s)
    return "" if len(v) == 2 and all(1 <= x <= 10**12 for x in v) else "ngoài ràng buộc"


def _p03351(s):
    v = _ints(s)
    return "" if len(v) == 4 and all(1 <= x <= 100 for x in v) else "ngoài ràng buộc"


def _p03633(s):
    v = _ints(s); n = v[0]; t = v[1:]
    if not (1 <= n <= 100 and len(t) == n and all(1 <= x <= 10**18 for x in t)):
        return "ngoài ràng buộc"
    from math import gcd
    l = 1
    for x in t:
        l = l * x // gcd(l, x)
    return "" if l <= 10**18 else "đáp án vượt 10^18"


RULES = {"p02263": _rpn, "p02917": _p02917, "p03378": _p03378, "p03416": _p03416, "p03813": _p03813,
         "p01137": _p01137, "p02699": _p02699, "p03681": _p03681, "p03731": _p03731, "p03546": _p03546,
         "p03196": _p03196, "p03351": _p03351, "p03633": _p03633}


def _p03253(s):
    v = _ints(s)
    return "" if len(v) == 2 and 1 <= v[0] <= 10**5 and 1 <= v[1] <= 10**9 else "ngoài ràng buộc"


def _p02729(s):
    v = _ints(s)
    return "" if len(v) == 2 and all(0 <= x <= 100 for x in v) and v[0] + v[1] >= 2 else "ngoài ràng buộc"


def _p00003(s):
    v = _ints(s); n = v[0]; r = v[1:]
    if not (1 <= n <= 1000 and len(r) == 3 * n):
        return "N ngoài ràng buộc hoặc thiếu dữ liệu"
    return "" if all(1 <= x <= 1000 for x in r) else "cạnh ngoài [1, 1000]"


def _p00144(s):
    v = _ints(s); i = 0; n = v[i]; i += 1
    if not 1 <= n <= 100:
        return "n ngoài ràng buộc"
    seen = set()
    for _ in range(n):
        r, k = v[i], v[i + 1]; ts = v[i + 2:i + 2 + k]; i += 2 + k
        if not (1 <= r <= n) or r in seen or len(ts) != k or any(not 1 <= t <= n for t in ts):
            return "thông tin router không hợp lệ"
        seen.add(r)
    p = v[i]; i += 1
    if not 0 <= p <= 1000 or len(v) - i != 3 * p:
        return "số gói tin không khớp"
    for j in range(p):
        a, b, ttl = v[i + 3 * j:i + 3 * j + 3]
        if not (1 <= a <= n and 1 <= b <= n and a != b and 0 <= ttl <= 10000):
            return "gói tin ngoài ràng buộc"
    return ""


def _p02240(s):
    v = _ints(s); n, m = v[0], v[1]
    if not (2 <= n <= 100000 and 0 <= m <= 100000):
        return "n, m ngoài ràng buộc"
    e = v[2:2 + 2 * m]; q = v[2 + 2 * m]; qs = v[3 + 2 * m:]
    if len(e) != 2 * m or not 1 <= q <= 10000 or len(qs) != 2 * q:
        return "số dòng không khớp"
    return "" if all(0 <= x < n for x in e + qs) else "id ngoài [0, n)"


def _p03712(s):
    lines = s.split("\n"); h, w = map(int, lines[0].split())
    rows = [l for l in lines[1:] if l != ""]
    if not (1 <= h <= 100 and 1 <= w <= 100 and len(rows) == h):
        return "H, W ngoài ràng buộc"
    return "" if all(len(r) == w and r.isalpha() and r.islower() for r in rows) else "pixel không hợp lệ"


RULES.update({"p03253": _p03253, "p02729": _p02729, "p00003": _p00003, "p00144": _p00144,
              "p02240": _p02240, "p03712": _p03712})


def _p02832(s):
    v = _ints(s); n = v[0]; a = v[1:]
    return "" if 1 <= n <= 200000 and len(a) == n and all(1 <= x <= n for x in a) else "ngoài ràng buộc"


def _p01125(s):
    t = s.split(); i = 0; ok_ds = 0
    while True:
        n = int(t[i]); i += 1
        if n == 0:
            break
        if not 1 <= n <= 20:
            return "N ngoài [1, 20]"
        gems = set()
        for _ in range(n):
            x, y = int(t[i]), int(t[i + 1]); i += 2
            if not (0 <= x <= 20 and 0 <= y <= 20) or (x, y) == (10, 10) or (x, y) in gems:
                return "toạ độ đá quý không hợp lệ"
            gems.add((x, y))
        m = int(t[i]); i += 1
        if not 1 <= m <= 30:
            return "M ngoài [1, 30]"
        x, y = 10, 10
        for _ in range(m):
            d, l = t[i], int(t[i + 1]); i += 2
            if d not in "NESW" or l <= 0:
                return "lệnh không hợp lệ"
            x += {"E": l, "W": -l}.get(d, 0); y += {"N": l, "S": -l}.get(d, 0)
            if not (0 <= x <= 20 and 0 <= y <= 20):
                return "robot ra ngoài phạm vi"
        ok_ds += 1
    return "" if ok_ds and i == len(t) else "thiếu dòng kết thúc 0"


def _p03274(s):
    v = _ints(s); n, k = v[0], v[1]; x = v[2:]
    if not (1 <= n <= 10**5 and 1 <= k <= n and len(x) == n):
        return "N, K ngoài ràng buộc"
    if any(abs(a) > 10**8 for a in x) or any(x[i] >= x[i + 1] for i in range(n - 1)):
        return "x không tăng ngặt hoặc vượt 10^8"
    return ""


def _p00013(s):
    v = _ints(s)
    if not 1 <= len(v) <= 100:
        return "số dòng ngoài [1, 100]"
    st, used = [], set()
    for x in v:
        if x == 0:
            if not st:
                return "lệnh 0 khi đường ray trống"
            st.pop()
        elif 1 <= x <= 10 and x not in used:
            st.append(x); used.add(x)
        else:
            return "số hiệu toa không hợp lệ hoặc lặp lại"
    return ""


RULES.update({"p02832": _p02832, "p01125": _p01125, "p03274": _p03274, "p00013": _p00013})


def _p04005(s):
    v = _ints(s)
    return "" if len(v) == 3 and all(2 <= x <= 10**9 for x in v) else "ngoài ràng buộc"


def _p03986(s):
    x = s.strip()
    if not (2 <= len(x) <= 200000 and len(x) % 2 == 0 and set(x) <= {"S", "T"} and x.count("S") == len(x) // 2):
        return "X không hợp lệ"
    return ""


def _p02909(s):
    return "" if s.strip() in ("Sunny", "Cloudy", "Rainy") else "ngoài ràng buộc"


def _p02681(s):
    t = s.split()
    if len(t) != 2:
        return "sai định dạng"
    a, b = t
    ok = a.isalpha() and a.islower() and b.isalpha() and b.islower() and 1 <= len(a) <= 10 and len(b) == len(a) + 1
    return "" if ok else "ngoài ràng buộc"


RULES.update({"p04005": _p04005, "p03986": _p03986, "p02909": _p02909, "p02681": _p02681})




def _p03126(s):
    v = _ints(s)
    n, m = v[0], v[1]
    if not (1 <= n <= 30 and 1 <= m <= 30):
        return "N, M ngoài ràng buộc"
    i = 2
    for _ in range(n):
        k = v[i]; a = v[i + 1:i + 1 + k]; i += 1 + k
        if not (1 <= k <= m and len(a) == k and len(set(a)) == k and all(1 <= x <= m for x in a)):
            return "danh sách món không hợp lệ"
    return "" if i == len(v) else "thừa hoặc thiếu số"


RULES["p03126"] = _p03126

def _pfix01(s):
    """Bài giả lập của verify_grader.py: dòng 1 là N (1..10), dòng 2 là N số nguyên trong [-100, 100]."""
    v = _ints(s)
    if not v:
        return "thiếu N"
    n, a = v[0], v[1:]
    return "" if 1 <= n <= 10 and len(a) == n and all(-100 <= x <= 100 for x in a) else "ngoài ràng buộc"


RULES["pFIX01"] = _pfix01

def validate(pid, text):
    f = RULES.get(pid)
    if f is None:
        return None
    try:
        return f(text)
    except (ValueError, IndexError):
        return "sai định dạng"
