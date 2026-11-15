# Phản hồi PITest: mutant sống sót (p03378)

Mutation score: **8/11** (72.7%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 17 | SURVIVED | changed conditional boundary | `for(int i=0;i<=x;i++) {` |
| 20 | SURVIVED | changed conditional boundary | `for(int i=x;i<n;i++) {` |
| 27 | NO_COVERAGE | replaced int return with 0 for codenet/Main::sample | `return n;` |
