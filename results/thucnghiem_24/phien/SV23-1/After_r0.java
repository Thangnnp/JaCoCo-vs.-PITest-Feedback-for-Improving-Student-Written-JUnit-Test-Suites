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

    
}
