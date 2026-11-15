# Kiểm chứng Câu hỏi Nghiên cứu và Xác thực Khoảng trống (RQ Validation)

- **Nhóm thực hiện:** Nhóm 3 (`RT-SWT301-004-nhom3`)
- **Đường dẫn lưu trữ đề xuất:** `team-synthesis/rq-validation.md`
- **Ngày cập nhật:** 22/10/2026; cập nhật theo RQ mới ngày 29/10/2026
- **Thành viên đóng góp dữ liệu:**
  1. **Trần Triều Tiên** — Nguồn IEEE Xplore ($41$ bài chính $+$ $2$ bài trong $12$ tháng qua) & Lớp tìm kiếm bổ sung **L2**
  2. **Phùng Thanh Nhân** — Nguồn gộp mã `N-P##` ($26$ bài sau khi loại `N-P27` không có toàn văn) & Phản chứng bổ sung
  3. **Phạm Nhật Thăng** — Nguồn OpenAlex $+$ Snowballing từ seed `DSpot` ($27$ bài) & Lớp bổ sung Tuần 7 (`T-P28`, `T-P29`, truy vấn `Q1`–`Q4`)
  4. **Ngô Minh Tiến** — Nguồn ACM Digital Library $+$ Snowballing ($48$ bản ghi) & Lớp tìm kiếm bổ sung **L3**

> **Thay đổi ngày 29/10/2026.** RQ đổi theo trao đổi với giảng viên (email ngày 22/10/2026, xem `team-synthesis/gap1.md`): thước đo kết quả (O) đổi từ mức tăng mutation score ($\Delta\text{MS}$) sang mức tăng tỉ lệ phát hiện các bài nộp Wrong Answer (WA) thật được giữ kín ($\Delta\text{WADR}$). RQ cũ: *"Khi sinh thêm kiểm thử JUnit cho $12$ chương trình Java thuộc IBM CodeNet, sinh viên dùng phản hồi độ bao phủ nhánh của JaCoCo và sinh viên dùng phản hồi mutant sống sót của PITest cải thiện mutation score ($\Delta\text{MS}$) khác nhau như thế nào so với bộ kiểm thử họ viết trước khi xem phản hồi?"*
> Các phần sửa: §1.1–§1.3 (RQ, PICO/S, câu gap ban đầu); cột O và mức giống ở §3.2–§3.3 (chấm lại theo O mới); mô tả G1, G4, G6 ở §4.1; §5.1, §5.2-A; cỡ mẫu ở §5.2-B; §6. Số liệu đếm của Bước 3–5 (mẫu số $N = 120$, số paper mỗi gap) giữ nguyên vì không phụ thuộc RQ. Chi tiết thiết kế hiện hành: proposal (bản _7) và `team-synthesis/gap1.md`.

---

## 1. Câu hỏi nghiên cứu (RQ) đã đăng ký và Câu Gap ban đầu (Việc 1)

### 1.1. Câu hỏi nghiên cứu (RQ) chính thức
> **RQ1:** *"Trong cùng ngân sách thời gian bổ sung kiểm thử, phản hồi nhánh chưa phủ của JaCoCo và phản hồi mutant sống sót của PITest tạo ra chênh lệch như thế nào về mức tăng tỉ lệ phát hiện các bài nộp Wrong Answer được giữ kín của cùng bài toán, so với bộ JUnit ban đầu?"*

### 1.2. Cấu trúc PICO/S chuẩn hóa của nhóm
| Thành phần | Định nghĩa nghiêm ngặt theo thiết kế đã đăng ký của nhóm |
| :--- | :--- |
| **P (Population / Context)** | Sinh viên ngành Công nghệ phần mềm (mục tiêu $n = 48$, tối thiểu $24$) viết và bổ sung kiểm thử JUnit 5 cho $12$ bài toán Java chọn ngẫu nhiên theo tiêu chí công khai từ **IBM CodeNet**; mỗi bài dùng một bài nộp Accepted làm chương trình kiểm thử (PUT); mỗi sinh viên làm hai bài khác nhau. |
| **I (Intervention)** | Hai quy trình phản hồi thủ công tách biệt: **(1)** Phản hồi độ bao phủ nhánh (Branch Coverage) từ **JaCoCo 0.8.12** và **(2)** Phản hồi danh sách đột biến sống sót (Surviving Mutants) từ **PITest 1.16.1**. |
| **C (Comparison)** | Đối chiếu mức cải thiện của hai điều kiện phản hồi (J: JaCoCo, P: PITest) trên **cùng người viết test**, lấy **bộ JUnit ban đầu (Before.java)** do chính sinh viên viết trong $15$ phút trước khi xem phản hồi làm mốc. |
| **O (Outcome)** | $\Delta\text{WADR} = \text{WADR(After)} - \text{WADR(Before)}$: mức tăng tỉ lệ bài nộp WA thật của cùng bài toán, giữ kín, bị chính bộ JUnit của sinh viên phát hiện (test hợp lệ fail do assertion). Mutation score và branch coverage chỉ là thước đo phụ. |
| **S (Study Design)** | Thực nghiệm có kiểm soát, thiết kế vắt chéo (**crossover**) trong cùng sinh viên, cân bằng thứ tự và bài toán, cùng ngân sách thời gian; kiểm định **Wilcoxon signed-rank** ghép cặp trên hiệu $d = \Delta\text{WADR}(P) - \Delta\text{WADR}(J)$, ước lượng Hodges–Lehmann và khoảng tin cậy 95%. |

