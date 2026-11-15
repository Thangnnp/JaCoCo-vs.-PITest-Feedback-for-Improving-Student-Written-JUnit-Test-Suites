# Phản hồi PITest: mutant sống sót (p03546)

Mutation score: **34/38** (89.5%)

| Dòng | Trạng thái | Thay đổi của mutant | Mã nguồn |
| ---: | :-: | :--- | :--- |
| 22 | SURVIVED | removed call to codenet/Main::dijkstra | `dijkstra(c,end,d);` |
| 54 | SURVIVED | changed conditional boundary | `if (map[marked][j]>0 && !fixed[j]) { // 未確定ならば` |
| 58 | SURVIVED | changed conditional boundary | `if (newDistance < distance[j]) distance[j] = newDistance;` |
| 70 | SURVIVED | changed conditional boundary | `if (!fixed[i] && distance[i]<distance[idx]) idx=i;` |
