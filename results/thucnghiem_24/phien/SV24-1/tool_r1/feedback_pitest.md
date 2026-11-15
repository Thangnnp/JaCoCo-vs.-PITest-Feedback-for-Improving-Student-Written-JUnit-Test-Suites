# Phản hồi PITest: mutant sống sót (p03253)

Mutation score: **78/91** (85.7%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 75 | SURVIVED | changed conditional boundary | `if (bufLength <= 0)` |
| 96 | SURVIVED | changed conditional boundary | `while (b >= '0' && b <= '9') {` |
| 96 | SURVIVED | changed conditional boundary | `while (b >= '0' && b <= '9') {` |
| 105 | NO_COVERAGE | removed negation | `return minus ? -n : n;` |
| 124 | SURVIVED | changed conditional boundary | `for (long i = 1; i <= n; i++)` |
| 141 | SURVIVED | changed conditional boundary | `if (n < 0 \|\| r < 0 \|\| n < r)` |
| 141 | SURVIVED | changed conditional boundary | `if (n < 0 \|\| r < 0 \|\| n < r)` |
| 141 | SURVIVED | changed conditional boundary | `if (n < 0 \|\| r < 0 \|\| n < r)` |
| 144 | NO_COVERAGE | replaced long return with 0 for codenet/Main$Combination::ncr | `return 1;` |
| 165 | NO_COVERAGE | Replaced integer addition with subtraction | `for (int j = i * i; j <= max; j += i) {` |
| 165 | SURVIVED | Replaced integer multiplication with division | `for (int j = i * i; j <= max; j += i) {` |
| 165 | SURVIVED | changed conditional boundary | `for (int j = i * i; j <= max; j += i) {` |
| 184 | SURVIVED | changed conditional boundary | `if (count > 0)` |
