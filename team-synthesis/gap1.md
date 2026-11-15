# GAP 1: bảng đối chiếu, RQ và pilot

Phiên bản 2, ngày 2026-10-24, theo email giảng viên ngày 2026-10-24. Bản 1 (2026-10-23) giữ trong lịch sử repo.

Tài liệu gồm: bảng đối chiếu nghiên cứu gần nhất (§1–§2), RQ và đóng góp dự kiến (§3–§4), pilot (§5), hồ sơ bằng chứng và phiên bản (§6).

## 0. Thay đổi so với bản 2026-10-23

| Yêu cầu trong email 2026-10-24 | Thay đổi | Mục |
|---|---|---|
| 1. Phép đo phải kiểm tra expected output và assertion; không trích lời gọi trong chú thích | Giữ RQ về bộ JUnit. Phép đo chính đổi sang **chạy chính bộ JUnit** của sinh viên trên từng bài WA (`junit_eval.py`). Test chỉ hợp lệ khi pass trên chương trình đúng; bài WA bị phát hiện khi có test hợp lệ fail do assertion. Không còn so output với oracle chung để chấm phiên. Bộ trích đầu vào bỏ chú thích trước khi tìm, xử lý đúng text block | 5.9, 5.10 |
| 2. Chốt baseline và tập đánh giá; không tự thêm Sample Input; khoá tập WA; nhóm hành vi dùng tập đầu vào tham chiếu cố định | Bộ test được chấm đúng như nộp, không thêm gì. Đề xuất baseline bắt buộc: bộ JUnit chỉ gồm các cặp Sample (phát sẵn). Khoá 13 manifest WA và tập đầu vào tham chiếu bằng SHA-256 (`frozen_index.json`). Nhóm hành vi chỉ là số mô tả trên tập tham chiếu cố định, không đồng nhất với lỗi gốc | 5.11, 5.8 |
| 3. Hiệu ứng trần: chốt bài và thời lượng qua mini-pilot theo tiêu chí công khai; giữ mọi phiên hợp lệ; báo riêng tỉ lệ chạm trần; sửa 11/12 thành 10/12 | Sửa thành 10/12 (giá trị chưa làm tròn). Bỏ đề xuất phân tích loại phiên ≥ 0,95; mọi phiên hợp lệ nằm trong phân tích chính, tỉ lệ chạm trần báo riêng. Thêm tiêu chí công khai chọn bài và thời lượng, kèm kết quả kiểm tra phản hồi khả dụng của JaCoCo và PITest | 5.8, 5.12, 5.13 |
| 4. Đồng bộ hồ sơ; phiên bản/commit; đối chiếu Hall & Baniassad (2022) | Bổ sung Hall & Baniassad (2022), đọc toàn văn; thay đổi paper gần nhất. Ghi SHA-256 của script, công cụ và dữ liệu; commit do PL thực hiện | §1, §2, §3, §6 |
| Ví dụ đầy đủ (email 2026-10-23) | Ví dụ p01137: JUnit ban đầu → báo cáo JaCoCo/PITest → test bổ sung → mức tăng phát hiện WA, chạy bằng JUnit 5, JaCoCo và PITest thật | 5.14 |

### 0.1 Thay đổi ngày 2026-10-28 (email 2026-10-27, mục 1, 4, 5)

| Mục trong email 2026-10-27 | Thay đổi | Mục |
|---|---|---|
| 1. Cách gọi "mục không làm được" | Đổi thành "mục chưa phủ/diệt được bằng tập tham chiếu" ở mọi chỗ (proposal, file này, tên trường trong `scan_put.py`, `frozen_index.json`, các file quét). Chỉ gọi một mục là "không đạt được" hay "tương đương" khi có kiểm tra riêng: hai thành viên lập luận độc lập trên mã, ghi lý do, người thứ ba quyết. Ba mục ở §5.12 và §5.14 trước đây được gọi là không đạt được/tương đương nay ghi là lập luận của một người, chưa qua kiểm tra riêng | 5.12, 5.13, 5.14, 5.16 |
| 4. Căn cứ cỡ mẫu | Bỏ cách lấy SD của Alonge. Thêm `power_sim.py`: mô hình phiên có hiệu ứng sinh viên, bài, thứ tự; quét σ, ρ, τ, N; Wilcoxon signed-rank trên d như phân tích chính; báo power, MDE, xác suất thoả quy tắc kết luận. Mục tiêu vẫn 48; 24 là thăm dò | 5.7, 5.17 |
| 5. Kiểm chứng bộ chấm | Thêm `verify_grader.py` (bài giả lập, 80 kiểm tra có kỳ vọng ghi trước), `pick_ac.py` (4 bài AC khác tác giả mỗi bài), `junit_eval.py --ac-list/--review` (test bất đồng AC tạm loại, hai người duyệt, người thứ ba quyết, phân tích độ nhạy giữ/loại), kiểm tra test phụ thuộc thứ tự | 5.17 |

### 0.2 Thay đổi ngày 2026-10-29 (email 2026-10-27, mục 2, 3, 6, 7; proposal bản _7)

| Mục | Thay đổi | Mục |
|---|---|---|
| 3. Phân tích | Wilcoxon signed-rank ghép cặp, hiệu bằng 0 xử lý theo Pratt, hạng trùng lấy hạng trung bình; ước lượng Hodges–Lehmann trên mọi d và khoảng tin cậy 95% bằng nghịch đảo kiểm định; mô hình tuyến tính hỗn hợp (điều kiện, thứ tự, bài cố định; sinh viên ngẫu nhiên) là phân tích bổ sung. `power_sim.py` chạy lại với Pratt: bảng MDE không đổi | 5.17 |
| 6. Quy trình phiên | T bắt đầu khi nộp Before.java; chạy lại công cụ không giới hạn, ghi số lần; 10 phút luyện cả hai công cụ trước phiên 1; Before không biên dịch hoặc báo cáo rỗng vẫn giữ phiên; thiếu phiên thì loại khỏi ghép cặp và tuyển người thay đúng ô lịch | proposal §5.3 |
| 7. Danh sách bài | Theo cùng thứ tự seed và cùng tiêu chí: bài 26 p04005 dự phòng (PUT s226763049, 206 WA); bài 27 p03986 và bài 28 p02909 là bài pilot (PUT s263632960, 85 WA; s470507275, 102 WA); bài 29 p02681 là bài luyện tập (không có PUT đạt đủ 5 điều kiện trong 30 ứng viên; PUT luyện tập s228096635 là ứng viên đầu tiên đạt điều kiện 1–3). Mỗi bài có 4 AC đối chiếu, khoá trong `data/frozen/extra/` | 5.16 |
| 7. Khác | Tài liệu tham khảo, Appendix A–C, nhãn J/P thống nhất ở §5.1 | proposal |

## 1. Bảng đối chiếu nghiên cứu gần nhất

| Nghiên cứu (nguồn đã đọc) | Đối tượng | Loại phản hồi | Thiết kế | Loại lỗi dùng để đánh giá | Thước đo | Phần khác biệt còn lại so với GAP 1 |
|---|---|---|---|---|---|---|
| **Alonge (2025)**, luận văn ThS, Cal Poly (W7-01, ngoài SLR theo IC-L). Toàn văn 69 trang | 10 sinh viên, mỗi nhóm 5 (Table 5.1, tr. 48); Python, ứng dụng Muttle (tr. 25, 30) | Branch coverage hoặc mutation coverage, xem khi luyện tập (tr. 12, 37) | Chia ngẫu nhiên hai nhóm độc lập (tr. 12). Pre-test 5 bài chỉ có mô tả → luyện 10 bài có phản hồi → post-test 5 bài **khác**, không phản hồi (tr. 35, 37, 43) | "Conceptual mutants" do nhà nghiên cứu thiết kế cho giống lỗi thật (tr. 32, 34) | Tỉ lệ conceptual mutant bị diệt (tr. 47): branch 0,65 → 0,71; mutation 0,69 → 0,80 (Table 5.2, tr. 48). Số test chỉ báo cáo trung bình (Table 5.3, tr. 49). Không có kiểm định thống kê ở chương kết quả | Lỗi do nhà nghiên cứu soạn, không phải bài làm sai thật; đo kỹ năng chuyển giao sang bài mới, không đo mức cải thiện của chính bộ test trên cùng chương trình; không cân bằng thời gian; hai nhóm độc lập 5 người |
| **Mansur, Domino, Thompson, Shaffer, Edwards (2026)**, Computer Science Education (W7-10). Toàn văn bài báo không truy cập được; cùng nghiên cứu được mô tả ở chương 5 luận án Mansur (2025) (W7-03, PDF tr. 77–119) | Sinh viên môn Cấu trúc dữ liệu (post-CS2), Java, dự án 3–4 tuần; 328, 346, 381 sinh viên ở ba học kỳ, 38 phỏng vấn (Table 5.2, PDF tr. 84) | Code coverage; PIT gốc; PIT có phản hồi sửa đổi kèm tài liệu hướng dẫn (PDF tr. 80) | So sánh giữa ba học kỳ, mixed methods (PDF tr. 80–81) | Mutant MuJava trên mã của chính sinh viên; test ẩn của giảng viên chấm mã của sinh viên (PDF tr. 81, 86) | Mutation coverage MuJava: 48%, 65%, 73% (Figure 5.6, PDF tr. 115–116); điểm đúng của mã sinh viên | Không đo khả năng bộ test phát hiện bài làm sai của người khác; so giữa các học kỳ khác nhau; không cân bằng thời gian; không kiểm soát kích thước bộ test |
| **T-P28** Mansur, Shaffer, Edwards (2024), SIGCSE Virtual. Toàn văn 7 trang | Như dòng trên, khoảng 400–500 sinh viên mỗi học kỳ | Chấm theo coverage (Fall 2019–2021) so với chấm theo mutation PIT (Fall 2023, Spring 2024) | So sánh giữa các học kỳ; tác giả nêu chính sách chấm điểm có thể gây ra khác biệt (5 Threats to Validity, tr. 6) | Mutant MuJava trên bộ test cuối; test ẩn của giảng viên chấm mã của sinh viên | MuJava 60→74, 46→73, 72→79, 62→81 (%) ở 4 project; Kruskal–Wallis, p ≤ 0,001 (Table 1, tr. 4) | Như dòng trên |
| **Clegg, McMinn, Fraser (2021)**, SIGCSE (W7-08). Toàn văn bản tác giả | 197 bài làm thật (biên dịch được) của sinh viên năm nhất, Java, 3 khoá, 3 bài tập (Section 3) | Không có. Không có sinh viên nào nhận phản hồi | Tương quan, quan sát. Bộ test là tập con ngẫu nhiên của test chấm điểm (của giảng viên hoặc EvoSuite), kích thước từ 2 test đến 70% bộ gốc (Section 3) | **Bài làm sai thật của sinh viên**; mutant PIT và Major sinh từ lời giải mẫu | Tương quan Spearman với tỉ lệ phát hiện bài làm sai: mutation score PIT 0,59; line coverage 0,61 (Section 4.2–4.3, Table 3). Có kiểm soát kích thước bộ test | Bộ test không do sinh viên viết, không có phản hồi để so; quan sát, không thực nghiệm |
| **Perretta, DeOrio, Guha, Bell (2022)**, ISSTA (W7-09). Toàn văn bản NSF PAR | Bộ test của sinh viên, 2.711 bài nộp, 3 trường, C++/JavaScript/TypeScript (Section 3.2, tr. 266–267) | Trong khoá học, sinh viên chỉ thấy số lỗi do giảng viên cài sẵn bị phát hiện (Section 3.2, tr. 266) | Tương quan, quan sát (Section 4, tr. 267–271) | Lỗi do giảng viên cài; **bài làm sai thật của sinh viên khác** (all-pairs) | Tương quan mutation score với tỉ lệ phát hiện all-pairs: r = 0,67 và 0,79 ở hai bài tập (Section 4). Có kiểm soát coverage, không kiểm soát kích thước | Không so hai loại phản hồi; không gán phản hồi theo thiết kế; không phải Java |
| **T-P29** Earle, Bell (2026), SPLASH-E. Toàn văn 13 trang | Môn CS 3100, Java, 1.893 bài nộp | Gợi ý cho mutant chưa bị diệt (LLM viết rõ thêm); không có nhánh coverage | Quan sát; sinh viên tự chọn xin gợi ý: "RQ3 therefore reports adoption and an observational pair-level association, not a causal hint effect." (6.4, tr. 11) | Mutant chọn tay của giảng viên | Kill rate; tỉ lệ NO_COVERAGE; cải thiện ở lần nộp sau gấp 1,62 lần (tr. 11) | Không có phản hồi coverage để so; quan sát; không dùng bài làm sai thật |
| **Hall, Baniassad (2022)**, SPLASH-E, tr. 24–34 (W7-12). Toàn văn 11 trang | Môn kỹ thuật phần mềm năm 3, khoảng 300 sinh viên; dự án TypeScript; giai đoạn Testing 2 tuần (3.1, tr. 26) | Coverage Grader: điểm statement coverage trên lời giải mẫu. Mutation Grader: 16 mutant viết tay, phản hồi số mutant bị diệt theo từng mục đặc tả và danh sách test fail trên lời giải mẫu (4.1–4.2, tr. 27–28) | So hai học kỳ: Coverage Term n = 290 (Winter 2021) và Mutant Term n = 306 (Fall 2021) (5.1, tr. 28). Khác biệt ngoài loại phản hồi: học kỳ Mutant không được phát starter code (tr. 28); cơ chế điểm thưởng có thể "capping" (5.4.1, tr. 29) | Mutation Oracle: 73 mutant viết tay bởi một giảng viên độc lập (5.2, tr. 29) | Oracle score: Coverage Term 63,46% (SD 15,88), Mutant Term 54,08% (SD 20,37) (5.4.1, tr. 29). Tỉ lệ test fail trên lời giải mẫu (over-asserting): 15,37% so với 7,42% (5.4.3, tr. 30). Kết luận: "Results did not show that the fault finding abilities of the test suites written by the Mutant Term were stronger" (7, tr. 33). Không có kiểm định thống kê cho chênh lệch giữa hai học kỳ | Lỗi do người soạn (mutant), không phải bài làm sai thật; phản hồi gắn với điểm số; so giữa hai học kỳ có khác biệt khác ngoài phản hồi; không cân bằng thời gian; TypeScript |
| **Shin, Kazerouni (2024)**, ACM TOCE 24(1) (W7-11). Chỉ đọc tóm tắt; toàn văn không truy cập được | 12 sinh viên, phỏng vấn think-aloud | Branch coverage và mutation, mỗi nhiệm vụ một loại | Định tính (grounded theory) | Không có | Mô hình quá trình; phản hồi mutation thường gây quá tải nhận thức | Không có số liệu định lượng, không đo lỗi |

