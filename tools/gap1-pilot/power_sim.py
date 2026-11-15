#!/usr/bin/env python3
"""Mô phỏng cỡ mẫu cho GAP 1 (thay cho cách lấy độ lệch chuẩn từ Alonge 2025, Table 5.1).

Vì sao không dùng số của Alonge: Alonge đo một đại lượng khác (tỉ lệ mutant khái niệm bị bắt ở bài kiểm tra sau),
trên 5 + 5 sinh viên Python, thiết kế giữa hai nhóm. Độ lệch chuẩn đó không phải độ lệch chuẩn của ΔWADR, và thiết kế
giữa nhóm không cho biết tương quan giữa hai phiên của cùng một sinh viên. Hiện CHƯA có số liệu nào ước lượng được
hai đại lượng này cho ΔWADR, nên script quét một dải giả định và cho bảng tra; mini-pilot (tuần 8) cho biết dòng nào
gần thực tế nhất. Mọi giả định nằm ở đầu file và trong bảng kết quả.

MÔ HÌNH (một phiên = một sinh viên i, một điều kiện c ∈ {J, P}, một bài p, một thứ tự k ∈ {1, 2}):
    ΔWADR(i, c) = μ + θ·[c = P] + π·[k = 2] + u_i + v_p + e_ic
  u_i ~ N(0, ρ·σ²)        hiệu ứng sinh viên (chung cho hai phiên của cùng người)
  e_ic ~ N(0, (1−ρ)·σ²)   phần riêng của từng phiên
  v_p ~ N(0, τ²)          hiệu ứng bài toán (bài dễ/khó cải thiện), rút một lần cho mỗi lần lặp
  σ  = độ lệch chuẩn của ΔWADR giữa các sinh viên làm CÙNG một bài, cùng điều kiện
  ρ  = tương quan giữa hai phiên của cùng một sinh viên khi không có hiệu ứng bài (tương quan ghép cặp)
  τ  = độ lệch chuẩn của hiệu ứng bài; π = hiệu ứng thứ tự (phiên 2 so với phiên 1)
  Phân bổ bài và thứ tự lấy đúng lịch crossover (crossover_design.py): ô k làm bài k và k+6, 12 ô đầu JaCoCo trước.
  Mỗi sinh viên cho d_i = ΔWADR(i, P) − ΔWADR(i, J). Var(d) = 2(1−ρ)σ² + 2τ² (khi π = 0).

KIỂM ĐỊNH CHÍNH (giống §6, chốt 2026-10-29): Wilcoxon signed-rank hai phía trên d, α = 0,05,
  scipy.stats.wilcoxon(zero_method="pratt"): hiệu bằng 0 được giữ khi xếp hạng rồi bỏ khỏi tổng hạng (Pratt);
  hạng trùng lấy hạng trung bình; method="auto": chính xác khi n ≤ 50 và không có hiệu bằng 0 hay hạng trùng,
  ngược lại xấp xỉ chuẩn có hiệu chỉnh hạng trùng. Ước lượng: Hodges–Lehmann (giả trung vị) trên mọi d, kể cả d = 0.
  power         = P(p < 0,05)
  P(quy tắc)    = P(p < 0,05 và |HL| ≥ δ)  (quy tắc kết luận "khác biệt đáng quan tâm", δ = 0,10)
  MDE           = θ nhỏ nhất (bước 0,01) có power ≥ 0,80
PHÂN TÍCH BỔ SUNG: hồi quy d theo hiệu ứng bài (12 bài, +1 bài PITest, −1 bài JaCoCo) và thứ tự; kiểm định t
  cho hệ số chặn. Chỉ để so sánh: phân tích này loại được τ nhưng tốn 12 bậc tự do.

KỊCH BẢN B (độ nhạy, --floor): ΔWADR bị chặn dưới ở 0 (bộ sau không phát hiện ít hơn bộ trước), μ = 0,10.
  Tạo nhiều phiên ΔWADR = 0 và hiệu d = 0 (hạng trùng, hiệu bằng 0) như dữ liệu thật có thể có.
  θ báo trong bảng là θ danh nghĩa; cột theta_thuc_te là chênh lệch trung bình sau khi chặn.

  python power_sim.py --out power_sim            # bảng chính + kịch bản B, seed 2026, 2000 lần lặp mỗi ô
"""
import argparse, csv, itertools, json
from pathlib import Path

import numpy as np
from scipy import stats

SIGMAS = [0.10, 0.15, 0.20, 0.25]
RHOS = [0.0, 0.3, 0.6]
TAUS = [0.0, 0.05, 0.10]
NS = [24, 48]
THETAS = [0.05, 0.10]
DELTA = 0.10
GRID = np.round(np.arange(0.01, 0.41, 0.01), 2)


