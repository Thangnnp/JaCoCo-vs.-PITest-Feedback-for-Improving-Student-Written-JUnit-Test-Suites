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

    @Test
    public void testCase3() {
        assertEquals("-1", Judge.run("2 1 0\n1 0"));
    }

    @Test
    public void testCase4() {
        assertEquals("0", Judge.run("6 2 5\n3 5"));
    }

    @Test
    public void testCase5() {
        assertEquals("-1", Judge.run("7 3 2\n2 4 6"));
    }

    @Test
    public void testCase6() {
        assertEquals("0", Judge.run("8 3 5\n1 2 4 7"));
    }

    @Test
    public void testCase7() {
        assertEquals("-1", Judge.run("9 2 4\n1 3 5"));
    }

    @Test
    public void testCase8() {
        assertEquals("0", Judge.run("10 6 5\n1 2 3 4 6 8 9 7"));
    }
}