**Paper gần nhất (cập nhật 2026-10-24): Hall & Baniassad (2022).** Hall & Baniassad giống RQ ở P (sinh viên), I (phản hồi mutation) và C (phản hồi coverage), khác ở O (mutant do người soạn, không phải bài làm sai thật). Như vậy giống 3/4 yếu tố, ngang Alonge (2025), nhưng là bài có bình duyệt và quy mô lớn hơn (596 sinh viên so với 10). Alonge giữ vai trò paper gần thứ hai. Nhãn tính mới không đổi: **extension**, khác 1 yếu tố có gap (O), cùng với thiết kế (cùng sinh viên, cùng thời gian) là hệ quả của gap.

Điểm Hall & Baniassad liên quan trực tiếp tới phép đo của nhóm: họ chạy test của sinh viên trên lời giải mẫu trước, test fail ở đó được tính là "over-asserting" (tr. 30); mutant chỉ tính là bị diệt khi test pass trên lời giải mẫu và fail trên mutant (4.2, tr. 27). Phép đo mới của nhóm (§5.9) dùng đúng quy tắc này, thay mutant bằng bài nộp WA thật.

### 1.1 Trả lời ba câu hỏi về Alonge (2025)

- **Loại lỗi:** conceptual mutants, tức các biến thể có lỗi do chính nhà nghiên cứu thiết kế (tr. 32, 34). Không dùng bài làm sai thật của người viết mã.
- **Giai đoạn đo:** đo ở post-test, trên 5 bài **khác** với bài luyện tập, sinh viên không được xem phản hồi (tr. 43). Kết quả phản ánh kỹ năng chuyển giao, không phải mức cải thiện của bộ test trên chương trình vừa nhận phản hồi.
- **Khác thiết kế dự kiến ở đâu:**
  - Hai nhóm độc lập 5 người, so với crossover trên cùng sinh viên.
  - Không cân bằng thời gian giữa hai điều kiện. Tác giả tự nêu: "time constraints of the study may have reduced students' opportunity to fully process the feedback" (6.4, tr. 62).
  - Không có kiểm định thống kê ở chương kết quả. Tác giả nêu: "the study was conducted with a relatively small sample size, which limits the scope of the findings" (6.4, tr. 62).
  - Python, ứng dụng Muttle, so với Java, JaCoCo và PITest.

## 2. Kiểm tra nghiên cứu tiếp nối

Tra các bài trích dẫn qua Semantic Scholar API ngày 2026-10-22 (Hall & Baniassad: ngày 2026-10-24), và tìm kiếm web ngày 2026-10-21 và 2026-10-22 (truy vấn Q5–Q7 trong `Pham Nhat Thang/SLR/search-log.md` §8).

| Bài gốc | Số bài trích dẫn | Có bài nào làm phần khác biệt còn lại không |
|---|---|---|
| Alonge (2025) | Không có bản ghi trên Semantic Scholar; tìm kiếm web không thấy bài trích dẫn | Không |
| Clegg et al. (2021) | 7 | Không. Gồm Perretta 2022 (dòng trên), T-P19, AutoFeedback (CSE 2025, phản hồi cho mã sinh viên), sinh bài làm sai bằng LLM (2024), công cụ mutation cho Racket (2023), khung test hệ thống (2025), "Diagnosability, Adequacy & Size: How Test Suites Impact Autograding" (HICSS 2022). Không bài nào so phản hồi coverage với mutation |
| Perretta et al. (2022) | 9 | Không. Gồm T-P29, Perretta et al. 2025 (gợi ý viết tay, chỉ mutation, C++), hai bài về phát hiện mutant tương đương bằng LLM, Faded Parsons, công cụ mutation cho Racket, sinh bài làm sai bằng LLM, và hai bài ngoài chủ đề (MutDBD cho mạng nơ-ron; Differential Prompting tìm test gây lỗi) |
| T-P28 (2024) | 4 | Mansur et al. 2026 (dòng trên), T-P19, chi phí mutation trên hệ thống chấm (2025), một bài đề xuất chưa đánh giá trên lớp học (ICPEC 2025) |
| T-P29 (2026) | 0 | — |
| Hall & Baniassad (2022) | 6 (Semantic Scholar, 2026-10-24) | Không. Gồm T-P28, T-P29, Mansur et al. 2026, Shin & Kazerouni (TOCE), AutoFeedback (CSE 2025, phản hồi theo test của giảng viên cho mã sinh viên, so hai khoá), bucket grading (TOCE 2025, so hai khoá, cách chấm điểm). Hai bài 2025 chỉ đọc tóm tắt; cả hai không so phản hồi coverage với mutation |
| Mansur et al. (2026) | 1 | Chỉ có bài về chi phí mutation trên hệ thống chấm (2025) |

## 3. Điểm mới và đóng góp dự kiến

**Điểm mới cần chứng minh:** so sánh phản hồi nhánh chưa phủ của JaCoCo và phản hồi mutant sống sót của PITest theo **mức cải thiện khả năng phát hiện bài làm sai độc lập**, thay vì chỉ đánh giá bằng chính chỉ số mà sinh viên được hướng dẫn tối ưu.

Phạm vi khẳng định: trong các nghiên cứu ở §1 và các nghiên cứu tiếp nối ở §2, chưa thấy nghiên cứu nào đồng thời có ba điều sau:
1. Loại phản hồi được gán theo thiết kế trên cùng sinh viên.
2. Đánh giá bằng tập bài nộp sai thật, được giữ kín, của cùng bài toán.
3. Hai điều kiện có cùng ngân sách thời gian.

Hall & Baniassad (2022) và T-P28 so hai loại phản hồi giữa các học kỳ (không có điều 1 trên cùng sinh viên), đo bằng mutant, không có điều 2 và 3. Alonge (2025) có điều 1 ở dạng hai nhóm độc lập nhưng không có điều 2 và 3. Clegg (2021) và Perretta (2022) có bài làm sai thật nhưng không có điều 1. Đổi thước đo từ mutation score sang tỉ lệ phát hiện WA chỉ là một phần của điểm mới.

**Đóng góp dự kiến:**
1. Bằng chứng thực nghiệm về chênh lệch mức cải thiện khả năng phát hiện bài WA giữa hai loại phản hồi, trong cùng ngân sách thời gian.
2. Phân tích xem chênh lệch đó đến từ việc bổ sung nhiều test hơn, hay vẫn còn khi so các bộ test cùng kích thước. Kích thước tính theo số đầu vào kiểm thử độc lập.
3. Bộ dữ liệu đánh giá và quy trình chạy tái lập được: tiêu chí chọn bài, danh sách bài AC/WA kèm manifest SHA-256, cách xác định oracle, bộ test trước–sau, và mã phân tích (`tools/gap1-pilot/`).

Không đưa khuyến nghị về chi phí sử dụng PITest. Nghiên cứu không đo thời gian chạy công cụ và thời gian xử lý phản hồi đủ để kết luận cho CI hoặc dự án lớn.

