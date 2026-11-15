# Search Log

| Date | Database | Query ID | Query | Raw Records | After Dedup | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-10-08 | IEEE Xplore & ACM | OA-V0-01 | `("unit testing" OR "unit test" OR JUnit OR Java OR "test augmentation" OR "test generation" OR "test improvement") AND ("mutation testing" OR mutant OR "code coverage" OR "branch coverage" OR "line coverage") AND ("mutation score")` | 260 | 258 | Raw search results |
| **2026-10-08** | **TỔNG CỘNG** | **V1 Retrieval** | **Tất cả các nguồn** | **260** | **258** | **Hoàn thành bỏ trùng (Dedup 2 bài)** |

---

### Pre-screening Check (Kiểm tra trước khi Screening)
*Thực hiện trên file `01_all_records.csv` gồm 260 records trước khi bỏ trùng:*
- **Số ô trống ở cột `doi`:** 15 (Đã được cập nhật đủ trong quá trình xử lý)
- **Số ô trống ở cột `abstract`:** 1 (Đã được cập nhật đủ)
- **Số ô trống ở cột `year`:** 0
- **Kết luận:** Dữ liệu hợp lệ để tiến hành vòng Screening 1.

---

### V1 Screening Results (Kết quả Lọc Vòng 1)
*Thực hiện trên 258 records sau khi bỏ trùng, áp dụng tiêu chí IC/EC cơ bản trên Title và Abstract:*
- **EXCLUDE:** 58 bài (Lý do chính: Thiếu sự can thiệp thủ công IC-I, sai ngôn ngữ EC-O, không có định lượng EC-N, hoặc ngoài mốc năm IC-Y).
- **INCLUDE:** 200 bài.
- **Quyết định:** 200 bài này được chuyển sang Vòng 2 (Tải file PDF và đọc toàn văn - Full-text Screening).

---

### V2 Screening Results (Kết quả Lọc Vòng 2 - Full-text)
*Thực hiện trên 200 records lọt qua Vòng 1, áp dụng nghiêm ngặt bộ tiêu chí IC/EC cho cả bài tìm kiếm và bài RQ Seed:*
- **EXCLUDE:** 153 bài (Lý do chính: Đa phần thiếu sự đối chiếu trực tiếp giữa Mutation Testing và Code Coverage hoặc quy trình sinh test 100% tự động mà không có can thiệp/phân tích thủ công của con người).
- **INCLUDE:** 47 bài.
- **Quyết định:** Chốt danh sách 47 bài xuất sắc nhất từ phễu tìm kiếm chính.

---

### Snowballing
**Lý do chọn seed 1:** Chọn bài **R226** (Straubinger 2024, *Improving Testing Behavior by Gamifying IntelliJ*) vì thỏa mãn tiêu chí A2b: Đã PASS vòng 2 (INCLUDE), độ sát RQ đạt tối đa 3/4 yếu tố trở lên (thực tế đạt 4/4 P/I/C/O), là bài Empirical Study mới xuất bản nên citation nằm trong khoảng an toàn cho phép (khoảng 10-200), và không bị trùng seed với thành viên khác.

**Lý do chọn seed 2 (Sheet 2):** Theo yêu cầu của Giảng viên về việc chọn thêm một bài phản chứng có độ sát RQ cao và có số lượng trích dẫn (Citation) đạt ngưỡng cao nhất, nhóm chọn bài **R206** (Fraser 2012, *Mutation-Driven Generation of Unit Tests and Oracles*). Bài này đạt 3/4 yếu tố RQ và có số lượng Citation cao thứ nhì toàn bảng (132 bài), thỏa mãn luật `< 200 citation` của Checklist.

**Ứng viên phản chứng (RBL-2):** Bài **R264** (Mezzaro et al., 2024) thu thập được từ hướng tiến có độ sát RQ đạt 4/4 (P/I/C/O) nên được đưa vào danh sách ứng viên phản chứng.

**Bảng thống kê Snowballing**

| DOI seed | Vòng | Hướng | Số đã lướt | Số thêm vào 01 | Số include cuối |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 10.48550/arxiv.2310.11171 (Seed 1) | 1 | lùi | 60 | 2 | 0 |
| 10.48550/arxiv.2310.11171 (Seed 1) | 1 | tiến | 8 | 4 | 1 |
| 10.1109/TSE.2011.93 (Seed 2) | 1 | lùi | 39 | 8 | 0 |
| 10.1109/TSE.2011.93 (Seed 2) | 1 | tiến | 132 | 45 | 3 |

*(Ghi chú Seed 2: Đã lướt 171 bài, lọc ra 61 bài tiềm năng, nhưng có 8 bài bị trùng lặp với phễu chính nên chỉ thực thêm 53 bài (8 lùi + 45 tiến) vào file 01_all_records. Qua V1 Screening nghiêm ngặt giữ lại 23 bài. Đọc Full-text V2 cho 17/23 bài (6 bài không tìm được PDF bị loại do EC-A) chốt được 3 bài "Số include cuối" hoàn toàn từ hướng tiến).*

**Tổng kết chung cuộc:** 47 (Phễu chính) + 1 (Snowballing S1) + 3 (Snowballing S2) = **51 bài Final Included.**


---

### V3: Rà nghiên cứu mạnh nhất gần đây (RBL-2 Tuần 7)  
*Thực hiện trên IEEE Xplore để tìm 2-3 paper mạnh nhất xuất bản trong 12 tháng gần nhất (2025-2026), nhằm đối chiếu tính mới (phản chứng RQ).*  

| Date | Database | Query ID | Query | Raw Records | Selected | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-10-19 | IEEE Xplore | V3-01 | `("mutation testing" OR "PITest") AND "JUnit" AND "coverage"` | 1 | 1 | Lọc năm 2025-2026. Trả về đúng 1 kết quả hợp lệ, tải được PDF. |
| 2026-10-19 | IEEE Xplore | V3-02 | `"mutation score" AND "Java" AND "testing"` | 2 | 1 | Lọc năm 2025-2026. Trả về 2 bài nhưng chỉ tải được PDF 1 bài (xuất bản tại ICSE). |

**Kết quả vớt bài mới nhất:**  
- Đã rà soát danh sách từ query V3-01 và V3-02 trên IEEE Xplore.  
- **Chốt chọn 2 bài báo mạnh nhất:**  
  1. *AI-Powered Unit Test Generation via Multi-LLM Chaining: A Case Study With GPT-4o, Gemini, and Claude-3.5* (IEEE Access, 2025).  
  2. *Increasing the Effectiveness of Automatically Generated Tests by Improving Class Observability* (ICSE, 2025).  
- **Lý do chọn:** Đây là 2 bài báo xuất bản mới nhất (2025) trên các tạp chí và hội nghị hạng A uy tín nhất của IEEE (Access, ICSE), phù hợp với tiêu chí "venue lớn, bài mạnh".  
- **Quyết định:** Đã đưa 2 bài báo này vào bảng đối chiếu P/I/C/O cá nhân (file `rq-check.md`) để phân tích gap và củng cố kết luận phản chứng RQ (xác nhận đề tài đạt tính mới).  
