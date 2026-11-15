# Phản hồi PITest: mutant sống sót (p03196)

Mutation score: **18/146** (12.3%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 32 | NO_COVERAGE | removed call to java/io/PrintStream::println | `System.err.println(Arrays.deepToString(os));` |
| 38 | NO_COVERAGE | Replaced Shift Left with Shift Right | `for (int i = 0; i < (1 << n); i++) {` |
| 38 | NO_COVERAGE | changed conditional boundary | `for (int i = 0; i < (1 << n); i++) {` |
| 38 | NO_COVERAGE | negated conditional | `for (int i = 0; i < (1 << n); i++) {` |
| 40 | NO_COVERAGE | changed conditional boundary | `for (int j = 0; j < n; j++) {` |
| 40 | NO_COVERAGE | negated conditional | `for (int j = 0; j < n; j++) {` |
| 41 | NO_COVERAGE | Replaced Shift Right with Shift Left | `boolean isJthBitSet = ((i >> j) & 1) == 1;` |
| 41 | NO_COVERAGE | Replaced bitwise AND with OR | `boolean isJthBitSet = ((i >> j) & 1) == 1;` |
| 41 | NO_COVERAGE | negated conditional | `boolean isJthBitSet = ((i >> j) & 1) == 1;` |
| 44 | NO_COVERAGE | removed call to java/util/function/Consumer::accept | `func.accept(arg);` |
| 67 | NO_COVERAGE | negated conditional | `if (f.compareTo(p.f) != 0) {` |
| 68 | NO_COVERAGE | replaced int return with 0 for codenet/Main$Pair::compareTo | `return f.compareTo(p.f);` |
| 70 | NO_COVERAGE | replaced int return with 0 for codenet/Main$Pair::compareTo | `return s.compareTo(p.s);` |
| 75 | NO_COVERAGE | Replaced XOR with AND | `return f.hashCode() ^ s.hashCode();` |
| 75 | NO_COVERAGE | replaced int return with 0 for codenet/Main$Pair::hashCode | `return f.hashCode() ^ s.hashCode();` |
| 80 | NO_COVERAGE | negated conditional | `if (this == o) {` |
| 81 | NO_COVERAGE | replaced boolean return with false for codenet/Main$Pair::equals | `return true;` |
| 83 | NO_COVERAGE | negated conditional | `if (o == null \|\| this.f == null \|\| this.s == null) {` |
| 83 | NO_COVERAGE | negated conditional | `if (o == null \|\| this.f == null \|\| this.s == null) {` |
| 83 | NO_COVERAGE | negated conditional | `if (o == null \|\| this.f == null \|\| this.s == null) {` |
| 84 | NO_COVERAGE | replaced boolean return with true for codenet/Main$Pair::equals | `return false;` |
| 86 | NO_COVERAGE | negated conditional | `if (this.getClass() != o.getClass()) {` |
| 87 | NO_COVERAGE | replaced boolean return with true for codenet/Main$Pair::equals | `return false;` |
| 90 | NO_COVERAGE | negated conditional | `return this.f.equals(p.f) && this.s.equals(p.s);` |
| 90 | NO_COVERAGE | negated conditional | `return this.f.equals(p.f) && this.s.equals(p.s);` |
| 90 | NO_COVERAGE | replaced boolean return with true for codenet/Main$Pair::equals | `return this.f.equals(p.f) && this.s.equals(p.s);` |
| 95 | NO_COVERAGE | replaced return value with "" for codenet/Main$Pair::toString | `return "{" + f.toString() + ", " + s.toString() + "}";` |
| 100 | NO_COVERAGE | negated conditional | `if (b == 0) {` |
| 101 | NO_COVERAGE | replaced int return with 0 for codenet/Main::gcd | `return a;` |
| 103 | NO_COVERAGE | Replaced integer modulus with multiplication | `return gcd(b, a % b);` |
| 103 | NO_COVERAGE | replaced int return with 0 for codenet/Main::gcd | `return gcd(b, a % b);` |
| 107 | NO_COVERAGE | changed conditional boundary | `for (int i = 2; i <= ((int) Math.sqrt(n)); i++) {` |
| 107 | NO_COVERAGE | negated conditional | `for (int i = 2; i <= ((int) Math.sqrt(n)); i++) {` |
| 108 | NO_COVERAGE | Replaced integer modulus with multiplication | `if (n % i == 0) {` |
| 108 | NO_COVERAGE | negated conditional | `if (n % i == 0) {` |
| 109 | NO_COVERAGE | replaced boolean return with true for codenet/Main::isPrime | `return false;` |
| 112 | NO_COVERAGE | negated conditional | `return n != 1;` |
| 112 | NO_COVERAGE | replaced boolean return with true for codenet/Main::isPrime | `return n != 1;` |
| 116 | NO_COVERAGE | Replaced integer division with multiplication | `for (int i = 0; i < array.length / 2; i++) {` |
| 116 | NO_COVERAGE | changed conditional boundary | `for (int i = 0; i < array.length / 2; i++) {` |
| 116 | NO_COVERAGE | negated conditional | `for (int i = 0; i < array.length / 2; i++) {` |
| 118 | NO_COVERAGE | Replaced integer subtraction with addition | `array[i] = array[array.length - i - 1];` |
| 118 | NO_COVERAGE | Replaced integer subtraction with addition | `array[i] = array[array.length - i - 1];` |
| 119 | NO_COVERAGE | Replaced integer subtraction with addition | `array[array.length - i - 1] = temp;` |
| 119 | NO_COVERAGE | Replaced integer subtraction with addition | `array[array.length - i - 1] = temp;` |
| 124 | NO_COVERAGE | Replaced integer division with multiplication | `for (int i = 0; i < array.length / 2; i++) {` |
| 124 | NO_COVERAGE | changed conditional boundary | `for (int i = 0; i < array.length / 2; i++) {` |
| 124 | NO_COVERAGE | negated conditional | `for (int i = 0; i < array.length / 2; i++) {` |
| 126 | NO_COVERAGE | Replaced integer subtraction with addition | `array[i] = array[array.length - i - 1];` |
| 126 | NO_COVERAGE | Replaced integer subtraction with addition | `array[i] = array[array.length - i - 1];` |
| 127 | NO_COVERAGE | Replaced integer subtraction with addition | `array[array.length - i - 1] = temp;` |
| 127 | NO_COVERAGE | Replaced integer subtraction with addition | `array[array.length - i - 1] = temp;` |
| 132 | NO_COVERAGE | Replaced long addition with subtraction | `for (long i = 2; i <= ((long) Math.sqrt(n)); i++) {` |
| 132 | NO_COVERAGE | changed conditional boundary | `for (long i = 2; i <= ((long) Math.sqrt(n)); i++) {` |
| 132 | NO_COVERAGE | negated conditional | `for (long i = 2; i <= ((long) Math.sqrt(n)); i++) {` |
| 133 | NO_COVERAGE | Replaced long modulus with multiplication | `if (n % i == 0) {` |
| 133 | NO_COVERAGE | negated conditional | `if (n % i == 0) {` |
| 134 | NO_COVERAGE | replaced boolean return with true for codenet/Main::isPrime | `return false;` |
| 137 | NO_COVERAGE | negated conditional | `return n != 1;` |
| 137 | NO_COVERAGE | replaced boolean return with true for codenet/Main::isPrime | `return n != 1;` |
| 143 | SURVIVED | changed conditional boundary | `for (long i = 2; i <= ((long) Math.sqrt(n)); i++) {` |
| 158 | NO_COVERAGE | Replaced long addition with subtraction | `for (long i = 1; i <= ((long) Math.sqrt(n)); i++) {` |
| 158 | NO_COVERAGE | changed conditional boundary | `for (long i = 1; i <= ((long) Math.sqrt(n)); i++) {` |
| 158 | NO_COVERAGE | negated conditional | `for (long i = 1; i <= ((long) Math.sqrt(n)); i++) {` |
| 159 | NO_COVERAGE | Replaced long modulus with multiplication | `if (n % i == 0) {` |
| 159 | NO_COVERAGE | negated conditional | `if (n % i == 0) {` |
| 161 | NO_COVERAGE | Replaced long division with multiplication | `if (i != n / i) {` |
| 161 | NO_COVERAGE | negated conditional | `if (i != n / i) {` |
| 162 | NO_COVERAGE | Replaced long division with multiplication | `list.add(n / i);` |
| 167 | NO_COVERAGE | replaced return value with Collections.emptyList for codenet/Main::divisors | `return list;` |
| 171 | NO_COVERAGE | Replaced integer division with multiplication | `return a / gcd(a, b) * b;` |
| 171 | NO_COVERAGE | Replaced integer multiplication with division | `return a / gcd(a, b) * b;` |
| 171 | NO_COVERAGE | replaced int return with 0 for codenet/Main::lcm | `return a / gcd(a, b) * b;` |
| 176 | NO_COVERAGE | Replaced integer subtraction with addition | `int min = Math.min(k, n - k);` |
| 177 | NO_COVERAGE | changed conditional boundary | `for (int i = 1; i <= min; i++) {` |
| 177 | NO_COVERAGE | negated conditional | `for (int i = 1; i <= min; i++) {` |
| 178 | NO_COVERAGE | Replaced integer subtraction with addition | `ret = (ret * modPow(i, M - 2, M)) % M;` |
| 178 | NO_COVERAGE | Replaced long modulus with multiplication | `ret = (ret * modPow(i, M - 2, M)) % M;` |
| 178 | NO_COVERAGE | Replaced long multiplication with division | `ret = (ret * modPow(i, M - 2, M)) % M;` |
| 180 | NO_COVERAGE | Replaced integer addition with subtraction | `for (int i = n - min + 1; i <= n; i++) {` |
| 180 | NO_COVERAGE | Replaced integer subtraction with addition | `for (int i = n - min + 1; i <= n; i++) {` |
| 180 | NO_COVERAGE | changed conditional boundary | `for (int i = n - min + 1; i <= n; i++) {` |
| 180 | NO_COVERAGE | negated conditional | `for (int i = n - min + 1; i <= n; i++) {` |
| 181 | NO_COVERAGE | Replaced long modulus with multiplication | `ret = (ret * i) % M;` |
| 181 | NO_COVERAGE | Replaced long multiplication with division | `ret = (ret * i) % M;` |
| 183 | NO_COVERAGE | replaced int return with 0 for codenet/Main::nCk | `return (int) ret;` |
| 190 | NO_COVERAGE | changed conditional boundary | `while (b > 0) {` |
| 190 | NO_COVERAGE | negated conditional | `while (b > 0) {` |
| 191 | NO_COVERAGE | Replaced bitwise AND with OR | `if ((b & 1) == 1) ret = (ret * tmp) % M;` |
| 191 | NO_COVERAGE | Replaced long modulus with multiplication | `if ((b & 1) == 1) ret = (ret * tmp) % M;` |
| 191 | NO_COVERAGE | Replaced long multiplication with division | `if ((b & 1) == 1) ret = (ret * tmp) % M;` |
| 191 | NO_COVERAGE | negated conditional | `if ((b & 1) == 1) ret = (ret * tmp) % M;` |
| 192 | NO_COVERAGE | Replaced long modulus with multiplication | `tmp = (tmp * tmp) % M;` |
| 192 | NO_COVERAGE | Replaced long multiplication with division | `tmp = (tmp * tmp) % M;` |
| 193 | NO_COVERAGE | Replaced Shift Right with Shift Left | `b = b >> 1;` |
| 195 | NO_COVERAGE | replaced long return with 0 for codenet/Main::modPow | `return ret;` |
| 201 | SURVIVED | Replaced bitwise AND with OR | `if ((b & 1) == 1) ret = (ret * tmp);` |
| 202 | SURVIVED | Replaced long multiplication with division | `tmp = (tmp * tmp);` |
| 203 | SURVIVED | Replaced Shift Right with Shift Left | `b = b >> 1;` |
| 210 | NO_COVERAGE | negated conditional | `if (tree[idx] == idx) return idx;` |
| 210 | NO_COVERAGE | replaced int return with 0 for codenet/Main::find | `if (tree[idx] == idx) return idx;` |
| 211 | NO_COVERAGE | replaced int return with 0 for codenet/Main::find | `else return tree[idx] = find(tree, tree[idx]);` |
| 223 | NO_COVERAGE | Replaced integer subtraction with addition | `while (Math.abs(ok - ng) > 1) {` |
| 223 | NO_COVERAGE | changed conditional boundary | `while (Math.abs(ok - ng) > 1) {` |
| 223 | NO_COVERAGE | negated conditional | `while (Math.abs(ok - ng) > 1) {` |
| 224 | NO_COVERAGE | Replaced integer addition with subtraction | `int mid = (ok + ng) / 2;` |
| 224 | NO_COVERAGE | Replaced integer division with multiplication | `int mid = (ok + ng) / 2;` |
| 225 | NO_COVERAGE | changed conditional boundary | `if (list[mid] >= target) {` |
| 225 | NO_COVERAGE | negated conditional | `if (list[mid] >= target) {` |
| 231 | NO_COVERAGE | replaced int return with 0 for codenet/Main::lowerBound | `return ok;` |
| 237 | NO_COVERAGE | Replaced integer subtraction with addition | `while (Math.abs(ok - ng) > 1) {` |
| 237 | NO_COVERAGE | changed conditional boundary | `while (Math.abs(ok - ng) > 1) {` |
| 237 | NO_COVERAGE | negated conditional | `while (Math.abs(ok - ng) > 1) {` |
| 238 | NO_COVERAGE | Replaced integer addition with subtraction | `int mid = (ok + ng) / 2;` |
| 238 | NO_COVERAGE | Replaced integer division with multiplication | `int mid = (ok + ng) / 2;` |
| 239 | NO_COVERAGE | changed conditional boundary | `if (list[mid] >= target) {` |
| 239 | NO_COVERAGE | negated conditional | `if (list[mid] >= target) {` |
| 245 | NO_COVERAGE | replaced int return with 0 for codenet/Main::lowerBound | `return ok;` |
| 249 | NO_COVERAGE | Replaced XOR with AND | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) >= 0) ? 1 : -1);` |
| 249 | NO_COVERAGE | changed conditional boundary | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) >= 0) ? 1 : -1);` |
| 249 | NO_COVERAGE | negated conditional | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) >= 0) ? 1 : -1);` |
| 249 | NO_COVERAGE | replaced int return with 0 for codenet/Main::lambda$lowerBound$1 | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) >= 0) ? 1 : -1);` |
| 249 | NO_COVERAGE | replaced int return with 0 for codenet/Main::lowerBound | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) >= 0) ? 1 : -1);` |
| 253 | NO_COVERAGE | Replaced XOR with AND | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) > 0) ? 1 : -1);` |
| 253 | NO_COVERAGE | changed conditional boundary | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) > 0) ? 1 : -1);` |
| 253 | NO_COVERAGE | negated conditional | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) > 0) ? 1 : -1);` |
| 253 | NO_COVERAGE | replaced int return with 0 for codenet/Main::lambda$upperBound$2 | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) > 0) ? 1 : -1);` |
| 253 | NO_COVERAGE | replaced int return with 0 for codenet/Main::upperBound | `return ~Collections.binarySearch(list, target, (x, y) -> (x.compareTo(y) > 0) ? 1 : -1);` |