## 4. RQ

> Trong cùng ngân sách thời gian bổ sung kiểm thử, phản hồi nhánh chưa phủ của JaCoCo và phản hồi mutant sống sót của PITest tạo ra chênh lệch như thế nào về mức tăng tỉ lệ phát hiện các bài nộp Wrong Answer được giữ kín của cùng bài toán, so với bộ JUnit ban đầu?

- **P:** sinh viên bổ sung JUnit cho 12 chương trình Java thuộc IBM CodeNet. Mỗi chương trình là một bài nộp Accepted của một bài toán.
- **I / C:** phản hồi nhánh chưa phủ (JaCoCo) so với phản hồi mutant sống sót (PITest); mốc so sánh là bộ JUnit sinh viên viết trước khi xem phản hồi.
- **O:** mức tăng tỉ lệ bài nộp WA (của cùng bài toán, được giữ kín) bị bộ test phát hiện, sau trừ trước.
- **Ngân sách thời gian:** mỗi phiên bổ sung test có cùng thời lượng cho cả hai loại phản hồi. Thời lượng cụ thể chốt bằng mini-pilot với 5 sinh viên.
- **Phân tích bổ sung về kích thước:** kích thước bộ test là số đầu vào kiểm thử độc lập, tức số chuỗi đầu vào khác nhau sau chuẩn hoá xuống dòng, không phải số phương thức JUnit. Chênh lệch được ước lượng lại khi kiểm soát kích thước. Ngoài ra so riêng các cặp phiên có cùng số đầu vào độc lập.

## 5. Pilot

Toàn bộ script nằm trong `tools/gap1-pilot/`:
- `codenet_subset.py`: chọn bài và trích dữ liệu.
- `wa_pilot.py`: đo WA.
- `crossover_design.py`: lịch crossover và cỡ mẫu.

Cách chạy lại có trong README của thư mục đó.

### 5.1 Chọn bài

`codenet_subset.py` lấy ngẫu nhiên 15 bài (12 chính, 3 dự phòng), seed 2026, trong số bài đạt cả bốn tiêu chí:
- có ít nhất một cặp Sample Input/Output;
- có đáp án duy nhất: loại bài chấm số thực có sai số, bài nhiều đáp án, bài tương tác;
- có ít nhất 30 bài Java Accepted và 30 bài Java Wrong Answer;
- trung vị kích thước mã AC không quá 2.000 byte và trung vị thời gian chạy AC không quá 1.000 ms.

Lý do đạt hoặc không đạt của từng bài được ghi trong `candidates.csv`.

**Kết quả trên CodeNet (tập con trích ngày 2026-10-23, `candidates.csv`, `selected.csv`):**
- Metadata có 4.053 bài; 722 bài đạt cả bốn tiêu chí. Số bài vi phạm từng tiêu chí (một bài có thể vi phạm nhiều tiêu chí): Java WA < 30: 2.825; Java AC < 30: 2.552; trung vị mã AC > 2.000 byte: 2.151; trung vị CPU AC > 1.000 ms: 1.233; không có Sample Input/Output: 609; không có đáp án duy nhất: 488; không có mô tả: 54.
- 15 bài được chọn theo thứ tự: p02263, p02917, p03378, p03416, p03813, p01137, p02699, p03681, p03731, p03546, p03196, p03609 (12 chính); p03501, p03351, p03633 (dự phòng).
- **Quy tắc bổ sung sau pilot (chốt trước thực nghiệm):** loại bài mà riêng các Sample Input đã phát hiện 100% bài WA, vì phép đo không còn chỗ tăng. p03609 (45/45) và p03501 (36/36) bị loại theo quy tắc này. p03351 (dự phòng thứ hai) thay p03609.
- **12 bài dùng cho thực nghiệm:** p02263, p02917, p03378, p03416, p03813, p01137, p02699, p03681, p03731, p03546, p03196, p03351. Còn một bài dự phòng: p03633. Lịch crossover theo 12 bài này nằm trong `schedule_24.csv`; mỗi tổ hợp (chương trình, phiên, loại phản hồi) xuất hiện đúng 1 lần.

### 5.2 Áp dụng cùng đầu vào trên các bài nộp có cấu trúc mã khác nhau

- **Cách làm:** mọi bài nộp CodeNet là chương trình hoàn chỉnh, đọc stdin và ghi stdout. Mỗi bài nộp được chạy như một tiến trình độc lập (`java Main`), không sửa mã. File được chép nguyên văn sang `Main.java` vì Java yêu cầu tên file trùng tên lớp public.
- **Bài nộp bị loại:** bài có khai báo `package`, lớp chính không phải `Main`, hoặc không có hàm `main`. Các bài này được loại và đếm, không chuyển đổi mã.
- **Đầu vào của sinh viên:** lấy từ đối số chuỗi của `Judge.run(...)` trong file JUnit. Quy ước cho sinh viên: đầu vào phải là hằng chuỗi, nên lời gọi dùng biến sẽ không được tính và được đếm riêng.
- **Adapter duy nhất:** chương trình sinh viên kiểm thử phải chạy qua `Judge.run` (thêm `package codenet;`) để dùng được JUnit, JaCoCo và PITest. Pilot kiểm tra adapter này bằng cách chạy mọi đầu vào qua `Judge.run` trong một JVM (giống JUnit), so với output khi chạy tiến trình. Chỉ chọn chương trình khớp ở mọi đầu vào.
- **Kiểm thử trên dữ liệu tự tạo:** kiểm tra này đã bắt đúng trường hợp `static Scanner`, khớp 1/3 đầu vào.

**Kết quả trên CodeNet:**
- 0/1.170 bài AC và 0/1.112 bài WA của 12 bài bị loại do cấu trúc. Mọi bài nộp đều dùng lớp `Main`, không có `package`.
- Chọn được chương trình kiểm thử khớp `Judge.run` ở 100% đầu vào hợp lệ cho cả 13 bài (12 chính, 1 dự phòng).
- Kiểm tra adapter đã loại 3 ứng viên lệch khi chạy qua `Judge.run` trong một JVM: p02917 có 1 ứng viên (0/15 đầu vào khớp); p03378 có 2 ứng viên (mỗi ứng viên 1/8). Cả ba khớp khi chạy tiến trình độc lập nhưng lệch khi gọi nhiều lần trong một JVM, đúng dạng trạng thái `static` mà kiểm tra này nhắm tới. Nếu không có bước kiểm tra, bộ test của sinh viên trên hai bài này sẽ cho kết quả sai khi chạy bằng JUnit.

### 5.3 Xác định đầu ra đúng cho đầu vào mới

- **Cách làm:** chạy mỗi đầu vào trên một nhóm 20 bài AC (chọn ngẫu nhiên, đã loại trùng và bài không tất định). Oracle là output chung của ít nhất 90% bài AC chạy thành công, với tối thiểu 5 bài.
- Trước bước này, đầu vào được kiểm tra theo ràng buộc của đề (`validators.py`); đầu vào ngoài ràng buộc bị loại.
- Đầu vào không đạt ngưỡng đồng thuận bị loại, vì có thể có nhiều đáp án hoặc nằm ngoài ràng buộc mà bước kiểm tra chưa bắt được.
- Với Sample Input, oracle còn phải trùng Sample Output của đề.
- Nhãn WA không cho biết đầu vào nào làm bài nộp sai. Một bài WA chỉ tính là bị phát hiện khi có ít nhất một đầu vào hợp lệ của bộ test cho output khác oracle.

**Kết quả trên CodeNet:**
- **Sample Input:** 36/36 đầu vào của 12 bài có oracle. Oracle trùng Sample Output của đề ở 36/36. 20/20 bài AC trong nhóm oracle cho cùng output ở mọi Sample Input. Không có bài AC không tất định.
- **Đầu vào mới:** để thử phép đo, nhóm nghiên cứu viết 158 đầu vào bổ sung bằng `gen_extra.py` (đầu vào biên viết tay và đầu vào ngẫu nhiên theo seed). Đây không phải dữ liệu sinh viên. Trong số đó, 11 đầu vào vi phạm ràng buộc của đề (p03378: 8, vì có trạm thu phí ở ô N; p02917, p03196, p03731: mỗi bài 1). Quy tắc đồng thuận 90% chỉ loại được 4/11 đầu vào này; với 7 đầu vào còn lại, các bài AC vẫn cho cùng output.
- **Thay đổi quy trình:** thêm bước kiểm tra ràng buộc của đề trước khi xác định oracle (`validators.py`, viết tay cho 13 bài theo mục Constraints và Input). Đầu vào ngoài ràng buộc bị loại và đếm riêng, không dùng để tính phát hiện. Trong thực nghiệm, quy tắc này áp dụng cho đầu vào trong bộ JUnit của sinh viên.
- **Sau khi thêm bước kiểm tra:** cả 147 đầu vào bổ sung trong ràng buộc đều có oracle. Tổng cộng 183 đầu vào hợp lệ. Mức đồng thuận cụ thể:
  - 144 đầu vào: 20/20 bài AC cho cùng output.
  - 2 đầu vào: 18/18 bài AC chạy thành công cho cùng output.
  - 1 đầu vào: 19/20 bài AC cho cùng output (0,95).

### 5.4 Giữ kín tập WA đánh giá

- Danh sách bài WA đánh giá của mỗi bài toán được cố định trước khi thực nghiệm. Pilot đã tạo manifest cho 13 bài (12 chính, 1 dự phòng), bằng file `pXXXXX_heldout_manifest.csv` (mã bài nộp và SHA-256).
- Sinh viên chỉ nhận chương trình cần kiểm thử, cùng báo cáo JaCoCo hoặc PITest chạy trên chính chương trình đó. Sinh viên không có quyền truy cập thư mục WA và không chạy được bộ test trên bài WA trong phiên.
- Việc chạy bộ test trên tập WA chỉ thực hiện sau khi phiên kết thúc, bằng `wa_pilot.py`.

### 5.5 Mã trùng, lỗi biên dịch, timeout, lỗi hạ tầng

| Trường hợp | Cách xử lý |
|---|---|
| Mã trùng | Hai bài có cùng chuỗi token sau khi bỏ chú thích và khoảng trắng chỉ giữ một bài. Cặp gần trùng (Jaccard 5-gram token ≥ 0,9) được báo cáo |
| Lỗi biên dịch | Biên dịch bằng JDK 21; bài không biên dịch được bị loại |
| Không tất định | Mỗi cặp (bài WA, đầu vào) chạy hai lần. Bài cho kết quả khác nhau giữa hai lần bị loại |
| Timeout | Không tính là phát hiện. Nếu một lần quá giờ, một lần không, chạy lại với thời gian gấp 3 |
| Lỗi hạ tầng | JVM không khởi động được: chạy lại một lần, không tính là phát hiện. Tràn stack hoặc hết bộ nhớ trong lúc chạy tính là ngoại lệ (xem kết quả bên dưới) |
| Ngoại lệ | Chỉ tính "output khác oracle" là phát hiện ở thước đo chính. Ngoại lệ do chính chương trình (thoát với mã khác 0) chỉ tính ở thước đo phụ |