### 1.3. Câu phát biểu Gap ban đầu (trước khi kiểm chứng phản chứng)
> *"Các nghiên cứu hiện tại chủ yếu dùng độ bao phủ (coverage) hoặc đột biến (mutation) làm tín hiệu tự động dẫn hướng công cụ/LLM sinh test, hoặc chỉ khảo sát một loại phản hồi đơn lẻ trong giáo dục, và đánh giá bằng chính mutation score hay coverage; chưa có nghiên cứu nào so sánh phản hồi nhánh chưa phủ của JaCoCo với phản hồi mutant sống sót của PITest khi sinh viên tự bổ sung kiểm thử JUnit, đo bằng mức tăng tỉ lệ phát hiện các bài nộp sai thật được giữ kín so với bộ JUnit ban đầu của chính họ."*

---

## 2. Thống kê tổng hợp dữ liệu từ 4 bảng cá nhân

Trước khi thực hiện Bước 2 đến Bước 7, nhóm tiến hành đồng bộ và khử trùng lặp giữa 4 bảng cá nhân:

| Thành viên | Nguồn phụ trách & Lớp bổ sung | Số dòng cá nhân | Các mã trùng lặp liên nguồn đã gộp | Số bài có trích xuất hạn chế (Verified/Extracted) |
| :--- | :--- | :---: | :--- | :---: |
| **Trần Triều Tiên** | IEEE Xplore $+$ Lớp L2 (`SE Education`) | $43$ | `R255` trùng `T-P14` & `ACM-087`; bài *Class Observability (ICSE 2025)* trùng `ACM-097` | $43 / 43$ |
| **Phùng Thanh Nhân** | Nguồn gộp `N-P##` $+$ Đối chiếu phản chứng | $26$ | Không trùng mã với 3 bảng còn lại (đã loại `N-P27` do thiếu full-text) | $19 / 26$ *(7 bài chưa có full-text/mục Limitations)* |
| **Phạm Nhật Thăng** | OpenAlex $+$ Snowballing `DSpot` $+$ Tuần 7 (`Q1`–`Q4`) | $29$ | `T-P01` $=$ `ACM-021`; `T-P10` $=$ `SB-ACM055-066`; `T-P14` $=$ `R255` $=$ `ACM-087`; `T-P21` $=$ `TEACHER-004`; `T-P23` $=$ `ACM-055`; `T-P26` $=$ `ACM-125` | $29 / 29$ |
| **Ngô Minh Tiến** | ACM Digital Library $+$ Snowballing $+$ Lớp L3 | $48$ | Chứa các bản ghi gốc trùng với bảng của Thăng và Tiên nêu trên | $36 / 48$ *(12 bài thiếu PDF hoặc text bị cắt cột)* |
| **Tổng toàn nhóm** | **4 nguồn chính $+$ 3 lớp tìm kiếm bổ sung** | **$146$ dòng** | **Khử $8$ lượt trùng lặp $\rightarrow$ Còn $138$ paper độc lập** | **$N = 120$ paper độc lập có nêu hạn chế** |

> **Ghi chú mẫu số $N = 120$:** Trong $138$ bài độc lập của toàn nhóm, sau khi trừ $7$ bài của Nhân (`N-P03`, `N-P06`, `N-P08`, `N-P15`, `N-P16`, `N-P34`, `N-P41`) và $11$ bài độc lập của Minh Tiến (`ACM-007`, `ACM-039`, `ACM-046`, `ACM-053`, `ACM-054`, `ACM-062`, `ACM-066`, `ACM-085`, `ACM-098`, `ACM-111`, `ACM-181`) chưa có mục *Limitations/Threats to Validity* nguyên văn từ PDF, toàn nhóm có chính xác **$N = 120$ paper độc lập** dùng làm mẫu số chung cho Bước 5. Các bài cùng nhóm tác giả trên cùng chuỗi thực nghiệm (như `ACM-055`/`T-P23` và `ACM-086` của Fraser et al., hoặc `ACM-152` và `ACM-156` của Ma et al.) được đếm gộp là **$1$** theo đúng quy tắc của giảng viên.

---

## 3. Phản chứng của nhóm và Phân loại RQ (Bước 2)

### 3.1. Bảng lấy mức giống cao nhất từ 4 bảng cá nhân

| Thành viên | Mức giống cao nhất trong bảng chính | Bài báo đạt mức giống cao nhất | Phản chứng tìm thấy ở Lớp bổ sung (trong & ngoài phễu SLR) | Kết luận cấp cá nhân |
| :--- | :---: | :--- | :--- | :--- |
| **Trần Triều Tiên** | **$1/4$** | `R264` (*Code Defenders*, 2024 — chỉ khớp P là đối tượng $37$ sinh viên) | Truy vấn L2 trên IEEE Xplore ($34$ kết quả) chủ yếu là Gamification và Auto-grading; không có bài nào so sánh 2 loại phản hồi thủ công trên sinh viên. | Không có phản chứng trong phạm vi IEEE Xplore. |
| **Phùng Thanh Nhân** | **$2/4$** | `N-P02`, `N-P03`, `N-P14`, `N-P20`, `N-P22`, `N-P41` (khớp P và O nhưng đều là công cụ/LLM tự động) | Ghi nhận $4$ phản chứng gần RQ ở mục 2: **Alonge (2025)**, **Mansur et al. (2024)**, **Earle & Bell (2026)**, **Perretta et al. (2025)**. | Trong 26 bài chính không có phản chứng; ngoài phễu có nghiên cứu gần RQ. |
| **Phạm Nhật Thăng** | **$4/4$ (chấm thô)** / **$3/4$ (chấm chặt)** | `T-P19` (*Scaffolding & Visualizations*, 2025 — $4/4$ thô); `T-P29` (*Curated Semantic Mutants*, 2026 — $3/4$) và $7$ bài công cụ/LLM đạt $3/4$ | Phát hiện phản chứng trực tiếp nhất ngoài SLR là **Alonge (2025)** ($3/4$: I, C, O); bổ sung vào SLR hai bài **T-P28 (Mansur et al., 2024)** ($2/4$) và **T-P29 (Earle & Bell, 2026)** ($3/4$). | **Có phản chứng**; RQ của nhóm là **Mở rộng (Extension)**. |
| **Ngô Minh Tiến** | **$2/4$ Có** *(chấm chặt)* | $22$ bài đạt $2/4$ Có (như `ACM-001`, `ACM-018`, `ACM-055`... do chấm chặt I và C phải gắn với sinh viên) | Lớp L3 phát hiện thêm **Shin & Kazerouni (2024)** ($12$ sinh viên dùng branch coverage & mutation feedback trên Python) và **Mansur et al. (2026)** (*Computer Science Education*). | **Có phản chứng**; phân loại RQ theo RBL-2 là **Mở rộng (Extension)**. |

