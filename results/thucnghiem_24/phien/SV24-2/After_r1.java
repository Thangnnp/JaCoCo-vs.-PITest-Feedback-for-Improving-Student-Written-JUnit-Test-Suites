package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testExample1() {
        assertEquals("1", Judge.run("5 3 3\n1 2 4"));
    }

    @Test
    public void testExample2() {
        assertEquals("0", Judge.run("7 3 2\n4 5 6"));
    }

    @Test
    public void testExample3() {
        assertEquals("3", Judge.run("10 7 5\n1 2 3 4 6 8 9"));
    }

    @Test
    public void testCase1() {
        assertEquals("-1", Judge.run("4 2 2\n1 3"));
    }

    @Test
    public void testCase2() {
        assertEquals("0", Judge.run("5 3 2\n2 4 6"));
    }

    @Test
    public void testEdgeCase() {
        assertEquals("0", Judge.run("5 1 3\n1"));
    }
}