**Kết quả trên CodeNet (12 bài, sample cùng đầu vào bổ sung):**
- Mã trùng: loại 25 bài AC và 36 bài WA. Có 242 cặp WA gần trùng được báo cáo, không loại.
- Lỗi biên dịch: 0 bài, JDK 21.
- Không tất định: 1 bài WA (p03196) bị loại.
- Timeout: 64 lượt chạy (cặp bài WA, đầu vào), chiếm 0,4% trong 17.247 lượt. Có 1 cặp phải chạy lại với thời gian gấp 3.
- Ngoại lệ: 102 lượt.
- Lỗi hạ tầng: 0 lượt.
- **Thay đổi quy tắc:** bản đầu xếp `StackOverflowError` và `OutOfMemoryError` vào lỗi hạ tầng. Pilot cho thấy ở bài dự phòng p03633, 21 bài WA bị `StackOverflowError` vì hàm gcd đệ quy vô hạn sau khi tràn số, trong khi bài AC chạy bình thường trên cùng đầu vào với cùng giới hạn bộ nhớ. Đó là lỗi của chính chương trình. Bản hiện tại chỉ xếp vào lỗi hạ tầng trường hợp JVM không khởi động được; tràn stack và hết bộ nhớ khi chạy được tính là ngoại lệ (thước đo phụ). Thước đo chính (output khác oracle) không đổi.
- Tập WA đánh giá cuối cùng: 1.075 bài WA thuộc 12 bài. Manifest `pXXXXX_heldout_manifest.csv` ghi mã bài nộp, SHA-256 và trạng thái (đánh giá hoặc lý do loại) của từng bài.

### 5.6 Đối trọng thứ tự và phân công bài trong crossover

- Mỗi sinh viên làm hai phiên trên **hai chương trình khác nhau**: một phiên dùng phản hồi JaCoCo, một phiên dùng PITest. Không sinh viên nào cải thiện lại cùng một chương trình bằng cả hai loại phản hồi.
- Lịch cho mỗi khối 24 sinh viên:
  - sinh viên ở ô k (1–24) làm chương trình k và k+6 (lấy theo vòng 12);
  - 12 ô đầu làm JaCoCo trước, 12 ô sau làm PITest trước;
  - sinh viên được gán ngẫu nhiên vào ô (seed 2026).
- Kiểm tra: mỗi tổ hợp (chương trình, phiên 1 hoặc 2, JaCoCo hoặc PITest) xuất hiện đúng 1 lần trong mỗi khối 24 sinh viên (`schedule_24.csv`). Như vậy chương trình, thứ tự và loại phản hồi được cân bằng hoàn toàn.

### 5.7 Cỡ mẫu và cách phân tích dữ liệu lặp

**Phân tích chính:**
- Đơn vị phân tích là phiên (sinh viên × chương trình). Giá trị của mỗi phiên là mức tăng tỉ lệ phát hiện WA của phiên đó.
- Mỗi sinh viên cho một hiệu d = mức tăng (PITest) − mức tăng (JaCoCo). Kiểm định chính (theo proposal §6, từ 2026-10-28): Wilcoxon signed-rank ghép cặp trên d, ước lượng Hodges–Lehmann và khoảng tin cậy 95%. Hồi quy d theo thứ tự làm bài (crossover 2×2) là phân tích bổ sung để kiểm tra ảnh hưởng của thứ tự.
- Ảnh hưởng của chương trình được cân bằng nhờ lịch ở §5.6.
- Các lượt chạy trên từng bài WA chỉ dùng để tính tỉ lệ của phiên, không được xem là quan sát độc lập.

**Phân tích bổ sung:** mô hình hỗn hợp nhị phân ở cấp bài WA, với hiệu ứng ngẫu nhiên cho sinh viên, chương trình và bài WA.

**Cỡ mẫu:** (thay ngày 2026-10-28) bản trước lấy SD từ Alonge (Table 5.1). Cách này đã bỏ, vì Alonge đo đại lượng khác, thiết kế giữa nhóm, nên không cho biết độ biến thiên của ΔWADR hay tương quan giữa hai phiên của cùng sinh viên. Cỡ mẫu nay tính bằng mô phỏng nhiều kịch bản, xem §5.17.

### 5.8 Tỉ lệ ở cấp bài nộp và nhóm hành vi (pilot 2026-10-23, tập đầu vào tham chiếu)

Tỉ lệ phát hiện WA được báo cáo ở hai cấp:
- **Cấp bài nộp:** tỉ lệ bài WA bị phát hiện.
- **Nhóm hành vi (chỉ để mô tả):** các bài WA cho cùng output trên **tập đầu vào tham chiếu cố định** (Sample Input và đầu vào do nhóm nghiên cứu viết, đã khoá ở §5.11). Hai bài cùng nhóm chỉ có nghĩa là chúng giống nhau trên tập đầu vào đã khảo sát; **không suy ra chúng có cùng lỗi gốc**, vì với đầu vào khác chúng có thể tách ra. Nhóm hành vi không dùng làm thước đo chính.

Thước đo chính là tỉ lệ ở cấp bài nộp, trên mẫu số WA cố định. Tỉ lệ này cũng không đồng nghĩa với tỉ lệ phát hiện lỗi gốc độc lập.

**Kết quả trên CodeNet:**

Nhóm hành vi được xác định trên toàn bộ đầu vào hợp lệ của bài. Cột "sample + bổ sung" dùng đầu vào do nhóm nghiên cứu viết (§5.3), không phải bộ test của sinh viên.

| Bài | WA đánh giá | Nhóm hành vi | Đầu vào sample | Phát hiện bài nộp | Phát hiện nhóm | Đầu vào sample + bổ sung | Phát hiện bài nộp | Phát hiện nhóm |
|---|---|---|---|---|---|---|---|---|
| p02263 | 92 | 50 | 2 | 63/92 (0,69) | 33/50 (0,66) | 15 | 91/92 (0,99) | 49/50 (0,98) |
| p02917 | 106 | 54 | 3 | 52/106 (0,49) | 35/54 (0,65) | 15 | 106/106 (1,00) | 54/54 (1,00) |
| p03378 | 48 | 25 | 3 | 14/48 (0,29) | 8/25 (0,32) | 8 | 45/48 (0,94) | 24/25 (0,96) |
| p03416 | 81 | 28 | 2 | 21/81 (0,26) | 15/28 (0,54) | 16 | 80/81 (0,99) | 27/28 (0,96) |
| p03813 | 33 | 10 | 2 | 21/33 (0,64) | 8/10 (0,80) | 15 | 33/33 (1,00) | 10/10 (1,00) |
| p01137 | 29 | 18 | 1 | 18/29 (0,62) | 11/18 (0,61) | 14 | 28/29 (0,97) | 17/18 (0,94) |
| p02699 | 108 | 27 | 3 | 85/108 (0,79) | 26/27 (0,96) | 17 | 108/108 (1,00) | 27/27 (1,00) |
| p03681 | 128 | 65 | 4 | 92/128 (0,72) | 52/65 (0,80) | 18 | 128/128 (1,00) | 65/65 (1,00) |
| p03731 | 48 | 28 | 5 | 21/48 (0,44) | 19/28 (0,68) | 16 | 48/48 (1,00) | 28/28 (1,00) |
| p03546 | 89 | 25 | 3 | 6/89 (0,07) | 6/25 (0,24) | 14 | 88/89 (0,99) | 24/25 (0,96) |
| p03196 | 92 | 34 | 4 | 15/92 (0,16) | 11/34 (0,32) | 17 | 75/92 (0,81) | 32/34 (0,94) |
| p03351 | 221 | 73 | 4 | 164/221 (0,74) | 54/73 (0,74) | 18 | 209/221 (0,95) | 72/73 (0,99) |

- Riêng các Sample Input phát hiện trung vị 0,56 bài WA (thấp nhất 0,07, cao nhất 0,79).
- Ở p03546, sample phát hiện 6/89 bài nộp (0,07) nhưng 6/25 nhóm (0,24). Như vậy phần lớn bài WA có cùng output trên tập tham chiếu, nên tỉ lệ cấp bài nộp và cấp nhóm có thể khác nhau nhiều. Cả hai cấp đều được báo cáo.

**Độ nhạy và hiệu ứng trần của thước đo** (`headroom.py`): thêm k đầu vào bổ sung, chọn ngẫu nhiên 2.000 lần, vào bộ sample.

| Bài | WA | Sample | +1 đầu vào (TB [P10–P90]) | +3 đầu vào (TB [P10–P90]) | +5 đầu vào (TB [P10–P90]) | + toàn bộ |
|---|---|---|---|---|---|---|
| p01137 | 29 | 0,62 | 0,72 [0,62–0,79] | 0,81 [0,72–0,93] | 0,86 [0,72–0,97] | 0,97 (13) |
| p02263 | 92 | 0,68 | 0,90 [0,75–0,97] | 0,97 [0,96–0,99] | 0,98 [0,96–0,99] | 0,99 (13) |
| p02699 | 108 | 0,79 | 0,82 [0,79–1,00] | 0,87 [0,79–1,00] | 0,91 [0,79–1,00] | 1,00 (14) |
| p02917 | 106 | 0,49 | 0,82 [0,49–1,00] | 0,98 [0,86–1,00] | 1,00 [1,00–1,00] | 1,00 (12) |
| p03196 | 92 | 0,16 | 0,31 [0,16–0,55] | 0,50 [0,21–0,77] | 0,62 [0,53–0,82] | 0,82 (13) |
| p03351 | 221 | 0,74 | 0,79 [0,75–0,87] | 0,85 [0,76–0,91] | 0,89 [0,80–0,93] | 0,95 (14) |
| p03378 | 48 | 0,29 | 0,54 [0,35–0,85] | 0,82 [0,67–0,92] | 0,94 [0,94–0,94] | 0,94 (5) |
| p03416 | 81 | 0,26 | 0,50 [0,27–0,91] | 0,79 [0,56–0,98] | 0,91 [0,62–0,99] | 0,99 (14) |
| p03546 | 89 | 0,07 | 0,46 [0,07–0,87] | 0,79 [0,39–0,97] | 0,91 [0,79–0,98] | 0,99 (11) |
| p03681 | 128 | 0,72 | 0,84 [0,72–0,95] | 0,94 [0,94–0,99] | 0,96 [0,95–1,00] | 1,00 (14) |
| p03731 | 48 | 0,44 | 0,52 [0,44–0,54] | 0,64 [0,46–0,98] | 0,76 [0,54–1,00] | 1,00 (11) |
| p03813 | 33 | 0,64 | 0,67 [0,64–0,64] | 0,72 [0,64–1,00] | 0,77 [0,64–1,00] | 1,00 (13) |

