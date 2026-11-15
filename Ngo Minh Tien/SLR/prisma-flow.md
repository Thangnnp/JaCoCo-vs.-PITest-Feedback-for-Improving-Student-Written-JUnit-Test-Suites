# PRISMA Flow — Ngo Minh Tien (ACM Digital Library + snowballing)

## Current reproducible snapshot — 2026-10-20 (supersedes unreconciled row-count summaries)

These counts were recomputed from the current branch files `01_all_records.csv`, `02_after_screening_v1.csv`, `03_final_included.csv`, and the raw ACM-055 export. This block reports what those files directly support; it does **not** claim the full PRISMA flow is closed.

| Stage/check | Recomputed value | Status / interpretation |
|---|---:|---|
| Primary ACM Digital Library records in `01_all_records.csv` | 335 | Reproduced from `source=ACM Digital Library` |
| Snowball records currently appended | 125 | Reproduced from the combined corpus; not 125 proven globally unique studies |
| Teacher-source records | 18 | 6 teacher-list + 12 Zotero-source records |
| Additional targeted L3 record | 1 | `L3-001`; V1 EXCLUDE, retained in working corpus for traceability |
| Combined working corpus | 479 | 335 + 125 + 18 + 1 |
| Rows in `02_after_screening_v1.csv` | 282 | 138 primary + 125 snowball + 18 teacher + 1 L3 |
| V1 INCLUDE / EXCLUDE / UNCLEAR | 19 / 130 / 133 | Row-level decisions sum to 282; not final included counts |
| Final included rows in `03_final_included.csv` | 48 | 46 primary + 1 snowball (`SB-ACM055-066`) + 1 teacher (`TEACHER-004`) |
| Raw ACM-055 snowball export | 152 candidate rows | 46 backward + 106 forward |
| Raw candidates matching 335 primary records by normalized DOI/title | 22 | Row-level matching; 21 stored YES flags, so one flag discrepancy remains |

### V1 decisions by source

| Source group | INCLUDE | EXCLUDE | UNCLEAR | Rows |
|---|---:|---:|---:|---:|
| Primary ACM | 14 | 1 | 123 | 138 |
| Snowballing | 5 | 120 | 0 | 125 |
| Teacher-assigned list | 0 | 1 | 5 | 6 |
| Zotero teacher source | 0 | 7 | 5 | 12 |
| Targeted L3 search | 0 | 1 | 0 | 1 |
| **Total** | **19** | **130** | **133** | **282** |

### Items not yet reproducible — do not present as closed PRISMA counts

- The historical primary V2 breakdown of 46 included / 92 excluded cannot be reconstructed from per-record V2 decisions in the current V1 CSV; 46 primary records are present in the final-included file, but the 92 exclusions lack a complete decision ledger.
- The historical “157 full-text assessed / 109 excluded” combines the unverified primary V2 count with the 5 snowball V2 records and 14 teacher PDFs. Treat the total as historical until every assessed record has a source-level decision row.
- The 454 ACM hits are documented in the search log, but the export-access breakdown currently explains 335 captured + 106 inaccessible = 441, leaving 13 hits unaccounted for. Do not assign those 13 to a category without source evidence.
- The 152 raw snowball rows versus 125 appended rows is not fully explained by primary matching alone. The row-level report is a first reconciliation pass, not a complete global deduplication or V1/V2 audit.
- The four unavailable teacher full texts remain pending; they are not exclusions.

**Reporting rule:** use the reproduced 479 / 282 / 48 row counts with their stated units. Keep historical V2/full-text totals visibly marked as unreconciled; do not use them as confirmed final PRISMA flow values until the per-record decision ledger is restored.

---

> Số liệu đối chiếu với `01_all_records.csv`, `02_after_screening_v1.csv`, `03_final_included.csv`, `search-log.md` và `evidence-table.md` (snapshot 2026-10-13). Phân biệt số lượt tìm kiếm, số dòng collector, số bản ghi trong corpus, số lượt full-text đã đánh giá và số nghiên cứu được include cuối; các đơn vị này không thể thay thế cho nhau.

