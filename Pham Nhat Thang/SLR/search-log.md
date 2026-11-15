# Search Log — Phạm Nhật Thăng (LR)

**Nguồn phụ trách:** OpenAlex + 20 paper nền trên thẻ RQ
**Công cụ:** `scripts/fetch_all_sources.py` (OpenAlex API, cursor pagination, `MAX_RECORDS = None`)
**Trường tìm kiếm:** tham số `search` của OpenAlex (title + abstract + fulltext index)
**Bộ lọc năm:** không áp dụng ở bước truy vấn; năm được xử lý ở screening theo IC-Y

---

## 1. Các lượt truy vấn

| Ngày           | Nguồn               | Query ID                | Câu lệnh tìm kiếm (nguyên văn)                                                                                                                                                                                                                                  | Số kết quả (raw) | Sau dedup | Trạng thái                                                               |
| :------------- | :------------------ | :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------: | --------: | :----------------------------------------------------------------------- |
| 2026-10-06     | OpenAlex            | OA-V1-00                | `("unit testing" OR JUnit OR "unit test") AND ("mutation testing" OR "mutation score" OR mutant*) AND ("code coverage" OR "branch coverage" OR "line coverage") AND ("test augmentation" OR "test generation" OR "test improvement") AND Java`                  |                0 |         0 | Lỗi HTTP 400: OpenAlex không cho wildcard`*` trong `search`. Không dùng. |
| 2026-10-06     | OpenAlex            | OA-V1-01                | `("unit testing" OR JUnit OR "unit test") AND ("mutation testing" OR "mutation score" OR mutant) AND ("code coverage" OR "branch coverage" OR "line coverage") AND ("test augmentation" OR "test generation" OR "test improvement") AND Java`                   |              741 |       740 | Lượt thử,**không đưa vào corpus** (thay bằng String A, xem mục 2).       |
| 2026-10-06     | OpenAlex            | **OA-V1-02** (String A) | `("JUnit testing" OR "unit test augmentation" OR "IBM CodeNet" OR "Project_CodeNet_Java250") AND (JaCoCo OR PITest OR "coverage-guided testing" OR "mutation-guided testing") AND ("mutation score" OR "mutant detection" OR "mutation testing effectiveness")` |           **76** |    **72** | Corpus chính thức                                                        |
| 2026-10-11     | Thẻ RQ (giảng viên) | **RQ-CARD**             | Danh sách 20 paper nền đi kèm RQ (không phải search string)                                                                                                                                                                                                     |           **20** |    **18** | Đưa vào 01 như record ứng viên; lấy đủ 20 bài, không lọc năm             |
| **2026-10-11** | **TỔNG CỘNG**       | **OA-V1-02 + RQ-CARD**  |                                                                                                                                                                                                                                                                 |           **96** |    **90** | 6 bản trùng bị loại (mục 3) = số dòng`source = search` trong 01          |

## 2. Thay đổi (change log — Review Protocol §7)

