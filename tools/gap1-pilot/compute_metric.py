#!/usr/bin/env python3
"""Tính metric của RQ1 từ kết quả chấm của junit_eval.py (gate E4, lộ trình Tuần 8).

Định nghĩa (proposal §4, §6):
  WADR       = số bài WA bị phát hiện / số bài WA trong manifest (mẫu số cố định của bài).
               Bài WA bị phát hiện khi ít nhất một test hợp lệ fail do assertion ở cả 2 lần chạy
               (junit_eval.py đã áp quy tắc này; trường "WA_phat_hien_assertion" và "WA_mau_so").
  ΔWADR      = WADR(After) − WADR(Before)
  d          = ΔWADR(P) − ΔWADR(J), tính cho từng sinh viên có đủ hai phiên
  θ̂          = ước lượng Hodges–Lehmann (giả trung vị) của d: trung vị mọi trung bình Walsh (d_i + d_j)/2, i ≤ j
  Kiểm định  = Wilcoxon signed-rank hai phía trên d, α = 0,05, hiệu bằng 0 xử lý theo Pratt
               (giữ khi xếp hạng, bỏ khỏi tổng hạng), hạng trùng lấy hạng trung bình
  Quy tắc    = "khác biệt đáng quan tâm" khi p < α VÀ |θ̂| ≥ δ; ngược lại "chưa thấy khác biệt" (không kết luận tương đương)

Quy tắc phiên (proposal §5.3, góp ý 27/10 mục 6):
  Before không biên dịch được -> WADR(Before) = 0, phiên vẫn giữ.
  After không biên dịch được  -> proposal chưa quy định; mặc định ở đây là KHÔNG tính phiên đó (--after-loi bo),
                                 phân tích độ nhạy với --after-loi bang_0 (After coi như không phát hiện bài nào).
  Sinh viên thiếu một phiên  -> bị loại khỏi phân tích ghép cặp.

  python compute_metric.py --sessions results/pilot_sessions --sample data/lich_phien_minipilot.csv --T after_T20 --out results/pilot_metric.json
  python compute_metric.py --self-test        # kiểm tra trên dữ liệu giả và các ca có đáp án tính tay
"""
import argparse, csv, json, math, sys, tempfile
from pathlib import Path

import numpy as np
from scipy import stats

ALPHA, DELTA = 0.05, 0.10


# ---------------------------------------------------------------- metric cơ bản
def wadr(detected, denom):
    if denom <= 0:
        raise ValueError("Mẫu số WA phải > 0")
    if not 0 <= detected <= denom:
        raise ValueError("Số WA phát hiện phải nằm trong [0, mẫu số]")
    return detected / denom


def wadr_of_suite(bo, denom, role, after_loi="bo"):
    """WADR của một bộ test trong summary.json của junit_eval. role: 'before' hoặc 'after'."""
    if bo is None:
        return None
    if bo.get("bien_dich") != "ok":
        if role == "before":
            return 0.0                      # quy tắc phiên: Before không biên dịch -> 0
        return 0.0 if after_loi == "bang_0" else None
    return wadr(bo["WA_phat_hien_assertion"], denom)


def hodges_lehmann(d):
    d = np.asarray(d, dtype=float)
    if d.size == 0:
        return float("nan")
    i, j = np.triu_indices(d.size)
    return float(np.median((d[i] + d[j]) / 2))


def wilcoxon_pratt(d):
    d = np.asarray(d, dtype=float)
    if d.size == 0 or np.all(d == 0):
        return float("nan"), float("nan")
    # Chọn phương pháp tường minh theo đúng mô tả ở §6 / power_sim.py: chính xác khi n ≤ 50 và không có hiệu bằng 0
    # hay hạng trùng; ngược lại xấp xỉ chuẩn (có hiệu chỉnh hạng trùng, không hiệu chỉnh liên tục).
    # Không dùng method="auto" vì từ SciPy 1.13 "auto" xử lý hiệu bằng 0 khác các bản cũ (cho p khác nhau theo phiên bản).
    absd = np.abs(d[d != 0])
    exact_ok = d.size <= 50 and np.all(d != 0) and np.unique(absd).size == absd.size
    r = stats.wilcoxon(d, zero_method="pratt", alternative="two-sided", method="exact" if exact_ok else "approx")
    return float(r.statistic), float(r.pvalue)


def decide(p, hl, alpha=ALPHA, delta=DELTA):
    if math.isnan(p) or math.isnan(hl):
        return "không đủ dữ liệu"
    return "khác biệt đáng quan tâm" if (p < alpha and abs(hl) >= delta) else "chưa thấy khác biệt"


