# Search Log

## A. Initial database search

| Date | Database / source | Query ID | Query | Raw records | Duplicates removed | After dedup / imported | Note |
|---|---|---|---|---:|---:|---:|---|
| 2026-10-06 | Semantic Scholar | OA-V1-02 | `("unit testing" OR JUnit OR "unit test") AND ("mutation testing" OR "mutation score" OR mutant) AND ("code coverage" OR "branch coverage" OR "line coverage") AND ("test augmentation" OR "test generation" OR "test improvement") AND Java` | 198 | 2 | 196 | Raw results exported via Zotero; 2 records removed during deduplication; 196 records retained/imported into file 01 |
| 2026-10-06 | **Database search subtotal** | **OA-V1-02** | **Semantic Scholar** | **198** | **2** | **196** | Raw retrieval count is 198; post-dedup count is 196 |

## B. Additional records tracked in screening file

| Source category | Count in file 02 | How to report |
|---|---:|---|
| Search | 196 | Records originating from the database search after deduplication |
| User-provided / manually added | 11 | Report separately from database retrieval; record provenance for each item |
| Snowball-backward | 4 | Records found by backward snowballing; do not count these as initial database hits |
| **Total records in file 02** | **211** | 196 + 11 + 4 |

**Clarification:** `196` is only the Semantic Scholar search set after deduplication. The current `01_all_records.csv` contains **230 records total**: 196 with `source = Semantic Scholar` plus 34 other/additional records (including manually added records, snowballing records, and records whose source needs checking). Thus 230 is the total in file 01, not the raw result count for the Semantic Scholar query.

## C. Snowballing log

| Date | Seed paper | Direction | Round | Records found | Records added to file 02 | Screening status |
|---|---|---|---:|---:|---:|---|
| 2026-10-15 | Seed paper needs to be explicitly confirmed in the project record | Backward reference-list snowballing | 1 | 4 | 4 | 1 INCLUDE, 3 UNCLEAR in V1; all require V2/full-text decision |

The four records currently marked `snowball-back` in file 02 are:
1. *Knowledge Matters: Injecting Project and Testing Knowledge into LLM-based Unit Test Generation* — UNCLEAR
2. *LLM Test Generation via Iterative Hybrid Program Analysis* — UNCLEAR
3. *TestART: Improving LLM-based Unit Testing via Co-evolution of Automated Generation and Repair Iteration* — UNCLEAR
4. *Mutation-Guided Unit Test Generation With a Large Language Model* — INCLUDE

## D. Screening snapshot (2026-10-15)

| File / status | Count |
|---|---:|
| Raw Semantic Scholar results before deduplication | 198 |
| Duplicates removed | 2 |
| Search records after deduplication / imported into 01 | 196 |
| `01_all_records.csv` total records | 230 |
| Records in 01 with `source = Semantic Scholar` | 196 |
| Other/additional records in 01 (source not Semantic Scholar) | 34 |
| `02_after_screening_v1_FINAL_Beautiful.csv` total records | 211 |
| V1 INCLUDE | 29 |
| V1 UNCLEAR | 13 |
| V1 EXCLUDE | 169 |
| `03_final_included_Perfect.csv` records | 42 |
| Records present in 01 but not represented in 02 (to reconcile) | 19 |

## E. Reproducibility notes and pending work

- The 198 raw results, 2 removed duplicates, and 196 retained/imported search records refer to different stages of the same database search; they are not interchangeable counts.
- The 19-record discrepancy between files 01 and 02 must be resolved before claiming complete screening coverage.
- The 42 records in file 03 do not yet match the 29 V1 INCLUDE records; manually added items and items without documented V2 decisions need record-level reconciliation. Do not treat all 42 as confirmed final included studies without that check.
- The exact seed paper and its selection rationale must be recorded. The seed is the starting paper; the four `snowball-back` records are papers discovered through snowballing, not the seed itself.
- Final PRISMA counts should follow the PRISMA 2020 flow-diagram structure for database/register and other-source records: https://www.prisma-statement.org/prisma-2020-flow-diagram