| Ngày       | Thay đổi                                                                                                                       | Lý do                                                                                                                                                                            | Ảnh hưởng                                                           |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| 2026-10-06 | Bỏ wildcard`mutant*` → `mutant`                                                                                                | OpenAlex trả lỗi 400 với wildcard trong`search`                                                                                                                                  | Chỉ ảnh hưởng lượt OA-V1-01 (không dùng)                            |
| 2026-10-06 | Dùng**String A** (search string trên thẻ RQ do giảng viên cung cấp) làm truy vấn chính thay cho OA-V1-01                       | RBL-1 quy định "String A = search string trên thẻ RQ"; OA-V1-01 trả 741 kết quả, phần lớn ngoài phạm vi RQ                                                                       | Corpus giảm 741 → 76. Bù độ phủ bằng snowballing (mục 6)            |
| 2026-10-11 | Bổ sung dedup theo tiêu đề + tác giả + năm (trước đây chỉ dedup theo DOI)                                                      | Phát hiện 4 cặp cùng một bài nhưng khác DOI (bản Zenodo/arXiv/kho trường)                                                                                                        | 76 → 72                                                             |
| 2026-10-11 | Thêm 20 paper nền trên thẻ RQ vào 01 (`database = RQ card`, `source = search`)                                                 | Hướng dẫn RBL-1 ngày 2–3: "paper dẫn chứng trên thẻ RQ đưa vào 01_all_records.csv như record ứng viên"                                                                           | +18 dòng sau dedup (72 → 90)                                        |
| 2026-10-11 | Cột`source` đổi thành `database`; thêm cột `source` (search / snowball-back / snowball-fwd) và `seed`; bỏ cột `citation_count` | Checklist snowballing yêu cầu cột`source` và `seed`; số trích dẫn chỉ cần cho việc chọn seed (ghi ở mục 6)                                                                       | Không đổi số dòng                                                   |
| 2026-10-17 | Thêm giá trị`source = supplement-w7` cho record từ lớp bổ sung (§8); `database = Web search` hoặc `OpenAlex` (theo truy vấn), `seed` để trống                  | RBL-2 Bước 2 mục 4: ghi truy vấn và ngày vào search-log; "cập nhật CSV, evidence table và PRISMA cho mọi record mới". Lớp này không phải snowballing (§6 chỉ một lượt, seed P10) | +7 dòng trong 01/02 (109 → 116), +4 dòng trong 03, +2 INCLUDE (P28, P29) |
| 2026-10-22 | Thêm giá trị `database = Semantic Scholar` cho record tìm qua tra cứu nghiên cứu tiếp nối (§8, Q6) | Email giảng viên ngày 2026-10-22: kiểm tra các nghiên cứu tiếp nối và đối chiếu nghiên cứu gần nhất trước khi chốt GAP 1 | +4 dòng trong 01/02 (116 → 120), +3 dòng trong 03 (51 → 54), không có INCLUDE mới |
| 2026-10-24 | Thêm giá trị `database = Lecturer email` cho record do giảng viên gợi ý (§8, Q8) | Email giảng viên ngày 2026-10-24 yêu cầu đối chiếu Hall & Baniassad (2022) |

## 3. Bỏ trùng (dedup)

Quy tắc: cùng DOI chuẩn hóa, **hoặc** cùng tiêu đề chuẩn hóa + tác giả + năm (hoặc bản preprint/bản kho trường của cùng bài). Giữ bản xuất bản chính thức (EC-D).

| Bản bị loại                                                         | Giữ bản                         | Lý do                       |
| :------------------------------------------------------------------ | :------------------------------ | :-------------------------- |
| OpenAlex #12 Quality Metrics of Test Suites… (Zenodo)               | OA-009 (IJSEA 2018)             | Cùng bài, bản Zenodo        |
| OpenAlex #10 Characterization of Open-Source Applications… (Zenodo) | OA-012 (IJSEA 2018)             | Cùng bài, bản Zenodo        |
| OpenAlex #32 JUGE (arXiv 2021)                                      | OA-029 JUGE (STVR 2022)         | Preprint của bản journal    |
| OpenAlex #69 Mutation-based multi-agent test case update (SMU InK)  | OA-023 MuMuTestUp (PACMSE 2026) | Bản kho trường của cùng bài |
| RQ-13 LM2Alloy (arXiv 2607.18555)                                   | RQ-12 LM2Alloy (ICST 2026)      | Cùng tên + tác giả + năm    |
| RQ-14 Mutation-based multi-agent test case update (SMU InK)         | OA-023 MuMuTestUp               | Đã có trong corpus OpenAlex |

## 4. Pre-screening check (90 record `source = search`)

- Thiếu DOI: 12 (có URL thay thế)
- Thiếu abstract: 3 (OA-011, OA-017, OA-045). Đã lấy abstract của OA-017 (Springer) và OA-045 (Research Square) từ trang nhà xuất bản ngày 2026-10-11; OA-011 (SSRN) lấy từ trang SSRN ở vòng 2.
- Trường abstract không phải abstract thật: 3 (OA-046, OA-068, OA-071)
- Thiếu năm: 1 (OA-072)
- Kết luận: tỷ lệ thiếu abstract < 10%, đủ điều kiện screening vòng 1.

## 5. Kết quả screening

