# ACM-098 — kiểm toán toàn văn

**Trạng thái:** BLOCKED — chưa đủ điều kiện đóng kiểm toán toàn văn.  
**Ngày kiểm tra:** 2026-10-21  
**Bản ghi:** ACM-098  
**Bài báo:** *Measuring and Mitigating Gaps in Structural Testing*  
**DOI:** https://doi.org/10.1109/ICSE48619.2023.00147

## 1. Nguồn và định danh

- PDF được cung cấp trong cuộc hội thoại: `MeasuringandMitigatingGapsinStructuralTesting(1).pdf`.
- SHA-256 của tệp đã kiểm tra: `76dc3d5cb954e1026c44b22a733c23a301d8a56748603e708087d93c311437d3`.
- PDF có 12 trang; metadata ghi ngày tạo 2023-01-20.
- Tiêu đề và bốn tác giả trong PDF khớp với hồ sơ xuất bản của tác giả và hồ sơ ICSE 2023: Soneya Binta Hossain, Matthew B. Dwyer, Sebastian Elbaum, Anh Nguyen-Tuong.
- Trang công bố của tác giả ghi bài thuộc ICSE 2023, DOI trên, và số trang kỷ yếu 1712–1723: https://soneyahossain.github.io/publications
- Hồ sơ ICSE 2023: https://conf.researchr.org/details/icse-2023/icse-2023-technical-track/131/Measuring-and-Mitigating-Gaps-in-Structural-Testing
- IEEE Xplore bản ghi xuất bản: https://ieeexplore.ieee.org/document/10172745

## 2. Xác định phiên bản — chưa đạt xác minh độc lập cuối cùng

PDF được cung cấp không thể được xác nhận là PDF cuối cùng của nhà xuất bản. Phần Data Availability ở PDF p. 11 ghi artifact nằm tại kho ẩn danh `icse2023anon/cc-gap-artifacts` và “will be made publicly available upon acceptance”. Đây là dấu hiệu rõ rằng tệp là bản thảo ẩn danh/trước khi chấp nhận, không phải bản xuất bản cuối cùng.

IEEE Xplore được xác định là bản ghi xuất bản chính thức, nhưng nội dung PDF trên IEEE Xplore không truy xuất/đọc được trong lần kiểm tra này. Do đó chưa thể xác nhận rằng mọi câu chữ, hình/bảng, tham chiếu và phân trang trong bản thảo trùng với bản nhà xuất bản.

## 3. Đối chiếu nội dung của PDF đã tải lên

| Hạng mục | Kết quả trong PDF | Vị trí PDF nội bộ | Trạng thái |
|---|---|---:|---|
| Định danh bài và tác giả | Tiêu đề và bốn tác giả khớp hồ sơ tác giả/ICSE | p. 1 | Đã đối chiếu metadata |
| Quy mô nghiên cứu | 13 ứng dụng Java, khoảng 16K test cases, 51.6K assertions; gap tối đa 51 điểm phần trăm, trung bình 34 điểm phần trăm | p. 1 | Khớp abstract |
| Thuật ngữ | Bài dùng “host coverage” và “checked host coverage (HCC)”; không nên ghi gộp thành “host checked coverage” | pp. 3–4 | Đã sửa cách ghi trong evidence table |
| RQ2 | Thay đổi tỷ lệ assertion được bật/tắt trong test suites hiện có và dùng PIT mutation testing để nghiên cứu quan hệ giữa gap và fault-detection effectiveness | pp. 7–9 | Đã sửa mô tả; không gọi đây là “generated test suites” |
| RQ4 | Đánh giá bổ sung assertion được đề xuất trong test suite của Joda-Time chronology package | pp. 9–10 | Khớp với PDF |
| Giới hạn công cụ | JavaSlicer không xử lý ổn định một số lớp Java lõi; có thể làm ước lượng coverage gap cao hơn | p. 10 | Có căn cứ trong PDF |
| Chi phí checked coverage | Tác giả nói chưa đánh giá chi phí; overhead trong thí nghiệm tăng khoảng một bậc độ lớn | p. 11 | Có căn cứ trong PDF |
| Môi trường VirtualBox | Không tìm thấy căn cứ cho tuyên bố rằng nghiên cứu phụ thuộc môi trường VirtualBox trong PDF này | — | Loại khỏi hạn chế trong evidence table |

## 4. Kiểm tra tham chiếu và số trang

- Danh mục tài liệu tham khảo trong bản PDF nằm trên các trang nội bộ 11–12.
- Các tham chiếu có liên quan trực tiếp đến mô tả phương pháp gồm [11] (PIT), [31] (Joda-Time), [40] và [41] (checked coverage). Nội dung bài viện dẫn các tài liệu này tại phần nền tảng/phương pháp và mô tả thí nghiệm.
- Số trang kỷ yếu chính thức được trang tác giả ghi là 1712–1723 (12 trang). PDF đã tải lên cũng có 12 trang nội bộ, nhưng chưa có bản PDF nhà xuất bản để xác nhận ánh xạ từng trang nội bộ sang số trang kỷ yếu. Không tự động cộng độ lệch trang hoặc ghi các số trang nội bộ như thể đã xác minh là số trang IEEE.
- Evidence table hiện ghi rõ trang nội bộ của PDF được kiểm tra và cảnh báo chưa xác minh ánh xạ sang phân trang nhà xuất bản.

## 5. Điều kiện để gỡ BLOCKED

1. Lấy bản PDF cuối cùng từ IEEE Xplore hoặc bản toàn văn chính thức do tác giả lưu trữ, có thể xác định chắc chắn là cùng phiên bản xuất bản.
2. So sánh nội dung theo từng trang: tiêu đề/tác giả, abstract, RQ2/RQ4, hình/bảng, phần hạn chế và danh mục tham khảo.
3. Xác minh phân trang 1712–1723 bằng chính bản PDF xuất bản.
4. Kiểm tra từng claim của ACM-098 trong evidence table với vị trí cụ thể của bản xuất bản.
5. Chỉ sau khi hoàn tất các bước trên mới chuyển trạng thái kiểm toán sang CLOSED.

**Kết luận:** Đã sửa các nội dung không được PDF hỗ trợ và các mô tả phương pháp chưa chính xác. Chưa xác minh độc lập bản PDF cuối cùng của nhà xuất bản; ACM-098 vẫn BLOCKED.
