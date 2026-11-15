package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testSampleInput1() {
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    public void testSampleInput2() {
        assertEquals("18", Judge.run("3 12"));
    }

    @Test
    public void testSmallPrimeFactorization() {
        assertEquals("6", Judge.run("5 30"));
    }
    
    @Test
    public void testLargeInput() {
        assertEquals("957870001", Judge.run("100000 1000000000"));
    }

    @Test
    public void testEdgeCase1() {
        assertEquals("1", Judge.run("1 1"));
    }

    @Test
    public void testEdgeCase2() {
        assertEquals("2", Judge.run("2 2"));
    }
}
