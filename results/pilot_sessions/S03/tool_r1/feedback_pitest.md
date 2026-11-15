# Phản hồi PITest: mutant sống sót (p03986)

Mutation score: **10/18** (55.6%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 14 | SURVIVED | removed call to java/util/Scanner::close | `sc.close();` |
| 18 | SURVIVED | Replaced integer addition with subtraction | `while(p>0&&p+d<x.length()&&x.charAt(p-1)=='S'&&x.charAt(p+d)=='T') {` |
| 18 | SURVIVED | Replaced integer subtraction with addition | `while(p>0&&p+d<x.length()&&x.charAt(p-1)=='S'&&x.charAt(p+d)=='T') {` |
| 18 | SURVIVED | changed conditional boundary | `while(p>0&&p+d<x.length()&&x.charAt(p-1)=='S'&&x.charAt(p+d)=='T') {` |
| 18 | SURVIVED | negated conditional | `while(p>0&&p+d<x.length()&&x.charAt(p-1)=='S'&&x.charAt(p+d)=='T') {` |
| 18 | SURVIVED | negated conditional | `while(p>0&&p+d<x.length()&&x.charAt(p-1)=='S'&&x.charAt(p+d)=='T') {` |
| 23 | SURVIVED | Changed increment from -1 to 1 | `if(p!=0)p--;` |
| 23 | SURVIVED | negated conditional | `if(p!=0)p--;` |
