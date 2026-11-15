# Báo cáo mini-pilot (Tuần 8)

Đề tài FA26-W5-13, SWT301 nhóm 3. LR: Phạm Nhật Thăng. Thời gian: 01–05/11/2026.

## 1. Mục đích

Theo quy tắc mini-pilot của proposal (§4) và góp ý ngày 27/10 (mục 2), mini-pilot kiểm tra:

- quy trình phiên chạy được từ đầu đến cuối;
- người tham gia viết được bộ test ban đầu chạy được, hiểu báo cáo công cụ và bổ sung được test;
- ΔWADR đủ phân tán để so sánh, có hiện tượng chạm trần hay không;
- dữ liệu để chọn T (15, 20 hoặc 30 phút);
- tỉ lệ phiên không hợp lệ (INVALID) và thời gian chạy công cụ.

Mini-pilot không dùng để so sánh JaCoCo với PITest và không đưa vào phân tích xác nhận.

## 2. Người tham gia và bài toán

- 5 sinh viên, mã ẩn danh SV1–SV5. Trình độ: 1 fresher, 3 junior, 1 semi-senior (theo tỉ lệ dự kiến của nhóm cho thực nghiệm: 15% fresher, 65% junior, 20% semi-senior).

| SV  | Trình độ    |
| --- | ----------- |
| SV1 | semi-senior |
| SV2 | junior      |
| SV3 | junior      |
| SV4 | fresher     |
| SV5 | junior      |

- Bài pilot theo proposal: p03986 (PUT s263632960, 85 WA) và p02909 (PUT s470507275, 102 WA). Bài luyện tập: p02681.

## 3. Quy trình phiên

- Mỗi sinh viên làm 2 phiên trên 2 bài khác nhau, một phiên JaCoCo (J), một phiên PITest (P), thứ tự đảo giữa các sinh viên:

| Phiên | SV  | Thứ tự | Bài    | Công cụ |
| ----- | --- | ------ | ------ | ------- |
| S01   | SV1 | 1      | p03986 | J       |
| S02   | SV1 | 2      | p02909 | P       |
| S03   | SV2 | 1      | p03986 | P       |
| S04   | SV2 | 2      | p02909 | J       |
| S05   | SV3 | 1      | p02909 | J       |
| S06   | SV3 | 2      | p03986 | P       |
| S07   | SV4 | 1      | p02909 | P       |
| S08   | SV4 | 2      | p03986 | J       |
| S09   | SV5 | 1      | p03986 | J       |
| S10   | SV5 | 2      | p02909 | P       |

- Trình tự: luyện tập trên p02681 với cả hai công cụ (trước phiên 1); Bước 1 (15 phút) viết `Before.java`, chưa chạy công cụ; Bước 2–3: chạy công cụ được phân, đọc báo cáo, thêm hoặc sửa test, được chạy lại công cụ không giới hạn. Bộ test được lưu ở các mốc 15, 20 và 30 phút sau khi nộp Before để so sánh các giá trị T.
- Tài liệu phát: đề bài, `Main.java` (PUT), `Judge.java`, file test rỗng, lệnh chạy công cụ (Appendix A). Sinh viên được dùng IDE quen tay (NetBeans, VS Code hoặc IntelliJ), IDE có báo lỗi biên dịch, nhưng không được chạy thử trong IDE.
- Chấm: `junit_eval.py` (test hợp lệ phải pass trên PUT, đối chiếu 4 AC độc lập, chạy 2 lần trên mỗi bài WA, timeout 4 s mỗi test).
- Công cụ: JDK 21, JUnit 5.10.2, JaCoCo 0.8.12, PITest 1.16.1 + pitest-junit5-plugin 1.2.1.

## 4. Kết quả

