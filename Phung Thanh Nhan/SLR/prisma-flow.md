# PRISMA Flow

## PHIẾU CHÍNH

```text
[Records trong 01 (N = 230; search sau dedup = 196 + nguồn khác = 34)]
        ↓
[Loại V1 trong 02 (N = 207 records không thuộc snowball-back)]
        ↓
[V1: INCLUDE = 28, UNCLEAR = 10, EXCLUDE = 169]
        ↓
[Final phiếu chính trong 03 (N = 41)]
        ← 32 source = search + 8 user-provided + 1 screening_v1_include

## NHÁNH SNOWBALLING
(seed = bài seed của dự án; backward snowballing)

[Snowballing được ghi trong 02 (N = 4)]
        ↓
[Loại V1: INCLUDE = 1, UNCLEAR = 3, EXCLUDE = 0]
        ↓
[Included từ snowballing trong 03 (N = 1)]

## TỔNG

TỔNG: Final included ghi trong 03 = 41 + 1 = 42
      ← tổng số dòng trong 03
```

**Lưu ý:** File 02 ghi 211 dòng: 196 search + 11 user-provided + 4 snowball-back. Số V1 ở phiếu chính phía trên được tính bằng cách loại 4 dòng snowball-back khỏi tổng 02; 28 = 27 search INCLUDE + 1 user-provided INCLUDE, 10 = 6 search UNCLEAR + 4 user-provided UNCLEAR, và 169 = 163 search EXCLUDE + 6 user-provided EXCLUDE. File 03 hiện có 42 dòng. Đây là số bài được ghi trong file 03; file 02 chưa có trường quyết định V2 đầy đủ để xác nhận riêng số loại V2.
