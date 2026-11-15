package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testSinglePalindrome() {
        assertEquals("1", Judge.run("100 111"));
    }

    @Test
    public void testRangeWithNoPalindromes() {
        assertEquals("0", Judge.run("1234 5678"));
    }

    @Test
    public void testFullRangeOfPalindromes() {
        assertEquals("90", Judge.run("100 190"));
    }

    @Test
    public void testEdgeCaseA() {
        assertEquals("0", Judge.run("1000 1002"));
    }

    @Test
    public void testEdgeCaseB() {
        assertEquals("1", Judge.run("1000 1003"));
    }

    @Test
    public void testLargeRange() {
        assertEquals("8915", Judge.run("10000 20000"));
    }
}
