# results/thucnghiem_24: thực nghiệm 24 người (Tuần 9)

12 bài chính, lịch crossover 24 người (`data/lich_phien_thucnghiem_24.csv`), mỗi người 2 phiên (một JaCoCo, một PITest). Đủ 48/48 phiên.

| File | Nội dung |
|---|---|
| `phien/<session_id>/` | Before.java, After_r0–r4.java (mốc 15/20/30 phút = sau lần chạy công cụ thứ 2/3/4), báo cáo công cụ từng lần chạy (`tool_r*/`; `pit_log.txt` khi PITest dừng vì có test fail), kết quả chấm (`grade/summary.json`, `grade/per_wa.csv`) |
| `phien_thucnghiem_24.csv` | Bảng 48 phiên: biên dịch, số test, test hợp lệ, WADR ở Before và các mốc 15/20/30 phút, ΔWADR, thời gian chạy công cụ và chấm |
| `duyet_bat_dong_AC.csv`, `duyet_bat_dong_AC_khoa.csv` | Phiếu duyệt 3 test bất đồng AC (§5.4) và bảng khoá nối mã với phiên; không dùng (quyết định 2026-11-15 trong `notes.md`) |
| `phan_tich/metric_T{15,20,30}_after_loi_{bo,bang_0}.json` | Kết quả `tools/gap1-pilot/compute_metric.py`: WADR, ΔWADR theo phiên; d theo người; θ̂; Wilcoxon |

## Kết quả (quy tắc đăng ký trước: p < 0,05 và |θ̂| ≥ δ = 0,10)

| Phân tích | T | After không biên dịch | n ghép cặp | θ̂ (Hodges–Lehmann) | p (Wilcoxon, Pratt) | Kết luận |
|---|---|---|---|---|---|---|
| Chính | 20 | không tính | 22 | −0,012 | 0,483 | chưa thấy khác biệt |
| Độ nhạy | 20 | WADR = 0 | 24 | −0,016 | 0,350 | chưa thấy khác biệt |
| Độ nhạy | 15 | không tính | 23 | 0,000 | 0,927 | chưa thấy khác biệt |
| Độ nhạy | 15 | WADR = 0 | 24 | −0,006 | 0,774 | chưa thấy khác biệt |
| Độ nhạy | 30 | không tính | 22 | −0,012 | 0,504 | chưa thấy khác biệt |
| Độ nhạy | 30 | WADR = 0 | 24 | −0,016 | 0,365 | chưa thấy khác biệt |

Khoảng tin cậy 95% của θ̂ ở phân tích chính: [−0,118; 0,074]; rank-biserial r = −0,16. Bảng đầy đủ (kể cả mô hình hỗn hợp, crossover, nhóm con, thước đo phụ): `results/summary.csv`, `results/full_analysis.ipynb`.

d = ΔWADR(P) − ΔWADR(J). Ở phân tích chính: d > 0 ở 7 người, d < 0 ở 11 người, d = 0 ở 4 người; có hiệu bằng 0 nên Wilcoxon dùng xấp xỉ chuẩn. ΔWADR(T20) trung bình: JaCoCo 0,131 (24 phiên), PITest 0,119 (22 phiên). Hai người bị loại ở phân tích chính (SV14, SV24) có phiên PITest mà After T20 không biên dịch.

Lệnh tái tạo (từ thư mục gốc repo):

```
python tools/gap1-pilot/compute_metric.py --sessions results/thucnghiem_24/phien --sample data/lich_phien_thucnghiem_24.csv --T after_T20 --after-loi bo --out results/thucnghiem_24/phan_tich/metric_T20_after_loi_bo.json
```