- **Thước đo nhạy:** thêm 1–3 đầu vào hợp lệ đã làm tỉ lệ phát hiện tăng rõ ở phần lớn bài. Ví dụ p03546 tăng từ 0,07 lên trung bình 0,46 với 1 đầu vào và 0,79 với 3 đầu vào.
- **Thước đo có trần:** với toàn bộ đầu vào bổ sung (5–14 đầu vào mỗi bài), **10/12 bài** đạt ít nhất 0,94 tính trên giá trị chưa làm tròn. Hai bài còn lại là p03378 (45/48 = 0,9375) và p03196 (75/92 = 0,815). Bản 2026-10-23 ghi 11/12 do so giá trị đã làm tròn 0,94; đã sửa.
- **Hệ quả:** nếu ngân sách thời gian cho phép sinh viên viết nhiều đầu vào ở cả hai điều kiện, cả hai điều kiện có thể chạm trần và chênh lệch bị thu hẹp bất kể loại phản hồi.
- **Các việc cần chốt trước thực nghiệm:**
  1. Chọn ngân sách thời gian bằng mini-pilot 5 sinh viên, sao cho mức sau phản hồi chưa chạm trần.
  2. Giữ mọi phiên hợp lệ trong phân tích chính, kể cả phiên có mức sau phản hồi ≥ 0,95. Tỉ lệ phiên chạm trần được báo cáo riêng theo từng điều kiện. (Bản 2026-10-23 đề xuất phân tích loại các phiên này; đã bỏ, vì loại phiên dựa trên kết quả làm lệch so sánh.)
  3. Chọn bài và chương trình kiểm thử theo tiêu chí công khai ở §5.12–5.13 (thay cho đề xuất thay riêng ba bài p02699, p03813, p03351 ở bản 2026-10-23).


### 5.9 Phép đo chính: chạy chính bộ JUnit của sinh viên (thay đổi 2026-10-24)

Bản 2026-10-23 chỉ trích đầu vào từ `Judge.run(...)` rồi so output của bài WA với oracle chung. Cách đó bỏ qua expected output và assertion của sinh viên, nên đo khả năng của **tập đầu vào**, không phải của **bộ JUnit**. RQ được giữ nguyên (về bộ JUnit); phép đo đổi như sau (`junit_eval.py`):

- **Test hợp lệ:** pass trên chương trình được kiểm thử (PUT) ở cả hai lần chạy, và mọi đầu vào test đó truyền vào `Judge.run` nằm trong ràng buộc của đề.
  - Test fail trên PUT (expected sai, assertion sai) bị loại, nhãn `method`. Đây là quy tắc "over-asserting" của Hall & Baniassad (2022, 5.4.3, tr. 30).
  - Test dùng đầu vào ngoài ràng buộc bị loại, nhãn `parse`: bài WA có thể sai ở đó mà vẫn đúng trong phạm vi đề.
  - Test lúc pass lúc fail trên PUT bị loại.
- **Bài WA bị phát hiện (thước đo chính):** có ít nhất một test hợp lệ **fail do assertion** (`AssertionError`, gồm `AssertionFailedError` của JUnit 5) trên bài WA đó, ở cả hai lần chạy.
- **Thước đo phụ:** tính thêm trường hợp test hợp lệ báo lỗi do bài WA ném ngoại lệ.
- **Không tính là phát hiện, bài WA vẫn nằm trong mẫu số:** quá 4 giây mỗi test, JVM dừng (`System.exit`), hoặc hai lần chạy cho kết quả khác nhau.
- **Mẫu số cố định:** danh sách WA trạng thái "đánh giá" trong manifest đã khoá (§5.11). Không có bài WA nào bị loại sau khi khoá.
- **WADR** = số WA bị phát hiện / mẫu số; **ΔWADR** = WADR sau phản hồi − WADR trước phản hồi.
- **Kích thước bộ test:** số đầu vào độc lập mà các test hợp lệ **thực sự** truyền vào `Judge.run`, ghi lại lúc chạy trên PUT. Cách này đếm được cả đầu vào ghép bằng hàm phụ, điều trích tĩnh không làm được.
- **Không tự thêm đầu vào nào:** bộ test được chấm đúng như sinh viên nộp. Sample Input chỉ có mặt nếu nằm trong bộ test (xem baseline ở §5.11).

**Cách chạy.** Assertion dùng JUnit 5.10.2 thật (`junit-platform-console-standalone-1.10.2.jar`). Mỗi lượt (một bộ test × một chương trình) chạy trong một JVM riêng; các test chạy theo thứ tự tên. Bộ chấm dùng một bản `Judge` cùng API với `Judge.java` của sinh viên (`EvalJudge.java`), khác ba điểm để kết quả trong JVM giống khi chạy chương trình như tiến trình:
1. Mỗi lần gọi nạp lại `Main` trong ClassLoader mới, nên biến static không mang sang lần gọi sau.
2. Chờ các luồng do chương trình tạo kết thúc. Ví dụ p02917 `s040638807` chạy phần chính trong `new Thread(...)`; nếu không chờ, output rỗng và bài bị tính "phát hiện" sai.
3. Không flush hộ `System.out` khi chương trình tự bọc nó bằng bộ đệm. Ví dụ p02917 `s744727054` không bao giờ flush nên khi chạy thật không in gì (đó là lý do bị WA); nếu bộ chấm flush hộ, bài này lại cho output đúng.

Lớp `Main` không public (ví dụ `class Main {`) cũng chạy được, như khi chạy `java Main`. Lỗi của chính bộ chấm có trạng thái riêng `HARNESS`, không tính là phát hiện.

Môi trường **của sinh viên** vẫn dùng `Judge.java` gốc, vì PITest thay lớp `Main` bằng mutant trong bộ nạp lớp của nó; nạp lại từ đĩa sẽ làm hỏng phân tích mutant.

**Trích đầu vào tĩnh** (`wa_pilot.inputs_from_junit`) nay bỏ chú thích `//` và `/* */` trước khi tìm, và xử lý text block theo quy tắc của Java (bỏ thụt lề chung). Hàm này chỉ còn dùng để báo cáo, không dùng để chấm.

### 5.10 Kiểm tra phép đo mới

**(a) Đối chiếu với phép đo cũ trên bộ Sample.** Với bộ JUnit chỉ gồm các cặp Sample (mỗi cặp một `assertEquals` toàn bộ output), số WA phát hiện bằng JUnit thật trùng đúng với phép đo theo đầu vào ở §5.8, ở cả 12/12 bài:

| Bài | p02263 | p02917 | p03378 | p03416 | p03813 | p01137 | p02699 | p03681 | p03731 | p03546 | p03196 | p03351 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WA phát hiện / mẫu số | 63/92 | 52/106 | 14/48 | 21/81 | 21/33 | 18/29 | 85/108 | 92/128 | 21/48 | 6/89 | 15/92 | 164/221 |

Hai phép đo chỉ được kỳ vọng trùng khi assertion so toàn bộ output; chúng khác nhau khi assertion yếu hoặc expected sai, như ví dụ (b). Trước khi sửa ba điểm của bộ chấm ở §5.9, p02917 cho 55/106 thay vì 52/106 (5 bài lệch, do luồng riêng và bộ đệm chưa flush).

**(b) Bộ test thử trên p03546** (`probe_p03546/`):
- Test có expected sai (`"6"`, đúng là `"5"`): fail trên PUT, bị loại với lý do "FAIL trên PUT: expected: <6> but was: <5>".
- Test assertion yếu `assertFalse(Judge.run(x).isEmpty())`: phát hiện 0/89 bài WA. Cùng đầu vào x với `assertEquals("5", Judge.run(x))`: phát hiện 5/89. Phép đo cũ (so output với oracle) sẽ tính cả test yếu là phát hiện 5/89.
- Lời gọi `Judge.run` nằm trong chú thích không được tính.

### 5.11 Baseline, khoá tập WA và tập đầu vào tham chiếu

**Baseline (đề xuất, nhóm chốt):** bộ JUnit ban đầu là **bộ Sample bắt buộc**, phát sẵn cho mọi sinh viên (`make_sample_suite.py`: mỗi cặp Sample Input/Output của đề một `@Test` với `assertEquals`). Lý do:
- Mọi sinh viên bắt đầu từ cùng một bộ test, nên WADR trước phản hồi của mỗi bài là cố định và đã biết (bảng 5.10a).
- Báo cáo JaCoCo và PITest ban đầu được tính trên cùng bộ test này, nên hai điều kiện nhận báo cáo về cùng một điểm xuất phát.
- Phương án còn lại, để sinh viên tự viết bộ ban đầu, cũng chấm được bằng `junit_eval.py`, nhưng thêm biến thiên giữa sinh viên và cần thêm thời gian. Nếu chọn phương án này, WADR trước phản hồi tính trên đúng bộ sinh viên viết, không thêm Sample.
- Trong RQ, "bộ JUnit ban đầu" khi đó là bộ Sample phát sẵn; proposal cần ghi rõ điều này.

**Khoá tập WA (2026-10-24):** 13 manifest (12 bài chính, 1 dự phòng), tổng 1.075 bài WA đánh giá ở 12 bài chính. SHA-256 của từng manifest ghi trong `frozen/frozen_index.json`. Từ nay mẫu số không đổi.

**Tập đầu vào tham chiếu cố định (chỉ cho phân tích nhóm hành vi):** Sample Input cùng các đầu vào do nhóm nghiên cứu viết, đã qua kiểm ràng buộc: 183 đầu vào ở 12 bài, lưu ở `frozen/reference_inputs/` kèm SHA-256. Nhóm hành vi chỉ tính trên tập này, không tính trên bộ test của từng sinh viên, và chỉ dùng để mô tả.

### 5.12 Phản hồi có điều để báo ở cả hai điều kiện không

Câu hỏi của giảng viên: hai loại phản hồi có được cung cấp trong điều kiện công bằng không? Pilot chạy JaCoCo 0.8.12 và PITest 1.16.1 (mutator mặc định) trên bộ Sample của 12 chương trình kiểm thử hiện tại:

| Bài | WADR trước (bộ Sample) | Nhánh phủ (JaCoCo) | Dòng còn nhánh chưa phủ | Mutant bị diệt (PITest) | SURVIVED | NO_COVERAGE |
|---|---|---|---|---|---|---|
| p02263 | 63/92 (0,685) | 6/6 | 0 | 6/6 | 0 | 0 |
| p02917 | 52/106 (0,491) | 8/8 | 0 | 14/15 | 1 | 0 |
| p03378 | 14/48 (0,292) | 6/6 | 0 | 8/11 | 2 | 1 |
| p03416 | 21/81 (0,259) | 4/4 | 0 | 9/10 | 1 | 0 |
| p03813 | 21/33 (0,636) | 4/4 | 0 | 3/5 | 2 | 0 |
| p01137 | 18/29 (0,621) | 12/14 | 2 | 21/26 | 4 | 1 |
| p02699 | 85/108 (0,787) | 2/2 | 0 | 5/5 | 0 | 0 |
| p03681 | 92/128 (0,719) | 9/10 | 1 | 19/21 | 2 | 0 |
| p03731 | 21/48 (0,438) | 8/8 | 0 | 15/17 | 2 | 0 |
| p03546 | 6/89 (0,067) | 35/36 | 1 | 34/38 | 4 | 0 |
| p03196 | 15/92 (0,163) | 25/122 | 44 | 46/274 | 1 | 227 |
| p03351 | 164/221 (0,742) | 5/6 | 1 | 8/11 | 3 | 0 |

