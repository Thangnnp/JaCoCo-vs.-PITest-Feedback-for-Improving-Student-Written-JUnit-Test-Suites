package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void testSample1() {
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    void testSample2() {
        assertEquals("18", Judge.run("3 12"));
    }

    @Test
    void testSample3() {
        // Large input
        assertEquals("957870001", Judge.run("100000 1000000000"));
    }

    @Test
    void testMIsOne() {
        // N=5, M=1. M=1 has no prime factors, ans should be 1.
        assertEquals("1", Judge.run("5 1"));
    }

    @Test
    void testPrimeM() {
        // N=2, M=7. {1,7}, {7,1}.
        assertEquals("2", Judge.run("2 7"));
    }

    @Test
    void testNIsOne() {
        // N=1, M=10. Sequence {10}. Result should be 1.
        assertEquals("1", Judge.run("1 10"));
    }

    
}
