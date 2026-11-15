# Bộ tiêu chí Chọn và Loại bài báo (Inclusion & Exclusion Criteria - IC/EC)

> **Dự án:** SLR - Mutation Testing vs. Code Coverage for Test Augmentation (IBM CodeNet / Java JUnit)

## 1. Tiêu chí Chọn vào (Inclusion Criteria - IC)

*   **IC-P (Problem / Dataset / Target):** Bài báo tập trung vào kiểm thử unit test cho ngôn ngữ Java / JUnit hoặc các dataset chuẩn hóa/quy mô tương đương (ví dụ: IBM CodeNet, HumanEval, Defects4J, SF110).
*   **IC-I (Intervention / Technology):** Bài báo trực tiếp nghiên cứu, áp dụng hoặc so sánh giữa Mutation Testing (PITest, mutant score) và Code Coverage (JaCoCo, line/branch/statement coverage) cho bài toán tăng cường/sinh bộ kiểm thử (Test Augmentation / Test Generation). Nêu rõ tên cụ thể của Tool/LLM (ví dụ: GPT-4o, LLaMA-3-70B, PITest, JaCoCo), không ghi chung chung "AI model" hay "testing tool".
*   **IC-O (Outcome / Metrics):** Bài báo có đo lường và báo cáo kết quả bằng các metric cụ thể (BLEU, F1, Cosine similarity, Mutation Score %, Coverage %, Compilation rate,...).
*   **IC-E (Empirical Evaluation):** Bài báo là nghiên cứu thực nghiệm (Empirical Study, Controlled Experiment, Benchmark Evaluation), có con số kết quả định lượng cụ thể trích xuất được từ Table/Figure của paper.
*   **IC-L (Language & Quality):** Bài báo được viết bằng tiếng Anh, đăng trên các hội thảo/tạp chí uy tín đã qua phản biện (Peer-reviewed) hoặc các kho lưu trữ uy tín (arXiv).
*   **IC-Y (Publication Year):** Bài báo xuất bản từ năm 2010 đến nay (đảm bảo tính cập nhật cho các công nghệ kiểm thử hiện đại).

---

## 2. Tiêu chí Loại ra (Exclusion Criteria - EC)

*   **EC-O (Out of Scope / Domain Mismatch):**
    *   Bài báo thuộc ngôn ngữ khác (C++, Python, Mobile, C#) không có tính tổng quát hóa cho Java/JUnit.
    *   Bài báo chỉ nói về AI code generation/LLM chung chung mà không áp dụng hay đo lường trực tiếp Mutation Testing hoặc Code Coverage.
*   **EC-N (No Empirical Data / Non-empirical):**
    *   Bài báo lý thuyết thuần túy, bài định hướng (vision paper, position paper, keynotes, literature review).
    *   Bài báo không có con số kết quả định lượng từ Table/Figure để điền vào Evidence Table (không chấp nhận bài chỉ nêu định tính).
*   **EC-S (Short Paper / Non-peer-reviewed):** Bài báo ngắn ($\le$ 4 trang), bài Poster, Extended Abstract, bài trình diễn công cụ (Tool demonstration paper).
*   **EC-A (Accessibility / Missing Content):** Bài báo bị rỗng Abstract, lỗi font không đọc được, hoặc không thể truy cập/tải được file PDF toàn văn (Full-text).
*   **EC-D (Duplicate):** Bài báo trùng lặp nội dung với một bài báo khác đã được thu thập từ nguồn khác (ưu tiên giữ bản hoàn chỉnh hoặc bản xuất bản chính thức trên Journal/Conference).

---

## Phân công nguồn tìm kiếm (Search Sources Allocation)

| Thành viên | Nguồn phụ trách | Ghi chú |
| :--- | :--- | :--- |
| **Trần Triều Tiên** | IEEE Xplore | |
| **Ngô Minh Tiến** | ACM Digital Library |  |
| **Phạm Nhật Thăng** | OpenAlex | Scopus |
| **Phùng Thanh Nhân** | Semantic Scholar | Google Scholar |
