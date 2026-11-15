# Phản hồi JaCoCo và PITest khi sinh thêm kiểm thử JUnit bằng tay

**Mã đề tài (Topic code):** FA26-W5-13
**Repo:** RT-SWT301-004-nhom3
**Môn:** SWT301 — Research-Based Learning
**Nhóm:** Nhóm 3 — Fall 2026
**Thành viên:** Phạm Nhật Thăng (LR), Trần Triều Tiên (PL), Ngô Minh Tiến (DG), Phùng Thanh Nhân (MS)
**Giảng viên hướng dẫn:** L.T.Q.Chi

## Tiến độ

- [x] RBL-1: Tìm paper (Tuần 6)
- [x] RBL-2 + RBL-3: Kiểm chứng RQ, Proposal (Tuần 7). Proposal bản \_7 (29/10) sửa theo email giảng viên 27/10, đã được giảng viên duyệt: `team-synthesis/proposal-v1.docx` và `team-synthesis/proposal-v1.pdf`. Gắn tag `proposal-v1` lên commit chứa bản được duyệt
- [x] RBL-4: Pilot (Tuần 8), Thực nghiệm đầy đủ (Tuần 9). Đã chạy mini-pilot (5 người tham gia, 10 phiên, 01–05/11) và thực nghiệm 24 người (48 phiên, 10–13/11): kết quả trong `results/` và `results/thucnghiem_24/`
- [x] RBL-5: Báo cáo và trình bày (Tuần 8-10)

## Tái lập kết quả

1. Cài Python 3.9+ (đã chạy với 3.13) và `pip install -r requirements.txt`; JDK 17+ (đã chạy với JDK 21).
2. Tải các file .jar vào `tools/gap1-pilot/lib/` theo danh sách trong `tools/gap1-pilot/README.md` (SHA-256 trong `tools/gap1-pilot/pilot-results-2026-10-24/SHA256_tools.txt`). Giải nén `data/raw/codenet_pilot_subset_45.zip` (nguồn và giấy phép: `data/raw/README.md`).
3. Chấm lại một phiên (tuỳ chọn): `tools/gap1-pilot/junit_eval.py` với manifest và danh sách AC trong `data/frozen/main12/` (cách gọi: `tools/gap1-pilot/README.md`). Kết quả chấm đã lưu ở `results/thucnghiem_24/phien/<session_id>/grade/`.
4. Tính metric: `python tools/gap1-pilot/compute_metric.py --sessions results/thucnghiem_24/phien --sample data/lich_phien_thucnghiem_24.csv --T after_T20 --after-loi bo --out <file>.json` (kiểm script: `--self-test`).
5. Phân tích đầy đủ: mở `results/full_analysis.ipynb`, Restart & Run All (hoặc `jupyter nbconvert --to notebook --execute --inplace results/full_analysis.ipynb`). Notebook ghi `results/summary.csv`, `results/excluded.csv` và hai hình trong `results/figures/`.

## Cấu trúc

- `team-synthesis/`: tổng hợp của nhóm. Proposal hiện hành: `proposal-v1.docx` (bản PDF: `proposal-v1.pdf`); GAP 1, pilot kỹ thuật và phản hồi email giảng viên: `gap1.md`.
- `<Thành viên>/SLR/`: SLR cá nhân (RBL-1, RBL-2).
- `tools/gap1-pilot/`: script chọn bài, khoá dữ liệu, tạo báo cáo JaCoCo/PITest, chấm phiên, kiểm chứng bộ chấm, mô phỏng cỡ mẫu; kết quả theo ngày trong `pilot-results-*`. Cách chạy: `tools/gap1-pilot/README.md`.
- `tools/codenet-toolchain/`: bộ kiểm tra công cụ bằng Maven của Tuần 7 (gate E3), đã được thay bằng `tools/gap1-pilot/`.
- `data/raw/`: tập con IBM CodeNet đã trích (chỉ đọc). `data/frozen/`: manifest bài WA, đầu vào tham chiếu, AC đối chiếu đã khoá bằng SHA-256.
- `data/lich_phien_minipilot.csv`: lịch 10 phiên mini-pilot (người tham gia, bài, công cụ, thứ tự phiên). `data/lich_phien_thucnghiem_24.csv`: lịch 48 phiên thực nghiệm.
- `results/`: kết quả và báo cáo mini-pilot. Đọc trước: `results/README.md`.
- `notes.md`: quyết định kỹ thuật, lệch so với proposal và nhật ký lỗi.
- `paper/`: các section của bài (`sections/` tiếng Anh, `sections_vi/` tiếng Việt), project LaTeX (`latex/`: `main.tex`, `references.bib`, hình), bản cuối `output/paper_final.pdf`, kiểm tra chất lượng (`quality/ai_check_log.md`) và bảng claim (`claims.md`).
- `presentation/`: slide trình bày `slides_final.pptx` và `slides_final.pdf`.