```text
PHỄU CHÍNH — ACM DIGITAL LIBRARY
[Search hits trên ACM (N = 454)]
    ↓
[Records captured/exported (N = 335)]
    ├── [Không truy cập được khi export (N = 106)]
    └── [13 hits chưa được giải trình trong breakdown hiện có]
    ↓  V1: title/abstract screening
[Loại V1 (N = 197)]
    ↓
[V1 accounting lịch sử: 138 được ghi nhận giữ lại (14 INCLUDE + 124 UNCLEAR)]
    ↓  V2 / full-text — số liệu lịch sử đã ghi nhận
[V2 accounting lịch sử (N = 138)]
    ├── [Loại V2 (N = 92; chưa có decision ledger đầy đủ trong CSV hiện tại)]
    └── [Included từ phễu chính (N = 46)]


NHÁNH SNOWBALLING — 1 SEED
[Seed = ACM-055: Does Automated Unit Test Generation Really Help Software Testers? A Controlled Empirical Study]
    ↓  1 lượt backward + 1 lượt forward
[Collector export (N = 152 rows): backward 46 + forward 106]
    ↓  125 dòng được append vào corpus; 27 dòng chênh lệch chưa được reconcile đầy đủ
[Snowball records trong 01 và 02 (N = 125)]
    ↓  V1
[Loại V1 (N = 120)]
    ↓
[Qua V1, chuyển sang V2 (N = 5)]
    ↓  V2 / full-text
[Loại V2 (N = 4)]
    ↓
[Included từ snowballing (N = 1): SB-ACM055-066]


TỔNG HỢP
[Full-text/V2 assessed (N = 157): primary 138 + snowball 5 + teacher PDFs 14]
    ├── [Loại full-text/V2 (N = 109): primary 92 + snowball 4 + teacher 13]
    └── [Final included (N = 48): primary 46 + snowball 1 + teacher 1]
[Unavailable teacher full texts still pending (N = 4; not yet assessed)]
```

## Kiểm cộng trừ

- V1 phễu chính (historical accounting): 197 EXCLUDE + 138 reported retained = 335 captured ✓
- Current `02_after_screening_v1.csv` primary rows: 14 INCLUDE + 123 UNCLEAR + 1 EXCLUDE = 138; this differs by one decision from the historical 14 INCLUDE + 124 UNCLEAR accounting and is explicitly left unreconciled.
- ACM access breakdown: 335 captured + 106 inaccessible = 441, còn 13/454 search hits chưa được giải trình trong breakdown hiện có; không tự gán 13 hits này vào một nhóm khi chưa có bằng chứng.
- Snowball collector: 46 backward + 106 forward = 152 rows ✓
- Snowball corpus/screening: 125 rows được append; chênh lệch 152 − 125 = 27 rows chưa được reconcile đầy đủ. Không diễn giải 125 rows là 125 nghiên cứu mới, duy nhất trên toàn cục.
- Snowball V1: 120 EXCLUDE + 5 chuyển V2 = 125 ✓
- Snowball V2: 4 EXCLUDE + 1 INCLUDE = 5 ✓
- Teacher-source full-text: 13 EXCLUDE + 1 INCLUDE = 14 PDFs screened; 4 unavailable PDFs remain pending and are not counted as exclusions.
- Full-text assessed: 138 primary (historical V2 accounting) + 5 snowball + 14 teacher PDFs = 157.
- Documented full-text exclusions: 92 primary (historical) + 4 snowball + 13 teacher = 109; 4 teacher PDFs remain pending.
- Final included: 46 primary + 1 snowball + 1 teacher = 48; matches the 48 records in `03_final_included.csv`. `evidence-table.md` has been updated to contain 48 study rows.

## Lưu ý kiểm toán

1. `01_all_records.csv` hiện có 478 dòng dữ liệu: 335 primary-search + 125 snowballing + 18 teacher-source records. `02_after_screening_v1.csv` hiện có 281 dòng: 138 primary-search + 125 snowballing + 18 teacher-source. V1 decisions in the current file total 19 INCLUDE, 129 EXCLUDE and 133 UNCLEAR; these are V1 decisions, not V2 outcomes.
2. Con số 46 INCLUDE / 92 EXCLUDE của phễu chính là V2 accounting được ghi nhận trước đó. Các trường V2 hiện để trống cho 138 primary-search rows trong CSV, nên không thể đếm lại độc lập 92 quyết định loại V2 từ file này. Cần khôi phục hoặc liên kết decision ledger theo từng record để tái lập đầy đủ.
3. Collector export 152 dòng chưa được xác nhận là 152 công trình riêng biệt. Còn sáu dòng thiếu title và các vấn đề chuẩn hóa/đối chiếu DOI, gồm biến thể `10.1109/sbst.2017..6` cần đối chiếu với `ACM-185`. Không báo cáo số nghiên cứu snowballing duy nhất toàn cục trước khi hoàn tất reconciliation.
4. 106 hits không export được được báo cáo riêng và không tính là records đã screening. Breakdown hiện tại chưa giải trình 13 hits còn lại trong tổng 454 search hits.
5. Evidence table contains the 48 final included studies (46 primary-search, 1 snowballing, 1 teacher-source). Do not add the 4 snowball records excluded at V2, the 120 snowball records excluded at V1, or the 13 teacher papers excluded at full text to final included.