- **JaCoCo báo 100% nhánh ở 8/12 bài**, tức điều kiện JaCoCo không nhận được gì để làm, trong khi WADR trước còn thấp (ví dụ p03378 0,29; p03416 0,26).
- **PITest không còn mutant sống sót ở 2/12 bài** (p02263, p02699).
- Chỉ 4/12 bài cả hai báo cáo đều có nội dung (p01137, p03681, p03546, p03351), chưa kể p03196 có 44 dòng còn nhánh chưa phủ chủ yếu nằm trong mã không dùng.
- Một phần nội dung còn lại chưa phủ/diệt được bằng các test đã thử. Ba mục dưới đây được một thành viên lập luận trên mã; đây chưa phải kiểm tra riêng theo quy tắc mới (hai người độc lập, người thứ ba quyết), nên chỉ được gọi là "chưa phủ/diệt được bằng tập tham chiếu": p01137 dòng 15 và 24 (vế `Math.pow((int)Math.cbrt(e),3) <= e` gần như luôn đúng vì phép ép kiểu làm tròn xuống; 4 test nhắm vào hai dòng này ở §5.14 vẫn không phủ được), p03546 dòng 51 (lập luận: theo ràng buộc mọi chi phí c_ij ≥ 1 với i ≠ j, nên đồ thị luôn liên thông và nhánh `distance == MAX_VALUE` có thể không xảy ra); mutant xoá lời gọi `dijkstra` ở dòng 22 của p03546 (lập luận: mảng kết quả bị tính lại trước mỗi lần dùng, nên mutant có thể tương đương).

Nếu giữ nguyên, so sánh ở 8/12 bài thực chất là "báo cáo PITest so với báo cáo rỗng", không phải so hai loại phản hồi. Vấn đề này sửa được trong phạm vi đề tài bằng tiêu chí chọn chương trình kiểm thử (§5.13). WADR trước phản hồi không đổi khi đổi PUT, vì bộ Sample pass trên mọi bài AC và chỉ phụ thuộc vào tập WA.

### 5.13 Tiêu chí công khai chọn bài, chương trình kiểm thử và thời lượng

**Chương trình kiểm thử (PUT)** (`scan_put.py`): duyệt các bài AC của mỗi bài theo thứ tự ngẫu nhiên cố định (seed 2026), tối đa 30 ứng viên, chọn ứng viên đầu tiên đạt cả năm điều kiện:
1. không gọi `System.exit` (lệnh này làm dừng cả lượt chạy JUnit của sinh viên; PUT hiện tại của p01137 có lệnh này);
2. chạy qua `Judge.run` (mọi đầu vào trong một JVM) cho output giống hệt oracle trên toàn bộ tập tham chiếu;
3. trên bộ Sample, JaCoCo còn ít nhất 1 nhánh chưa phủ **và** PITest còn ít nhất 1 mutant SURVIVED;
4. ít nhất 1 nhánh chưa phủ đó được bộ test tham chiếu phủ;
5. bộ test tham chiếu diệt được ít nhất 1 mutant sống sót đó.

Bộ test tham chiếu = mỗi đầu vào tham chiếu một test, expected = oracle. Một bản trước của điều kiện 4 đòi bộ tham chiếu phủ 100% chương trình; trên p02263 không ứng viên nào trong 30 đạt, vì nhánh còn lại sau bộ Sample gần như luôn là nhánh mà tập tham chiếu chưa phủ được (ví dụ nhánh xử lý toán tử `/` mà đề không có), nên đã nới thành điều kiện 4 hiện tại. Số nhánh và mutant trong báo cáo mà bộ tham chiếu cũng chưa phủ/diệt được (mục chưa phủ/diệt được bằng tập tham chiếu) được ghi lại và báo cáo như một đặc điểm của từng bài.

**Kết quả quét (2026-10-24,** `scan_put/`**):**

| Bài | Ứng viên đã xét | JaCoCo 100% trên bộ Sample | Nhánh còn lại đều chưa phủ được bằng tập tham chiếu | Lý do khác (System.exit, Judge.run lệch, PITest rỗng hoặc mutant không diệt được) | PUT đạt |
|---|---|---|---|---|---|
| p02263 | 27 | 11 | 11 | 4 | **s781975706**: JaCoCo 12/14 (tập tham chiếu phủ được 1, chưa phủ được 1); PITest 18/24, sống sót 2 (diệt được 1) |
| p02917 | 30 | 26 | 1 | 3 | không có |
| p03378 | 8 | 5 | 2 | 0 | **s045451427**: JaCoCo 5/6 (tập tham chiếu phủ được 1, chưa phủ được 0); PITest 7/10, sống sót 3 (diệt được 1) |
| p03416 | 13 | 9 | 3 | 0 | **s526219859**: JaCoCo 6/8 (tập tham chiếu phủ được 2, chưa phủ được 0); PITest 19/25, sống sót 6 (diệt được 3) |
| p03813 | 30 | 26 | 2 | 2 | không có |
| p01137 | 30 | 12 | 5 | 13 | không có |
| p02699 | 30 | 24 | 2 | 4 | không có |
| p03681 | 6 | 2 | 0 | 3 | **s735700476**: JaCoCo 7/8 (tập tham chiếu phủ được 1, chưa phủ được 0); PITest 16/18, sống sót 2 (diệt được 1) |
| p03731 | 30 | 20 | 2 | 8 | không có |
| p03546 | 30 | 13 | 8 | 9 | không có |
| p03196 | 2 | 0 | 0 | 1 | **s773186766**: JaCoCo 9/78 (tập tham chiếu phủ được 1, chưa phủ được 68); PITest 18/146, sống sót 4 (diệt được 2) |
| p03351 | 1 | 0 | 0 | 0 | **s945187436**: JaCoCo 5/6 (tập tham chiếu phủ được 1, chưa phủ được 0); PITest 7/10, sống sót 3 (diệt được 2) |

- **6/12 bài có PUT đạt** (p02263, p03378, p03416, p03681, p03196, p03351). **6/12 bài không có PUT nào đạt trong 30 ứng viên** (p02917, p03813, p01137, p02699, p03731, p03546).
- Lý do chính: với bộ Sample, đa số lời giải AC đã được phủ 100% nhánh. Khi còn nhánh chưa phủ, tập tham chiếu thường cũng chưa phủ được nhánh đó (ví dụ nhánh xử lý toán tử không có trong đề).
- PUT đạt của p03196 vẫn có 68 nhánh mà tập tham chiếu chưa phủ được trong báo cáo (phần lớn trong mã mẫu không dùng tới), tức báo cáo JaCoCo có nhiều mục nhiễu. Đề xuất thêm điều kiện: số nhánh chưa phủ được bằng tập tham chiếu trong báo cáo baseline không quá số nhánh phủ được [CẦN NHÓM CHỐT]; nếu áp dụng, p03196 cũng cần thay.
- **Hệ quả cho thiết kế:** với baseline là bộ Sample, một nửa số bài đã chọn không để lại trong báo cáo JaCoCo nhánh nào mà tập tham chiếu phủ được. Đây là đặc điểm của bài lập trình nhỏ, không phải lỗi của công cụ, và chính là một giới hạn cần nêu ở §7 của proposal: kết quả chỉ suy rộng cho bài mà cả hai báo cáo đều có nội dung.
- **Bài dự phòng p03633:** có PUT đạt (s203672004, ứng viên thứ 16; JaCoCo 5/6, PITest 11/14, sống sót 2), nên thay được một bài. Còn thiếu 5 bài.
- **Cách xử lý trong phạm vi đề tài:** chọn thêm bài theo đúng thứ tự ngẫu nhiên seed 2026 trong 722 bài đạt, chạy cùng quy trình (oracle, khoá WA, validator, quét PUT) cho tới khi đủ 12 bài đạt. Chạy `codenet_subset.py` với `--n 45` cho 15 bài đầu trùng với lần chọn trước (đã kiểm tra), 30 bài tiếp theo là p03253, p02729, p00003, p03712, p00144, p02240, p02832, …; mỗi bài mới cần viết validator ràng buộc đề.
- **Phương án khác (nhóm chọn):** dùng baseline yếu hơn bộ Sample (ví dụ chỉ Sample đầu tiên) để còn nhánh cho JaCoCo báo. Phương án này giữ được bài nhưng baseline trở nên tuỳ ý, nên không đề xuất.

**Bài:** giữ bốn tiêu chí ở §5.1, thêm hai tiêu chí: (5) bộ Sample không phát hiện 100% WA; (6) tìm được PUT theo năm điều kiện trên trong 30 ứng viên. Bài không đạt (6) được thay bằng bài dự phòng p03633, rồi bằng bài chọn tiếp theo seed 2026 trong 722 bài đạt.

**Thời lượng (chốt bằng mini-pilot, §5.15):** thử T = 20, 30, 40 phút cho mỗi phiên, gồm cả thời gian chạy công cụ. Đề xuất quy tắc chọn, nhóm chốt trước mini-pilot: lấy T nhỏ nhất thoả cả hai điều kiện
- ít nhất 80% phiên viết thêm được ít nhất 1 test hợp lệ;
- không quá 25% phiên có WADR sau ≥ 0,95.

Ngưỡng 0,95 chỉ để chọn thời lượng; trong nghiên cứu chính mọi phiên hợp lệ đều được phân tích và tỉ lệ chạm trần báo riêng.

### 5.14 Ví dụ đầy đủ: p01137, từ bộ JUnit ban đầu đến mức tăng phát hiện WA

Ví dụ do nhóm nghiên cứu thực hiện, không phải dữ liệu sinh viên. Mục đích là chạy hết quy trình bằng công cụ thật; không dùng để so sánh hai loại phản hồi (một bài, một người viết test, người viết biết đề). Không đo thời gian. Tệp trong `pilot-results-2026-10-24/example_p01137/`.

1. **Bộ JUnit ban đầu** `SampleTest.java`: 1 test, 6 dataset của đề (1, 2, 4, 27, 300, 1250). WADR = 18/29 = 0,621.
2. **Báo cáo trên bộ ban đầu** (chương trình kiểm thử `s864796692`):
   - JaCoCo: 12/14 nhánh; còn nhánh chưa phủ ở dòng 15 và 24 (`1a_feedback_jacoco_before.md`).
   - PITest: 21/26 mutant bị diệt; SURVIVED ở dòng 15, 24, 29, 34; NO_COVERAGE ở dòng 40 (`System.exit`) (`1b_feedback_pitest_before.md`).
