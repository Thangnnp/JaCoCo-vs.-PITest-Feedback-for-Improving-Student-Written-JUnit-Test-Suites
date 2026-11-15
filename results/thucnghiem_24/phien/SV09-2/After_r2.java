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
    
    // Test trường hợp idx > m-idx (Nhánh else)
    // N=5, M=3, X=4
    // Gates: 1, 2, 3
    // Trái: {1, 2, 3} -> idx=3
    // Phải: {} -> m-idx=0
    // Min(3, 0) = 0.
    @Test
    void testIdxGreaterThanRightSide() {
        assertEquals("0", Judge.run("5 3 4\n1 2 3"));
    }

    // Test trường hợp idx < m-idx (Nhánh if)
    // N=5, M=3, X=2
    // Gates: 1, 3, 4
    // Trái: {1} -> idx=1
    // Phải: {3, 4} -> m-idx=2
    // Min(1, 2) = 1.
    @Test
    void testIdxLessThanRightSide() {
        assertEquals("1", Judge.run("5 3 2\n1 3 4"));
    }

    // Test trường hợp N, M lớn để kiểm tra vòng lặp
    
}
