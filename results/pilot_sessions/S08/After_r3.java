package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After extends Before {
    @Test
    public void testSingleSTSubstringAtEnd() {
        assertEquals("2", Judge.run("TSTS"));
    }

    @Test
    public void testEmptyStringWithOneST() {
        assertEquals("0", Judge.run("S"));
    }

    @Test
    public void testMultipleConsecutiveSTSubstrings() {
        assertEquals("4", Judge.run("SSSSSTTTT"));
    }
}
