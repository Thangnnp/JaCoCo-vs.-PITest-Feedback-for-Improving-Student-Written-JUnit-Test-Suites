package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    void testSample() {
        String input = "7\n" +
                       "1 4 2 5 4 3\n" +
                       "2 1 5\n" +
                       "3 1 6\n" +
                       "4 1 7\n" +
                       "5 2 7 6\n" +
                       "6 1 1\n" +
                       "7 0\n" +
                       "6\n" +
                       "1 2 2\n" +
                       "1 5 3\n" +
                       "1 2 1\n" +
                       "5 1 3\n" +
                       "6 3 3\n" +
                       "1 7 4";
        String expected = "2\n2\nNA\n3\n3\n3";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testNoPath() {
        // 2 routers, no connections between them.
        // Input: N=2, R1=1(0 neighbors), R2=2(0 neighbors), 1 packet (1->2, TTL=10)
        String input = "2\n" +
                       "1 0\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("NA", Judge.run(input));
    }

    @Test
    void testTTLBoundary() {
        // 2 routers connected 1->2. Distance is 2 (nodes 1, 2).
        // Packet 1: 1->2, TTL=1. Router 1 decrements 1->0. Packet should be discarded (NA).
        // Packet 2: 1->2, TTL=2. Router 1 decrements 2->1. Packet arrives at 2 (ans 2).
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "2\n" +
                       "1 2 1\n" +
                       "1 2 2";
        assertEquals("NA\n2", Judge.run(input));
    }
}
