package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    void testSample1() {
        String input = "1 2 +";
        assertEquals("3", Judge.run(input));
    }

    @Test
    void testSample2() {
        String input = "1 2 + 3 4 - *";
        assertEquals("-3", Judge.run(input));
    }

    @Test
    void testEdgeCase() {
        String input = "100000";
        assertEquals("100000", Judge.run(input));
    }

    // Thêm test mới:
    @Test
    void testNegativeNumber() {
        String input = "-1 2 -";
        assertEquals("-3", Judge.run(input));
    }

    @Test
    void testOperatorOrder() {
        String input = "1 + 2 * 3 -";
        assertEquals("0", Judge.run(input));
    }

    // Sửa test EdgeCase để kiểm tra trường hợp số quá lớn:
    @Test
    void testEdgeCaseLargerNumber() {
        String input = "10000000"; // Thay vì 100000
        assertEquals("10000000", Judge.run(input));
    }
}
