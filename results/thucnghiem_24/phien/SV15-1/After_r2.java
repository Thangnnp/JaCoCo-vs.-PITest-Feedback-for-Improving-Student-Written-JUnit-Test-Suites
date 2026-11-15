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
        // Cân bằng (2 <= 2). 
        assertEquals("2", Judge.run("10 4 5\n1 4 6 9"));
    }

    @Test
    void testLoopBoundary() {
        // Đảm bảo vòng lặp đọc hết M cổng.
        assertEquals("0", Judge.run("5 2 5\n1 2"));
    }

    @Test
    void testAllLeft() {
        // Cổng tập trung toàn bộ bên trái.
        assertEquals("0", Judge.run("5 3 4\n1 2 3"));
    }
    
    @Test
    void testExtremeXLeft() {
        // X = 1 (cực trái), không thể đi sang trái nữa.
        // N=5, M=1, X=1. Cổng ở 2.
        // Bên trái: 0, Phải: 1. Min = 0.
        assertEquals("0", Judge.run("5 1 1\n2"));
    }
    
    @Test
    void testExtremeXRight() {
        // X = N-1 (cực phải).
        // N=5, M=1, X=4. Cổng ở 3.
        // Bên trái: 1, Phải: 0. Min = 0.
        assertEquals("0", Judge.run("5 1 4\n3"));
    }

    
}
