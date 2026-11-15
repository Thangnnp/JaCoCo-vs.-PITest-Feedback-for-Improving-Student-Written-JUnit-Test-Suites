# Phản hồi PITest: mutant sống sót (p00144)

Mutation score: **29/110** (26.4%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 15 | NO_COVERAGE | replaced return value with "" for codenet/Main$Point::toString | `@Override public String toString(){	return "("+this.x+","+this.y+")";}` |
| 17 | NO_COVERAGE | changed conditional boundary | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | changed conditional boundary | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | changed conditional boundary | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | changed conditional boundary | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | negated conditional | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | negated conditional | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | negated conditional | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | negated conditional | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 17 | NO_COVERAGE | replaced boolean return with true for codenet/Main$Point::ok | `return (min<=x&&x<X && min<=y&&y<Y)?true:false;` |
| 19 | NO_COVERAGE | replaced boolean return with false for codenet/Main$Point::ok | `static boolean ok(int x,int y,int X,int Y){	return ok(x,y,X,Y,0);}` |
| 19 | NO_COVERAGE | replaced boolean return with true for codenet/Main$Point::ok | `static boolean ok(int x,int y,int X,int Y){	return ok(x,y,X,Y,0);}` |
| 26 | NO_COVERAGE | negated conditional | `while(sc.hasNext()){` |
| 29 | NO_COVERAGE | Changed increment from 1 to -1 | `for(int i=0; i<N; i++)	c[i]=new C0145(sc.nextInt(),sc.nextInt());` |
| 29 | NO_COVERAGE | changed conditional boundary | `for(int i=0; i<N; i++)	c[i]=new C0145(sc.nextInt(),sc.nextInt());` |
| 29 | NO_COVERAGE | negated conditional | `for(int i=0; i<N; i++)	c[i]=new C0145(sc.nextInt(),sc.nextInt());` |
| 31 | NO_COVERAGE | removed call to java/io/PrintStream::println | `out.println(ans);` |
| 43 | NO_COVERAGE | negated conditional | `while(sc.hasNext())	queue.add(sc.nextInt());` |
| 45 | NO_COVERAGE | removed call to java/util/Arrays::fill | `Arrays.fill(seat, -1);` |
| 46 | NO_COVERAGE | changed conditional boundary | `for(int i=0; i<MAX; i++){` |
| 46 | NO_COVERAGE | negated conditional | `for(int i=0; i<MAX; i++){` |
| 47 | NO_COVERAGE | Replaced integer modulus with multiplication | `num[i]=(i%5==1?5:2);` |
| 47 | NO_COVERAGE | negated conditional | `num[i]=(i%5==1?5:2);` |
| 48 | NO_COVERAGE | Replaced integer addition with subtraction | `atime[i]=(17*(i%2)+3*(i%3)+19);` |
| 48 | NO_COVERAGE | Replaced integer addition with subtraction | `atime[i]=(17*(i%2)+3*(i%3)+19);` |
| 48 | NO_COVERAGE | Replaced integer modulus with multiplication | `atime[i]=(17*(i%2)+3*(i%3)+19);` |
| 48 | NO_COVERAGE | Replaced integer modulus with multiplication | `atime[i]=(17*(i%2)+3*(i%3)+19);` |
| 48 | NO_COVERAGE | Replaced integer multiplication with division | `atime[i]=(17*(i%2)+3*(i%3)+19);` |
| 48 | NO_COVERAGE | Replaced integer multiplication with division | `atime[i]=(17*(i%2)+3*(i%3)+19);` |
| 52 | NO_COVERAGE | changed conditional boundary | `while(gno<=99){` |
| 52 | NO_COVERAGE | negated conditional | `while(gno<=99){` |
| 55 | NO_COVERAGE | Replaced integer multiplication with division | `if(temp>=0 && min>=gno*5){` |
| 55 | NO_COVERAGE | changed conditional boundary | `if(temp>=0 && min>=gno*5){` |
| 55 | NO_COVERAGE | changed conditional boundary | `if(temp>=0 && min>=gno*5){` |
| 55 | NO_COVERAGE | negated conditional | `if(temp>=0 && min>=gno*5){` |
| 55 | NO_COVERAGE | negated conditional | `if(temp>=0 && min>=gno*5){` |
| 56 | NO_COVERAGE | Replaced integer multiplication with division | `ans[gno]=max(0,min-gno*5);` |
| 56 | NO_COVERAGE | Replaced integer subtraction with addition | `ans[gno]=max(0,min-gno*5);` |
| 57 | NO_COVERAGE | Changed increment from 1 to -1 | `for(int i=temp; i<temp+num[gno]; i++)	seat[i]=gno;` |
| 57 | NO_COVERAGE | Replaced integer addition with subtraction | `for(int i=temp; i<temp+num[gno]; i++)	seat[i]=gno;` |
| 57 | NO_COVERAGE | changed conditional boundary | `for(int i=temp; i<temp+num[gno]; i++)	seat[i]=gno;` |
| 57 | NO_COVERAGE | negated conditional | `for(int i=temp; i<temp+num[gno]; i++)	seat[i]=gno;` |
| 59 | NO_COVERAGE | Changed increment from 1 to -1 | `gno++;` |
| 63 | NO_COVERAGE | Changed increment from 1 to -1 | `min++;` |
| 67 | NO_COVERAGE | negated conditional | `while(!queue.isEmpty())	out.println(ans[queue.poll()]);` |
| 67 | NO_COVERAGE | removed call to java/io/PrintStream::println | `while(!queue.isEmpty())	out.println(ans[queue.poll()]);` |
| 70 | NO_COVERAGE | Replaced integer subtraction with addition | `for(int i=0; i<=17-n; i++){` |
| 70 | NO_COVERAGE | changed conditional boundary | `for(int i=0; i<=17-n; i++){` |
| 70 | NO_COVERAGE | negated conditional | `for(int i=0; i<=17-n; i++){` |
| 72 | NO_COVERAGE | changed conditional boundary | `for(int j=0; j<n; j++){` |
| 72 | NO_COVERAGE | negated conditional | `for(int j=0; j<n; j++){` |
| 73 | NO_COVERAGE | Replaced integer addition with subtraction | `if(seat[i+j]!=-1){` |
| 73 | NO_COVERAGE | negated conditional | `if(seat[i+j]!=-1){` |
| 78 | NO_COVERAGE | negated conditional | `if(flag)	return i;` |
| 78 | NO_COVERAGE | replaced int return with 0 for codenet/Main::find | `if(flag)	return i;` |
| 80 | NO_COVERAGE | replaced int return with 0 for codenet/Main::find | `return -1;` |
| 83 | NO_COVERAGE | changed conditional boundary | `for(int i=0; i<17; i++){` |
| 83 | NO_COVERAGE | negated conditional | `for(int i=0; i<17; i++){` |
| 84 | NO_COVERAGE | changed conditional boundary | `if(seat[i]<0)	continue;` |
| 84 | NO_COVERAGE | negated conditional | `if(seat[i]<0)	continue;` |
| 85 | NO_COVERAGE | Replaced integer addition with subtraction | `int emin=itime[seat[i]]+atime[seat[i]];` |
| 86 | NO_COVERAGE | changed conditional boundary | `if(min>=emin)	seat[i]=-1;` |
| 86 | NO_COVERAGE | negated conditional | `if(min>=emin)	seat[i]=-1;` |
| 88 | NO_COVERAGE | replaced return value with null for codenet/Main::exit | `return seat;` |
| 91 | NO_COVERAGE | removed call to java/io/PrintStream::print | `out.print(min+"m : ");` |
| 92 | NO_COVERAGE | Changed increment from 1 to -1 | `for(int i=0; i<17; i++)	out.print(seat[i]+" ");` |
| 92 | NO_COVERAGE | changed conditional boundary | `for(int i=0; i<17; i++)	out.print(seat[i]+" ");` |
| 92 | NO_COVERAGE | negated conditional | `for(int i=0; i<17; i++)	out.print(seat[i]+" ");` |
| 92 | NO_COVERAGE | removed call to java/io/PrintStream::print | `for(int i=0; i<17; i++)	out.print(seat[i]+" ");` |
| 93 | NO_COVERAGE | removed call to java/io/PrintStream::println | `out.println();` |
| 117 | SURVIVED | Replaced integer addition with subtraction | `if(R[now.now][j] && now.c+1<close[j]){` |
| 117 | SURVIVED | changed conditional boundary | `if(R[now.now][j] && now.c+1<close[j]){` |
| 119 | SURVIVED | changed conditional boundary | `ans=(ans<0?now.c+1:min(ans,now.c+1));` |
| 123 | SURVIVED | Replaced integer addition with subtraction | `close[j]=now.c+1;` |
| 127 | SURVIVED | changed conditional boundary | `out.println(((ans<0)?"NA":ans));` |
| 137 | NO_COVERAGE | replaced int return with 0 for codenet/Main$C0144::compareTo | `if(this.c<o.c)	return -1;` |
| 137 | SURVIVED | changed conditional boundary | `if(this.c<o.c)	return -1;` |
| 137 | SURVIVED | negated conditional | `if(this.c<o.c)	return -1;` |
| 138 | SURVIVED | changed conditional boundary | `if(this.c>o.c)	return 1;` |
| 138 | SURVIVED | negated conditional | `if(this.c>o.c)	return 1;` |
| 138 | SURVIVED | replaced int return with 0 for codenet/Main$C0144::compareTo | `if(this.c>o.c)	return 1;` |
