# Dữ liệu

Quy tắc (gate E2): `data/raw/` chỉ đọc. Mọi bước xử lý ghi ra file mới bằng script trong `tools/gap1-pilot/`, không sửa file trong `data/raw/`.

## data/raw/
Nguồn, giấy phép, ngày tải và cấu trúc cột: `data/raw/README.md`.

| File | Nội dung | Tạo bằng |
|---|---|---|
| `codenet_pilot_subset.zip` | Tập con IBM CodeNet ban đầu (15 bài): mã AC/WA Java, metadata, đề bài | `tools/gap1-pilot/codenet_subset.py` từ `Project_CodeNet.tar.gz`, seed 2026 |
| `codenet_pilot_subset_45.zip` | Tập con 45 bài theo cùng thứ tự seed (chứa cả 12 bài chính, bài dự phòng, bài pilot, bài luyện tập) | như trên |

SHA-256: `SHA256SUMS.txt`. Nguồn gốc: IBM Project CodeNet (Puri et al., 2021), https://github.com/IBM/Project_CodeNet.

## data/frozen/
- `main12/`: 12 bài chính, khoá ngày 2026-10-25. `frozen_index.json` ghi PUT, số WA đánh giá, SHA-256 của manifest và của tập đầu vào tham chiếu; `ac_check/` là 4 bài AC đối chiếu mỗi bài (khoá ngày 2026-10-28, SHA-256 trong `frozen_index.json`).
- `extra/`: bài 26 p04005 (dự phòng), 27 p03986 và 28 p02909 (pilot), 29 p02681 (luyện tập), khoá ngày 2026-10-29, cùng cấu trúc. Bài pilot và luyện tập không thuộc tập chính thức.

## Lịch phiên
- `lich_phien_minipilot.csv`: 10 phiên mini-pilot.
- `lich_phien_thucnghiem_24.csv`: 48 phiên thực nghiệm 24 người. Cột: `results/codebook.md`.