Quy tắc V1: chỉ EXCLUDE khi abstract cho bằng chứng rõ là vi phạm IC/EC; thiếu thông tin → Unsure. Không suy luận từ tiêu đề; không tìm full-text ở vòng này. INCLUDE + Unsure → V2 (chỉ INCLUDE/Unsure mới cần full-text ở vòng 2).

Quy tắc V2: INCLUDE khi (a) test mức unit/JUnit cho Java; (b) có can thiệp sinh/bổ sung/cải thiện test (tự động hoặc thủ công); (c) **cả** mutation và code coverage đều có mặt — mỗi thước đo được báo cáo bằng số hoặc được dùng làm phản hồi trong can thiệp; (d) có kết quả định lượng; (e) đạt IC-L.

| Vòng    | Nhánh         | INCLUDE | Unsure | EXCLUDE (mã)                          | Tổng |
| :------ | :------------ | ------: | -----: | :------------------------------------ | ---: |
| V1 (02) | search        |      14 |     21 | 55 — EC-O 32, IC-L 11, EC-N 9, EC-S 3 |   90 |
| V2 (03) | search        |      22 |      0 | 13 — IC-I 8, IC-P 2, EC-O 2, EC-A 1   |   35 |
| V1 (02) | snowball-back |       1 |      4 | 2 — EC-O 1, EC-N 1                    |    7 |
| V2 (03) | snowball-back |       2 |      0 | 3 — IC-I 2, EC-A 1                    |    5 |
| V1 (02) | snowball-fwd  |       0 |      7 | 5 — EC-N 4, EC-O 1                    |   12 |
| V2 (03) | snowball-fwd  |       3 |      0 | 4 — IC-I 2, EC-A 2                    |    7 |
| V1 (02) | supplement-w7 |       0 |      7 | 4 — IC-L 2, EC-O 1, IC-E 1            |   11 |
| V2 (03) | supplement-w7 |       2 |      0 | 5 — EC-O 2, IC-I 2, EC-A 1            |    7 |

**EC-A:** RQ-05 TestForge, SB-07, SF-06, SF-10 (không truy cập được full-text, không có quyền IEEE/Wiley và không tìm thấy bản mở); W7-10 Mansur et al. 2026 (Taylor & Francis, không có bản mở).

**Diễn giải IC-L:** luận văn/luận án trong kho lưu trữ của trường không phải venue có phản biện cũng không phải arXiv → EXCLUDE (IC-L).

**Sử dụng AI:** quyết định V1/V2 được soạn nháp bằng AI (Claude) từ title + abstract (V1) và full-text (V2), sau đó rà và chốt từng dòng.

## 6. Snowballing

### 6.1 Lý do chọn seed

**Seed:** Danglot B., Vera-Perez O., Baudry B., Monperrus M. (2019). _Automatic test improvement with DSpot: a study with ten mature open-source projects._ Empirical Software Engineering 24, 2603–2635. DOI `10.1007/s10664-019-09692-y` (record OA-017, mã P10).

| Tiêu chí (A2b)                   | Đánh giá                                                                                                                                                                                                                                             |
| :------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đã INCLUDE ở vòng 2              | Có (03, P10)                                                                                                                                                                                                                                         |
| Khớp ≥ 3/4 yếu tố P/I/C/O        | 3/4:**I** (khuếch đại test dựa trên mutation score PIT), **C** (bộ JUnit do lập trình viên viết là điểm xuất phát), **O** (mutation score / mutant bị diệt). Khác RQ ở **P**: dự án mã nguồn mở thật, không phải CodeNet, và không có người tham gia |
| Citation trong khoảng 10–200     | 48 (OpenAlex, tra ngày 2026-10-11)                                                                                                                                                                                                                   |
| Không trùng seed người khác      | Trần Triều Tiên dùng`10.1109/ICSE.2017.61`; Ngô Minh Tiến dùng ACM-055                                                                                                                                                                               |
| Vì sao không chọn bài sát RQ hơn | RQ-06 (Scaffolding, 4/4) chỉ có 1 trích dẫn; P02 MUTGEN và P01 CANDOR có 3; P14 MuMuTestUp có 0 — đều dưới ngưỡng 10                                                                                                                                 |

