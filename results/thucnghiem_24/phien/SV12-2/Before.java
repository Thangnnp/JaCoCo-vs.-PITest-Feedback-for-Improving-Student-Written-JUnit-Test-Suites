package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
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
}
