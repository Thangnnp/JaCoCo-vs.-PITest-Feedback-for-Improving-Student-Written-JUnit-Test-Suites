# results: mini-pilot Tuần 8 và thực nghiệm 24 người Tuần 9

| File                                                              | Nội dung                                                                                                                                                                |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BAO_CAO_MINIPILOT_1_SINH_VIEN.md`                                | Báo cáo mini-pilot (5 người tham gia, 10 phiên)                                                                                                                         |
| `pilot_sessions.csv`                                              | Bảng 10 phiên: biên dịch, số test, test hợp lệ, WADR ở Before và các mốc 15/20/30 phút, ΔWADR, thời gian chạy công cụ và chấm                                           |
| `pilot_sessions/Sxx/`                                             | Before.java, After_r1–r4.java (mốc 15/20/30 phút = sau lần chạy công cụ thứ 2/3/4), báo cáo công cụ từng lần chạy, kết quả chấm`grade/summary.json`, `grade/per_wa.csv` |
| `pilot_analysis.ipynb`                                            | Phân tích pilot (8.3): metric ở T = 15/20/30, trần, phân phối, xác nhận kiểm định, độ nhạy                                                                              |
| `figures/`                                                        | Hình do notebook tạo                                                                                                                                                    |
| `full_analysis.ipynb`                                             | Phân tích thực nghiệm 24 người (Tuần 9): kiểm dữ liệu, N hợp lệ, mô tả, kiểm định chính, effect size, phân tích bổ sung và độ nhạy (§6), kết luận RQ1                   |
| `summary.csv`, `excluded.csv`, `codebook.md`, `run_manifest.json` | Bảng kết quả, mục bị loại, nghĩa các cột, cấu hình và phiên bản dữ liệu của lần chạy                                                                                    |
| `figures/fig1_distribution.png`, `figures/fig2_comparison.png`    | Hình thực nghiệm (300 DPI)                                                                                                                                              |
| `thucnghiem_24/`                                                  | Thực nghiệm 24 người (48 phiên) và kết quả phân tích. Đọc trước:`thucnghiem_24/README.md`                                                                               |

Lịch phiên: `data/lich_phien_minipilot.csv`. Metric: `tools/gap1-pilot/compute_metric.py`. Mục pilot không bao giờ đưa vào phân tích xác nhận.