### 3.2. Phân tích đối chiếu các phản chứng mạnh nhất của toàn nhóm

Bảng dưới đây đối chiếu chi tiết RQ của nhóm với **6 nghiên cứu gần nhất** (gồm các bài đạt điểm cao nhất trong SLR và các phản chứng từ lớp tìm kiếm bổ sung L2, L3, Tuần 7):

| Nghiên cứu phản chứng | Trạng thái trong SLR | P (Java / CodeNet / SV) | I (JaCoCo Branch vs. PIT Mutants) | C (Baseline cá nhân trước feedback) | O ($\Delta\text{WADR}$: bài nộp sai thật giữ kín) | Điểm khác biệt cốt lõi so với RQ đã đăng ký của nhóm |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Alonge (2025)** — *MS Thesis, Cal Poly* | **Ngoài SLR** (`EXCLUDE`: Luận văn chưa phản biện $+$ Python) | ✗ *(Python, $10$ SV)* | ✓ *(Branch vs. Mutation feedback)* | ✓ *(Có đo Pre-test / Post-test)* | ✗ *(Đo tỉ lệ mutant khái niệm bị bắt, lỗi do người thiết kế)* | **Gần RQ nhất ($2/4$: I, C)** nhưng dùng **Python (MutPy/Muttle)**, cỡ mẫu rất nhỏ ($n = 10$ chia $2$ nhóm độc lập $5/5$, không phải crossover trên cùng người) và **chỉ dùng thống kê mô tả**, không có kiểm định suy luận. |
| **2. `T-P19` Potter et al. (2025)** — *FSE Companion* | **Trong SLR** (`INCLUDE`) | ✓ *(SV, Java `Triangle` $52$ LOC)* | Một phần *(Chỉ có Mutation report)* | ✓ *(Bổ sung vào bộ test sẵn có)* | ✗ *(Đo Mutation score)* | Khớp $3/4$ khi chấm thô (P, I, C) nhưng **không có nhánh phản hồi Coverage để đối chiếu với nhánh Mutation**; chỉ so sánh cách trình bày báo cáo mutation giữa các khóa học khác nhau, không phân bổ ngẫu nhiên và không kiểm định thống kê. |
| **3. `T-P28` Mansur, Shaffer & Edwards (2024)** — *SIGCSE Virtual* | **Trong SLR** (`INCLUDE` — bổ sung Tuần 7) | Một phần *(SV Java, dự án dài 3–4 tuần)* | ✓ *(So Coverage với PIT trên Web-CAT)* | ✗ *(So giữa các học kỳ khác nhau)* | ✗ *(Đo Mutation coverage MuJava)* | Có so sánh phản hồi coverage và PITest cho sinh viên viết test Java ($1/4$ cộng P một phần), nhưng **so sánh giữa các học kỳ khác nhau**, đo bằng mutation coverage, không đo mức tăng phát hiện bài nộp sai thật từ bộ test baseline cá nhân trước phản hồi và bị nhiễu bởi chính sách chấm điểm (*grading policy*). |
| **4. `T-P29` Earle & Bell (2026)** — *SPLASH-E 2026* | **Trong SLR** (`INCLUDE` — bổ sung Tuần 7) | Một phần *(SV Java CS 3100, project môn học)* | Một phần *(Chỉ có gợi ý Mutant sống sót)* | ✓ *(So với lần nộp trước của cùng SV)* | ✗ *(Đo tỉ lệ diệt mutant)* | Khớp $2/4$ (I một phần, C) nhưng **chỉ có nhánh phản hồi mutation (không có nhánh JaCoCo branch coverage)**; việc sinh viên xin gợi ý là tự chọn (*self-selection*) nên tác giả khẳng định kết quả chỉ là liên hệ quan sát, không phải hiệu ứng nhân quả. |
| **5. Shin & Kazerouni (2024)** — *ACM TOCE* | **Ngoài SLR** (Phản chứng L3, Python) | ✗ *(Python, $12$ SV)* | ✓ *(Branch coverage & Mutation feedback)* | Không rõ *(Nghiên cứu quá trình)* | ✗ *(Mô hình định tính hành vi)* | Khảo sát $12$ sinh viên dùng phản hồi branch coverage và mutation nhưng trên **Python**, tập trung xây dựng mô hình định tính (qualitative model) về hành vi viết test chứ không đo mức tăng phát hiện bài nộp sai thật trong thiết kế crossover. |
| **6. Perretta et al. (2025)** — *SIGCSE TS 2025* | **Ngoài SLR** (`EXCLUDE`: Bài tập C++) | ✗ *(C++, $4.122$ SV)* | Một phần *(Chỉ có Instructor Hints cho mutant)* | ✗ *(So Fall 2023 vs. Spring 2024)* | ✗ *(Đo tỉ lệ diệt mutant)* | Quy mô lớn trên người học nhưng viết test bằng **C++ (`test.cpp`)**, chỉ xét gợi ý cho mutant chưa bị diệt mà không đối chiếu với phản hồi branch coverage trên cùng người học. |

