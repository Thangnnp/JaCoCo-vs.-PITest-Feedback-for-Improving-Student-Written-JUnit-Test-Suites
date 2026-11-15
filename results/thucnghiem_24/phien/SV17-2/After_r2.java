package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    /**
     * Test Sample 1: N = M
     * 2! * 2! * 2 = 8
     */
    @Test
    void testEqualCount() {
        assertEquals("8", Judge.run("2 2"));
    }

    /**
     * Test Sample 2: N = M + 1
     * 3! * 2! = 6 * 2 = 12
     */
    @Test
    void testDiffByOneN() {
        assertEquals("12", Judge.run("3 2"));
    }

    /**
     * Test phủ nhánh n+1 == m ở dòng 18
     * 2! * 3! = 2 * 6 = 12
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
     * Test Sample 4: Số lớn tối đa để kiểm tra Modulo và tràn số
     */
    @Test
    void testLargeInput() {
        assertEquals("530123477", Judge.run("100000 100000"));
    }

    /**
     * Test biên nhỏ nhất của nhánh N = M + 1
     * 2! * 1! = 2
     */
    @Test
    void testSmallestDiffN() {
        assertEquals("2", Judge.run("2 1"));
    }

    /**
     * Test biên nhỏ nhất của nhánh M = N + 1
     * 1! * 2! = 2
     */
    @Test
    void testSmallestDiffM() {
        assertEquals("2", Judge.run("1 2"));
    }

    /**
     * Test thêm trường hợp N = M để chắc chắn về hàm modfact
     * 3! * 3! * 2 = 6 * 6 * 2 = 72
     */
    @Test
    void testEqualCountThree() {
        assertEquals("72", Judge.run("3 3"));
    }
}
