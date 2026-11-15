> **Ghi chú 2026-10-29:** bộ kiểm tra này (Maven) là sản phẩm gate E3 của Tuần 7. Thực nghiệm hiện dùng `tools/gap1-pilot/` (chạy bằng dòng lệnh với các file .jar, không cần Maven).

# codenet-toolchain — kiểm tra bộ công cụ thực nghiệm (việc của LR, tuần 7)

Bản tương đương `test_api.py` cho RQ của nhóm. RQ không dùng API LLM, nên cần kiểm tra rằng với **một** submission CodeNet ta làm được 4 việc:

1. Đóng gói `Main.java` thành dự án Maven + JUnit 5 mà test gọi được (input qua stdin, so output).
2. Chạy **JaCoCo** → branch coverage + danh sách nhánh chưa phủ (= phản hồi của nhánh JaCoCo).
3. Chạy **PITest** → mutation score + danh sách mutant sống sót (= phản hồi của nhánh PITest).
4. Xuất số liệu ra `summary.json` (MS dùng tiếp cho `compute_metric.py`).

## Cần có
- JDK 17+ và Maven 3.8+ trong PATH; máy có mạng để Maven tải JUnit, JaCoCo, PITest ở lần chạy đầu.
- Python 3.9+.
- `problem_descriptions.tar.gz` trong repo CodeNet (`doc/`), để lấy Sample Input/Output làm test mẫu.
- Submission thật: file `sXXXXXXXXX.java` trong `Project_CodeNet_Java250/pXXXXX/`. Repo GitHub **không** chứa code mẫu; dữ liệu nằm trong `Project_CodeNet.tar.gz` (7.8 GB), phần DG tải về `data/raw/`.

## Các bước
```
python check_toolchain.py env
python check_toolchain.py new --submission demo/Main.java --problem p02546 --descriptions <repo CodeNet>/doc/problem_descriptions.tar.gz --out projects/p02546_demo
python check_toolchain.py run --project projects/p02546_demo
```
`demo/Main.java` là lời giải tự viết cho bài p02546, chỉ để thử công cụ khi chưa có dataset. Khi DG có dữ liệu, thay bằng submission thật:
```
python check_toolchain.py new --submission data/raw/Project_CodeNet_Java250/p02546/s123456789.java --problem p02546 --descriptions ... --out projects/p02546_s123456789
```

## Đạt khi (gate E2–E4)
- `env`: in `[OK]` cho java ≥ 17 và maven.
- `new`: in số test mẫu > 0 và **không có cảnh báo**.
- `run`: in `[OK] Maven chạy xong` và tạo trong `<project>/feedback/`:
  - `summary.json`: `branch_coverage`, `mutation_score`, `mutants_total`, …
  - `feedback_jacoco.md`: bảng nhánh chưa phủ theo dòng, kèm mã nguồn.
  - `feedback_pit.md`: bảng mutant sống sót theo dòng, kèm mã nguồn.
  - `maven.log`: log đầy đủ.

## Ghi vào proposal / notes
- Phiên bản công cụ (ghim trong `template/pom.xml`): JUnit 5.10.2 · JaCoCo 0.8.12 · PITest 1.16.1 + pitest-junit5-plugin 1.2.1 · mutator `DEFAULTS` · Java release 17.
- Mutation score = mutant bị phát hiện (KILLED, TIMED_OUT, MEMORY_ERROR, RUN_ERROR) / tổng mutant, đúng cách PIT tính. `test_strength` loại mutant NO_COVERAGE khỏi mẫu số.
- Hai file `feedback_*.md` có cùng một định dạng bảng cho cả hai nhánh, để phản hồi giữa hai điều kiện không thiên lệch (bài học từ P19: sinh viên thấy báo cáo PIT khó đọc).

## Tiêu chí loại submission khi chọn 12 chương trình (gửi DG)
`new` tự cảnh báo khi submission có:
- `System.exit(...)`: JUnit/PIT bị dừng giữa chừng.
- `static Scanner/BufferedReader ... = new ...(System.in)`: test thứ hai đọc phải stream cũ.
- Thread / ExecutorService: dễ timeout, flaky khi chạy PIT.
- Đọc file thay vì stdin.

Chỉ chọn submission **không có cảnh báo** và có ≥ 1 Sample Input/Output trong đề.