### 3.3. Kết luận Bước 2: Phân loại RQ theo khung RBL-2
- **Mức giống cao nhất toàn nhóm (chấm lại theo O mới):** **$2/4$ theo tiêu chí chặt** (`Alonge 2025`: I, C; `T-P29`: I một phần, C) và **$3/4$ theo tiêu chí sàng lọc thô** (`T-P19`: P, I, C). Không nghiên cứu nào khớp O: tất cả đo bằng mutant (do công cụ sinh hoặc do người thiết kế) hoặc coverage, không đo bằng bài nộp sai thật được giữ kín.
- **Phân loại RQ:** **Mở rộng (Extension)** — không còn là *New* (vì đã có `Alonge 2025`, `T-P28`, `Shin & Kazerouni 2024` đặt vấn đề so sánh phản hồi coverage với phản hồi mutation cho sinh viên), nhưng cũng chưa phải là *Replication* vì chưa có bất kỳ công trình nào kết hợp đầy đủ thiết kế của nhóm: **đối chiếu JaCoCo Branch Coverage với PITest Surviving Mutants trên cùng sinh viên, cùng ngân sách thời gian, đo bằng $\Delta\text{WADR}$ trên bài nộp WA thật giữ kín so với bộ JUnit ban đầu**. Khác biệt với công trình gần nhất (Alonge 2025) nằm ở thước đo kết quả (O); nhãn tính mới là **Extension (GAP-M)**, khớp proposal.

---

## 4. Tổng hợp hạn chế, Gạch cái đã giải quyết, Đếm và Gắn loại Gap (Bước 3, 4, 5, 6)

### 4.1. Bảng gộp các nhóm hạn chế chính (Gap mạnh $\ge 3$ paper)

Thực hiện đúng Bước 3 (gộp các hạn chế cùng nghĩa từ 4 bảng cá nhân), Bước 4 (lọc theo cột tương ứng để gạch nếu đã có bài giải quyết đủ tin cậy và cùng bài toán), Bước 5 (đếm trên mẫu số $N = 120$ paper có nêu hạn chế, gộp bài cùng nhóm tác giả là $1$) và Bước 6 (gắn loại `GAP-M`, `GAP-D`, `GAP-T`):