### 6.2 Bảng seed

| DOI seed                   | Vòng | Hướng                 | Số đã lướt | Số thêm vào 01 | Số include cuối |
| :------------------------- | :--: | :-------------------- | ---------: | -------------: | --------------: |
| 10.1007/s10664-019-09692-y |  1   | backward (References) |         33 |              7 |               2 |
| 10.1007/s10664-019-09692-y |  1   | forward (Citations)   |         48 |             12 |               3 |
| **Tổng**                   |      |                       |     **81** |         **19** |           **5** |

- **Backward:** danh mục tài liệu tham khảo trong bản arXiv 1811.08330 (33 mục; OpenAlex ghi 41 cho bản EMSE). Giữ 7 bài có vẻ liên quan (SB-01 … SB-07), bỏ các bài trước 2010 (IC-Y) và các bài ngoài chủ đề (fault localization, GUI, web, program repair, DevOps, sách).
- **Forward:** OpenAlex, filter `cites:W2901721765`, xuất CSV từ giao diện openalex.org ngày 2026-10-10 (lưu tại `snowball_fwd_openalex_export.csv`): 48 bài trích dẫn DSpot, tất cả từ 2019 trở đi (đạt IC-Y). Lướt tiêu đề, giữ 12 bài (SF-01 … SF-12) liên quan đến khuếch đại/bổ sung test dựa trên coverage hoặc mutation. Bỏ: test amplification cho Python/Pharo/Solidity/DSL, flaky test, clone, BreakBot, assertion survey, luận văn, và các bài đã có trong 01 (OA-043; bản arXiv của SF-01). Bài mới nhất sát RQ: SF-12 (Killing surviving mutants, ISSTA 2026) đã INCLUDE. Bài này bổ sung assertion để diệt mutant sống sót, nhưng làm tự động, không có người viết test và không so với phản hồi JaCoCo. SF-10 (Developer vs DSpot vs ChatGPT, ICST 2026) bị loại theo EC-A vì không truy cập được full-text. Chưa thấy bài nào làm đúng RQ trong lượt snowballing này (cập nhật: lớp bổ sung ở §8 tìm được Alonge 2025, so trực tiếp phản hồi branch coverage với mutation cho sinh viên, và Mansur et al. 2024 (P28), so chấm theo coverage với chấm theo mutation giữa các học kỳ — xem `rq-check.md`).
- Mỗi người chỉ làm một lượt backward + forward; bài mới INCLUDE không dùng làm seed vòng tiếp.

## 7. Kiểm chéo screening (ngày 5)

| Người kiểm | Số paper bị loại được kiểm (≥ 20% của EXCLUDE ở V1) | Số bất đồng | Cách xử lý |
| :--------- | --------------------------------------------------: | ----------: | :--------- |
|            |                                                     |             |            |

## 8. Lớp bổ sung (RBL-2, Bước 2 mục 4)

Mục đích: tìm 2–3 paper mạnh nhất trong 12 tháng gần đây cùng chủ đề, và kiểm phản chứng ngoài bảng gộp. Lớp này **không phải lượt snowballing**: §6 đã dùng hết một lượt backward + forward với seed P10. Record mới mang `source = supplement-w7`, `seed` để trống.

