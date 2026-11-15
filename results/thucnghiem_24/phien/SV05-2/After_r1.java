package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testLCM() {
        assertEquals(BigInteger.valueOf(6), Judge.run("2\n3"));
        assertEquals(BigInteger.valueOf(18), Judge.run("4\n5\n6"));
    }

    @Test
    void testLCMWithNegativeNumbers() {
        // Test case with negative numbers
        assertEquals(BigInteger.valueOf(6), Judge.run("-2\n-3"));
        assertEquals(BigInteger.valueOf(-18), Judge.run("-4\n-5\n-6"));
    }

    @Test
    void testLCMWithZero() {
        // Test case with zero
        assertEquals(BigInteger.ZERO, Judge.run("0\n1"));
        assertEquals(BigInteger.ZERO, Judge.run("2\n0"));
        assertEquals(BigInteger.ZERO, Judge.run("0\n3"));
    }
}
