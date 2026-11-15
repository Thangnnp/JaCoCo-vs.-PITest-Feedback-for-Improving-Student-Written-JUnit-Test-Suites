package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

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
        String input = "2\n" +
                       "1 0\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("NA", Judge.run(input));
    }

    @Test
    void testTTLBoundary() {
        // Logic: 1->2 distance 1. TTL=1. 
        // Decrement at 1: 1->0. Packet arrives at 2 with TTL=0.
        // Problem states: "宛先ルータでは TTL を減算する必要はありません" (No decrement at destination).
        // So TTL=1 should be sufficient to reach the destination.
        // This test exposes the bug where the code prematurely skips nodes with TTL=1.
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 1";
        assertEquals("1", Judge.run(input));
    }

    @Test
    void testTTLStrictness() {
        // Path 1->2->3. Distance 2. TTL=2.
        // 1->2 (TTL 2->1), 2->3 (TTL 1->0). Arrives at 3.
        String input = "3\n" +
                       "1 1 2\n" +
                       "2 1 3\n" +
                       "3 0\n" +
                       "1\n" +
                       "1 3 2";
        assertEquals("2", Judge.run(input));
    }

    @Test
    void testPathOptimization() {
        // Dijkstra check: 1->2 (cost 1) vs 1->3->2 (cost 2).
        // Expected: 1
        String input = "3\n" +
                       "1 2 2 3\n" +
                       "2 0\n" +
                       "3 1 2\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("1", Judge.run(input));
    }
    
    @Test
    void testDisconnectedComponent() {
        String input = "4\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "3 1 4\n" +
                       "4 0\n" +
                       "1\n" +
                       "1 4 10";
        assertEquals("NA", Judge.run(input));
    }
}
