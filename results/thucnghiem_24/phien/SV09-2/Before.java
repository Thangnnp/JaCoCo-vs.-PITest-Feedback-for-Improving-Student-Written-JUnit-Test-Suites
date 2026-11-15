package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    void testSample1() {
        // N=5, M=3, X=3
        // Gates: 1, 2, 4
        // Left of 3: {1, 2} -> count 2
        // Right of 3: {4} -> count 1
        // Min(2, 1) = 1
        assertEquals("1", Judge.run("5 3 3\n1 2 4"));
    }

    @Test
    void testSample2() {
        // N=7, M=3, X=2
        // Gates: 4, 5, 6
        // Left of 2: {} -> count 0
        // Right of 2: {4, 5, 6} -> count 3
        // Min(0, 3) = 0
        assertEquals("0", Judge.run("7 3 2\n4 5 6"));
    }

    @Test
    void testSample3() {
        // N=10, M=7, X=5
        // Gates: 1, 2, 3, 4, 6, 8, 9
        // Left of 5: {1, 2, 3, 4} -> count 4
        // Right of 5: {6, 8, 9} -> count 3
        // Min(4, 3) = 3
        assertEquals("3", Judge.run("10 7 5\n1 2 3 4 6 8 9"));
    }

    
}
