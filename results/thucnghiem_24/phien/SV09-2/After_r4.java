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
        // Gates bên trái: 1, 2, 3 (idx=3), bên phải: 0 (m-idx=0). Min(3,0) = 0
        assertEquals("0", Judge.run("10 3 5\n1 2 3"));
    }

    @Test
    void testLastGateOnLeft() {
        // Gates bên trái: 1, 2 (idx=2), bên phải: 0 (m-idx=0). Min(2,0) = 0
        assertEquals("0", Judge.run("5 2 3\n1 2"));
    }

    @Test
    void testGateImmediatelyRightOfX() {
        // X=3. Gate ở 4. Trái: 0, Phải: 1. Min(0,1) = 0
        assertEquals("0", Judge.run("5 1 3\n4"));
    }

    @Test
    void testEqualNumberGates() {
        // Trái: 1, Phải: 3. idx=1, m-idx=1. Kết quả: 1
        assertEquals("1", Judge.run("4 2 2\n1 3"));
    }
    
    @Test
    void testIdxGreaterThanRightSide() {
        // Trái: 1, 2, 3 (idx=3), Phải: 0 (m-idx=0). Kết quả: 0
        assertEquals("0", Judge.run("5 3 4\n1 2 3"));
    }

    @Test
    void testIdxLessThanRightSide() {
        // Trái: 1 (idx=1), Phải: 3, 4 (m-idx=2). Kết quả: 1
        assertEquals("1", Judge.run("5 3 2\n1 3 4"));
    }

    @Test
    void testLargeConstraints() {
        // Trái: 10, 20, 30 (3 cái), Phải: 60, 70 (2 cái). Min(3, 2) = 2
        assertEquals("2", Judge.run("100 5 50\n10 20 30 60 70"));
    }

    @Test
    void testXAdjacentToGateOnLeft() {
        assertEquals("1", Judge.run("5 2 3\n2 4"));
    }

    @Test
    void testXAdjacentToGateOnRight() {
        assertEquals("1", Judge.run("5 2 3\n1 4"));
    }
}
