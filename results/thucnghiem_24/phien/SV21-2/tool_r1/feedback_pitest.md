# Phản hồi PITest: mutant sống sót (p03274)

Mutation score: **21/27** (77.8%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 11 | SURVIVED | Replaced integer addition with subtraction | `int a = N+1;` |
| 15 | SURVIVED | changed conditional boundary | `if(l[i] >= 0 && !f){` |
| 22 | SURVIVED | changed conditional boundary | `if(a-1 >= K){` |
| 23 | NO_COVERAGE | Replaced integer subtraction with addition | `Mi = a-1;` |
| 24 | NO_COVERAGE | Replaced integer subtraction with addition | `mi = a-K;` |
| 32 | NO_COVERAGE | removed negation | `ans = Math.min(ans, -l[mi]);` |