# ---------------------------------------------------------------- đọc kết quả phiên
def load_sessions(sess_dir, sample_csv, T, after_loi):
    rows = {r["session_id"]: r for r in csv.DictReader(open(sample_csv, encoding="utf-8"))}
    out = []
    for sid, r in rows.items():
        f = Path(sess_dir) / sid / "grade" / "summary.json"
        rec = {"session_id": sid, "sv_id": r["sv_id"], "pid": r["pid"], "tool": r["tool"],
               "dieu_kien": "P" if r["tool"] == "pitest" else "J", "thu_tu_phien": int(r["thu_tu_phien"]),
               "trinh_do": r.get("trinh_do", ""), "WA_mau_so": None, "WADR_before": None, "WADR_after": None,
               "dWADR": None, "ghi_chu": ""}
        if not f.exists():
            rec["ghi_chu"] = "chưa có kết quả chấm"; out.append(rec); continue
        s = json.loads(f.read_text(encoding="utf-8"))
        denom = s["WA_mau_so"]; bo = s["bo_test"]
        b = wadr_of_suite(bo.get("before"), denom, "before")
        a = wadr_of_suite(bo.get(T), denom, "after", after_loi)
        rec.update({"WA_mau_so": denom, "WADR_before": b, "WADR_after": a,
                    "dWADR": None if (a is None or b is None) else a - b})
        notes = []
        if bo.get("before", {}).get("bien_dich") != "ok":
            notes.append("Before không biên dịch (WADR = 0)")
        if bo.get(T, {}).get("bien_dich") != "ok":
            notes.append("After không biên dịch (" + ("coi = 0" if after_loi == "bang_0" else "không tính") + ")")
        rec["ghi_chu"] = "; ".join(notes)
        out.append(rec)
    return out


def paired(sessions):
    by = {}
    for s in sessions:
        by.setdefault(s["sv_id"], {})[s["dieu_kien"]] = s
    res = []
    for sv, c in sorted(by.items()):
        ok = "J" in c and "P" in c and c["J"]["dWADR"] is not None and c["P"]["dWADR"] is not None
        res.append({"sv_id": sv, "dWADR_J": c.get("J", {}).get("dWADR"), "dWADR_P": c.get("P", {}).get("dWADR"),
                    "d": (c["P"]["dWADR"] - c["J"]["dWADR"]) if ok else None,
                    "trong_phan_tich": ok})
    return res


def analyse(sessions):
    pr = paired(sessions)
    d = [p["d"] for p in pr if p["trong_phan_tich"]]
    stat, p = wilcoxon_pratt(d)
    hl = hodges_lehmann(d)
    return {"n_ghep_cap": len(d), "d": d, "HL_theta": hl, "wilcoxon_stat": stat, "p": p,
            "ket_luan": decide(p, hl), "theo_sinh_vien": pr}


# ---------------------------------------------------------------- tự kiểm tra
def _fake_summary(denom, det_before, det_after, after_ok=True, before_ok=True, T="after_T20"):
    def bo(det, ok):
        return {"bien_dich": "ok" if ok else "lỗi", "WA_phat_hien_assertion": det if ok else None}
    return {"WA_mau_so": denom, "bo_test": {"before": bo(det_before, before_ok), T: bo(det_after, after_ok)}}