3. **Test bổ sung** (mỗi điều kiện 4 test; expected tính theo đề bằng cách duyệt mọi (y, z), không lấy từ chương trình):
   - Theo JaCoCo (`JacocoGuidedTest.java`), nhắm dòng 15 và 24: e = 63, 64, 999999, 1000000.
   - Theo PITest (`PitGuidedTest.java`), nhắm biên `<=` ở dòng 15, 24 và điều kiện `z >= 0` ở dòng 34: e = 8, 9, 16, 28.
4. **Kết quả** (JUnit 5 thật, mẫu số 29):

| Bộ test | Test hợp lệ | Đầu vào độc lập | WA phát hiện | WADR | ΔWADR | Chỉ số của công cụ sau khi bổ sung |
|---|---|---|---|---|---|---|
| Ban đầu (Sample) | 1/1 | 1 | 18/29 | 0,621 | — | JaCoCo 12/14; PITest 21/26 |
| Ban đầu + 4 test theo JaCoCo | 5/5 | 5 | 27/29 | 0,931 | +0,310 | JaCoCo vẫn 12/14 |
| Ban đầu + 4 test theo PITest | 5/5 | 5 | 19/29 | 0,655 | +0,034 | PITest 22/26 (diệt mutant dòng 34) |

Ví dụ cho thấy ba điều về quy trình, không phải về hai loại phản hồi:
- Quy trình chạy được từ đầu đến cuối với JUnit 5, JaCoCo và PITest thật; số đầu vào độc lập và test hợp lệ được ghi tự động.
- Chỉ số của công cụ và mức tăng phát hiện WA có thể đi ngược nhau: bộ theo JaCoCo không tăng coverage (4 test nhắm vào hai nhánh còn lại vẫn chưa phủ được chúng) nhưng tăng WADR 0,31; bộ theo PITest tăng mutation score nhưng WADR chỉ tăng 0,03. Đây là lý do đo bằng WA, không bằng chỉ số của công cụ.
- PUT của p01137 vi phạm điều kiện 1 (gọi System.exit), nên được thay theo §5.13.

### 5.15 Kế hoạch mini-pilot (trước nghiên cứu chính)

- **Người tham gia:** 4–6 sinh viên ngoài mẫu chính, có ký phiếu đồng ý; mỗi người làm 2 phiên (một JaCoCo, một PITest) trên 2 bài khác nhau theo lịch crossover.
- **Tài liệu phát:** project mẫu (PUT trong package `codenet`, `Judge.java`, bộ Sample), lệnh chạy JaCoCo hoặc PITest, báo cáo ban đầu, hướng dẫn viết test (đầu vào là hằng chuỗi hoặc ghép chuỗi; chỉ dùng `@Test` và `Assertions` của JUnit 5).
- **Thu:** file test sau phiên, thời điểm bắt đầu/kết thúc, phiếu hỏi ngắn (hướng dẫn có rõ không, báo cáo có dùng được không).
- **Kiểm tra:**
  - Hướng dẫn: tỉ lệ test bị loại và lý do (`method`, `parse`).
  - Thời gian: quy tắc ở §5.13.
  - Thu thập: `junit_eval.py` chấm được mọi bài nộp, không có trạng thái `HARNESS`.
  - Tỉ lệ chạm trần theo điều kiện.
- **Không** dùng mini-pilot để kết luận hai loại phản hồi khác nhau. Kết quả chỉ dùng để chốt bài, PUT, thời lượng và hướng dẫn; mọi điều chỉnh ghi kèm lý do trong proposal.
- Cỡ mẫu tính bằng mô phỏng (§5.17), không dùng số liệu Alonge (2025). Mini-pilot chỉ cho ước lượng thô của σ; nhóm báo dòng tương ứng của bảng mô phỏng, không dùng mini-pilot để đổi N.

### 5.16 Chọn bổ sung bài và danh sách 12 bài cuối cùng (2026-10-25)

Tập con mới `codenet_pilot_subset_45.zip` (seed 2026, `--n 45`): 15 bài đầu trùng đúng lần chọn trước; xét tiếp từ bài thứ 16 theo thứ tự. Mỗi bài được chạy đủ quy trình: pilot với Sample, viết validator ràng buộc đề và đầu vào tham chiếu (`validators.py`, `gen_extra.py`), xác định oracle, khoá manifest, rồi quét PUT theo năm điều kiện ở §5.13. Không đầu vào tham chiếu nào của 10 bài mới bị loại vì ngoài ràng buộc hay vì bài AC không đồng thuận.

| Thứ tự | Bài | WA đánh giá | Bộ Sample phát hiện | Kết quả quét PUT |
|---|---|---|---|---|
| 16 | p03253 | 116 | 46/116 (0,397) | **Đạt**: s490019423 (ứng viên thứ 2); JaCoCo 46/62, nhánh tập tham chiếu phủ được/chưa phủ được 1/15; PITest 79/91, sống sót 9 (diệt được 2) |
| 17 | p02729 | 71 | 60/71 (0,845) | Không đạt trong 30 ứng viên (phản hồi rỗng ở JaCoCo 23; mọi nhánh JaCoCo báo đều chưa phủ được bằng tập tham chiếu 3; phản hồi rỗng ở PITest 3; có System.exit 1) |
| 18 | p00003 | 288 | 163/288 (0,566) | **Đạt**: s021864564 (ứng viên thứ 1); JaCoCo 8/10, nhánh tập tham chiếu phủ được/chưa phủ được 2/0; PITest 9/11, sống sót 2 (diệt được 2) |
| 19 | p03712 | 46 | 43/46 (0,935) | Không đạt trong 30 ứng viên (phản hồi rỗng ở JaCoCo 27; mọi nhánh JaCoCo báo đều chưa phủ được bằng tập tham chiếu 1; phản hồi rỗng ở PITest 1; Judge.run lệch 1) |
| 20 | p00144 | 38 | 3/38 (0,079) | **Đạt**: s135751390 (ứng viên thứ 14); JaCoCo 27/72, nhánh tập tham chiếu phủ được/chưa phủ được 1/44; PITest 28/110, sống sót 11 (diệt được 1) |
| 21 | p02240 | 66 | 10/66 (0,152) | Không đạt trong 30 ứng viên (mọi nhánh JaCoCo báo đều chưa phủ được bằng tập tham chiếu 14; phản hồi rỗng ở JaCoCo 11; mọi mutant sống sót đều chưa diệt được bằng tập tham chiếu 5) |
| 22 | p02832 | 93 | 50/93 (0,538) | Không đạt trong 30 ứng viên (phản hồi rỗng ở JaCoCo 19; phản hồi rỗng ở PITest 6; mọi nhánh JaCoCo báo đều chưa phủ được bằng tập tham chiếu 3; Judge.run lệch 2) |
| 23 | p01125 | 71 | 34/71 (0,479) | **Đạt**: s918252364 (ứng viên thứ 3); JaCoCo 28/31, nhánh tập tham chiếu phủ được/chưa phủ được 1/2; PITest 23/30, sống sót 5 (diệt được 5) |
| 24 | p03274 | 321 | 72/321 (0,224) | **Đạt**: s722595737 (ứng viên thứ 14); JaCoCo 14/16, nhánh tập tham chiếu phủ được/chưa phủ được 2/0; PITest 21/27, sống sót 3 (diệt được 1) |
| 25 | p00013 | 53 | 16/53 (0,302) | Không đạt trong 30 ứng viên (phản hồi rỗng ở JaCoCo 23; phản hồi rỗng ở PITest 3; Judge.run lệch 2; mọi nhánh JaCoCo báo đều chưa phủ được bằng tập tham chiếu 2) |

Đến bài thứ 24 đã đủ 12 bài; bài thứ 25 cũng đã chạy và không đạt. Pilot với Sample đã chạy cho cả 30 bài mới (ví dụ bài thứ 36, p03795, bộ Sample phát hiện 100% WA nên sẽ bị loại), và một lượt sàng lọc nhanh (điều kiện 1–3) được dùng để biết trước bài nào cần viết validator; việc chọn bài chỉ dựa trên quy trình đầy đủ, theo đúng thứ tự.

**12 bài cuối cùng** (theo thứ tự chọn), khoá ngày 2026-10-25 trong `final12/frozen/frozen_index.json`:

| Thứ tự | Bài | WA đánh giá (mẫu số) | PUT | Nhánh phủ bởi bộ Sample | Nhánh chưa phủ: tập tham chiếu phủ được / chưa phủ được | Mutant bị diệt | Mutant sống sót (diệt được bằng tập tham chiếu) |
|---|---|---|---|---|---|---|---|
| 1 | p02263 | 92 | s781975706 | 12/14 | 1 / 1 | 18/24 | 2 (1) |
| 3 | p03378 | 48 | s045451427 | 5/6 | 1 / 0 | 7/10 | 3 (1) |
| 4 | p03416 | 81 | s526219859 | 6/8 | 2 / 0 | 19/25 | 6 (3) |
| 8 | p03681 | 128 | s735700476 | 7/8 | 1 / 0 | 16/18 | 2 (1) |
| 11 | p03196 | 92 | s773186766 | 9/78 | 1 / 68 | 18/146 | 4 (2) |
| 14 | p03351 | 221 | s945187436 | 5/6 | 1 / 0 | 7/10 | 3 (2) |
| 15 | p03633 | 143 | s203672004 | 5/6 | 1 / 0 | 11/14 | 2 (1) |
| 16 | p03253 | 116 | s490019423 | 46/62 | 1 / 15 | 79/91 | 9 (2) |
| 18 | p00003 | 288 | s021864564 | 8/10 | 2 / 0 | 9/11 | 2 (2) |
| 20 | p00144 | 38 | s135751390 | 27/72 | 1 / 44 | 28/110 | 11 (1) |
| 23 | p01125 | 71 | s918252364 | 28/31 | 1 / 2 | 23/30 | 5 (5) |
| 24 | p03274 | 321 | s722595737 | 14/16 | 2 / 0 | 21/27 | 3 (1) |

- Tổng mẫu số: 1.639 bài WA; tập đầu vào tham chiếu: 178 đầu vào.
- Lịch crossover theo 12 bài này: `final12/schedule_24.csv`; mỗi tổ hợp (bài, phiên, loại phản hồi) xuất hiện đúng 1 lần.
- **Báo cáo có nhiều mục chưa phủ/diệt được bằng tập tham chiếu** (số mục chưa phủ/diệt được lớn hơn số mục phủ/diệt được, trên bộ Sample): báo cáo JaCoCo của p03196 (68/1), p00144 (44/1), p03253 (15/1), p01125 (2/1); báo cáo PITest của p00144 (9/1), p03253 (5/2), p03378 (2/1), p03274 (2/1). Theo quyết định của nhóm, các báo cáo này được giữ nguyên; phân tích độ nhạy ở §6 của proposal áp dụng cho các bài này (bản trước chỉ ghi p03196).
- Trong 25 bài đã xét theo thứ tự, 12 bài đạt; lý do loại phổ biến nhất vẫn là JaCoCo báo 100% nhánh ngay với bộ Sample.

