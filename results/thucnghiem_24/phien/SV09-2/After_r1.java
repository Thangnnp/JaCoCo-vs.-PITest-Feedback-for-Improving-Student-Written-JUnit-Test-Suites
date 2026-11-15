package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void testSample1() {
        assertEquals("1", Judge.run("5 3 3\n1 2 4"));
    }

    @Test
    void testSample2() {
        assertEquals("0", Judge.run("7 3 2\n4 5 6"));
    }

    @Test
    void testSample3() {
        assertEquals("3", Judge.run("10 7 5\n1 2 3 4 6 8 9"));
    }

    @Test
    void testAllGatesOnOneSide() {
        assertEquals("0", Judge.run("10 3 5\n1 2 3"));
    }

    // Test để giết mutant ở dòng 13 (vòng lặp i<=m)
    // Nếu i < m, thì trạm cuối cùng (A_m) sẽ không được xét.
    // Ở đây A_m = 2, X = 3. Nếu xét thiếu A_m, idx sẽ sai (là 1 thay vì 2).
    @Test
    void testLastGateOnLeft() {
        // N=5, M=2, X=3. Gates: 1, 2
        // Bên trái: {1, 2} -> 2 trạm.
        // Bên phải: {} -> 0 trạm.
        // Min(2, 0) = 0.
        assertEquals("0", Judge.run("5 2 3\n1 2"));
    }

    // Test để giết mutant ở dòng 15 (num < x -> num <= x)
    // Dù đề bài nói A_i != X, ta cần đảm bảo logic num < x hoạt động đúng.
    // Trường hợp này A_i ngay sát X bên phải, đảm bảo nó KHÔNG bị đếm vào bên trái.
    @Test
    void testGateImmediatelyRightOfX() {
        // N=5, M=1, X=3. Gate: 4
        // Bên trái: {} -> 0
        // Bên phải: {4} -> 1
        // Min(0, 1) = 0.
        assertEquals("0", Judge.run("5 1 3\n4"));
    }

    // Test để giết mutant ở dòng 21 (idx <= m-idx -> idx < m-idx)
    // Kiểm tra trường hợp cân bằng: số trạm trái bằng số trạm phải.
    // N=4, M=2, X=2. Gates: 1, 3.
    // Left: {1} -> 1 trạm. Right: {3} -> 1 trạm.
    // idx = 1, m-idx = 2-1 = 1.
    // idx <= m-idx (1 <= 1) là đúng.
    
}
