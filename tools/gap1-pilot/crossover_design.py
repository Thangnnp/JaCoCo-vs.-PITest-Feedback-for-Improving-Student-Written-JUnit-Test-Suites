#!/usr/bin/env python3
"""Lịch crossover và ước lượng cỡ mẫu cho GAP 1.

Thiết kế: mỗi sinh viên làm 2 phiên. Mỗi phiên là một chương trình KHÁC NHAU, một phiên với phản hồi
JaCoCo, một phiên với phản hồi PITest. Không sinh viên nào cải thiện cùng một chương trình bằng cả hai
loại phản hồi. Với mỗi khối 24 sinh viên, mỗi chương trình xuất hiện đúng 4 lần: (phiên 1, JaCoCo),
(phiên 1, PITest), (phiên 2, JaCoCo), (phiên 2, PITest), nên chương trình, thứ tự và loại phản hồi
được cân bằng hoàn toàn.

Phân tích chính: đơn vị là phiên (sinh viên x chương trình), kết quả là mức tăng tỉ lệ phát hiện WA
của phiên đó; mỗi sinh viên cho một hiệu d = Δ(PITest) − Δ(JaCoCo). Hồi quy d theo thứ tự làm bài
(phân tích crossover 2x2 chuẩn), nên các lượt chạy trên từng bài WA không bị xem là quan sát độc lập.

  python crossover_design.py schedule --students 24 --programs P1 ... P12 --seed 2026 --out schedule.csv
  python crossover_design.py power

Lưu ý 2026-10-28: phân tích chính hiện là Wilcoxon signed-rank trên d (proposal §6); hồi quy d theo thứ tự là phân
tích bổ sung. Lệnh `power` dùng SD từ Alonge (2025) và chỉ còn để đối chiếu bản cũ. Cỡ mẫu chính thức tính bằng
power_sim.py (mô phỏng nhiều kịch bản σ, ρ, τ; Wilcoxon signed-rank trên d).
"""
import argparse, csv, random, sys
from collections import Counter

import numpy as np

# Số liệu từng sinh viên của Alonge (2025), Table 5.1, tr. 48: FDR trước và sau (conceptual mutants)
ALONGE_BRANCH = [(0.615, 0.533), (0.643, 0.933), (0.706, 0.533), (0.706, 0.667), (0.588, 0.867)]
ALONGE_MUT = [(0.647, 0.733), (0.647, 0.800), (0.824, 0.933), (0.706, 0.933), (0.647, 0.600)]


def schedule(n_students, programs, seed):
    if n_students % 24 or len(programs) != 12:
        raise SystemExit("Lịch cân bằng cần 12 chương trình và số sinh viên là bội của 24.")
    rows = []
    for block in range(n_students // 24):
        for k in range(24):
            p1, p2 = programs[k % 12], programs[(k + 6) % 12]
            first = "JaCoCo" if k < 12 else "PITest"
            second = "PITest" if first == "JaCoCo" else "JaCoCo"
            rows.append({"slot": block * 24 + k + 1, "phien1_chuong_trinh": p1, "phien1_phan_hoi": first,
                         "phien2_chuong_trinh": p2, "phien2_phan_hoi": second})
    rng = random.Random(seed)
    ids = [f"SV{i:02d}" for i in range(1, n_students + 1)]
    rng.shuffle(ids)  # gán ngẫu nhiên sinh viên vào các ô của lịch
    for r, sid in zip(rows, ids):
        r["sinh_vien"] = sid
    return rows


def check_balance(rows):
    c = Counter()
    for r in rows:
        assert r["phien1_chuong_trinh"] != r["phien2_chuong_trinh"]
        c[(r["phien1_chuong_trinh"], 1, r["phien1_phan_hoi"])] += 1
        c[(r["phien2_chuong_trinh"], 2, r["phien2_phan_hoi"])] += 1
    return set(c.values())


def alonge_inputs():
    db = np.array([b - a for a, b in ALONGE_BRANCH])
    dm = np.array([b - a for a, b in ALONGE_MUT])
    return db, dm


def simulate_power(n, effect, sd_session, rho, sd_program, reps=4000, seed=1):
    """d_i = β + γ·thứ_tự + (v_progPIT − v_progJaCoCo) + (e_PIT − e_JaCoCo); phần ngẫu nhiên của sinh viên
    triệt tiêu trong hiệu. sd_session là độ lệch chuẩn của Δ một phiên; rho là tỉ phần phương sai do sinh viên."""
    from scipy import stats
    rng = np.random.default_rng(seed)
    sd_e = np.sqrt(max(sd_session ** 2 * (1 - rho) - sd_program ** 2, 1e-9))
    order = np.array([0.5] * (n // 2) + [-0.5] * (n - n // 2))
    X = np.column_stack([np.ones(n), order])
    hits = 0
    for _ in range(reps):
        d = effect + 0.0 * order + rng.normal(0, np.sqrt(2) * sd_program, n) + rng.normal(0, np.sqrt(2) * sd_e, n)
        beta, *_ = np.linalg.lstsq(X, d, rcond=None)
        resid = d - X @ beta
        s2 = resid @ resid / (n - 2)
        se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[0, 0])
        t = beta[0] / se
        if 2 * stats.t.sf(abs(t), n - 2) < 0.05:
            hits += 1
    return hits / reps


def main(argv=None):
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("schedule")
    s.add_argument("--students", type=int, default=24)
    s.add_argument("--programs", nargs=12, default=[f"P{i:02d}" for i in range(1, 13)])
    s.add_argument("--seed", type=int, default=2026)
    s.add_argument("--out", default="schedule.csv")
    sp.add_parser("power")
    a = ap.parse_args(argv)
    if a.cmd == "schedule":
        rows = schedule(a.students, a.programs, a.seed)
        print("Số lần mỗi (chương trình, phiên, phản hồi) xuất hiện:", check_balance(rows))
        with open(a.out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["sinh_vien", "slot", "phien1_chuong_trinh", "phien1_phan_hoi",
                                              "phien2_chuong_trinh", "phien2_phan_hoi"])
            w.writeheader(); w.writerows(sorted(rows, key=lambda r: r["slot"]))
        print("Đã ghi", a.out)
        return
    db, dm = alonge_inputs()
    sd_b, sd_m = db.std(ddof=1), dm.std(ddof=1)
    sd_pool = float(np.sqrt((sd_b ** 2 + sd_m ** 2) / 2))
    diff = dm.mean() - db.mean()
    print(f"Alonge 2025 (Table 5.1): Δ branch TB {db.mean():.3f} (SD {sd_b:.3f}); Δ mutation TB {dm.mean():.3f} "
          f"(SD {sd_m:.3f}); chênh {diff:.3f}; SD gộp {sd_pool:.3f}")
    print("n,hieu_ung,rho,power")
    for eff in (round(diff, 3), 0.10):
        for rho in (0.0, 0.3, 0.5):
            for n in (24, 48, 72, 96, 120):
                print(f"{n},{eff},{rho},{simulate_power(n, eff, sd_pool, rho, 0.05):.2f}")
    # hiệu ứng nhỏ nhất phát hiện được với 80% power
    for n in (24, 48):
        for rho in (0.0, 0.3, 0.5):
            lo, hi = 0.0, 0.5
            for _ in range(14):
                mid = (lo + hi) / 2
                if simulate_power(n, mid, sd_pool, rho, 0.05, reps=2000) >= 0.8:
                    hi = mid
                else:
                    lo = mid
            print(f"MDE n={n} rho={rho}: {hi:.3f}")


if __name__ == "__main__":
    main()