|  #  | Truy vấn nguyên văn                                                                                          | Nguồn        | Ngày       | Số kết quả | Kết quả                                                                                                                                                                                                                                                                                                   |
| :-: | :----------------------------------------------------------------------------------------------------------- | :----------- | :--------- | ---------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1  | `mutation testing feedback students unit tests`, filter `from_publication_date:2025-10-17`                   | OpenAlex API | 2026-10-19 |      1.931 | Lần chạy ngày 17 bị 429, chạy lại ngày 19 thành công<br />Lướt 25 bài đầu: #15 *Auditing and Decomposing Feedback-Driven Evolution…* (N-P34) và #4 _Test vs Mutant_ (ACM-001) đã có trong bảng<br />3 record mới: W7-05 Earle & Bell (2026); W7-06 Andleeb et al. (2025); W7-07 El Bolock, Sabty, Fraser, Abdennadher (2026) |
| Q2  | `coverage feedback mutation feedback test improvement developers`, filter `from_publication_date:2025-10-17` | OpenAlex API | 2026-10-18 |      1.198 | Lướt 25 kết quả đầu; sát chủ đề chỉ có MUTGEN (P02) và MuMuTestUp (P14), đã có trong 03                                                                                                                                                                                                                   |
| Q3  | `students mutation testing feedback versus code coverage feedback controlled experiment test suite quality`  | Web search   | 2026-10-18 |          9 | 3 record mới: W7-01 Alonge 2025 (luận văn, Cal Poly), W7-02 Perretta et al. 2025 (SIGCSE TS), W7-03 Mansur 2025 (luận án, Virginia Tech)                                                                                                                                                                  |
| Q4  | `"mutation" "coverage" feedback student-written tests Web-CAT experiment mutation score improvement study`   | Web search   | 2026-10-18 |          9 | 1 record mới: W7-04 Mansur, Shaffer, Edwards 2024 (SIGCSE Virtual)                                                                                                                                                                                                                                        |
| Q5  | `are mutants a valid substitute for real faults in student programs incorrect submissions test suite evaluation mutation score correlation` | Web search | 2026-10-21 | 9 liên kết | 2 record mới: W7-08 Clegg, McMinn, Fraser 2021 (SIGCSE); W7-09 Perretta, DeOrio, Guha, Bell 2022 (ISSTA). Kết quả còn lại: Just et al. 2014 và Papadakis et al. 2018 (đã có, R033) không dùng thêm |
| Q6  | Tra cứu nghiên cứu tiếp nối (bài trích dẫn) qua Semantic Scholar API cho Alonge 2025, Clegg 2021, Perretta 2022, P28, P29 | Semantic Scholar | 2026-10-22 | Clegg 7; Perretta 9; P28 4; P29 0; Alonge không có bản ghi | 1 record mới: W7-10 Mansur, Domino, Thompson, Shaffer, Edwards 2026 (Computer Science Education), trích dẫn P28. Các bài trích dẫn còn lại đã có trong bảng (P19, P29, Perretta 2025) hoặc không so loại phản hồi và không đánh giá bằng lỗi thật (xem `team-synthesis/gap1-phan-hoi.md` §2) |
| Q7  | `student test suites real faults detection coverage feedback versus mutation feedback experiment 2025 2026 incorrect submissions evaluation` | Web search | 2026-10-22 | 9 liên kết | 1 record mới: W7-11 Shin, Kazerouni 2024 (ACM TOCE). Kết quả còn lại: W7-10, Perretta 2022 (W7-09), Kazerouni et al. 2021 (chỉ giảm chi phí mutation), Ayad et al. (không có sinh viên), Dick et al. 2024 (arXiv, chỉ coverage) |
| Q8  | Không có truy vấn: giảng viên gợi ý DOI 10.1145/3563767.3568132 | Email giảng viên | 2026-10-24 | 1 | 1 record mới: W7-12 Hall, Baniassad 2022 (SPLASH-E). Kiểm tra lại: bài này có trong danh mục tham khảo của T-P28 [16], T-P29 [7] và luận án Mansur 2025 [27]; lớp bổ sung không làm backward snowballing trên các bài này nên đã bỏ sót |

**Sàng lọc 11 record mới** (cùng quy tắc V1/V2 ở §5):

