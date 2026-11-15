package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
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
    
    
}
