package codenet;

import static org.junit.jupiter.api.Assertions.*;

import java.math.BigInteger;

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

    @Test
    void testLCMWithLargeNumbers() {
        // Test case with very large numbers to check for overflow or incorrect results
        BigInteger a = new BigInteger("1000000000000000000");
        BigInteger b = new BigInteger("2000000000000000000");
        assertEquals(BigInteger.valueOf(6), Judge.run(a + "\n" + b));
    }

    @Test
    void testLCMWithNegativeLargeNumbers() {
        // Test case with negative and very large numbers
        BigInteger a = new BigInteger("-2000000000000000000");
        BigInteger b = new BigInteger("1000000000000000000");
        assertEquals(BigInteger.valueOf(6), Judge.run(a + "\n" + b));
    }

    @Test
    void testLCMWithZeroAndLargeNumber() {
        // Test case with zero and a very large number to check for zero result
        BigInteger a = new BigInteger("1000000000000000000");
        assertEquals(BigInteger.ZERO, Judge.run("0\n" + a));
    }

    @Test
    void testLCMWithZeroAndNegativeNumber() {
        // Test case with zero and a negative number to check for zero result
        BigInteger a = new BigInteger("-1000000000000000000");
        assertEquals(BigInteger.ZERO, Judge.run("0\n" + a));
    }

    @Test
    void testLCMWithNegativeAndPositiveNumbers() {
        // Test case with negative and positive numbers to check for correct result
        BigInteger a = new BigInteger("-2000000000000000000");
        BigInteger b = new BigInteger("1000000000000000000");
        assertEquals(BigInteger.valueOf(6), Judge.run(a + "\n" + b));
    }

    @Test
    void testLCMWithNegativeAndZero() {
        // Test case with negative number and zero to check for zero result
        BigInteger a = new BigInteger("-1000000000000000000");
        assertEquals(BigInteger.ZERO, Judge.run("0\n" + a));
    }

    @Test
    void testLCMWithPositiveAndZero() {
        // Test case with positive number and zero to check for correct result
        BigInteger a = new BigInteger("1000000000000000000");
        assertEquals(BigInteger.ZERO, Judge.run("0\n" + a));
    }
}