def self_test():
    ok = True

    def check(name, got, exp, tol=1e-4):
        nonlocal ok
        good = (isinstance(exp, str) and got == exp) or (not isinstance(exp, str) and abs(got - exp) <= tol)
        ok &= good
        print(f"[{'ĐẠT' if good else 'SAI'}] {name}: tính được {got!r}, đáp án tính tay {exp!r}")

    # 1. Output hoàn hảo -> metric cao nhất; output rỗng -> metric thấp nhất (yêu cầu gate E4)
    check("WADR bộ test bắt mọi WA (85/85)", wadr(85, 85), 1.0)
    check("WADR bộ test rỗng (0/85)", wadr(0, 85), 0.0)
    # 2. Ca tính tay từ dữ liệu thật: p03986 có 85 WA; Before bắt 20, After bắt 23
    check("WADR(Before) = 20/85", wadr(20, 85), 0.2353)
    check("ΔWADR = 23/85 − 20/85 = 3/85", wadr(23, 85) - wadr(20, 85), 0.0353)
    # 3. Hodges–Lehmann: d = [0,1; 0,2; 0,4] -> trung bình Walsh {0,1; 0,15; 0,2; 0,25; 0,3; 0,4} -> trung vị (0,2+0,25)/2
    check("Hodges–Lehmann của [0,1; 0,2; 0,4]", hodges_lehmann([0.1, 0.2, 0.4]), 0.225)
    # 4. Wilcoxon Pratt: d = [0; 0,1; −0,2; 0,3; 0,4]; hạng |d| = 1..5 (hạng 1 là hiệu 0, bỏ khỏi tổng)
    #    W+ = 2+4+5 = 11, W− = 3 -> thống kê = 3; xấp xỉ chuẩn Pratt: kỳ vọng = (5·6 − 1·2)/4 = 7,
    #    phương sai = (5·6·11 − 1·2·3)/24 = 13,5; z = (3 − 7)/√13,5 = −1,0887; p = 2Φ(−1,0887) = 0,2763
    st, p = wilcoxon_pratt([0, 0.1, -0.2, 0.3, 0.4])
    check("Wilcoxon (Pratt) thống kê", st, 3.0)
    check("Wilcoxon (Pratt) p hai phía", p, 0.2763, tol=5e-4)
    # 5. Quy tắc kết luận
    check("Quy tắc: p = 0,2763, θ̂ = 0,225", decide(0.2763, 0.225), "chưa thấy khác biệt")
    check("Quy tắc: p = 0,01, θ̂ = 0,05 (< δ)", decide(0.01, 0.05), "chưa thấy khác biệt")
    check("Quy tắc: p = 0,01, θ̂ = −0,12", decide(0.01, -0.12), "khác biệt đáng quan tâm")
    # 6. Toàn bộ đường đi trên dữ liệu giả (2 sinh viên, 4 phiên) + quy tắc phiên
    with tempfile.TemporaryDirectory() as tdir:
        t = Path(tdir)
        fake = {"F1": ("SVA", "jacoco", _fake_summary(85, 20, 23)),
                "F2": ("SVA", "pitest", _fake_summary(100, 50, 60)),
                "F3": ("SVB", "jacoco", _fake_summary(85, 0, 10, before_ok=False)),
                "F4": ("SVB", "pitest", _fake_summary(100, 90, 0, after_ok=False))}
        with open(t / "s.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["session_id", "sv_id", "tool", "pid", "thu_tu_phien"])
            for i, (sid, (sv, tool, summ)) in enumerate(fake.items()):
                w.writerow([sid, sv, tool, "pX", 1 + i % 2])
                (t / sid / "grade").mkdir(parents=True)
                (t / sid / "grade" / "summary.json").write_text(json.dumps(summ), encoding="utf-8")
        s = {r["session_id"]: r for r in load_sessions(t, t / "s.csv", "after_T20", "bo")}
        check("Before không biên dịch -> WADR(Before) = 0", s["F3"]["WADR_before"], 0.0)
        check("ΔWADR của F3 = 10/85", s["F3"]["dWADR"], 10 / 85)
        a = analyse(list(s.values()))
        # SVA: d = (60−50)/100 − (23−20)/85 = 0,1 − 0,0353 = 0,0647; SVB: After của phiên P không biên dịch -> loại
        check("Số sinh viên ghép cặp (After lỗi -> bỏ)", a["n_ghep_cap"], 1)
        check("d của SVA = 0,1 − 3/85", a["d"][0], 0.1 - 3 / 85)
        s2 = load_sessions(t, t / "s.csv", "after_T20", "bang_0")
        a2 = analyse(s2)
        # SVB khi After lỗi coi = 0: ΔP = 0 − 0,9 = −0,9; ΔJ = 10/85; d = −0,9 − 0,1176 = −1,0176
        check("Độ nhạy After lỗi = 0: số ghép cặp", a2["n_ghep_cap"], 2)
        check("Độ nhạy After lỗi = 0: d của SVB", sorted(a2["d"])[0], -0.9 - 10 / 85)
    print("KẾT QUẢ:", "tất cả đạt" if ok else "có ca sai")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sessions"); ap.add_argument("--sample")
    ap.add_argument("--T", default="after_T20", choices=["after_T15", "after_T20", "after_T30"])
    ap.add_argument("--after-loi", dest="after_loi", default="bo", choices=["bo", "bang_0"])
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(0 if self_test() else 1)
    if not (a.sessions and a.sample):
        ap.error("cần --sessions và --sample (hoặc --self-test)")
    sess = load_sessions(a.sessions, a.sample, a.T, a.after_loi)
    res = {"T": a.T, "after_loi": a.after_loi, "alpha": ALPHA, "delta": DELTA, "phien": sess, **analyse(sess)}
    txt = json.dumps(res, ensure_ascii=False, indent=1, default=lambda x: None)
    if a.out:
        Path(a.out).write_text(txt, encoding="utf-8")
    print(txt)


if __name__ == "__main__":
    main()
