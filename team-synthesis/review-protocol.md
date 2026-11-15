# Review Protocol
## Khóa quy tắc tìm kiếm RBL-1

---

## 1. Thông tin nền tảng

### 1.1. Câu hỏi nghiên cứu (RQ)

> **Khi sinh thêm kiểm thử JUnit cho 12 chương trình Java thuộc IBM CodeNet, sinh viên dùng phản hồi độ bao phủ nhánh của JaCoCo và sinh viên dùng phản hồi mutant sống sót của PITest cải thiện mutation score khác nhau như thế nào so với bộ kiểm thử họ viết trước khi xem phản hồi?**

### 1.2. Khung PICOS

| Thành phần | Nội dung |
|---|---|
| **P – Population** | Nhiệm vụ viết và cải thiện JUnit cho 12 submission Java được chấp nhận thuộc benchmark `Project_CodeNet_Java250` của IBM CodeNet. |
| **I – Intervention** | Hai quy trình thủ công: xem báo cáo nhánh chưa phủ của JaCoCo hoặc xem danh sách mutant sống sót của PITest trước khi bổ sung test. |
| **C – Comparison** | Bộ kiểm thử JUnit ban đầu do chính sinh viên viết trước khi xem bất kỳ báo cáo nào. |
| **O – Outcome** | Mức tăng mutation score PITest so với baseline cá nhân; ngưỡng tăng có ý nghĩa được chốt bằng mini-pilot. |
| **S – Study Design** | Thiết kế crossover có cân bằng thứ tự với 24 sinh viên, mỗi người thực hiện một lượt cho mỗi quy trình trên hai chương trình ghép cặp; so sánh mức tăng bằng Wilcoxon ghép cặp. |

---

## 2. Chiến lược tìm kiếm & Phân công

### 2.1. Phạm vi tìm kiếm

| Tiêu chí | Quy định |
|---|---|
| **Trường tìm kiếm** | Title, Abstract, Keyword |
| **Khoảng năm xuất bản** | 2019 – 2026 |
| **Search string gốc** | `("mutation testing" OR "PITest") AND ("code coverage" OR "JaCoCo") AND ("JUnit" OR "test augmentation")` |

### 2.2. Phân công nguồn (A0)

| Thành viên | Nguồn |
|---|---|
| **Trần Triều Tiên** | IEEE Xplore |
| **Ngô Minh Tiến** | ACM Digital Library |
| **Phạm Nhật Thăng** | OpenAlex / Scopus |
| **Phùng Thanh Nhân** | Semantic Scholar / Google Scholar |

---

## 3. Tiêu chí Sàng lọc (IC/EC)

Việc sàng lọc:

- **Vòng 1:** Title / Abstract
- **Vòng 2:** Full-text

sẽ tuân thủ nghiêm ngặt bộ tiêu chí Chọn/Loại đã được thống nhất tại:

`team-synthesis/ie_criteria.md`

---

## 4. Khung trích xuất dữ liệu (Evidence Table – A4)

Mọi bài báo đạt điều kiện (`v2_decision = INCLUDE`) **bắt buộc** phải được trích xuất vào:

`evidence-table-merged.md`

### Cấu trúc 7 cột

| # | Cột | Nội dung yêu cầu |
|---:|---|---|
| 1 | **Paper** | Tên bài báo + Năm + Venue + DOI |
| 2 | **Tool/LLM** | Tên cụ thể, ví dụ: JaCoCo, PITest |
| 3 | **Dataset** | Tên + số lượng + domain của dữ liệu thực nghiệm |
| 4 | **Metric** | Tên cụ thể, ví dụ: Mutation score %, Branch coverage |
| 5 | **Kết quả** | Con số chính xác từ Table/Figure của paper, hoặc `N/A` |
| 6 | **Code** | GitHub URL, hoặc `N/A` |
| 7 | **Hạn chế (GAP)** | Trích xuất từ mục *Threats to Validity*, hoặc `N/A` |

---

## 5. Quy chuẩn phân loại GAP

Các bài báo trong `evidence_table_merged.md` được gán nhãn theo **4 nhóm GAP** phục vụ cho Proposal:

| GAP | Tên | Định nghĩa |
|---|---|---|
| **GAP-T** | Technology Gap | Công nghệ/phương pháp chưa được thử nghiệm. |
| **GAP-M** | Metric Gap | Khía cạnh/chỉ số chưa được đo lường cụ thể. |
| **GAP-D** | Data Gap | Dữ liệu/quy mô thực nghiệm còn thiếu, ví dụ: thiếu đánh giá trên tập CodeNet. |
| **GAP-S** | Shared Limitation | Hạn chế chung mà **≥ 40% paper** được chọn cùng thừa nhận. |

---

## 6. Quy trình xử lý bất đồng & Đồng thuận

### 6.1. Đo lường đồng thuận

Áp dụng phương pháp **Double Screening** vào Ngày 5.

Độ đồng thuận gán nhãn giữa 2 người kiểm chéo được đo bằng:

> **Cohen's κ (kappa)**

### 6.2. Ngưỡng duyệt

> **Cohen's κ ≥ 0.7**

Chỉ khi đạt ngưỡng này, kết quả sàng lọc mới được duyệt đi tiếp.

### 6.3. Xử lý khi không đạt ngưỡng

Nếu:

`κ < 0.7`

thì hai thành viên phải:

1. Làm rõ lại bộ hướng dẫn IC/EC.
2. Thống nhất lại cách áp dụng tiêu chí.
3. Tiến hành gán nhãn lại từ đầu.

### 6.4. Phán quyết cuối cùng

Mọi bất đồng không thể tự giải quyết trong quá trình **lọc** và **trích xuất** sẽ do **Trưởng nhóm (PL)** quyết định cuối cùng.

---

## 7. Ghi log thay đổi

Mọi thay đổi phát sinh **sau khi khóa luật** đều phải được ghi lại vào:

`search-log.md`

Các thay đổi bao gồm nhưng không giới hạn:

- Đổi từ khóa.
- Thêm nguồn tìm kiếm.
- Thay đổi chiến lược tìm kiếm.
- Thay đổi quy tắc xử lý.

Mỗi thay đổi phải ghi rõ:

> **Lý do + Ngày tháng + Nội dung thay đổi**

> ⚠️ **Không được âm thầm sửa `Review Protocol` để ép khớp với kết quả tìm kiếm.**

---
