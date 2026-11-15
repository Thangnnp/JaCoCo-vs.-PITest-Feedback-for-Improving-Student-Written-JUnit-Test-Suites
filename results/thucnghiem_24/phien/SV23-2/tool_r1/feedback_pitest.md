# Phản hồi PITest: mutant sống sót (p01125)

Mutation score: **23/30** (76.7%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 22 | NO_COVERAGE | Changed increment from 1 to -1 | `if(map[x][y])ans++;` |
| 30 | SURVIVED | negated conditional | `if (map[x][y]) {` |
| 38 | SURVIVED | negated conditional | `for (int j = 0; j < mov; j++) {` |
| 41 | NO_COVERAGE | Changed increment from 1 to -1 | `ans++;` |
| 48 | SURVIVED | changed conditional boundary | `for (int j = 0; j < mov; j++) {` |
| 60 | SURVIVED | negated conditional | `if (map[x][y]) {` |
| 61 | SURVIVED | Changed increment from 1 to -1 | `ans++;` |