| Record                                           | V1                                                                        | V2 (toàn văn)                                                           | Kết quả                                    |
| :----------------------------------------------- | :------------------------------------------------------------------------ | :---------------------------------------------------------------------- | :----------------------------------------- |
| W7-01 Alonge 2025                                | EXCLUDE (IC-L: luận văn thạc sĩ trong kho trường)                         | —                                                                       | Dùng làm phản chứng trong`rq-check.md` §2  |
| W7-02 Perretta et al. 2025                       | Unsure (abstract không nêu ngôn ngữ)                                      | EXCLUDE (EC-O: bộ test của sinh viên viết bằng C++,`test.cpp`)          | Dùng làm phản chứng trong`rq-check.md` §2  |
| W7-03 Mansur 2025                                | EXCLUDE (IC-L: luận án tiến sĩ trong kho trường; chương 4 chính là W7-04) | —                                                                       | —                                          |
| W7-04 Mansur et al. 2024                         | Unsure (abstract không nêu ngôn ngữ và công cụ mutation)                  | INCLUDE (IC-P, IC-I, IC-O, IC-E, IC-L: Java, PIT/MuJava/Major, 7 trang) | **P28** trong 03, evidence table và PRISMA |
| W7-05 Earle & Bell 2026                          | **Unsure** (abstract không nêu metric và ngôn ngữ)                        | INCLUDE (IC-P, IC-I, IC-O, IC-E, IC-L: CS 3100 dạy bằng Java, PIT/PreBakedMutator, có kill rate và tỉ lệ NO_COVERAGE, SPLASH-E 2026, 13 trang) | **P29** trong 03, evidence table và PRISMA |
| W7-06 Andleeb et al. 2025                        | **Unsure** (abstract không nêu metric và ngôn ngữ)                        | EXCLUDE (IC-I: phản hồi và kết quả chỉ là code coverage, không có mutation score) | —                                          |
| W7-07 El Bolock, Sabty, Fraser, Abdennadher 2026 | **EXCLUDE (EC-O)**: abstract ghi rõ Stryker.NET/Coverlet, tức là C#/.NET  | —                                                                       | Loại ở V1 nên không cần toàn văn           |
| W7-08 Clegg, McMinn, Fraser 2021 | Unsure (bản ghi không có abstract) | EXCLUDE (IC-I: tương quan mutation score và line coverage của bộ test chấm điểm với việc phát hiện 197 bài làm sai thật của sinh viên; không có can thiệp sinh/bổ sung test) | Dùng làm đối chiếu trong `team-synthesis/gap1-phan-hoi.md` |
| W7-09 Perretta, DeOrio, Guha, Bell 2022 | Unsure (bản ghi không có abstract) | EXCLUDE (EC-O: bộ test sinh viên viết bằng C++, JavaScript, TypeScript) | Dùng làm đối chiếu trong `team-synthesis/gap1-phan-hoi.md` |
| W7-10 Mansur et al. 2026 | Unsure (bản ghi không có abstract) | EXCLUDE (EC-A: không truy cập được toàn văn; cùng nghiên cứu ba học kỳ được mô tả ở chương 5 luận án W7-03) | Dùng làm đối chiếu, dựa trên chương 5 của W7-03 |
| W7-11 Shin, Kazerouni 2024 | **EXCLUDE (IC-E)**: abstract nêu nghiên cứu định tính, 12 phỏng vấn think-aloud, không có kết quả định lượng | — | Dùng làm đối chiếu trong `team-synthesis/gap1-phan-hoi.md` |
| W7-12 Hall, Baniassad 2022 | Unsure (abstract không nêu ngôn ngữ) | EXCLUDE (EC-O: test sinh viên viết bằng TypeScript, Mocha/Chai, mục 5.7, tr. 31) | Paper gần nhất trong `team-synthesis/gap1-phan-hoi.md` (cùng quy tắc loại với W7-09) |

Tổng lớp bổ sung: 12 record → loại V1 4 (IC-L 2, EC-O 1, IC-E 1) → đọc toàn văn 8 → loại V2 6 (EC-O 3, IC-I 2, EC-A 1) → **INCLUDE 2 (P28, P29)**. W7-12 thêm ngày 2026-10-24. Q5–Q7 được chạy theo email giảng viên ngày 2026-10-22 (đối chiếu nghiên cứu gần nhất cho GAP 1); không có record INCLUDE mới nên N của bảng gộp không đổi.

12 tháng gần đây, tính từ 2025-10-17: Alonge (12/2025), Andleeb et al. (11/2025) và Earle & Bell (10/2026) nằm trong khoảng này. Mansur et al. (12/2024) nằm ngoài khoảng, nên được thêm vào vì là phản chứng cho RQ, không phải vì là paper mới nhất.
