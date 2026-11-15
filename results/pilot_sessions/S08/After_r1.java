package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After extends Before {
    @Test
    public void testMultipleSTSubstrings() {
        assertEquals("2", Judge.run("SSSTTT"));
    }

    @Test
    public void testAdjacentSTSubstring() {
        assertEquals("1", Judge.run("TST"));
    }

    @Test
    public void testOneSTAtEnd() {
        assertEquals("0", Judge.run("TS"));
    }
}