| Phiên | Trình độ    | Bài    | ĐK  | Test hợp lệ Before | WADR Before | 15 phút | 20 phút | 30 phút | ΔWADR (T = 20) |
| ----- | ----------- | ------ | --- | ------------------ | ----------- | ------- | ------- | ------- | -------------- |
| S01   | semi-senior | p03986 | J   | 3/3                | 0,2353      | 0,2706  | 0,2706  | 0,3529  | 0,0353         |
| S02   | semi-senior | p02909 | P   | 3/3                | 1,000       | 1,000   | 1,000   | 1,000   | 0              |
| S03   | junior      | p03986 | P   | 3/3                | 0,2353      | 0,2471  | 0,2471  | 0,2471  | 0,0118         |
| S04   | junior      | p02909 | J   | 3/3                | 1,000       | 1,000   | 1,000   | 1,000   | 0              |
| S05   | junior      | p02909 | J   | 3/3                | 1,000       | 1,000   | 1,000   | 1,000   | 0              |
| S06   | junior      | p03986 | P   | 3/3                | 0,2353      | 0,2353  | 0,2353  | 0,2353  | 0              |
| S07   | fresher     | p02909 | P   | 3/3                | 1,000       | 1,000   | 1,000   | 1,000   | 0              |
| S08   | fresher     | p03986 | J   | 0/3                | 0           | –       | –       | –       | –              |
| S09   | junior      | p03986 | J   | 3/3                | 0,2353      | 0,1294  | 0       | 0       | −0,2353        |
| S10   | junior      | p02909 | P   | 0/1                | 0           | 0,7843  | 0       | 0       | 0              |

"–": After không biên dịch được (S08 khai báo `class After extends Before`, lệnh công cụ báo lỗi biên dịch ở mọi lần chạy và không được sửa).
S09, S10: dữ liệu được thu lại do lỗi hạ tầng ở lần đầu; ở lần thu lại, S10 vẫn có 1 vòng bị lỗi hạ tầng (vòng cuối, bộ test của vòng trước được giữ). Ở cả hai phiên, người tham gia thay các test đúng bằng test sai ở các vòng sau, nên WADR giảm.

## 5. Đánh giá theo các chỉ tiêu

| Chỉ tiêu                            | Kết quả                                                                                                                                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quy trình chạy được từ đầu đến cuối | Đạt: 10/10 phiên đi hết các bước; bộ chấm không có lỗi harness                                                                                                                                 |
| Phiên INVALID do lỗi hạ tầng        | 1/10 (S10, 1 vòng), dưới ngưỡng 20%                                                                                                                                                            |
| Thời gian chạy công cụ              | 3–9 s mỗi lần, JaCoCo và PITest tương đương trên 2 bài pilot                                                                                                                                   |
| Viết được bộ test ban đầu chạy được | 8/10 phiên có Before với ít nhất 2 test hợp lệ (thường là Sample của đề); 1 phiên fresher không có test hợp lệ                                                                                 |
| Lỗi biên dịch                       | Before: 0/10; After: 1/10 (S08)                                                                                                                                                                |
| Hiểu báo cáo và bổ sung test        | Rõ ở sinh viên semi-senior (số test hợp lệ tăng 3 → 5 → 7 ở các mốc 15, 20, 30 phút); junior thêm 0–1 test có ích, một junior (SV5) thay test đúng bằng test sai ở cả hai phiên; fresher không |
| ΔWADR đủ phân tán                   | Chưa: ở p03986, ΔWADR(T = 20) = 0,0353; 0,0118; 0; −0,2353 (S08 không tính được); ở p02909, ΔWADR(T = 20) = 0 ở cả 5 phiên                                                                     |
| Chạm trần                           | p02909 chạm trần ngay ở Before: 3 Sample của đề đạt WADR 1,000 (hoặc 0,902 khi thiếu một Sample); p03986 còn nhiều chỗ để tăng (đầu vào tham chiếu bắt 97,6% WA)                               |
| Chọn T                              | Chưa đủ căn cứ: 1 phiên (S01) tăng thêm ở mốc 30 phút, 2 phiên (S09, S10) giảm sau mốc 15 phút                                                                                                 |

## 6. Kết luận và đề xuất

1. Quy trình phiên, công cụ và bộ chấm đã sẵn sàng cho thực nghiệm.
2. p02909 không đo được ΔWADR vì chạm trần ngay ở bộ test ban đầu. Đề xuất xem xét thay bài pilot theo quy tắc bài dự phòng (cần amendment).
3. Ở p03986, mức cải thiện sau phản hồi nhỏ và phân tầng theo trình độ: chỉ sinh viên semi-senior cải thiện rõ.
4. Chưa đủ căn cứ để chọn T; giữ T = 20 phút làm giá trị tạm theo proposal. Dữ liệu duy nhất ủng hộ T dài hơn là S01 (tăng thêm ở mốc 30 phút).
5. Việc tiếp theo: bổ sung một phiên đối chiếu do thành viên nhóm làm trên p03986 (điều kiện P).
