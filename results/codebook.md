# Codebook: dữ liệu và kết quả thực nghiệm 24 người

Đơn vị: WADR, ΔWADR, d, θ̂ là tỉ lệ trong [0, 1] (ΔWADR, d, θ̂ trong [−1, 1]); thời gian tính bằng giây. Mã người: SV01–SV24; mã phiên: `SVxx-1`, `SVxx-2` (phiên 1, phiên 2). Điều kiện: `J` = JaCoCo, `P` = PITest. Định nghĩa WADR, ΔWADR, d, θ: proposal §4.

## data/lich_phien_thucnghiem_24.csv

| Cột | Nghĩa | Giá trị |
|---|---|---|
| `session_id` | Mã phiên | `SVxx-1`, `SVxx-2` |
| `sv_id` | Mã người tham gia | `SV01`–`SV24` |
| `thu_tu_phien` | Thứ tự phiên của người đó | 1, 2 |
| `pid` | Mã bài CodeNet | 12 bài chính (proposal §5.3) |
| `put` | Bài nộp Accepted dùng làm chương trình được kiểm thử | mã submission CodeNet |
| `tool` | Công cụ phản hồi của phiên | `jacoco`, `pitest` |
| `trinh_do` | Trình độ khai báo của người tham gia | `fresher`, `junior`, `semi-senior` |
| `slot` | Ô lịch crossover (proposal §5.6) | 1–24 |

## results/thucnghiem_24/phien_thucnghiem_24.csv

| Cột | Nghĩa | Giá trị |
|---|---|---|
| `session_id`, `sv_id`, `pid`, `thu_tu_phien` | Như lịch phiên | |
| `dieu_kien` | Điều kiện | `J`, `P` |
| `bien_dich_before` | Before.java biên dịch được | `ok`, `loi` |
| `so_test_before`, `so_test_after_T20` | Số phương thức @Test | số nguyên ≥ 0 |
| `hop_le_before`, `hop_le_after_T20` | Số test hợp lệ (pass trên PUT 2 lần, pass khi chạy riêng, đầu vào trong ràng buộc, không bất đồng AC) | số nguyên ≥ 0 |
| `WADR_before`, `WADR_after_T15`, `WADR_after_T20`, `WADR_after_T30` | WADR ở Before và ở mốc 15/20/30 phút; làm tròn 4 chữ số | [0, 1]; trống nếu bộ không biên dịch (After) |
| `dWADR_T20` | WADR(After T20) − WADR(Before) | [−1, 1] |
| `tool_giay_tb` | Thời gian trung bình một lần chạy công cụ | giây |
| `cham_giay` | Thời gian chấm phiên | giây |

## results/excluded.csv

| Cột | Nghĩa | Giá trị |
|---|---|---|
| `session_id`, `sv_id`, `dieu_kien`, `pid` | Phiên bị loại hoặc được ghi chú | |
| `fail_type` | Loại thất bại theo proposal §5.10 | `method`, `parse`, `timeout`, `harness`; trống nếu phiên bị loại chỉ vì phiên cùng người bị loại |
| `ly_do` | Lý do | văn bản |
| `pham_vi` | Phiên bị loại khỏi phân tích nào | văn bản |

## results/summary.csv

Mỗi dòng là một metric × điều kiện (mô tả) hoặc một phân tích trên d (kiểm định).

| Cột | Nghĩa | Giá trị |
|---|---|---|
| `metric` | Đại lượng | `WADR(Before)`, `WADR(After, T = 20)`, `ΔWADR (T = 20)`, `d = ΔWADR(P) − ΔWADR(J)` |
| `dieu_kien` | `J`, `P`, `P − J` (hiệu ghép cặp) hoặc `P so với J` (hệ số mô hình) | |
| `phan_tich` | Tên phân tích: chính, độ nhạy, phân tích bổ sung, nhóm con | văn bản |
| `N_hop_le` | Số phiên (dòng mô tả, mô hình) hoặc số người ghép cặp (dòng kiểm định) | số nguyên |
| `trung_vi`, `Q1`, `Q3` | Trung vị và tứ phân vị | |
| `kiem_dinh` | Kiểm định dùng | văn bản |
| `thong_ke` | Thống kê Wilcoxon (tổng hạng dương, Pratt) | |
| `p` | p hai phía, chưa làm tròn | [0, 1] |
| `HL_theta` | Ước lượng Hodges–Lehmann của θ | [−1, 1] |
| `CI95_thap`, `CI95_cao` | Khoảng tin cậy 95% (nghịch đảo Wilcoxon cho θ; Wald cho hệ số mô hình) | |
| `effect_size`, `loai_effect_size` | rank-biserial r ghép cặp (d ≠ 0; > 0 nghiêng về PITest) hoặc hệ số hồi quy của điều kiện P | r trong [−1, 1] |
| `delta` | Ngưỡng ý nghĩa thực tiễn δ | 0,10 (độ nhạy 0,05; 0,15) |
| `ket_luan` | Theo quy tắc proposal §4: "khác biệt đáng quan tâm" khi p < 0,05 và \|θ̂\| ≥ δ | `chưa thấy khác biệt`, `khác biệt đáng quan tâm` |
| `H0` | Kết quả kiểm định với α = 0,05 | `bác bỏ`, `không bác bỏ` |
| `nhan` | `exploratory` nếu phân tích không có trong proposal hoặc là nhóm con | |

## results/thucnghiem_24/phien/&lt;session_id&gt;/

`Before.java`, `After_r0.java` (= Before đổi tên lớp), `After_r1.java`–`After_r4.java` (sau lần chạy công cụ thứ 1–4; mốc 15/20/30 phút = r2/r3/r4); `tool_rK/feedback_jacoco.md` hoặc `feedback_pitest.md` và `summary.json` (báo cáo người tham gia nhận ở lần chạy K); `tool_rK/pit_log.txt` khi PITest dừng vì bộ test có test fail trên chương trình; `grade/summary.json`, `grade/per_wa.csv` (kết quả `junit_eval.py`).
