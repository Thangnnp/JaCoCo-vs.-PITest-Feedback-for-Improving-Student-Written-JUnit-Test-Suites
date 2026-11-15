package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testSingleClock() {
        assertEquals("2", Judge.run("1\n2"));
    }

    @Test
    public void testTwoClocks() {
        assertEquals("6", Judge.run("2\n2\n3"));
    }

    @Test
    public void testThreeClocks() {
        assertEquals("30", Judge.run("3\n5\n10\n15"));
    }

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
        assertEquals("39867475", Judge.run(input.toString()));
    }
}