| Mã | Nhóm hạn chế gộp từ 4 bảng cá nhân (Bước 3) | Danh sách paper nêu hạn chế này | Bước 4: Gạch cái đã giải quyết (Lọc theo cột Metric / Dataset / Tool) | Bước 5: Đếm ($x / 120$) & Độ mạnh | Bước 6: Loại Gap |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **G1** | **Thiếu thiết kế thực nghiệm kiểm soát chặt trên cùng người học để đo mức cải thiện từ baseline cá nhân giữa 2 loại phản hồi** (RQ cũ đo bằng $\Delta\text{MS}$; RQ mới đo bằng $\Delta\text{WADR}$): Chỉ xét 1 loại phản hồi đơn lẻ, hoặc so sánh giữa các khóa/học kỳ khác nhau gây nhiễu (*confounding* do chính sách chấm điểm), sinh viên tự chọn xem gợi ý (*self-selection bias*, chỉ là quan sát), không cân bằng thứ tự task (*no counterbalancing*), hoặc không kiểm định thống kê. | **Trong bảng chính ($8$ bài):** `R211`, `R264`; `T-P12`, `T-P17`, `T-P19`, `T-P20`, `T-P28`, `T-P29`.<br>*(Ngoài phễu bổ sung: `Alonge 2025`, `Perretta 2025`, `Shin & Kazerouni 2024`, `Ardic 2026`)*. | **Chưa giải quyết $\rightarrow$ GIỮ DÒNG:** Lọc cột **Metric / Thiết kế** — không có paper nào trong SLR đo mức cải thiện từ baseline cá nhân giữa hai nhánh JaCoCo và PITest tách biệt trên cùng người, dù bằng $\Delta\text{MS}$ hay bằng bài nộp sai thật. `Alonge (2025)` làm gần nhất nhưng trên Python, $10$ sinh viên chia $2$ nhóm độc lập và không có kiểm định thống kê (**"chưa đủ chắc"**). | **$8$ trên $120$ paper** *(11 nếu tính ngoài phễu)*<br>$\rightarrow$ **GAP MẠNH** ($\ge 3$ paper) | **GAP-M** *(Khía cạnh/chỉ số hiệu quả cải thiện chưa được đo đúng chuẩn)* |
| **G2** | **Cỡ mẫu người tham gia nhỏ hoặc bối cảnh thực nghiệm hẹp (1 lớp học, 1 trường, 1 công ty)**: Mẫu khảo sát/thực nghiệm trên con người nhỏ ($3$ đến $37$ người), đối tượng là sinh viên thiếu kinh nghiệm công nghiệp hoặc chỉ thu thập tại một cơ sở đào tạo/một công ty đơn lẻ, làm giảm sức mạnh thống kê và tính khái quát hóa. | **Trong bảng chính ($15$ cụm tác giả / $16$ bài):** `R102`, `R177`, `R210`, `R211`, `R264`; `N-P35`, `N-P38`; `T-P03`, `T-P12`, `T-P17`, `T-P19`, `T-P20`, `T-P21` (`TEACHER-004`), `T-P23` (`ACM-055` $+$ `ACM-086` cùng nhóm Fraser đếm là $1$), `T-P28`; `ACM-200`. | **Chưa đủ chắc $\rightarrow$ GIỮ DÒNG:** Lọc cột **Dataset / Đối tượng** — dù `T-P28` ($\sim 400$–$500$ SV/kỳ) và `T-P29` ($1.893$ bài nộp) có mẫu lớn nhưng là dữ liệu quan sát bài tập dài hạn bị nhiễu giữa các học kỳ; chưa giải quyết được bài toán thực nghiệm có kiểm soát (controlled crossover study). | **$15$ trên $120$ paper** *(đã gộp `ACM-055` & `ACM-086` là $1$)*<br>$\rightarrow$ **GAP MẠNH** ($\ge 3$ paper) | **GAP-D** *(Quy mô mẫu người học và bối cảnh dữ liệu thực nghiệm)* |
| **G3** | **Phạm vi bộ dữ liệu mã nguồn (Dataset / Benchmark) hạn chế**: Chỉ đánh giá trên số lượng ít các lớp/chương trình Java nhỏ, dự án đơn module, hoặc chỉ bó hẹp trong các benchmark cố định (`Defects4J`, `SF110`, `Classes2Test`, `HumanEval`), chưa kiểm chứng trên tập bài toán đa dạng hơn hoặc ngôn ngữ khác. | **Trong bảng chính ($52$ bài):**<br>- **Tiên ($26$):** `R033`, `R047`, `R057`, `R095`, `R098`, `R104`, `R132`, `R140`, `R155`, `R162`, `R165`, `R171`, `R176`, `R189`, `R191`, `R194`, `R207`, `R209`, `R210`, `R211`, `R217`, `R224`, `R234`, `R239`, `R294`, `AI-Powered (2025)`.<br>- **Nhân ($12$):** `N-P02`, `N-P10`, `N-P13`, `N-P14`, `N-P19`, `N-P20`, `N-P22`, `N-P23`, `N-P24`, `N-P30`, `N-P31`, `N-P32`.<br>- **Thăng ($7$):** `T-P01` (`ACM-021`), `T-P04`, `T-P07`, `T-P11`, `T-P15`, `T-P24`, `T-P27`.<br>- **M.Tiến ($7$):** `ACM-018`, `ACM-024`, `ACM-025`, `ACM-029`, `ACM-101`, `ACM-136`, `ACM-191`. | **Không gạch (Khác bài toán của RQ):** Lọc cột **Dataset** — các bài mở rộng lên hàng trăm class (`SF110`, `Defects4J`) đều là đánh giá **công cụ/LLM tự động**, khác bài toán sinh viên viết test của RQ (các bài trên người học như `T-P19`, `T-P03`, `T-P12` chỉ dùng $1$–$2$ class như `Triangle`, `Mars Rover`). Chưa bài nào đánh giá người học trên **$12$ bài IBM CodeNet**. | **$52$ trên $120$ paper**<br>$\rightarrow$ **GAP MẠNH** ($\ge 3$ paper) | **GAP-D** *(Domain hoặc quy mô bộ dữ liệu chương trình thử nghiệm)* |
| **G4** | **Chỉ đo Coverage hoặc dùng chỉ số đại diện (Proxy Metrics) chưa phản ánh đầy đủ khả năng phát hiện lỗi thực / chất lượng Assertion**: Nhiều nghiên cứu chỉ dùng line/branch coverage làm thước đo hoặc mục tiêu tối ưu mà bỏ qua độ mạnh của assertion / mutation score; hoặc chỉ xét tương quan mà không chứng minh được nhân quả. *(Cập nhật 29/10: đây là căn cứ trực tiếp của O mới — đo bằng bài nộp sai thật thay cho mutation score và coverage.)* | **Trong bảng chính ($13$ bài):** `R104`, `R209`, `ICSE-2025` (`ACM-097`); `N-P18`, `N-P32`; `T-P01`, `T-P06`, `T-P08`, `T-P18`; `ACM-001`, `ACM-087` (`T-P14`/`R255`), `ACM-235`, `ACM-236`. | **Đã giải quyết ở nhánh công cụ tự động, nhưng KHÔNG GẠCH vì khác bài toán RQ:** Lọc cột **Metric** — các bài như `T-P02`, `T-P10`, `T-P27` đã đo cả Mutation Score và Fault Detection cho công cụ tự động. Theo quy tắc của cô, nhóm **không gạch** mà giữ làm **tham khảo cách tính metric và nguồn ngưỡng**. | **$13$ trên $120$ paper**<br>$\rightarrow$ **GAP MẠNH** ($\ge 3$ paper) | **GAP-M** *(Khía cạnh chất lượng kiểm thử chưa được đo đầy đủ)* |
| **G5** | **Hạn chế của công cụ sinh test tự động & LLM (Lỗi biên dịch, Flaky/False Positive Assertions, Tính ngẫu nhiên, Data Leakage, Chi phí chạy lặp lại)**: Tỷ lệ cao test sinh tự động không biên dịch được ($15\%$–$66\%$), sinh oracle sai khi code gốc có bug, chịu phương sai do tính ngẫu nhiên (stochastic) nhưng chỉ chạy $1$–$6$ lần vì chi phí lớn, nguy cơ rò rỉ dữ liệu huấn luyện (data leakage). | **Trong bảng chính ($39$ cụm tác giả / $40$ bài):**<br>- **Tiên ($5$):** `R064`, `R155`, `R176`, `R255` (`T-P14`/`ACM-087`), `R264`.<br>- **Nhân ($11$):** `N-P09`, `N-P12`, `N-P13`, `N-P14`, `N-P17`, `N-P23`, `N-P24`, `N-P25`, `N-P30`, `N-P31`, `N-P32`.<br>- **Thăng ($10$):** `T-P02`, `T-P05`, `T-P08`, `T-P09`, `T-P10`, `T-P13`, `T-P16`, `T-P22`, `T-P25`, `T-P26` (`ACM-125`).<br>- **M.Tiến ($13$ cụm / $14$ bài):** `ACM-008`, `ACM-033`, `ACM-036`, `ACM-057`, `ACM-063`, `ACM-067`, `ACM-093`, `ACM-112`, `ACM-120`, `ACM-146`, `ACM-151`, `ACM-152` $+$ `ACM-156` (cùng nhóm Ma et al. đếm là $1$), `ACM-180`. | **Không gạch (Khác bài toán của RQ):** Đây là hạn chế của nhánh công cụ/LLM tự động. Với bài toán con người viết test của nhóm, hiện tượng $12\%$–$27\%$ bài nộp của sinh viên bị lỗi biên dịch (`T-P19`) và lỗi cấu hình classpath của PIT (`T-P26`) được nhóm dùng làm tham khảo để xây dựng script kiểm tra tự động `check_toolchain.py`. | **$39$ trên $120$ paper** *(đã gộp `ACM-152` & `ACM-156` là $1$)*<br>$\rightarrow$ **GAP MẠNH** ($\ge 3$ paper) | **GAP-T** *(Hạn chế kỹ thuật của công cụ/mô hình kiểm thử)* |
| **G6** | **Vấn đề Mutant tương đương (Equivalent Mutants), giới hạn của bộ toán tử đột biến mặc định (PIT/MuJava/EvoSuite) và chi phí chạy Mutation Analysis**: Không thể tự động phát hiện $100\%$ mutant tương đương, kết quả phụ thuộc vào tập toán tử mặc định hoặc lấy mẫu mutant, thời gian chạy mutation/dynamic slicing rất lớn trên dự án quy mô công nghiệp. | **Trong bảng chính ($27$ bài):**<br>- **Tiên ($25$):** `R016`, `R024`, `R033`, `R039`, `R048`, `R057`, `R073`, `R075`, `R084`, `R094`, `R095`, `R098`, `R112`, `R132`, `R162`, `R165`, `R171`, `R194`, `R207`, `R217`, `R234`, `R235`, `R239`, `R251`, `R294`.<br>- **M.Tiến ($2$):** `ACM-028`, `ACM-073`. | **Chưa giải quyết triệt để $\rightarrow$ GIỮ DÒNG:** Lọc cột **Tool / Metric** — phát hiện $100\%$ equivalent mutants là bài toán không thể quyết định (`R024`). Tuy nhiên, về thời gian chạy, `T-P02` chứng minh trên chương trình nhỏ $\sim 40$ LOC thì PITest chạy chỉ mất vài giây. Nhóm giữ dòng làm căn cứ không dùng mutation score làm thước đo chính. *(Cập nhật 29/10: nhóm không lọc mutant trong báo cáo; số mục mà tập đầu vào tham chiếu chưa phủ/diệt được được ghi lại và phân tích độ nhạy; chỉ gọi một mutant là tương đương khi có kiểm tra riêng.)* | **$27$ trên $120$ paper**<br>$\rightarrow$ **GAP MẠNH** ($\ge 3$ paper) | **GAP-T / GAP-M** *(Giới hạn của công cụ đột biến và độ chính xác của phép đo MS)* |

