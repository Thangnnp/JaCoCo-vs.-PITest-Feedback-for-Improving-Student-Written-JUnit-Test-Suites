# Claims (RBL-5a, RBL-5b bước 1)

Mỗi claim chính ở §1, §5, §7 và Abstract một dòng. Evidence trỏ tới ô notebook, file kết quả hoặc trang/mục của paper được trích; Warrant là lý do evidence đủ để nói claim đó.

| # | Claim (nguyên văn trong bài) | Section | Evidence | Warrant | Người kiểm | Trạng thái |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

## Nguồn số liệu cho §4 và Abstract

| Số liệu | Giá trị | Nguồn |
|---|---|---|
| N mục tiêu / N tham gia / N hợp lệ ghép cặp | 48 / 24 / 22 (91,7%) | `results/full_analysis.ipynb` mục 2; `results/excluded.csv` |
| Số người có d = 0, d > 0, d < 0 | 4, 7, 11 | mục 3 |
| ΔWADR(T20) trung vị (IQR), J | 0,044 (0,000–0,198), 24 phiên | mục 3; `results/summary.csv` |
| ΔWADR(T20) trung vị (IQR), P | 0,000 (0,000–0,225), 22 phiên | mục 3; `results/summary.csv` |
| θ̂ Hodges–Lehmann, KTC 95% | −0,012 [−0,118; 0,074] | mục 5; `results/summary.csv` dòng "Chính" |
| Wilcoxon signed-rank (Pratt) | W = 100, p = 0,483 | mục 5 |
| Effect size rank-biserial r | −0,158 | mục 5 |
| Kết luận theo quy tắc §4 | không bác bỏ H0; chưa thấy khác biệt (\|θ̂\| < δ = 0,10) | mục 8 |
| Độ nhạy T = 15 / 30, After lỗi = 0, δ = 0,05 / 0,15, giữ test bất đồng AC, thước đo phụ, bỏ bài có báo cáo khó | cùng kết luận | mục 7; `results/summary.csv` |
| Mô hình hỗn hợp, hệ số điều kiện P | −0,010 [−0,101; 0,081], p = 0,829 | mục 7 |
| Crossover 2×2: θ tách thứ tự; hiệu ứng thứ tự | −0,021 [−0,130; 0,089]; 0,004 (p = 0,934) | mục 7 |
| Lần chạy PITest có báo cáo | 30/96 (lần 1: 12/24); JaCoCo 96/96 | mục 7 |
| Hiệu ứng trần (After T20 ≥ 0,95) | J 0/24; P 1/22 | mục 7 |
| Hình | `results/figures/fig1_distribution.png`, `fig2_comparison.png` | mục 3, mục 7 |

## Nguồn số liệu cho §5

| Số liệu | Giá trị | Nguồn |
|---|---|---|
| Phiên ΔWADR = 0 | 20 (J 9, P 11); 17 không thêm đầu vào hợp lệ mới, 3 có thêm nhưng không bắt thêm WA | `results/full_analysis.ipynb` mục 7b |
| Tỉ lệ test hợp lệ ở After T20 | J 91/223 = 41%; P 90/210 = 43% | mục 7b |
| Lý do 249 test không hợp lệ | expected sai 132 (53%); ngoại lệ trên chương trình đúng 81 (33%); ngoài ràng buộc 34 (14%); quá giờ 2 | mục 7b |
| ΔWADR TB phiên P có / không có báo cáo PITest (exploratory) | 0,173 (11 phiên) / 0,066 (11 phiên) | mục 7b |
| Thời gian TB một lần chạy công cụ | J 6,9 giây; P 7,2 giây | mục 7b; `results/thucnghiem_24/phien_thucnghiem_24.csv` |
| Mô hình hỗn hợp + số đầu vào độc lập, hệ số P | −0,028 | mục 7 |

Bản nháp các section: `paper/sections/` (tiếng Anh) và `paper/sections_vi/` (tiếng Việt, cùng số liệu).
