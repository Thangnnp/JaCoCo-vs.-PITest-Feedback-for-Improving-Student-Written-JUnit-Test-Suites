package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testLargeInput() {
        assertEquals("1000000000000000000", Judge.run("2\n" +
                "1000000000000000000\n" +
                "1000000000000000000"));
    }

    @Test
    public void testEdgeCase() {
        assertEquals("1", Judge.run("2\n1\n1"));
    }

    @Test
    public void testManyClocks() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 50; i++) {
            input.append(i).append("\n");
        }
        assertEquals(39867475, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks2() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 100; i++) {
            input.append(i).append("\n");
        }
        assertEquals(4950, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks3() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 200; i++) {
            input.append(i).append("\n");
        }
        assertEquals(9950, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks4() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 250; i++) {
            input.append(i).append("\n");
        }
        assertEquals(30675, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks5() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 500; i++) {
            input.append(i).append("\n");
        }
        assertEquals(124750, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks6() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 1000; i++) {
            input.append(i).append("\n");
        }
        assertEquals(500500, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks7() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 2000; i++) {
            input.append(i).append("\n");
        }
        assertEquals(2001000, Long.parseLong(Judge.run(input.toString())));
    }

    @Test
    public void testManyClocks8() {
        StringBuilder input = new StringBuilder();
        for (int i = 1; i <= 3000; i++) {
            input.append(i).append("\n");
        }
        assertEquals(4501500, Long.parseLong(Judge.run(input.toString())));
    }
}
