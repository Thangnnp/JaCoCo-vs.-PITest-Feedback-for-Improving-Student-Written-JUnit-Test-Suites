package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
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
}
