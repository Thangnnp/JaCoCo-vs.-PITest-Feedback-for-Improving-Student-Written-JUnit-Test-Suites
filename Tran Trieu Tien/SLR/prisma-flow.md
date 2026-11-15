```text
PHỄU CHÍNH
[Paper từ IEEE Xplore, String A / IEEE-V1 (N = 241)]  +  [Paper nền trên thẻ RQ (N = 20)]
    ↓   bỏ 3 bản trùng (EC-D, xem search-log §3)
[Sau dedup (N = 258)]                    ← = số dòng source = search trong 01
    ↓
[Loại V1 (N = 58): EC-O = 14, IC-L = 0, IC-Y = 19, IC-I = 21, EC-N = 3, EC-A = 1]
    ↓
[Full-text đọc (N = 200)]                ← = INCLUDE 200 (source = search) trong 02
    ↓
[Loại V2 (N = 153): EC-A = 84, EC-I = 42, EC-N = 18, EC-O = 9]
    ↓
[Final phễu chính (N = 47)]              ← = dòng INCLUDE trong 03, source = search


NHÁNH SNOWBALLING (Seed 1 = R226, Straubinger 2024 & Seed 2 = R206, Fraser 2012)
[Snowballing (SS = 59)]                  ← = tổng "Số thêm vào 01": Seed 1 (6) + Seed 2 (53)
    ↓
[Loại V1 (N = 34): EC-O = 24, EC-N = 3, IC-Y = 7]
    ↓
[Full-text đọc (N = 25)]                 ← = INCLUDE 25 (Seed 1: 2, Seed 2: 23)
    ↓
[Loại V2 (N = 21): EC-O = 13, EC-N = 1, EC-S = 1, EC-A = 6]
    ↓
[Included từ snowballing (KK = 4)]       ← = tổng "Số include cuối" (Seed 1: 1 + Seed 2: 3)

TỔNG: Final included = 47 + 4 = 51       ← = số dòng INCLUDE trong 03
```
