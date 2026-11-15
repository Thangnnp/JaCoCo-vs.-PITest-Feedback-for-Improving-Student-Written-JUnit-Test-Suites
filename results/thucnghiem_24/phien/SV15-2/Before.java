package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    void testSample1() {
        // N=2, M=6. Prime factors: 2^1, 3^1. 
        // Ways for 2^1 in 2 pos: C(1+2-1, 1) = C(2,1) = 2.
        // Ways for 3^1 in 2 pos: C(1+2-1, 1) = C(2,1) = 2.
        // Total: 2 * 2 = 4. Correct.
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    void testSample2() {
        // N=3, M=12. Prime factors: 2^2, 3^1.
        // For 2^2 (e=2, n=3): C(2+3-1, 2) = C(4,2) = 6.
        // For 3^1 (e=1, n=3): C(1+3-1, 1) = C(3,1) = 3.
        // Total: 6 * 3 = 18. Correct.
        assertEquals("18", Judge.run("3 12"));
    }

    @Test
    void testMIsOne() {
        // N=5, M=1.
        // M=1, prime factors map is empty. Loop won't run, ans = 1.
        // There is only one sequence {1, 1, 1, 1, 1}.
        assertEquals("1", Judge.run("5 1"));
    }

    
}
