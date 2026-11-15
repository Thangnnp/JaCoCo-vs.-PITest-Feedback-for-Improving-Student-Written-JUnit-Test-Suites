#!/usr/bin/env python3
"""Tổng hợp summary.json của wa_pilot.py thành các bảng Markdown cho tài liệu pilot."""
import json, sys
from pathlib import Path

reps = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
g = lambda d, k: d.get(k, 0)

print("| Bài | AC / WA trích | Loại do cấu trúc (AC/WA) | Trùng mã (AC/WA) | Lỗi biên dịch (AC/WA) | WA không tất định | WA đánh giá | Nhóm hành vi |")
print("|---|---|---|---|---|---|---|---|")
for r in reps:
    c = r["dem"]
    print(f"| {r['problem_id']} | {g(c,'AC_tong')} / {g(c,'WA_tong')} | {g(c,'AC_loai_cau_truc')} / {g(c,'WA_loai_cau_truc')} | "
          f"{g(c,'AC_trung_ma')} / {g(c,'WA_trung_ma')} | {g(c,'AC_loi_bien_dich')} / {g(c,'WA_loi_bien_dich')} | "
          f"{g(c,'WA_khong_tat_dinh')} | {r['WA_danh_gia']} | {r['nhom_hanh_vi_WA']} |")
print()
print("| Bài | Đầu vào (sample / bổ sung) | Hợp lệ (có oracle) | Sample khớp oracle | AC không tất định | Chương trình kiểm thử | Judge.run khớp | Kết quả chạy WA |")
print("|---|---|---|---|---|---|---|---|")
for r in reps:
    o, v, p = r["oracle"], r["dau_vao"], r["chuong_trinh_kiem_thu"]
    last = p["cac_lan_thu"][-1] if p["cac_lan_thu"] else {}
    runs = ", ".join(f"{k} {v2}" for k, v2 in sorted(r["ket_qua_chay_WA"].items()))
    print(f"| {r['problem_id']} | {v['sample']} / {v['extra']} | {o['dau_vao_hop_le']} | {o['sample_khop_oracle']}/{o['sample_tong']} | "
          f"{o['ac_khong_tat_dinh']} | {p['submission'] or 'không chọn được'} (thử {len(p['cac_lan_thu'])}) | {last.get('judge_khop','')} | {runs} |")
print()
print("| Bài | Bộ test | Số đầu vào độc lập | WA phát hiện (output khác) | Tỉ lệ | + tính ngoại lệ | Nhóm hành vi phát hiện | Tỉ lệ nhóm |")
print("|---|---|---|---|---|---|---|---|")
for r in reps:
    for name, d in r["phat_hien"].items():
        print(f"| {r['problem_id']} | {name} | {d['so_dau_vao_doc_lap']} | {d['phat_hien_MISMATCH']}/{r['WA_danh_gia']} | {d['ty_le']} | "
              f"{d['phat_hien_MISMATCH_hoac_RE']} | {d['nhom_hanh_vi_phat_hien']}/{r['nhom_hanh_vi_WA']} | {d['ty_le_nhom']} |")