### 4.2. Các hạn chế nhỏ lẻ khác ($1$–$2$ paper $\rightarrow$ Gap yếu, chỉ ghi nhận để đầy đủ hồ sơ)
- **Độ phân giải thời gian đo năng lượng của công cụ JoularJX ($1\text{ ms}$):** Chỉ có $1 / 120$ paper nêu (`ACM-108`) $\rightarrow$ **Gap yếu**, khác bài toán RQ.
- **Yêu cầu viết truy vấn Boolean (`enabledness queries`) thủ công cho từng phương thức public:** Chỉ có $1 / 120$ paper nêu (`ACM-153`) $\rightarrow$ **Gap yếu**, khác bài toán RQ.

---

## 5. Đối chiếu với Câu Gap ban đầu và Viết Phát biểu Gap + RQ cho từng Gap mạnh (Bước 6 & Bước 7)

### 5.1. Đặt câu Gap RQ ban đầu cạnh Bảng Gap để đối chiếu (Bước 6)

| Câu Gap RQ ban đầu (Việc 1) | Đối chiếu với Bảng Gap (G1 $\rightarrow$ G6) và Phản chứng (Mục 3) | Quyết định về Gap của nhóm |
| :--- | :--- | :--- |
| *"Chưa có nghiên cứu nào so sánh phản hồi nhánh chưa phủ của JaCoCo với phản hồi mutant sống sót của PITest khi sinh viên tự bổ sung kiểm thử JUnit, đo bằng mức tăng tỉ lệ phát hiện các bài nộp sai thật được giữ kín so với bộ JUnit ban đầu của chính họ."* | - **Khớp trực tiếp với Gap mạnh `G1` (`GAP-M`, $8/120$ bài trong SLR $+$ $3$ bài ngoài phễu)** và giao thoa bối cảnh với **`G2`, `G3` (`GAP-D`, $15/120$ và $52/120$ bài)**.<br>- **Cần tinh chỉnh do có phản chứng:** Vì `Alonge (2025)` (Python, $n=10$), `T-P28` (Java, so giữa các học kỳ) và `Shin & Kazerouni (2024)` (Python, định tính) đã bước đầu so sánh phản hồi coverage và mutation cho sinh viên, nhóm **không giữ tuyên bố mới hoàn toàn (New)** mà thu hẹp về đúng **Gap mở rộng (`Extension` theo `GAP-M`)**. | 1. **Giữ trục chính của RQ đã đăng ký**, vì chưa có bài nào so sánh JaCoCo và PITest trên cùng người viết test trong thiết kế crossover có kiểm định thống kê, đo bằng bài nộp sai thật giữ kín ($\Delta\text{WADR}$).<br>2. **Tuân thủ nguyên tắc 1 phát biểu = 1 loại Gap:** Tách riêng phát biểu `GAP-M`, `GAP-D` và `GAP-T`, không trộn lẫn nhiều loại gap trong cùng một câu phát biểu. |