def design(n):
    """(bài PITest, bài JaCoCo, PITest ở phiên 2?) cho từng sinh viên theo lịch crossover."""
    rows = []
    for b in range(n // 24):
        for k in range(24):
            p1, p2 = k % 12, (k + 6) % 12
            jac_first = k < 12
            rows.append((p2, p1, True) if jac_first else (p1, p2, False))
    return np.array([r[0] for r in rows]), np.array([r[1] for r in rows]), np.array([r[2] for r in rows])


def draw(n, sigma, rho, tau, pi, reps, rng, theta, floor=False, mu=0.10):
    """Trả về d (reps × n) và chênh lệch thực tế trung bình."""
    pp, pj, pit_second = design(n)
    u = rng.normal(0, np.sqrt(rho) * sigma, (reps, n))
    v = rng.normal(0, tau, (reps, 12))
    eP = rng.normal(0, np.sqrt(1 - rho) * sigma, (reps, n))
    eJ = rng.normal(0, np.sqrt(1 - rho) * sigma, (reps, n))
    yP = mu + theta + pi * pit_second + u + v[:, pp] + eP
    yJ = mu + pi * (~pit_second) + u + v[:, pj] + eJ
    if floor:
        yP, yJ = np.maximum(yP, 0), np.maximum(yJ, 0)
    return yP - yJ, float(np.mean(yP - yJ))


def hodges_lehmann(d):
    n = d.shape[1]
    i, j = np.triu_indices(n)
    return np.median((d[:, i] + d[:, j]) / 2, axis=1)


def wilcoxon_p(d):
    with np.errstate(all="ignore"):
        p = stats.wilcoxon(d, axis=1, zero_method="pratt").pvalue
    return np.nan_to_num(p, nan=1.0)  # mọi hiệu bằng 0: không bác bỏ


def mixed_p(d, n):
    pp, pj, pit_second = design(n)
    X = np.zeros((n, 12)); X[np.arange(n), pp] += 1; X[np.arange(n), pj] -= 1
    X = np.column_stack([np.ones(n), X[:, 1:], np.where(pit_second, 0.5, -0.5)])  # bỏ 1 cột bài (tổng = 0)
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = d @ X @ XtX_inv
    resid = d - beta @ X.T
    df = n - np.linalg.matrix_rank(X)
    se = np.sqrt((resid ** 2).sum(1) / df * XtX_inv[0, 0])
    return 2 * stats.t.sf(np.abs(beta[:, 0] / se), df)


def scenario(n, sigma, rho, tau, pi, reps, seed, floor=False):
    rng = np.random.default_rng(seed)
    base, _ = draw(n, sigma, rho, tau, pi, reps, rng, 0.0, floor)  # nhiễu chung, cộng θ (số ngẫu nhiên chung)
    out = {}
    if not floor:
        p0 = wilcoxon_p(base)
        out["sai_lam_loai_I"] = float(np.mean(p0 < 0.05))
        mde = None
        for th in GRID:
            if np.mean(wilcoxon_p(base + th) < 0.05) >= 0.80:
                mde = float(th); break
        out["MDE_wilcoxon"] = mde
    for th in THETAS:
        if floor:
            d, real = draw(n, sigma, rho, tau, pi, reps, np.random.default_rng(seed + int(th * 100)), th, True)
        else:
            d, real = base + th, th
        p = wilcoxon_p(d); hl = hodges_lehmann(d)
        out[f"power_{th:.2f}"] = float(np.mean(p < 0.05))
        out[f"P_quy_tac_{th:.2f}"] = float(np.mean((p < 0.05) & (np.abs(hl) >= DELTA)))
        if not floor:
            out[f"power_hoi_quy_{th:.2f}"] = float(np.mean(mixed_p(d, n) < 0.05))
        else:
            out[f"theta_thuc_te_{th:.2f}"] = round(real, 4)
            out[f"ti_le_d_bang_0_{th:.2f}"] = float(np.mean(d == 0))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--reps", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows = []
    for k, (n, sigma, rho, tau) in enumerate(itertools.product(NS, SIGMAS, RHOS, TAUS)):
        r = {"N": n, "sigma": sigma, "rho": rho, "tau": tau, "pi": 0.0,
             "SD_d": round(float(np.sqrt(2 * (1 - rho) * sigma ** 2 + 2 * tau ** 2)), 3)}
        r.update(scenario(n, sigma, rho, tau, 0.0, a.reps, a.seed + k))
        rows.append(r)
    extra = []  # hiệu ứng thứ tự và kịch bản B ở các ô đại diện
    for k, (n, sigma, rho) in enumerate(itertools.product(NS, [0.15, 0.20], [0.3])):
        r = {"N": n, "sigma": sigma, "rho": rho, "tau": 0.05, "pi": 0.05, "kich_ban": "A, có hiệu ứng thứ tự"}
        r.update(scenario(n, sigma, rho, 0.05, 0.05, a.reps, a.seed + 500 + k)); extra.append(r)
        r = {"N": n, "sigma": sigma, "rho": rho, "tau": 0.05, "pi": 0.0, "kich_ban": "B, chặn dưới ở 0, mu = 0,10"}
        r.update(scenario(n, sigma, rho, 0.05, 0.0, a.reps, a.seed + 700 + k, floor=True)); extra.append(r)
    for name, data in (("power_grid.csv", rows), ("power_extra.csv", extra)):
        keys = list(dict.fromkeys(k for r in data for k in r))
        with open(out / name, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(data)
    # bảng tóm tắt MDE (Wilcoxon, power 0,8) theo σ, ρ với τ = 0,05
    lines = ["# Mô phỏng cỡ mẫu (power_sim.py)", "",
             f"Seed {a.seed}, {a.reps} lần lặp mỗi ô, α = 0,05 hai phía, Wilcoxon signed-rank trên d.", "",
             "## MDE (power 0,80) theo σ và ρ, τ = 0,05", "",
             "| σ | ρ | SD(d) | MDE, N = 24 | MDE, N = 48 | power θ=0,10, N = 24 | power θ=0,10, N = 48 |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for sigma, rho in itertools.product(SIGMAS, RHOS):
        g = {r["N"]: r for r in rows if r["sigma"] == sigma and r["rho"] == rho and r["tau"] == 0.05}
        lines.append(f"| {sigma:.2f} | {rho:.1f} | {g[24]['SD_d']:.3f} | {g[24]['MDE_wilcoxon']} | {g[48]['MDE_wilcoxon']} | "
                     f"{g[24]['power_0.10']:.2f} | {g[48]['power_0.10']:.2f} |")
    lines += ["", "## Ảnh hưởng của τ (σ = 0,20, ρ = 0,3)", "",
              "| τ | sai lầm loại I N=24 | MDE N=24 | MDE N=48 | power Wilcoxon θ=0,10 N=24 / 48 | power hồi quy θ=0,10 N=24 / 48 |",
              "| --- | --- | --- | --- | --- | --- |"]
    for tau in TAUS:
        g = {r["N"]: r for r in rows if r["sigma"] == 0.20 and r["rho"] == 0.3 and r["tau"] == tau}
        lines.append(f"| {tau:.2f} | {g[24]['sai_lam_loai_I']:.3f} | {g[24]['MDE_wilcoxon']} | {g[48]['MDE_wilcoxon']} | "
                     f"{g[24]['power_0.10']:.2f} / {g[48]['power_0.10']:.2f} | "
                     f"{g[24]['power_hoi_quy_0.10']:.2f} / {g[48]['power_hoi_quy_0.10']:.2f} |")
    lines += ["", "## Kịch bản phụ", "", "| Kịch bản | N | σ | power θ=0,10 | P(quy tắc) θ=0,10 | ghi chú |", "| --- | --- | --- | --- | --- | --- |"]
    for r in extra:
        note = (f"θ thực tế {r['theta_thuc_te_0.10']}, tỉ lệ d = 0: {r['ti_le_d_bang_0_0.10']:.2f}" if "theta_thuc_te_0.10" in r
                else f"MDE {r['MDE_wilcoxon']}")
        lines.append(f"| {r['kich_ban']} | {r['N']} | {r['sigma']:.2f} | {r['power_0.10']:.2f} | {r['P_quy_tac_0.10']:.2f} | {note} |")
    t1 = [r["sai_lam_loai_I"] for r in rows]
    t0 = [r["sai_lam_loai_I"] for r in rows if r["tau"] == 0]
    lines += ["", f"Sai lầm loại I khi θ = 0: {min(t0):.3f}–{max(t0):.3f} khi τ = 0; {min(t1):.3f}–{max(t1):.3f} trên mọi ô. "
              "Khi τ > 0, hiệu d của các sinh viên không độc lập (dùng chung bài; lịch cân bằng làm tổng hiệu ứng bài bằng 0), "
              "nên Wilcoxon trở nên bảo thủ: sai lầm loại I dưới 0,05 và power thấp hơn một chút."]
    (out / "power_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "assumptions.json").write_text(json.dumps({"sigma": SIGMAS, "rho": RHOS, "tau": TAUS, "N": NS, "theta": THETAS,
                                                      "delta": DELTA, "alpha": 0.05, "reps": a.reps, "seed": a.seed},
                                                     ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
