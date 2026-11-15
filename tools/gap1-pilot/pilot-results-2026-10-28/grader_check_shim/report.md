# Kiểm chứng bộ chấm trên bài giả lập pFIX01

JUnit API: junit_shim. Kết quả: **80/80** kiểm tra khớp kỳ vọng.

## Bài WA giả lập

| Bài | Hành vi |
| --- | --- |
| w_neg | khởi tạo max = 0: sai khi mọi số âm |
| w_last | bỏ sót phần tử cuối (off-by-one) |
| w_throw1 | ném ArrayIndexOutOfBounds khi N = 1 |
| w_loop | lặp vô hạn khi hai số liền kề bằng nhau |
| w_exit | gọi System.exit(0) trước khi in khi N = 1 |
| w_static | biến static đếm số lần gọi main: đúng nếu mỗi lần chạy là một tiến trình mới |
| w_thread | tính trong luồng riêng, in chỉ số đánh từ 0 |
| w_noflush | logic đúng nhưng PrintWriter không flush: không in gì |
| w_nonpub | lớp Main không public, N chẵn thì in giá trị nhỏ nhất |
| w_tie | in chỉ số cuối khi trùng (đề cho phép) và đúng ở mọi chỗ khác |

## Kiểm tra

| Kiểm tra | Khớp | Chi tiết |
| --- | :-: | --- |
| pick_ac chọn đúng 4 bài AC độc lập | có | chọn ['s_ac_last', 's_ac_nonpub', 's_ac_stream', 's_ac_thread']; loại: s_ac_sameuser (trùng tác giả với PUT hoặc bài đã chọn); s_ac_exit (có System.exit) |
| S1_assertion_manh: test hợp lệ = ['t00_lienKeBang', 't01_moiSoAm', 't02_lonNhatOCuoi', 't03_motPhanTu', 't04_nChan', 't05_goiHaiLan'] | có | thực tế ['t00_lienKeBang', 't01_moiSoAm', 't02_lonNhatOCuoi', 't03_motPhanTu', 't04_nChan', 't05_goiHaiLan'] |
| S1_assertion_manh: test bị loại và lý do | có | {} |
| S1_assertion_manh: test bất đồng AC | có | [] |
| S1_assertion_manh / w_neg (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S1_assertion_manh / w_last (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S1_assertion_manh / w_throw1 (chính, phụ, giữ bất đồng) = KPK | có | thực tế KPK [phat_hien [ERROR]] |
| S1_assertion_manh / w_loop (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong [TIMEOUT]] |
| S1_assertion_manh / w_exit (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong [EXIT]] |
| S1_assertion_manh / w_static (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S1_assertion_manh / w_thread (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S1_assertion_manh / w_noflush (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S1_assertion_manh / w_nonpub (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S1_assertion_manh / w_tie (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu: test hợp lệ = ['y01', 'y02', 'y03'] | có | thực tế ['y01', 'y02', 'y03'] |
| S2_assertion_yeu: test bị loại và lý do | có | {} |
| S2_assertion_yeu: test bất đồng AC | có | [] |
| S2_assertion_yeu / w_neg (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu / w_last (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu / w_throw1 (chính, phụ, giữ bất đồng) = KPK | có | thực tế KPK [phat_hien [ERROR]] |
| S2_assertion_yeu / w_loop (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu / w_exit (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong [EXIT]] |
| S2_assertion_yeu / w_static (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu / w_thread (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu / w_noflush (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S2_assertion_yeu / w_nonpub (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S2_assertion_yeu / w_tie (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S3_expected_sai: test hợp lệ = ['e01_dung', 'e03_dung'] | có | thực tế ['e01_dung', 'e03_dung'] |
| S3_expected_sai: test bị loại và lý do | có | {"e02_sai": "FAIL trên PUT: java.lang.AssertionError: expected: <4 1> but was: <8 2>"} |
| S3_expected_sai: test bất đồng AC | có | [] |
| S3_expected_sai / w_neg (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S3_expected_sai / w_last (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S3_expected_sai / w_throw1 (chính, phụ, giữ bất đồng) = KPK | có | thực tế KPK [phat_hien [ERROR]] |
| S3_expected_sai / w_loop (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S3_expected_sai / w_exit (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong [EXIT]] |
| S3_expected_sai / w_static (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S3_expected_sai / w_thread (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S3_expected_sai / w_noflush (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S3_expected_sai / w_nonpub (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S3_expected_sai / w_tie (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S4_assertThrows_ngoai_le: test hợp lệ = ['x03_batNgoaiLe', 'x04_khongBat'] | có | thực tế ['x03_batNgoaiLe', 'x04_khongBat'] |
| S4_assertThrows_ngoai_le: test bị loại và lý do | có | {"x02_nemKhiHopLe": "FAIL trên PUT: java.lang.AssertionError: Expected java.lang.RuntimeException to be thrown, but nothing was thrown.", "x01_nemKhiRong": "dùng đầu vào ngoài ràng buộc của đề"} |
| S4_assertThrows_ngoai_le: test bất đồng AC | có | [] |
| S4_assertThrows_ngoai_le / w_neg (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S4_assertThrows_ngoai_le / w_last (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S4_assertThrows_ngoai_le / w_throw1 (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [ERROR,FAIL]] |
| S4_assertThrows_ngoai_le / w_loop (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S4_assertThrows_ngoai_le / w_exit (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong [EXIT]] |
| S4_assertThrows_ngoai_le / w_static (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S4_assertThrows_ngoai_le / w_thread (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S4_assertThrows_ngoai_le / w_noflush (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S4_assertThrows_ngoai_le / w_nonpub (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S4_assertThrows_ngoai_le / w_tie (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S5_flaky_ro_trang_thai: test hợp lệ = ['f02_flakyKhiSai', 'f03_ghiStatic'] | có | thực tế ['f02_flakyKhiSai', 'f03_ghiStatic'] |
| S5_flaky_ro_trang_thai: test bị loại và lý do | có | {"f01_flakyTrenPUT": "lúc pass lúc fail trên PUT", "f04_docStatic": "phụ thuộc thứ tự: FAIL khi chạy riêng trên PUT"} |
| S5_flaky_ro_trang_thai: test bất đồng AC | có | [] |
| S5_flaky_ro_trang_thai / w_neg (chính, phụ, giữ bất đồng) = UUU | có | thực tế UUU [khong_on_dinh] |
| S5_flaky_ro_trang_thai / w_last (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S5_flaky_ro_trang_thai / w_throw1 (chính, phụ, giữ bất đồng) = KPK | có | thực tế KPK [phat_hien [ERROR]] |
| S5_flaky_ro_trang_thai / w_loop (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S5_flaky_ro_trang_thai / w_exit (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong [EXIT]] |
| S5_flaky_ro_trang_thai / w_static (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S5_flaky_ro_trang_thai / w_thread (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S5_flaky_ro_trang_thai / w_noflush (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S5_flaky_ro_trang_thai / w_nonpub (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S5_flaky_ro_trang_thai / w_tie (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S6_bat_dong_AC: test hợp lệ = ['d02_binhThuong'] | có | thực tế ['d02_binhThuong'] |
| S6_bat_dong_AC: test bị loại và lý do | có | {} |
| S6_bat_dong_AC: test bất đồng AC | có | [{"test": "d01_trungChotChiSo", "ac_khong_pass": ["s_ac_last:FAIL"], "quyet_dinh": "chua_duyet"}] |
| S6_bat_dong_AC / w_neg (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S6_bat_dong_AC / w_last (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S6_bat_dong_AC / w_throw1 (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S6_bat_dong_AC / w_loop (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S6_bat_dong_AC / w_exit (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S6_bat_dong_AC / w_static (chính, phụ, giữ bất đồng) = KKK | có | thực tế KKK [khong] |
| S6_bat_dong_AC / w_thread (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S6_bat_dong_AC / w_noflush (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S6_bat_dong_AC / w_nonpub (chính, phụ, giữ bất đồng) = PPP | có | thực tế PPP [phat_hien [FAIL]] |
| S6_bat_dong_AC / w_tie (chính, phụ, giữ bất đồng) = KKP | có | thực tế KKP [khong] |
| S6 với file duyệt ghi 'giu' cho d01: w_tie được tính ở thước đo chính | có | phat_hien |
