# gap1-pilot: pilot phép đo Wrong Answer cho GAP 1

Cần Python 3.9+, JDK 17+ (đã thử với JDK 21), và cho `crossover_design.py` thêm `numpy`, `scipy`.

Từ 2026-10-24: thư mục `lib/` (không nằm trong repo, tải từ Maven Central) gồm `junit-platform-console-standalone-1.10.2.jar`, `jacocoagent.jar`, `jacococli.jar` (JaCoCo 0.8.12), `pitest-1.16.1.jar`, `pitest-entry-1.16.1.jar`, `pitest-command-line-1.16.1.jar`, `pitest-junit5-plugin-1.2.1.jar`, `commons-text-1.10.0.jar`, `commons-lang3-3.12.0.jar`. SHA-256 trong `pilot-results-2026-10-24/SHA256_tools.txt`.
`Judge.java` là bản sao của `tools/codenet-toolchain/template/Judge.java`; hai bản phải giống nhau.

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1. Chọn bài, trích dữ liệu (máy có CodeNet) | `python codenet_subset.py --codenet Project_CodeNet.tar.gz --out codenet_pilot_subset.zip` | `candidates.csv`, `selected.csv`, mã AC/WA của 15 bài |
| 2. Đo WA | giải nén zip vào `subset/`, rồi `python wa_pilot.py --subset subset --out results [--extra tests]` | `results/pXXXXX_report.json`, `pXXXXX_heldout_manifest.csv`, `pXXXXX_wa_runs.csv`, `summary.json` |
| 2b. Đầu vào kiểm tra độ nhạy (do nhóm nghiên cứu viết, không phải dữ liệu sinh viên) | `python gen_extra.py --out extra --seed 2026`, rồi chạy bước 2 với `--extra extra` | `extra/pXXXXX/*.in` |
| 3. Bảng tổng hợp | `python report.py results/summary.json` | Bảng Markdown dùng trong `team-synthesis/gap1-phan-hoi.md` §5 |
| 3b. Độ nhạy, hiệu ứng trần | `python headroom.py results --ks 1 3 5` | Tỉ lệ phát hiện khi thêm k đầu vào bổ sung |
| 4. Lịch crossover | `python crossover_design.py schedule --students 24 --programs <12 mã bài>` | `schedule.csv` |
| 5. Cỡ mẫu | `python power_sim.py --out power_sim` (từ 2026-10-28; `crossover_design.py power` chỉ để đối chiếu bản cũ) | `power_grid.csv`, `power_extra.csv`, `power_summary.md`, `assumptions.json` |

`--extra tests` trỏ tới thư mục `tests/pXXXXX/` chứa file `.in` (mỗi file một đầu vào) hoặc file JUnit `.java`. Với file JUnit, script lấy đối số chuỗi của `Judge.run(...)`. Trong thực nghiệm, đây là bộ test trước và sau phản hồi của từng sinh viên.

Các tham số mặc định:
- seed 2026;
- 20 bài AC dùng để xác định oracle;
- ngưỡng đồng thuận 90%, tối thiểu 5 bài AC;
- timeout 4 giây mỗi lần chạy.

`validators.py` kiểm tra đầu vào theo ràng buộc của đề cho 13 bài (12 chính, 1 dự phòng). `wa_pilot.py` loại đầu vào ngoài ràng buộc trước khi xác định oracle và ghi số đã loại vào `dau_vao.ngoai_rang_buoc`. Khi thay bài, phải viết validator cho bài mới trước khi chạy.

Kết quả pilot ngày 2026-10-23 nằm trong `pilot-results/`: report, manifest và wa_runs của 13 bài, `summary.json`, `report.md`, `headroom.md`.

## Từ 2026-10-24: chấm bằng chính bộ JUnit

