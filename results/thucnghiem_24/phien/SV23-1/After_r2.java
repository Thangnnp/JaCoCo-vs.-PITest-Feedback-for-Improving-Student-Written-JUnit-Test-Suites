package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void testSample1() {
        // N=3, P=24. 24 = 2^3 * 3^1. GCD power for 2: 3/3=1. GCD power for 3: 1/3=0. Ans: 2^1 * 3^0 = 2.
        assertEquals("2", Judge.run("3 24"));
    }

    @Test
    void testBoundaryN1() {
        // Sample 3: N=1, P=111. GCD should be P itself.
        assertEquals("111", Judge.run("1 111"));
    }

    @Test
    void testLargeN() {
        // N is very large, P is smaller than 2^N. GCD must be 1.
        // N=10^12, P=10^12.
        assertEquals("1", Judge.run("1000000000000 1000000000000"));
    }

    @Test
    void testPerfectPower() {
        // P = 10^9, N = 2.
        // 10^9 = 2^9 * 5^9. 
        // exponent/N = 9/2 = 4. 
        // GCD = 2^4 * 5^4 = 10^4 = 10000.
        assertEquals("10000", Judge.run("2 1000000000"));
    }

    @Test
    void testSample2() {
        // Sample 2: N=5, P=1. GCD must be 1.
        assertEquals("1", Judge.run("5 1"));
    }

    @Test
    void testPrimeP() {
        // P is a large prime, N=1. Ans: P.
        // P is a large prime, N=2. Ans: 1.
        assertEquals("999999999989", Judge.run("1 999999999989"));
        assertEquals("1", Judge.run("2 999999999989"));
    }

    @Test
    void testSquareNumber() {
        // P = 121 (11^2), N = 2. Ans: 11.
        assertEquals("11", Judge.run("2 121"));
    }

    @Test
    void testSample4() {
        // Sample 4: 4 972439611840
        assertEquals("206", Judge.run("4 972439611840"));
    }
    
    @Test
    void testExponentZero() {
        // N=10, P=2^5 * 3^5. exponents are 5. 5/10 = 0. Ans: 1.
        assertEquals("1", Judge.run("10 7776"));
    }

    

    

    
}
