# Phản hồi PITest: mutant sống sót (p03416)

Mutation score: **22/25** (88.0%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 10 | SURVIVED | changed conditional boundary | `boolean plusA = (A % 10000 / 1000) * 10 + (A / 10000) >= (A % 100);` |
| 11 | SURVIVED | Replaced integer multiplication with division | `boolean plusB = (B % 10000 / 1000) * 10 + (B / 10000) <= (B % 100);` |
| 11 | SURVIVED | changed conditional boundary | `boolean plusB = (B % 10000 / 1000) * 10 + (B / 10000) <= (B % 100);` |