### 5.17 Kiểm chứng bộ chấm, đối chiếu AC và mô phỏng cỡ mẫu (2026-10-28)

**Kiểm chứng bộ chấm** (`verify_grader.py --out grader_check [--junit-api ...]`). Bài giả lập pFIX01: in giá trị lớn nhất và một chỉ số của nó (đề cho phép chỉ số nào cũng được khi trùng). Gồm 8 bài AC (5 đạt tiêu chí đối chiếu; 3 phải bị loại: cùng tác giả với PUT, gọi System.exit, sai trên đầu vào tham chiếu), 10 bài WA, 6 bộ JUnit. Kỳ vọng ghi trước trong script. Kết quả: 80/80 kiểm tra khớp, với cả JUnit 5.10.2 thật và bản thay thế.

| Bộ test | Tình huống | Kết quả kỳ vọng (đã khớp) |
|---|---|---|
| S1 assertion mạnh | Test đúng; một test gọi Judge.run hai lần | Bài WA ném ngoại lệ chỉ tính ở thước đo phụ; vòng lặp vô hạn (TIMEOUT) và System.exit không tính; bài có biến static chỉ sai từ lần gọi thứ hai không bị tính (mỗi lần gọi nạp lại Main, như chạy tiến trình); bài tính trong luồng riêng, bài không flush, bài có Main không public được chấm đúng |
| S2 assertion yếu | assertNotNull, kiểm output khác rỗng | Chỉ bắt được bài không in gì |
| S3 expected sai | Một test có expected sai | Test đó bị loại (FAIL trên PUT); không dùng để tính phát hiện |
| S4 assertThrows, ngoại lệ | assertThrows trên đầu vào rỗng và trên đầu vào hợp lệ; test có try/catch rồi fail(); test không bắt | Test assertThrows bị loại (ngoài ràng buộc, hoặc FAIL trên PUT); try/catch làm ngoại lệ thành fail do assertion (thước đo chính) |
| S5 flaky, rò trạng thái | Test lúc pass lúc fail trên PUT; test chỉ lúc pass lúc fail khi bài WA sai; test đọc biến static do test trước ghi | Test thứ nhất bị loại; bài WA tương ứng của test thứ hai là "không ổn định", không tính; test thứ ba bị loại vì phụ thuộc thứ tự |
| S6 bất đồng AC | Test chốt chỉ số đầu tiên khi trùng | Test bất đồng với bài AC in chỉ số cuối, bị tạm loại; bài WA chỉ khác ở điểm này không được tính ở phân tích chính, được tính ở phân tích độ nhạy giữ test bất đồng; file duyệt ghi "giu" thì được tính |

Thay đổi bộ chấm đi kèm: (i) `junit_eval.py` chạy riêng từng test trên PUT, loại test phụ thuộc thứ tự (lý do: khi bài WA làm JVM dừng, các test sau chạy trong JVM mới; test dựa vào trạng thái của test trước có thể fail mà không do bài WA); (ii) `HarnessRunner` nhận thêm chỉ số kết thúc; (iii) thư mục harness biên dịch theo mã băm của HarnessRunner và EvalJudge.

**Đối chiếu AC** (`pick_ac.py`, `junit_eval.py --ac-list --review`). Tiêu chí chọn 4 bài AC cho mỗi bài: khác tác giả với PUT và với nhau (user_id), không gọi System.exit, output giống PUT trên mọi đầu vào tham chiếu; duyệt theo thứ tự ngẫu nhiên seed 2026. Thêm điều kiện mỗi lần chạy không quá 4 giây (bằng giới hạn mỗi test khi chấm), để test không bị coi là bất đồng chỉ vì bài AC chậm. Cả 12 bài chọn đủ 4 (`final12/frozen/ac_check/`), SHA-256 từng danh sách ghi trong `frozen_index.json` (`ac_check_sha256`). Bị loại khi chọn: p01125 một bài gọi System.exit; p03274 bài Accepted s082152055 in 0 trên 2/17 đầu vào tham chiếu hợp lệ (vd. N = 1, K = 1, nến ở −100000000, đáp án 100000000), tức nhãn Accepted và đa số AC không bảo đảm tuyệt đối. Chạy lại bộ Sample của 12 bài với đối chiếu AC: 0 test bất đồng, 0 test phụ thuộc thứ tự, WADR không đổi.

**Mô phỏng cỡ mẫu** (`power_sim.py --out power_sim`, seed 2026, 2.000 lần lặp mỗi ô). Mô hình: ΔWADR phiên = μ + θ·[PITest] + π·[phiên 2] + u_sinh_viên + v_bài + e, bài và thứ tự theo lịch crossover. σ là SD của ΔWADR giữa sinh viên trên cùng bài, ρ là tương quan giữa hai phiên của cùng sinh viên, τ là SD hiệu ứng bài. Kiểm định: Wilcoxon signed-rank hai phía trên d, α = 0,05.

MDE (power 0,80), τ = 0,05, ô ghi N = 24 / N = 48:

| σ | ρ = 0 | ρ = 0,3 | ρ = 0,6 |
|---|---|---|---|
| 0,10 | 0,10 / 0,07 | 0,09 / 0,06 | 0,07 / 0,05 |
| 0,15 | 0,14 / 0,10 | 0,12 / 0,08 | 0,10 / 0,07 |
| 0,20 | 0,19 / 0,13 | 0,16 / 0,11 | 0,12 / 0,09 |
| 0,25 | 0,23 / 0,16 | 0,19 / 0,13 | 0,15 / 0,10 |

- Với 48 sinh viên, MDE ≤ 0,10 khi σ ≤ 0,15, hoặc σ = 0,20–0,25 và ρ = 0,6. Với 24 sinh viên, MDE ≤ 0,10 chỉ khi σ = 0,10 hoặc σ = 0,15 và ρ = 0,6.
- Hiệu ứng bài làm Wilcoxon bảo thủ (τ = 0,10: sai lầm loại I 0,002–0,037; MDE tăng 0–0,04 so với τ = 0). Hồi quy d theo hiệu ứng bài và thứ tự giữ power gần như không đổi khi τ tăng (σ = 0,20, ρ = 0,3: 0,47–0,50 ở N = 24; 0,82–0,84 ở N = 48); sai lầm loại I của hồi quy chưa được kiểm trong mô phỏng.
- Hiệu bằng 0 xử lý theo Pratt như phân tích chính (chốt 2026-10-29, `zero_method="pratt"`); chạy lại cho cùng bảng MDE, chỉ kịch bản chặn dưới thay đổi không quá 0,01.
- Khi chênh lệch thật bằng δ = 0,10, xác suất thoả cả quy tắc "p < 0,05 và ước lượng HL ≥ δ" khoảng 0,48–0,52 ở các ô có power ≥ 0,80.
- Kịch bản chặn dưới ở 0 (μ = 0,10): θ danh nghĩa 0,10 còn 0,077–0,084 sau khi chặn; power gần như kịch bản không chặn, P(quy tắc) giảm còn 0,20–0,29. Bảng đầy đủ: `power_sim/power_grid.csv`, `power_extra.csv`, `power_summary.md`.

## 6. Hồ sơ bằng chứng đã cập nhật

- **`Pham Nhat Thang/SLR/01`, `02`, `03`:** thêm 4 record W7-08 đến W7-11 (Clegg 2021, Perretta 2022, Mansur et al. 2026, Shin & Kazerouni 2024). Alonge (W7-01), Mansur 2025 (W7-03), T-P28 (W7-04), T-P29 (W7-05) đã có từ trước.
- **`search-log.md` §5, §8:** thêm truy vấn Q5–Q7 và kết quả sàng lọc.
- **`prisma-flow.md`:** nhánh bổ sung từ 7 lên 11 record. Không có record INCLUDE mới, nên `evidence-table`, `evidence-table-merged.md` và `prisma-team.md` giữ nguyên (N = 137).
- **2026-10-24, Hall & Baniassad (2022):** thêm record W7-12 vào `01`, `02`, `03`, `search-log.md` §8 (Q8, nguồn: email giảng viên) và `prisma-flow.md` (nhánh bổ sung 12 record). V2: EXCLUDE (EC-O: test viết bằng TypeScript), cùng quy tắc với Perretta 2022 (W7-09); N của bảng gộp không đổi. Bài này có trong danh mục tham khảo của T-P28, T-P29 và luận án Mansur 2025; lớp bổ sung không làm backward snowballing trên các bài đó nên đã bỏ sót, ghi trong `search-log.md`.

## 7. Phiên bản

- **Script:** thư mục `tools/gap1-pilot/`; SHA-256 từng file trong `pilot-results-2026-10-24/SHA256_scripts.txt`. `wa_pilot.py` đã sửa phần trích đầu vào JUnit (bỏ chú thích, text block); kết quả §5.1–5.8 không đổi vì lượt pilot ngày 2026-10-23 chỉ dùng file `.in`.
- **Công cụ:** JDK 21.0.12.1; JUnit Platform Console Standalone 1.10.2 (JUnit Jupiter 5.10.2); JaCoCo 0.8.12; PITest 1.16.1, pitest-entry 1.16.1, pitest-command-line 1.16.1, pitest-junit5-plugin 1.2.1; commons-text 1.10.0, commons-lang3 3.12.0 (PITest cần để ghi báo cáo). SHA-256 trong `pilot-results-2026-10-24/SHA256_tools.txt`.
- **2026-10-28:** thêm `pick_ac.py`, `verify_grader.py`, `power_sim.py`; sửa `junit_eval.py` (--ac-list, --review, kiểm tra phụ thuộc thứ tự, WADR_giu_bat_dong), `junit_shim/HarnessRunner.java` (chỉ số kết thúc), `validators.py` (luật cho bài giả lập pFIX01), `scan_put.py` (tên trường). Danh sách AC đối chiếu: `final12/frozen/ac_check/`. Kết quả kiểm chứng: `grader_check_junit/report.md`, `grader_check_shim/report.md`.
- **Dữ liệu:** tập con CodeNet `codenet_pilot_subset.zip` và `codenet_pilot_subset_45.zip` (seed 2026). Danh sách 12 bài cuối cùng, PUT, manifest WA và tập đầu vào tham chiếu khoá ngày 2026-10-25 trong `pilot-results-2026-10-25/frozen/frozen_index.json`; kết quả pilot và quét PUT của 10 bài mới trong `pilot-results-2026-10-25/`.
- **Commit:** PL commit toàn bộ thư mục này lên repo `RT-SWT301-004-nhom3` và điền mã commit vào đây: `[mã commit]`.
