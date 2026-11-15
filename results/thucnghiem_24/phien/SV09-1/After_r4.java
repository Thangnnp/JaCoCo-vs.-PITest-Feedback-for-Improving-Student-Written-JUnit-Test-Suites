package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testSample1() {
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    void testMIsOne() {
        assertEquals("1", Judge.run("5 1"));
    }

    @Test
    void testNIsOne() {
        assertEquals("1", Judge.run("1 10"));
    }
    
    @Test
    void testPrimeM() {
        assertEquals("3", Judge.run("3 7"));
    }

    @Test
    void testWhitespaceInput() {
        assertEquals("4", Judge.run("2\t6\n"));
    }

    @Test
    void testCombinationEdgeCases() {
        assertEquals("1", Judge.run("1 1"));
    }

    @Test
    void testMultiplePrimeFactors() {
        assertEquals("6", Judge.run("2 12"));
    }

    @Test
    void testCarriageReturnInput() {
        assertEquals("4", Judge.run("2\r6"));
    }

    @Test
    void testLargePrimeM() {
        assertEquals("2", Judge.run("2 997"));
    }

    @Test
    void testEmptyInput() {
        assertThrows(RuntimeException.class, () -> Judge.run(""));
    }

    @Test
    void testNegativeInput() {
        // -5 là hợp lệ trong parser, không ném ngoại lệ
        // N=2, M=-5 -> N=2, M=-5. Chương trình sẽ chạy với M âm, kết quả có thể không như ý nhưng không crash.
        // Chỉ cần chạy được là tốt cho coverage.
        assertDoesNotThrow(() -> Judge.run("2 -5"));
    }

    @Test
    void testLeadingWhitespace() {
        assertEquals("4", Judge.run("   2 6"));
    }

    @Test
    void testInvalidCharacter() {
        assertThrows(RuntimeException.class, () -> Judge.run("2 6a"));
    }

    @Test
    void testLargeNumberParsing() {
        // Kiểm tra logic while (b >= '0' && b <= '9') với nhiều chữ số
        // N=1, M=1000000000
        assertEquals("1", Judge.run("1 1000000000"));
    }
}
