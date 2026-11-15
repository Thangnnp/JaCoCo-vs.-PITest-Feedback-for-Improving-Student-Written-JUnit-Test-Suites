# data/raw: dữ liệu gốc (chỉ đọc)

Không sửa file trong thư mục này (gate E2). Mọi bước xử lý ghi ra file mới bằng script trong `tools/gap1-pilot/`.

## Nguồn

- IBM Project CodeNet, bản 1.0.0 (Puri et al., 2021, "CodeNet: A Large-Scale AI for Code Dataset for Learning a Diversity of Coding Tasks", NeurIPS Datasets and Benchmarks).
- Repo: https://github.com/IBM/Project_CodeNet (nhóm dùng bản fork của repo này theo liên kết giảng viên cung cấp)
- File tải về: `Project_CodeNet.tar.gz` (khoảng 7,8 GB), https://codait-cos-dax.s3.us.cloud-object-storage.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet.tar.gz
- Ngày trích tập con: 2026-10-24 (ngày ghi trong các file zip).

## Giấy phép

- Mã nguồn trong repo CodeNet: Apache-2.0 (file LICENSE của repo).
- Bộ dữ liệu: trang repo không ghi giấy phép riêng cho dữ liệu; một bản sao trên Hugging Face ghi CDLA-Permissive-2.0. Cần đối chiếu với tài liệu chính thức của IBM trước khi công bố gói tái lập (chưa xác minh).

## File

| File | Nội dung | Tạo bằng |
|---|---|---|
| `codenet_pilot_subset.zip` | Tập con ban đầu 15 bài | `tools/gap1-pilot/codenet_subset.py --codenet Project_CodeNet.tar.gz`, seed 2026 |
| `codenet_pilot_subset_45.zip` | Tập con 45 bài theo cùng thứ tự seed (gồm 12 bài chính, bài dự phòng, 2 bài pilot, bài luyện tập) | như trên |
| `SHA256SUMS.txt` | SHA-256 của hai file zip | `sha256sum` |

## Cấu trúc trong mỗi file zip

| Đường dẫn | Nội dung |
|---|---|
| `candidates.csv` | Mọi bài Java đủ điều kiện xét: `problem_id`, `dataset`, `name`, `java_ac`, `java_wa`, `samples`, `median_ac_code_size`, `median_ac_cpu_ms`, `eligible`, `reasons`, `order` |
| `selected.csv` | Các bài được chọn, cùng cột |
| `metadata/<pid>.csv` | Metadata CodeNet của mọi bài nộp: `submission_id`, `problem_id`, `user_id`, `date` (Unix time), `language`, `original_language`, `filename_ext`, `status`, `cpu_time` (ms), `memory` (KB), `code_size` (byte), `accuracy` |
| `problem_descriptions/<pid>.html` | Đề bài |
| `data/<pid>/...` | Mã nguồn Java của bài nộp Accepted và Wrong Answer |
