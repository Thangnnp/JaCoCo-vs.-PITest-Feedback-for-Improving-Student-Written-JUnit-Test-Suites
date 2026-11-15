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

    @Test
    void testLastGateOnLeft() {
        assertEquals("0", Judge.run("5 2 3\n1 2"));
    }

    @Test
    void testGateImmediatelyRightOfX() {
        assertEquals("0", Judge.run("5 1 3\n4"));
    }

    @Test
    void testEqualNumberGates() {
        assertEquals("1", Judge.run("4 2 2\n1 3"));
    }
    
    @Test
    void testIdxGreaterThanRightSide() {
        assertEquals("0", Judge.run("5 3 4\n1 2 3"));
    }

    @Test
    void testIdxLessThanRightSide() {
        assertEquals("1", Judge.run("5 3 2\n1 3 4"));
    }

    @Test
    void testLargeConstraints() {
        assertEquals("2", Judge.run("100 5 50\n10 20 30 60 70"));
    }

    // Thêm test case biên: X nằm sát A_i (trạm bên trái)
    // N=5, M=2, X=3. Gates: 2, 4
    // Trái: {2} -> idx=1
    // Phải: {4} -> m-idx=1
    // Kết quả: 1. Đảm bảo logic num < x hoạt động đúng tại ranh giới
    @Test
    void testXAdjacentToGateOnLeft() {
        assertEquals("1", Judge.run("5 2 3\n2 4"));
    }

    // Thêm test case biên: X nằm sát A_i (trạm bên phải)
    // N=5, M=2, X=3. Gates: 1, 4
    // Trái: {1} -> idx=1
    // Phải: {4} -> m-idx=1
    // Kết quả: 1.
    @Test
    void testXAdjacentToGateOnRight() {
        assertEquals("1", Judge.run("5 2 3\n1 4"));
    }
}
