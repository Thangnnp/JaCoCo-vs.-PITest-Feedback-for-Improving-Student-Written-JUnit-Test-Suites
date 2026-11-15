package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    /**
     * Test Sample 1: N = M
     */
    @Test
    void testEqualCount() {
        assertEquals("8", Judge.run("2 2"));
    }

    /**
     * Test Sample 2: N = M + 1 (Nhánh n-1 == m)
     */
    @Test
    void testDiffByOneN() {
        assertEquals("12", Judge.run("3 2"));
    }

    /**
     * Test bổ sung để phủ nhánh n+1 == m ở dòng 18
     * N = 2, M = 3: 2! * 3! = 2 * 6 = 12
     */
    @Test
    void testDiffByOneM() {
        assertEquals("12", Judge.run("2 3"));
    }

    /**
     * Test Sample 3: |N - M| > 1
     */
    @Test
    void testDiffMoreThanOne() {
        assertEquals("0", Judge.run("1 8"));
    }

    /**
     * Test biên nhỏ nhất: N=1, M=1
     * 1! * 1! * 2 = 2
     */
    @Test
    void testMinimumConstraints() {
        assertEquals("2", Judge.run("1 1"));
    }

    /**
     * Test Sample 4: Số lớn để kiểm tra Modulo và tràn số
     */
    @Test
    void testLargeInput() {
        assertEquals("530123477", Judge.run("100000 100000"));
    }
}
