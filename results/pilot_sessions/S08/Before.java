package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
    @Test
    public void testEmptyString() {
        assertEquals("0", Judge.run(""));
    }

    @Test
    public void testNoSTSubstring() {
        assertEquals("5", Judge.run("ABCD"));
    }

    @Test
    public void testSingleSTSubstring() {
        assertEquals("3", Judge.run("SSTS"));
    }
}
