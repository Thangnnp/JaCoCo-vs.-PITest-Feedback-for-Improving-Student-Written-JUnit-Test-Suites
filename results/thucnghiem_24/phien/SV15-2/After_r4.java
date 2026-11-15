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
        assertEquals("1", Judge.run("1 10"));
    }

    @Test
    void testMIsPerfectSquare() {
        assertEquals("3", Judge.run("2 4"));
    }
    
    @Test
    void testNIsOneMIsPrime() {
        assertEquals("1", Judge.run("1 7"));
    }

    @Test
    void testLargePrimeM() {
        assertEquals("2", Judge.run("2 999999937"));
    }

    @Test
    void testManyPrimeFactors() {
        // M = 2 * 3 * 5 = 30. N = 2.
        assertEquals("8", Judge.run("2 30"));
    }

    @Test
    void testRepeatedPrimeFactors() {
        // M = 2^3 = 8. N = 2.
        assertEquals("4", Judge.run("2 8"));
    }

    @Test
    void testNIsLargeMIsPrime() {
        // N = 100, M = 2.
        // nCr(1 + 100 - 1, 1) = nCr(100, 1) = 100.
        assertEquals("100", Judge.run("100 2"));
    }
}
