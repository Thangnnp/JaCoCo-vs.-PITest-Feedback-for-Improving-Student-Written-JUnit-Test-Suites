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
    
    // --- Các test mới để tăng độ phủ FastScanner ---

    @Test
    void testNegativeInput() {
        // Trigger minus logic (lines 92, 93, 105)
        // Mặc dù không đúng đề bài, nhưng ép chạy nhánh
        assertThrows(RuntimeException.class, () -> Judge.run("-5 10"));
    }

    @Test
    void testLeadingWhitespace() {
        // Trigger "while (isSpaceChar(b))" (line 89)
        assertEquals("4", Judge.run("   2 6"));
    }

    
}
