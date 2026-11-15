package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
    /**
     * Trường hợp N = M:
     * Theo logic, số cách xếp là 2 * N! * M!
     * Với N=2, M=2: 2 * 2! * 2! = 2 * 2 * 2 = 8.
     */
    @Test
    void testEqualCount() {
        assertEquals("8", Judge.run("2 2"));
    }

    /**
     * Trường hợp |N - M| = 1:
     * Theo logic, số cách xếp là N! * M!
     * Với N=3, M=2: 3! * 2! = 6 * 2 = 12.
     */
    @Test
    void testDiffByOne() {
        assertEquals("12", Judge.run("3 2"));
    }

    /**
     * Trường hợp |N - M| > 1:
     * Không thể xếp xen kẽ, kết quả phải bằng 0.
     * Với N=1, M=8: Chênh lệch quá lớn.
     */
    @Test
    void testDiffMoreThanOne() {
        assertEquals("0", Judge.run("1 8"));
    }
}