| Bước | Lệnh | Kết quả |
|---|---|---|
| Khoá dữ liệu | `python freeze.py --subset subset --results results --extra extra --out frozen --problems <mã bài>` | `frozen/frozen_index.json` (SHA-256 manifest WA, tập đầu vào tham chiếu) |
| Bộ baseline | `python make_sample_suite.py --subset subset --pid pXXXXX --out SampleTest.java` | Bộ JUnit gồm các cặp Sample |
| Chọn PUT | `python scan_put.py --subset subset --frozen frozen --lib lib --pid pXXXXX --baseline SampleTest.java --out scan` | PUT đạt 5 điều kiện (§5.13) |
| Phản hồi cho sinh viên | `python feedback.py --tool jacoco|pitest --lib lib --subset subset --pid pXXXXX --put sXXXXXXXXX --test <file test> --out fb` | `feedback_jacoco.md` / `feedback_pitest.md` + HTML |
| Chấm một phiên | `python junit_eval.py --subset subset --pid pXXXXX --put sXXXXXXXXX --manifest frozen/pXXXXX_heldout_manifest.csv --suite before=<file> --suite after=<file> --junit-api lib/junit-platform-console-standalone-1.10.2.jar --out session` | `summary.json` (WADR trước/sau, test hợp lệ, lý do loại), `per_wa.csv` |

`EvalJudge.java` là `Judge` dùng khi chấm (nạp lại `Main` mỗi lần gọi, chờ luồng, không flush hộ). `junit_shim/` gồm `HarnessRunner.java` (chạy các `@Test`) và bản thay thế tối giản của JUnit 5 API chỉ để chạy thử khi không có `--junit-api`; kết quả chính thức dùng JUnit 5 thật. `wa_pilot.py` từ nay chỉ dùng cho bước chuẩn bị (oracle, tập tham chiếu, manifest), không dùng để chấm phiên.

## Từ 2026-10-28: kiểm chứng bộ chấm, đối chiếu AC, mô phỏng cỡ mẫu

| Bước | Lệnh | Kết quả |
|---|---|---|
| Kiểm chứng bộ chấm (trước khi tuyển mẫu chính; chạy lại sau mỗi lần sửa bộ chấm) | `python verify_grader.py --out grader_check --junit-api lib/junit-platform-console-standalone-1.10.2.jar` | `grader_check/report.md`, `report.json`; mã thoát 1 nếu có kiểm tra lệch kỳ vọng |
| Chọn 4 bài AC đối chiếu | `python pick_ac.py --subset subset --frozen frozen --pid pXXXXX --k 4 --out frozen/ac_check/pXXXXX.json` | Danh sách AC khác tác giả, kèm nhật ký lý do loại |
| Chấm phiên có đối chiếu AC | thêm `--ac-list frozen/ac_check/pXXXXX.json [--review review.csv]` vào lệnh `junit_eval.py` | `test_bat_dong_AC`, `WADR_giu_bat_dong` (phân tích độ nhạy) trong `summary.json`; cột `giu_bat_dong` trong `per_wa.csv` |
| Cỡ mẫu | `python power_sim.py --out power_sim` | Bảng power/MDE theo σ, ρ, τ, N |

`review.csv` có các cột `suite_sha256,test,quyet_dinh,nguoi_duyet_1,nguoi_duyet_2,nguoi_quyet`; `quyet_dinh` là `giu` hoặc `loai`. Test bất đồng AC không có dòng trong file này bị loại khỏi phân tích chính. `junit_eval.py` còn chạy riêng từng test trên PUT và loại test phụ thuộc thứ tự. Kết quả ngày 2026-10-28 nằm trong `pilot-results-2026-10-28/`.

## Từ 2026-11-03: tính metric (gate E4)

| Bước | Lệnh | Kết quả |
|---|---|---|
| Kiểm tra script trên dữ liệu giả và các ca tính tay | `python compute_metric.py --self-test` | 16 ca, mã thoát 1 nếu có ca sai |
| Tính metric từ kết quả chấm | `python compute_metric.py --sessions results/pilot_sessions --sample data/lich_phien_minipilot.csv --T after_T20 [--after-loi bo\|bang_0] --out <file>.json` | WADR, ΔWADR theo phiên; d theo sinh viên; θ̂ (Hodges–Lehmann); Wilcoxon (Pratt); kết luận theo quy tắc p < 0,05 và \|θ̂\| ≥ δ |

`compute_metric.py` chọn phương pháp Wilcoxon tường minh (chính xác khi n ≤ 50 và không có hiệu bằng 0 hay hạng trùng, ngược lại xấp xỉ chuẩn), vì từ SciPy 1.13 tuỳ chọn `method="auto"` xử lý hiệu bằng 0 khác các bản cũ.

