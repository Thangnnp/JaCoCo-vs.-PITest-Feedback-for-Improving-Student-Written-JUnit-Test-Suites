# Phản hồi PITest: mutant sống sót (p01137)

Mutation score: **22/26** (84.6%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 15 | SURVIVED | changed conditional boundary | `if(Math.pow(z=(int)Math.cbrt(energy),3.0)<=energy&&z>1.0){` |
| 24 | SURVIVED | changed conditional boundary | `if(Math.pow(y=(int)Math.sqrt(energy),2.0)<=energy&&y>1.0){` |
| 29 | SURVIVED | changed conditional boundary | `if(barrier<maxb){` |
| 40 | NO_COVERAGE | removed call to java/lang/System::exit | `System.exit(0);` |
