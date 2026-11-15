package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testSample1() {
        // N=2, M=6. Sequences: {1,6}, {2,3}, {3,2}, {6,1} -> 4
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    void testMIsOne() {
        // N=5, M=1. Only sequence: {1,1,1,1,1} -> 1
        assertEquals("1", Judge.run("5 1"));
    }

    @Test
    void testNIsOne() {
        // N=1, M=10. Only sequence: {10} -> 1
        assertEquals("1", Judge.run("1 10"));
    }
    
    @Test
    void testPrimeM() {
        // N=3, M=7. Sequences: {7,1,1}, {1,7,1}, {1,1,7} -> 3
        assertEquals("3", Judge.run("3 7"));
    }

    @Test
    void testWhitespaceInput() {
        // Kiểm tra input với tab và newline để bao phủ các nhánh trong isSpaceChar
        assertEquals("4", Judge.run("2\t6\n"));
    }

    @Test
    void testCombinationEdgeCases() {
        // N=1, M=1 -> ans=1 (Kiểm tra ncr khi n=r)
        assertEquals("1", Judge.run("1 1"));
    }

    @Test
    void testMultiplePrimeFactors() {
        // M = 12 = 2^2 * 3^1. N=2.
        // ans = 6.
        assertEquals("6", Judge.run("2 12"));
    }

    // --- Các test mới để tăng độ phủ ---

    @Test
    void testCarriageReturnInput() {
        // Covers \r in isSpaceChar (line 82)
        assertEquals("4", Judge.run("2\r6"));
    }

    @Test
    void testLargePrimeM() {
        // Tăng phạm vi chạy của generatePrimeNumbers (lines 163, 165)
        // M = 997 là số nguyên tố
        assertEquals("2", Judge.run("2 997"));
    }

    
    
    
}
