# Nhật ký tìm kiếm — Ngô Minh Tiến

## 1. Tìm kiếm cơ sở dữ liệu chính

| Researcher | Database | Search date | Query | Hits |
|---|---|---|---|---:|
| Ngo Minh Tien | ACM Digital Library | 2026-10-12 | (unit testing OR JUnit OR unit test) AND (mutation testing OR mutation score OR mutant*) AND (code coverage OR branch coverage OR line coverage) AND (test augmentation OR test generation OR test improvement) AND Java | 454 |

## 2. Thu thập và sàng lọc tìm kiếm chính (giữ nguyên)

- ACM search hits: **454**
- Records collected/exported: **335**
- Uncollected ACM hits: **106**
- Primary-search records in `01_all_records.csv`: **335**
- Historical primary-search V1 accounting: **335 = 14 INCLUDE, 124 UNCLEAR, 197 EXCLUDE** (the historical totals do not exactly match the current per-record decision values below).
- Current primary-search rows in `02_after_screening_v1.csv`: **138 = 14 INCLUDE, 123 UNCLEAR, 1 EXCLUDE**.
- Historical primary-search V2 accounting: **138 assessed = 46 INCLUDE, 92 EXCLUDE**; the 138 primary rows in the current combined CSV do not contain a complete per-record V2 decision ledger.

Đây là số liệu của tìm kiếm chính. Các ứng viên snowballing phải đi qua cùng quy trình xử lý bản ghi và không được tính là đã sàng lọc cho đến khi quyết định V1/V2 thực sự được ghi nhận.

## 3. Quy trình snowballing đã hiệu chỉnh — chỉ sử dụng một seed

Quy trình thăm dò trước đây sử dụng cả 46 bài INCLUDE ở V2 làm seed. Cách làm đó **không đáp ứng** quy trình đã hiệu chỉnh; số liệu trích dẫn của lượt chạy đó chỉ mang tính lịch sử. Lượt chạy hiện tại chỉ sử dụng đúng một seed.

### Seed được chọn