---

### 5.2. Phát biểu Gap hợp lệ và Câu hỏi nghiên cứu (RQ) cho từng Gap mạnh (Bước 7)

#### A. Gap mạnh 1 (`G1` & `G4`) — Loại `GAP-M` *(Gap và RQ chính thức của nhóm)*
- **Loại Gap:** `GAP-M` (Khía cạnh/chỉ số hiệu quả chưa được đo lường và kiểm định đúng chuẩn trên người học).
- **Tần suất xuất hiện:** **$8 / 120$ paper** trong bảng chính nêu hạn chế về thiết kế đo lường phản hồi trên người học (`R211`, `R264`, `T-P12`, `T-P17`, `T-P19`, `T-P20`, `T-P28`, `T-P29`) và **$13 / 120$ paper** nêu hạn chế về việc chỉ dùng chỉ số độ bao phủ/proxy metric (`G4`), cùng với $3$ phản chứng ngoài phễu (`Alonge 2025`, `Perretta 2025`, `Shin & Kazerouni 2024`).
- **Phát biểu Gap hợp lệ (chỉ tập trung vào `GAP-M`):**
  > *"Trong bài toán hỗ trợ sinh viên cải thiện bộ kiểm thử JUnit, các nghiên cứu hiện có (`T-P19`, `T-P28`, `T-P29`, Alonge 2025) đánh giá phản hồi bằng mutant (do công cụ sinh hoặc do người thiết kế) hay coverage, so giữa các học kỳ, giữa hai nhóm độc lập hoặc chỉ xét một nhánh phản hồi đột biến, chứ chưa đo trên cùng người học, trong cùng ngân sách thời gian, mức chênh lệch về khả năng phát hiện các bài nộp sai thật được giữ kín giữa phản hồi nhánh chưa phủ (JaCoCo) và phản hồi mutant sống sót (PITest), so với bộ JUnit ban đầu của chính sinh viên."*
- **Câu hỏi nghiên cứu tương ứng (RQ chính thức đã đăng ký):**
  > **RQ1 (`GAP-M`):** *"Trong cùng ngân sách thời gian bổ sung kiểm thử, phản hồi nhánh chưa phủ của JaCoCo và phản hồi mutant sống sót của PITest tạo ra chênh lệch như thế nào về mức tăng tỉ lệ phát hiện các bài nộp Wrong Answer được giữ kín của cùng bài toán, so với bộ JUnit ban đầu?"*

---

#### B. Gap mạnh 2 (`G2` & `G3`) — Loại `GAP-D` *(Gap về miền dữ liệu và quy mô mẫu thực nghiệm)*
- **Loại Gap:** `GAP-D` (Domain hoặc quy mô dữ liệu/cỡ mẫu thực nghiệm còn thiếu).
- **Tần suất xuất hiện:** **$52 / 120$ paper** nêu hạn chế về phạm vi bộ dữ liệu mã nguồn thử nghiệm (`G3`) và **$15 / 120$ paper** nêu hạn chế về cỡ mẫu người tham gia nhỏ hoặc bối cảnh đơn lẻ (`G2`).
- **Phát biểu Gap hợp lệ (chỉ tập trung vào `GAP-D`):**
  > *"Các nghiên cứu thực nghiệm có kiểm soát về việc người học sử dụng phản hồi kiểm thử (`T-P03`, `T-P12`, `T-P19`, `Alonge 2025`, `Shin & Kazerouni 2024`) mới chỉ đánh giá trên $1$ đến $2$ lớp mã nguồn đơn lẻ (như `Triangle`, `Mars Rover`) hoặc trên mẫu nhỏ $10$–$12$ sinh viên viết code Python, chưa được kiểm chứng trên miền dữ liệu các chương trình giải thuật Java độc lập có cấu trúc nhánh đa dạng thuộc bộ benchmark IBM CodeNet (Java250) với cỡ mẫu sinh viên lớn hơn (mục tiêu $n = 48$, tối thiểu $24$) để thực hiện kiểm định suy luận."*
- **Câu hỏi nghiên cứu tương ứng (RQ theo `GAP-D`):**
  > **RQ (`GAP-D`):** *"Trên tập $12$ chương trình Java có cấu trúc điều khiển đa dạng thuộc bộ dữ liệu IBM CodeNet (Java250) với mẫu $48$ (tối thiểu $24$) sinh viên Công nghệ phần mềm, hiệu quả cải thiện bộ kiểm thử JUnit sau khi nhận phản hồi công cụ biến thiên như thế nào giữa các bài toán có độ phức tạp nhánh khác nhau?"*

---

#### C. Gap mạnh 3 (`G5` & `G6`) — Loại `GAP-T` *(Gap về công cụ hỗ trợ, kiểm tra biên dịch và lọc đột biến tương đương)*
- **Loại Gap:** `GAP-T` (Công cụ/kỹ thuật kiểm thử còn hạn chế kỹ thuật hoặc gây rào cản khi áp dụng).
- **Tần suất xuất hiện:** **$39 / 120$ paper** nêu hạn chế về lỗi biên dịch và độ tin cậy của công cụ sinh test (`G5`) và **$27 / 120$ paper** nêu hạn chế về nhiễu do mutant tương đương (equivalent mutants) hoặc cấu hình công cụ đột biến (`G6`).
- **Phát biểu Gap hợp lệ (chỉ tập trung vào `GAP-T`):**
  > *"Khi áp dụng trực tiếp các công cụ phân tích đột biến và độ bao phủ chuẩn công nghiệp (PITest và JaCoCo) vào môi trường học tập (`T-P19`, `T-P26`, `R177`, `ACM-073`), người học thường gặp rào cản đọc hiểu báo cáo kỹ thuật, phát sinh $12\%$–$27\%$ bài nộp lỗi biên dịch và bị nhiễu bởi các mutant tương đương, nhưng chưa có quy trình thực nghiệm nào kết hợp đồng bộ tài liệu hướng dẫn đọc báo cáo (scaffolding), cổng kiểm tra biên dịch tự động và tiền sàng lọc mutant tương đương trước khi đo hiệu quả của sinh viên."*
