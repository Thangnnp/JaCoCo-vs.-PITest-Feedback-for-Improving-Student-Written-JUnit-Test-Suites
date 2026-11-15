# PRISMA Flow — Phạm Nhật Thăng (OpenAlex + RQ card)

> Số khớp với `01_all_records.csv`, `02_after_screening_v1.csv`, `03_final_included.csv` ngày 2026-10-11, cập nhật 2026-10-18, 2026-10-19 2026-10-22 và 2026-10-24 cho lớp bổ sung Tuần 7. Các bài không truy cập được full-text đã loại theo EC-A.

```text
PHỄU CHÍNH
[Paper từ OpenAlex, String A / OA-V1-02 (N = 76)]  +  [Paper nền trên thẻ RQ (N = 20)]
    ↓  bỏ 6 bản trùng (EC-D, xem search-log §3)
[Sau dedup (N = 90)]                         ← = số dòng source = search trong 01
    ↓
[Loại V1 (N = 55): EC-O = 32, IC-L = 11, EC-N = 9, EC-S = 3]
    ↓
[Full-text đọc (N = 35)]                     ← = INCLUDE 14 + Unsure 21 (source = search) trong 02
    ↓
[Loại V2 (N = 13): IC-I = 8, IC-P = 2, EC-O = 2, EC-A = 1]
    ↓
[Final phễu chính (N = 22)]                  ← = dòng INCLUDE trong 03, source = search


NHÁNH SNOWBALLING (seed = DSpot, P10; 1 seed, 1 lượt backward + 1 lượt forward)
[Snowballing (SS = 19)]                      ← = tổng "Số thêm vào 01": backward 7 + forward 12
    ↓
[Loại V1 (N = 7): EC-N = 5, EC-O = 2]
    ↓
[Full-text đọc (N = 12)]                     ← = INCLUDE 1 + Unsure 11 (source = snowball-*) trong 02
    ↓
[Loại V2 (N = 7): IC-I = 4, EC-A = 3]
    ↓
[Included từ snowballing (KK = 5)]           ← = tổng "Số include cuối" = dòng INCLUDE trong 03, source = snowball-*

NHÁNH BỔ SUNG TUẦN 7 (RBL-2 Bước 2 mục 4 + kiểm phản chứng; không phải snowballing, xem search-log §8)
[OpenAlex Q1 + Web search Q3, Q4, Q5, Q7 + Semantic Scholar Q6 + giảng viên gợi ý Q8 (WS = 12)]   ← = dòng source = supplement-w7 trong 01
    ↓
[Loại V1 (N = 4): IC-L = 2, EC-O = 1, IC-E = 1]
    ↓
[Full-text đọc (N = 8)]                      ← = Unsure 8 (source = supplement-w7) trong 02
    ↓
[Loại V2 (N = 6): EC-O = 3, IC-I = 2, EC-A = 1]
    ↓
[Included từ lớp bổ sung (N = 2)]            ← P28, P29, source = supplement-w7 trong 03

TỔNG: Final included = 22 + 5 + 2 = 29      ← = số dòng INCLUDE trong 03 (P01–P29)
```

## Kiểm cộng trừ

- 76 + 20 − 6 = 90 ✓
- 90 − 55 = 35 ✓
- 35 − 13 = 22 ✓
- Snowballing: 7 + 12 = 19; 19 − 7 = 12; 12 − 7 = 5 ✓
- Lớp bổ sung Tuần 7: 12 − 4 = 8; 8 − 6 = 2 ✓
- 22 + 5 + 2 = 29 ✓ (01 có 121 dòng = 90 search + 7 snowball-back + 12 snowball-fwd + 12 supplement-w7)