- **Record ID:** ACM-055
- **Title:** *Does Automated Unit Test Generation Really Help Software Testers? A Controlled Empirical Study*
- **Authors:** Gordon Fraser; Matt Staats; Phil McMinn; Andrea Arcuri; Frank Padberg
- **Year / venue:** 2015, ACM Transactions on Software Engineering and Methodology (TOSEM)
- **DOI:** [10.1145/2699688](https://doi.org/10.1145/2699688)
- **Điều kiện hợp lệ của seed:** có trạng thái INCLUDE ở V2 trong `03_final_included.csv`; PDF toàn văn được ghi nhận là sẵn có trong bảng V2.
- **Mức độ phù hợp với PICO:** P—phát triển/kiểm thử unit test; I—tạo unit test tự động bằng EvoSuite; C—viết test thủ công; O—độ bao phủ cấu trúc mã nguồn và lỗi phát hiện được. Bài phù hợp rõ với chủ đề tạo test tự động và hiệu quả kiểm thử; mutation score không phải trọng tâm chính trong phần tóm tắt, vì vậy không được phóng đại khía cạnh này.
- **Điều kiện số lượt trích dẫn:** lần kiểm tra trước trên Metascience Observatory Explorer ghi nhận 84 lượt trích dẫn (dữ liệu đến tháng 1/2025), nằm trong khoảng yêu cầu 10–200. Cần kiểm tra lại và ghi nguồn/ngày lấy số liệu khi thực hiện lượt thu thập đã hiệu chỉnh.
- **Tính duy nhất trong nhóm:** **chưa được xác minh**. Nhật ký tìm kiếm hiện có của các thành viên chưa ghi lại lựa chọn seed của những người khác. Không được khẳng định seed này duy nhất trong nhóm cho đến khi kiểm tra danh sách seed toàn nhóm.

### Cờ xác định seed duy nhất

Trong `01_all_records.csv`, `seed=TRUE` chỉ dành cho ACM-055; các bản ghi tìm kiếm chính còn lại có `seed=FALSE`. Cờ này xác định seed snowballing duy nhất được chọn, không thể hiện bản ghi có được đưa vào tổng quan hay không.

## 4. Quy trình thu thập và sàng lọc bản ghi

1. Thu thập tài liệu **trích dẫn ngược** từ ACM-055 và các công trình **trích dẫn xuôi** có trích dẫn ACM-055. Ghi lại công cụ/nguồn và ngày thu thập cho từng hướng.
2. Giữ nguyên thông tin nguồn gốc của bản ghi. Với cấu trúc 12 cột hiện có của `01_all_records.csv`, sử dụng:
   - `record_id`: unique stable ID that does not collide with existing IDs;
   - `source`: `Backward snowballing` or `Forward snowballing` plus the discovery backend;
   - `seed`: `FALSE` for discovered candidates (only ACM-055 is `TRUE`);
   - `query`: identify seed ACM-055 and direction/backend;
   - `fetched_date`: actual retrieval date.
3. Chuẩn hóa DOI và tiêu đề, sau đó loại trùng ứng viên giữa hai hướng và với corpus tìm kiếm chính hiện có. Giữ lại thông tin nguồn gốc/kiểm toán của bản ghi trùng; không tính các bản ghi đã có trong corpus chính thành bản ghi mới.
4. Chỉ thêm các bản ghi ứng viên mới đã loại trùng vào `01_all_records.csv`. Không tự tạo metadata; để trống trường không có dữ liệu và đánh dấu các bản ghi chưa xác minh để kiểm tra.
5. Sàng lọc tập bản ghi kết hợp ở V1 bằng cùng tiêu chí IC/EC và hệ thống nhãn quyết định như tìm kiếm chính. Ghi quyết định, lý do, ghi chú và người đánh giá cho từng bản ghi trong `02_after_screening_v1.csv`.
6. Chuyển các bản ghi INCLUDE/UNCLEAR ở V1 sang V2 theo quy trình hiện hành. Áp dụng cùng tiêu chí IC/EC cho toàn văn; ghi lại các trường hợp bị loại và reasons. Add only V2 INCLUDE papers to `03_final_included.csv`.
7. Update `evidence-table.md` and `prisma-flow.md` only from reconciled records and documented screening decisions.

## 5. Kiểm tra thu thập và loại trùng của lượt chạy đã hiệu chỉnh (kiểm tra ngày 2026-10-12)

### Số liệu corpus đang làm việc

| Check | Result |
|---|---:|
| Primary ACM records in `01_all_records.csv` | 335 |
| Corrected one-seed snowballing records appended | 125 |
| Total working-corpus records | 460 |
| Duplicate groups by normalized, non-empty title in the 460-record corpus | 0 |
| Duplicate groups by normalized, non-empty DOI in the 460-record corpus | 0 |
| Blank titles in the 460-record corpus | 0 |

For this check, titles were compared case-insensitively after Unicode normalization and removal of punctuation/spacing; DOI values were normalized by removing DOI URL/prefix forms and punctuation. The check confirms that the **current 460-row working corpus has no exact normalized title or DOI duplicates**. It does not prove that every candidate in the raw export has been reconciled correctly.

### Đối chiếu dữ liệu trích xuất trích dẫn thô

The raw file `snowballing-candidates-ACM-055.csv` contains **152 candidate rows**: 46 backward-citation rows and 106 forward-citation rows. It is retained as a provenance/audit export, not as the final deduplicated working corpus.

| Audit item | Result |
|---|---:|
| Candidate rows marked `already_in_primary_csv=YES` | 21 |
| Candidate rows matching the primary corpus by normalized title or DOI in a fresh check | 22 |
| Blank-title candidate rows | 6 |
| Repeated-title groups within the raw candidate export | 2 |
| Repeated-DOI groups within the raw candidate export | 1 |

The difference between the **21 YES flags** and **22 normalized primary matches** is one unresolved flag inconsistency: *EvoSuite at the SBST 2017 Tool Competition* appears with DOI `10.1109/sbst.2017.6` and malformed DOI `10.1109/sbst.2017..6`. The export also has two same-title groups: that EvoSuite paper, and *Construct Validity in Software Engineering* (journal DOI `10.1109/tse.2022.3176725` versus TechRxiv DOI `10.36227/techrxiv.14141027`). These raw rows should remain available for audit; they must not be counted as additional unique studies without reconciliation.

**Interpretation:** the current working corpus is title/DOI-unique under the normalization check, but the raw candidate export still contains six records without titles and duplicate/flag inconsistencies that should be reconciled before claiming complete end-to-end deduplication. Do not delete raw provenance rows merely to make the export appear unique; record their disposition and preserve traceability.

### Trạng thái sàng lọc hiện tại

| Stage | Current state |
|---|---|
| Primary records in working corpus | 335 |
| Snowballing records appended | 125 |
| Combined rows in `02_after_screening_v1.csv` | 281 (138 primary + 125 snowballing + 18 teacher-source records) |
| Combined V1 decisions recorded in the current CSV | 19 INCLUDE, 129 EXCLUDE, 133 UNCLEAR |
| Primary-search V1 decisions in the current CSV | 14 INCLUDE, 1 EXCLUDE, 123 UNCLEAR |
| Snowballing V1 | 5 INCLUDE, 120 EXCLUDE |
| Teacher-source V1 | 8 EXCLUDE, 10 UNCLEAR |
| Snowballing V2 | 1 INCLUDE (`SB-ACM055-066`), 4 EXCLUDE |
| Teacher-source full-text V2 | 1 INCLUDE (`TEACHER-004`), 13 EXCLUDE; 4 unavailable PDFs remain pending |
| Final included evidence set | 48 (46 primary-search + 1 snowballing + 1 teacher-source) |

The primary V2 totals (46 INCLUDE / 92 EXCLUDE) remain historical reported accounting; the full per-record decision ledger is not currently populated in the V2 columns of the combined screening CSV. The final included file and evidence table now also contain the separately full-text-screened teacher-source inclusion `TEACHER-004`.

## 6. Lượt chạy lịch sử — đã được thay thế, không thuộc kết quả đã hiệu chỉnh

An earlier exploratory run used 46 seeds and reported 3,083 per-seed/direction citation rows, 2,100 globally unique candidates, 171 matches to the primary corpus, and 1,929 candidates for V1. These figures are retained only to explain the previous workflow. They are **not** results of the corrected one-seed run and must not be used in the current PRISMA counts.

The earlier per-seed table and figures are not a substitute for raw exports and validation. Do not transfer the old ACM-055 row totals into the corrected run without retrieving and validating source records again.

## 7. Đối chiếu nguồn giảng viên trong Zotero và xử lý bản ghi trùng (2026-10-12)

The Zotero export `Source of teacher.csv` was compared with `01_all_records.csv` before importing records. The export contains 15 rows but only 14 unique titles because `PIT: a practical mutation testing tool for Java (demo)` appears twice; one of the duplicate Zotero entries is incomplete. The incomplete duplicate was not imported as a separate study. The complete PIT bibliographic record was retained as the representative record in the Zotero export.

The comparison used DOI and title matching to avoid adding records already represented in the working corpus. Twelve Zotero records absent from the working corpus were added with IDs `TEACHER-007`–`TEACHER-018`, continuing the `TEACHER` ID sequence used for the six records transcribed from the teacher-provided list (`TEACHER-001`–`TEACHER-006`). The existing `ACM-087` record, *MuMuTestUp: Mutation-Based Multi-agent Test Case Update*, was retained rather than added again. The dataset was then checked on `main`: it contains 478 data rows, including 18 added teacher-source records using one consistent `TEACHER-001`–`TEACHER-018` ID sequence: six records mapped from the teacher-provided list and twelve additional records reconciled from the Zotero export. The CSV schema remains the same 12 columns.

During the same reconciliation, `TEACHER-004` was corrected to *Productive Coverage: Improving the Actionability of Code Coverage* (teacher-list item 18), replacing the incorrectly mapped LLM2Alloy conference record. LLM2Alloy preprint metadata remains represented by `TEACHER-003` (item 12). The raw records were added for collection management only; no screening decisions were inferred from their presence.

**Limitations:** the newly added Zotero rows currently have blank abstract fields. The Zotero export should be used to populate those fields before evidence extraction. This log documents the deduplication actions performed; it does not claim that every metadata field in the imported records has been independently verified.

## 8. Sàng lọc toàn văn các bài do giảng viên giao (2026-10-12)

The screening details below consolidate the teacher-assigned V2 full-text review into this search log. The 14 available PDFs were screened; the four unavailable full texts remain pending and are not counted as exclusions.

Screened from the 14 PDFs supplied in `18pdf.zip`. PDF names were normalized to `Author_Year_ShortTitle.pdf`. Decisions apply the current `team-synthesis/ie_criteria.md`; evidence below is based on the supplied full text.

## Kết quả

> **Code audit:** During review, `EC-I` was found in the initial draft but is not defined in the shared `team-synthesis/ie_criteria.md`. Those labels were normalized to the existing `EC-O` code for out-of-scope/intervention mismatch. No screening decisions or counts were changed by this code-only correction.


- Số bài đã sàng lọc toàn văn: 14
- INCLUDE: 1 (`TEACHER-004`)
- EXCLUDE: 13
- PDF hiện vẫn chưa lấy được: `TEACHER-001`, `TEACHER-002`, `TEACHER-006`, `TEACHER-017`.


## 9. L3 — tìm kiếm bổ sung phản chứng cho RQ (2026-10-20)

**Mục đích:** tìm nghiên cứu giáo dục kiểm thử có phản hồi coverage/mutation để kiểm tra phản chứng cho RQ; lượt này là tìm kiếm bổ sung có mục tiêu, không thay thế tìm kiếm chính và không làm thay đổi số PRISMA.

| # | Ngày | Nguồn/phạm vi | Truy vấn nguyên văn | Kết quả xem xét | Phát hiện |
|---:|---|---|---|---|---|
| 1 | 2026-10-20 | Web index tổng quát | "coverage feedback" "mutation feedback" students software testing | 10 kết quả đầu; tổng hit không khả dụng | Alonge (2025) thesis; Shin & Kazerouni (2024), *A Model of How Students Engineer Test Cases With Feedback*. |
| 2 | 2026-10-20 | ACM DL domain | site:dl.acm.org students "branch coverage" "mutation testing" feedback | 10 kết quả đầu; tổng hit không khả dụng | Shin & Kazerouni (2024), DOI 10.1145/3628604; FRAFOL (2024) và nghiên cứu giáo dục liên quan. |
| 3 | 2026-10-20 | Web index tổng quát | "mutation testing" "coverage feedback" software testing education students | 10 kết quả đầu; tổng hit không khả dụng | FRAFOL (2024); *Instructor-Written Hints as Automated Test Suite Quality Feedback* (2025); nghiên cứu giáo dục liên quan. |
| 4 | 2026-10-20 | Web index tổng quát; bổ sung review/survey | "systematic review" OR survey "mutation testing" "software testing education" student feedback after:2023 | 10 kết quả đầu; tổng hit không khả dụng | Không thấy SLR phù hợp rõ ràng trong top 10; đây **không** phải bằng chứng rằng không có SLR. |
| 5 | 2026-10-20 | ACM DL domain; bổ sung review/survey | site:dl.acm.org "systematic review" "mutation testing" education student | 10 kết quả đầu; tổng hit không khả dụng | Trả về FRAFOL và nghiên cứu giáo dục; không thấy SLR phù hợp rõ ràng trong top 10. |

**Accounting:** 50 result slots qua 5 truy vấn; kết quả có trùng lặp nên không phải 50 record duy nhất. Công cụ tìm kiếm không trả tổng hit count ACM DL; không được báo 10 kết quả xem xét là số hit database.

### 9.1. Phản chứng L3 cần đưa vào sổ sàng lọc chính

- **Austin M. Shin & Ayaan M. Kazerouni (2024), “A Model of How Students Engineer Test Cases With Feedback,” ACM Transactions on Computing Education, DOI 10.1145/3628604.**
- Đã truy xuất publisher HTML và PDF 30 trang do tác giả lưu trữ. Nghiên cứu có 12 sinh viên tham gia think-aloud, làm bài kiểm thử Python, tiếp xúc cả branch-coverage và mutation-based feedback.
- Câu giới hạn nguyên văn: “Our study involved participants in a specific context—students in their third programming course testing Python programs.” Vị trí: §6, *Threats to Validity*, *External validity*; PDF page label 1:18 / article page 18.
- Đây là phản chứng cho gap rộng “chưa nghiên cứu tương tác của sinh viên với cả hai loại feedback”, nhưng không phải so sánh định lượng Δ mutation score theo baseline cá nhân và không dùng Java/CodeNet.
- **Trạng thái nhánh main tại ngày ghi log:** DOI/title chưa thấy trong 01_all_records.csv, 02_after_screening_v1.csv, hoặc 03_final_included.csv. Chưa tạo record và chưa ghi quyết định V1 trong các CSV hiện tại. Cần kiểm tra trùng lần cuối, thêm record có provenance, rồi áp dụng IC/EC hiện hành. Không tính paper này vào N=48 hoặc PRISMA trước khi hoàn tất bước đó.


## 10. L3 — tìm kiếm bổ sung trên ACM DL và chọn paper mạnh nhất (2026-10-21)

**Nguồn chính được yêu cầu:** ACM Digital Library. **Cửa sổ ngày xuất bản:** 2025-10-21 đến 2026-10-21, bao gồm hai mốc. Web search chỉ là bước bổ sung sau khi tìm trong ACM, không được ghi thay cho lượt truy vấn ACM. Quy tắc xếp ưu tiên: **cùng bài toán/metric → venue/benchmark lớn → mới nhất**.

### 10.1. Trạng thái truy vấn nguồn ACM

| # | Nguồn | Truy vấn nguyên văn | Bộ lọc ngày | Tổng kết quả ACM | Trạng thái |
|---:|---|---|---|---:|---|
| ACM-L3-Q1 | ACM Digital Library | `mutation testing feedback students unit tests` | Bộ lọc người dùng báo: `from_publication_date:2025-10-17`; ngày chạy 2026-10-21; **chưa xác nhận có ngày kết thúc 2026-10-21** | **361** (người dùng báo số hiển thị trên ACM) | Ghi nhận số hit được cung cấp; cần xác nhận/cài thêm ngày kết thúc để khớp cửa sổ xuất bản 2025-10-21–2026-10-21. Chưa có danh sách kết quả để thu thập/sàng lọc. |
| ACM-L3-Q2 | ACM Digital Library | `coverage feedback mutation feedback test improvement developers` | Bộ lọc người dùng báo: `from_publication_date:2025-10-17`; ngày chạy 2026-10-21; **chưa xác nhận có ngày kết thúc 2026-10-21** | **419** (người dùng báo số hiển thị trên ACM) | Ghi nhận số hit được cung cấp; cần xác nhận/cài thêm ngày kết thúc để khớp cửa sổ xuất bản 2025-10-21–2026-10-21. Chưa có danh sách kết quả để thu thập/sàng lọc. |
| ACM-L3-Q3 | ACM Digital Library | `"mutation testing" "software testing education" feedback` | Published 2025-10-21 through 2026-10-21 | **Chưa xác minh** | Chưa có kết quả truy vấn native ACM DL được truy xuất. Cần chạy trực tiếp trong ACM DL và lưu số lượng kết quả nguồn hiển thị. |

### 10.2. Truy vấn web bổ sung đã thử — không thay thế ACM

| # | Nguồn | Truy vấn nguyên văn | Tổng hit | Kết quả |
|---:|---|---|---|---|
| WEB-L3-Q1 | Web search, giới hạn domain ACM | `site:dl.acm.org "mutation testing" "feedback" students after:2025-10-20 before:2026-10-22` | Không được công cụ cung cấp | Không có kết quả trả về trong lượt tìm hiện tại; điều này không chứng minh ACM không có bài phù hợp. |
| WEB-L3-Q2 | Web search, giới hạn domain ACM | `site:dl.acm.org "branch coverage" "mutation feedback" students after:2025-10-20 before:2026-10-22` | Không được công cụ cung cấp | Không có kết quả trả về trong lượt tìm hiện tại; điều này không chứng minh ACM không có bài phù hợp. |
| WEB-L3-Q3 | Web search, giới hạn domain ACM | `site:dl.acm.org "mutation testing" "software testing education" feedback 2026 OR 2025` | Không được công cụ cung cấp | Không có kết quả trả về trong lượt tìm hiện tại; không thể dùng làm số hit ACM. |

**Accounting (cập nhật theo số liệu người dùng cung cấp ngày 2026-10-21):** Q1 = 361 hit; Q2 = 419 hit trên ACM DL. Đây là tổng hit được người dùng đọc từ nguồn ACM, chưa được trợ lý kiểm tra độc lập. Bộ lọc được cung cấp chỉ nêu `from_publication_date:2025-10-17`; mốc này sớm hơn cửa sổ 12 tháng đã quy định (2025-10-21) bốn ngày, và chưa xác nhận có bộ lọc ngày kết thúc. Vì vậy giữ nguyên số hit thực tế đã báo, nhưng không coi chúng là tổng hit của cửa sổ 2025-10-21–2026-10-21 cho đến khi lọc đúng ngày. Q3 vẫn chưa xác minh. Chưa có danh sách kết quả được thu thập, khử trùng và sàng lọc; không tuyên bố đã hoàn tất quy trình top 3.

### 10.3. Các ứng viên sơ bộ từ hồ sơ trước — chưa xếp hạng cuối cùng

Các bài dưới đây đã xuất hiện trong hồ sơ trước, nhưng **chưa được xác nhận là top 3 sau khi truy vấn ACM, thu thập kết quả, khử trùng và sàng lọc**:

- **Mansur et al. (2026), _Improving students’ testing skill through mutation testing with modified feedback and training_.** *Computer Science Education*. DOI 10.1080/08993408.2026.2671830.
- **Alonge (2025), _A Comparative Evaluation of Feedback Strategies for Enhancing Student Software Test Suite Writing Outcomes_.** MS thesis, California Polytechnic State University. Đây là luận văn ở kho trường đại học, không phải mặc nhiên là kết quả ACM DL.
- **Earle & Bell (2026), _Curated Semantic Mutants_.** SPLASH-E 2026. DOI 10.1145/3841644.3842688.

Đây chỉ là các ứng viên cần đối chiếu với kết quả truy vấn; không được coi thứ tự trên là thứ hạng cuối cùng. Alonge cần được ghi riêng là ứng viên từ nguồn ngoài ACM nếu không xuất hiện trong kết quả ACM.

### 10.4. Điều kiện để chốt top 3

1. Chạy các truy vấn trong bảng 10.1 trực tiếp trên ACM Digital Library với bộ lọc ngày chính xác và lưu ảnh chụp hoặc bản xuất kết quả có tổng số hit.
2. Thu thập danh sách kết quả của từng truy vấn; khử trùng theo DOI hoặc tiêu đề/tác giả/năm.
3. Báo cáo riêng tổng hit ACM, số record thu thập, số record đã xem xét và số bài phù hợp.
4. Sau đó mới chạy Web search bổ sung, phân biệt bài tìm được từ ACM với bài tìm từ nguồn khác.
5. Chỉ sau khi xem tập ứng viên mới chọn ba bài theo **cùng bài toán/metric → venue/benchmark lớn → mới nhất**, giải thích cho từng bài vì sao chọn và phần RQ còn đo mà bài chưa đo.

**Trạng thái:** chưa chốt top 3; chưa thay đổi tập INCLUDE hoặc số liệu PRISMA. Mục 2.1 trong `rq-check.md` được đánh dấu chưa chốt cho đến khi có kết quả ACM có thể kiểm chứng.

### 10.5. Web search Q3/Q4 — bổ sung ngày 2026-10-21

Hai truy vấn dưới đây được dùng như lớp Web search bổ sung, tách biệt với Q1/Q2 trên ACM Digital Library. Công cụ Web search không trả về tổng số hit có thể xác minh. Không dùng số lượng bài được nhận diện thay cho tổng hit.

| Mã | Truy vấn nguyên văn | Nguồn | Ngày | Tổng hit | Kết quả đã nhận diện |
|---|---|---|---|---|---|
| Q3 | `students mutation testing feedback versus code coverage feedback controlled experiment test suite quality` | Web search | 2026-10-21 | Không được công cụ cung cấp | Alonge (2025), luận văn so sánh feedback coverage và mutation; Mansur et al. (2026), nghiên cứu feedback mutation trong giảng dạy. |
| Q4 | `"mutation" "coverage" feedback student-written tests Web-CAT experiment mutation score improvement study` | Web search | 2026-10-21 | Không được công cụ cung cấp | Mansur et al. (2024), nghiên cứu mutation testing trong các khóa học; Alonge (2025) và Mansur et al. (2026) là các ứng viên trùng với Q3. |

Nguồn đối chiếu: Alonge (2025), https://digitalcommons.calpoly.edu/theses/3199 ; Mansur et al. (2026), https://doi.org/10.1080/08993408.2026.2671830 ; Mansur et al. (2024), https://doi.org/10.1145/3649165.3690110 .

Phạm vi bằng chứng: danh sách trên chỉ gồm các ứng viên đã nhận diện từ lượt Web search, không phải bản xuất đầy đủ của kết quả. Chưa xác minh vị trí xếp hạng, số record đã duyệt hoặc số record duy nhất sau dedup. Mansur et al. (2024) nằm ngoài cửa sổ 12 tháng, chỉ dùng làm phản chứng ngoài phễu chính. Không thay đổi corpus, INCLUDE hoặc PRISMA chỉ dựa vào lượt này.
