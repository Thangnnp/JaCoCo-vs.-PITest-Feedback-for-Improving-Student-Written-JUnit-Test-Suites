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
        assertEquals("957870001", Judge.run("100000 1000000000"));
    }

    @Test
    void testMIsOne() {
        assertEquals("1", Judge.run("5 1"));
    }

    @Test
    void testPrimeM() {
        assertEquals("2", Judge.run("2 7"));
    }

    @Test
    void testNIsOne() {
        // N=1, M=10. Sequence {10}. Result should be 1.
        // Also triggers ncr(cc, cc) inside Combination.
        assertEquals("1", Judge.run("1 10"));
    }

    @Test
    void testMIsPerfectSquare() {
        assertEquals("3", Judge.run("2 4"));
    }
    
    @Test
    void testNIsOneMIsPrime() {
        // N=1, M=7. Sequence {7}.
        // Triggers ncr(1, 1).
        assertEquals("1", Judge.run("1 7"));
    }

    @Test
    void testLargePrimeM() {
        // M is a large prime. 
        // 999999937 is prime.
        // N=2, M=999999937.
        // Formula: ncr(1+2-1, 1) = ncr(2, 1) = 2.
        assertEquals("2", Judge.run("2 999999937"));
    }
}
