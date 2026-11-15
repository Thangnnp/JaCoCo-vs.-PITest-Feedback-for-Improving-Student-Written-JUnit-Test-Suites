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
        // Case: No connection between routers
        String input = "2\n" +
                       "1 0\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("NA", Judge.run(input));
    }

    @Test
    void testTTLBoundary() {
        // Case: TTL constraints
        // Path 1->2 (length 1). 
        // TTL 1: 1->2 (hop 1, TTL becomes 0), valid? 
        // Actually, inside the loop: if(now.ttl-1<=0) continue;
        // So at node 1, ttl=1, ttl-1=0. Loop continues. Cannot forward.
        // Wait, the logic is: "宛先ルータでは TTL を減算する必要はありません".
        // The code checks (j == d) first.
        // My manual trace: 1->2, cost 1. Packet(1, 2, 1).
        // 1. open(1, 1, 1). 
        // 2. Poll(1, 1, 1). now.ttl(1)-1 <= 0? Yes, skip forward.
        // 3. Wait, the loop `for(int j=1; j<=N; j++)` checks neighbor.
        // If j==d, we set ans.
        // My test result for TTL=1 shows NA because the code logic skips forwarding if ttl-1 <= 0.
        // Let's verify this behavior.
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "2\n" +
                       "1 2 1\n" +
                       "1 2 2";
        // With TTL=1, packet 1->2: The destination 2 is a neighbor.
        // The loop finds j=2 (which is d). ans becomes 1. 
        // The check `if(now.ttl-1<=0)` happens *after* polling.
        // If I am at 1, TTL 1, I find 2. I set ans=1. 
        // Then I try to add to open queue? No, if j==d, I continue to next neighbor.
        // So actually, TTL=1 *should* work for 1-hop distance.
        // My previous expectation of NA might have been wrong if my understanding of the code's `if(j==d)` is right.
        // Let's test with the actual code behavior.
        assertEquals("1\n1", Judge.run(input));
    }

    @Test
    void testTTLStrictness() {
        // Path 1->2->3. Length 2.
        // TTL 1: 1->2 (hop 1), now at 2 with TTL 0. 
        // From 2, we need to go to 3. But TTL 0 <= 0, so cannot forward.
        // Result should be NA.
        // TTL 2: 1->2 (hop 1, TTL 1), 2->3 (hop 2, TTL 0). Success.
        String input = "3\n" +
                       "1 1 2\n" +
                       "2 1 3\n" +
                       "3 0\n" +
                       "2\n" +
                       "1 3 1\n" +
                       "1 3 2";
        assertEquals("NA\n2", Judge.run(input));
    }

    @Test
    void testPathOptimization() {
        // Multiple paths: 1->2 (cost 1), 1->3->2 (cost 2).
        // Dijkstra should pick cost 1.
        String input = "3\n" +
                       "1 2 2 3\n" +
                       "2 1 3\n" +
                       "3 1 2\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("1", Judge.run(input));
    }
    
    @Test
    void testDisconnectedComponent() {
        // 1->2, 3->4. Packet 1->4.
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
