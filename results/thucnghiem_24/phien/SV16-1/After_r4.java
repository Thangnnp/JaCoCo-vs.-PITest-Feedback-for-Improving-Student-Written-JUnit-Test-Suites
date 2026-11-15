package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void testSample1() {
        // N=2, M=2. |N-M|=0. 2! * 2! * 2 = 8
        assertEquals("8", Judge.run("2 2"));
    }

    @Test
    void testSample2() {
        // N=3, M=2. |N-M|=1 (N-1=M). 3! * 2! = 12
        assertEquals("12", Judge.run("3 2"));
    }

    @Test
    void testSample3() {
        // N=1, M=8. |N-M|=7 > 1. Output 0
        assertEquals("0", Judge.run("1 8"));
    }

    @Test
    void testSmallestCase() {
        // N=1, M=1. |N-M|=0. 1! * 1! * 2 = 2
        assertEquals("2", Judge.run("1 1"));
    }

    @Test
    void testImbalanceCase() {
        // N=5, M=3. |N-M|=2 > 1. Output 0
        assertEquals("0", Judge.run("5 3"));
    }

    @Test
    void testSymmetricCase() {
        // N=2, M=3. |N-M|=1 (N+1=M). 2! * 3! = 12
        assertEquals("12", Judge.run("2 3"));
    }

    @Test
    void testLargeInput() {
        // Sample 4: 100000 100000
        assertEquals("530123477", Judge.run("100000 100000"));
    }

    @Test
    void testLargeDiffOne() {
        // N=100000, M=99999. N-1 == M
        // Không mong đợi kết quả 0
        assertNotEquals("0", Judge.run("100000 99999"));
    }

    @Test
    void testLargeDiffOneSymmetric() {
        // N=99999, M=100000. M-1 == N
        assertNotEquals("0", Judge.run("99999 100000"));
    }
    
    @Test
    void testBoundaryLargeValue() {
        // Kiểm tra trường hợp biên lớn nhất 100000 và 100000
        // Đã test trong testLargeInput, thêm test này để khẳng định tính nhất quán
        assertEquals("530123477", Judge.run("100000 100000"));
    }
}