- **Câu hỏi nghiên cứu tương ứng (RQ theo `GAP-T`):**
  > **RQ (`GAP-T`):** *"Khi kết hợp tài liệu hướng dẫn đọc báo cáo (scaffolding), kịch bản kiểm tra biên dịch tự động (`check_toolchain.py`) và bộ lọc mutant tương đương cho JaCoCo 0.8.12 và PITest 1.16.1, tỷ lệ bài nộp JUnit hợp lệ và độ chính xác khi đo lường khả năng tiêu diệt mutant của sinh viên được đảm bảo như thế nào?"*

---

## 6. Ghi chú bảo vệ tính khả thi của thực nghiệm (Tổng hợp từ 138 bài báo)

Từ quá trình rà soát toàn văn của cả 4 thành viên, nhóm tổng hợp các căn cứ thực tiễn để bảo vệ tính khả thi cho thiết kế thực nghiệm của nhóm:

1. **Cỡ mẫu người tham gia (mục tiêu $n = 48$, tối thiểu $24$ sinh viên):**
   - Trong các nghiên cứu thực nghiệm có kiểm soát (controlled human studies) đã khảo sát, cỡ mẫu thường dao động từ $10$ đến $49$ người: $10$ sinh viên (`Alonge 2025`), $12$ sinh viên (`T-P20`, `Shin & Kazerouni 2024`), $15$ học viên (`T-P17`), $24$ lập trình viên (`T-P03`), $37$ sinh viên (`R264`), $49$ sinh viên (`T-P12`).
   - Thiết kế **crossover trên cùng người** (mỗi sinh viên làm hai bài khác nhau, một bài với mỗi loại phản hồi) giảm phương sai cá nhân. Cỡ mẫu được tính lại bằng mô phỏng nhiều kịch bản (`power_sim.py`, proposal §6), không dùng độ lệch chuẩn của Alonge: với $48$ sinh viên, chênh lệch nhỏ nhất phát hiện được (power 0,80) là $0{,}05$–$0{,}16$ tuỳ độ biến thiên; với $24$ sinh viên là $0{,}07$–$0{,}23$, nên mẫu $24$ chỉ được trình bày là thăm dò.
2. **Bộ dữ liệu chương trình thử nghiệm ($12$ bài IBM CodeNet - Java250):**
   - Nhằm tránh **hiệu ứng trần (ceiling effect)** — như trong `Alonge (2025)` khi nhóm branch coverage đã đạt mutation score $0.958$ ngay từ bài pre-test — nhóm chọn ngẫu nhiên $12$ bài theo tiêu chí công khai và loại bài mà bộ test chỉ gồm các cặp Sample đã phát hiện 100% bài WA; với bộ Sample, WADR của 12 bài từ $0{,}079$ đến $0{,}742$, còn chỗ tăng để đo $\Delta\text{WADR}$. Thời lượng bổ sung T được chốt bằng mini-pilot.
3. **Hạ tầng công cụ (Toolchain) và Thời gian chạy:**
   - Bộ công cụ **JUnit 5 $+$ JaCoCo 0.8.12 $+$ PITest 1.16.1** là mã nguồn mở, miễn phí; chạy bằng dòng lệnh với cùng bộ file .jar trên mọi máy (không cần Maven).
   - Dù phân tích đột biến trên dự án lớn rất tốn thời gian (`R039`, `R239`), nhưng trên các chương trình giải thuật nhỏ độc lập ($\sim 40$ LOC như `T-P02` và `IBM CodeNet`), thời gian chạy PITest chỉ mất vài giây trên laptop cá nhân.
   - Tiêu chí chọn chương trình kiểm thử (`scan_put.py`) loại bài nộp gọi `System.exit` và chỉ nhận bài cho output đúng khi chạy qua `Judge.run`; bộ chấm (`junit_eval.py`) đã được kiểm chứng trên bài giả lập (80/80 kiểm tra), xử lý quá giờ, `System.exit` và chương trình chạy trong luồng riêng (các rủi ro đã được cảnh báo ở `T-P26` và `R084`).
4. **Chi phí thực hiện ($0\text{ USD}$):**
   - Nghiên cứu không phụ thuộc vào việc gọi API thương mại của các mô hình LLM trả phí (so với `T-P29` tốn $7.81\text{ USD}$ hay các bài multi-agent tốn hàng trăm USD tiền token), đảm bảo khả năng tái lập $100\%$ với chi phí bằng $0$.
5. **Kiểm soát rủi ro bài nộp lỗi và rào cản đọc báo cáo:**
   - Trước tình trạng $12\%$–$27\%$ bài nộp của sinh viên không biên dịch được (`T-P19`) và khó khăn khi đọc báo cáo đột biến (`R177`): bộ test ban đầu không biên dịch được vẫn được giữ trong phân tích (WADR(Before) = 0, ghi "không có báo cáo"); mọi sinh viên luyện tập 10 phút với cả JaCoCo và PITest trước phiên 1 và nhận cùng hướng dẫn cho hai điều kiện.
