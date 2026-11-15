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
    void testEdgeMinM() {
        assertEquals("0", Judge.run("5 1 3\n4"));
    }
    
    @Test
    void testBalanced() {
        // M=4, X=5. Cổng: 1, 4, 6, 9. 
        // Bên trái: 1, 4 (2 cổng), Bên phải: 6, 9 (2 cổng).
        // idx = 2. m-idx = 2.
        // Test này sẽ giúp giết mutant ở dòng 21 (if idx <= m-idx)
        assertEquals("2", Judge.run("10 4 5\n1 4 6 9"));
    }

    @Test
    void testLoopBoundary() {
        // Kiểm tra mutant dòng 13 (vòng lặp).
        // Cần đảm bảo cổng cuối cùng được tính.
        // N=5, M=2, X=5. Cổng: 1, 2
        // Cả 2 cổng đều < 5. idx nên là 2. m-idx = 0.
        // Kết quả = min(2, 0) = 0.
        // Nếu vòng lặp chỉ chạy 1 lần (i < m), idx = 1, kết quả = min(1, 1) = 1 (SAI).
        assertEquals("0", Judge.run("5 2 5\n1 2"));
    }

    
}
