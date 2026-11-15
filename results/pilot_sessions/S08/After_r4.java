package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After extends Before {
    @Test
    public void testSingleSTSubstringAtBeginning() {
        assertEquals("4", Judge.run("SSTS"));
    }

    @Test
    public void testAllSameCharWithOneSTInMiddle() {
        assertEquals("2", Judge.run("TTTSSST"));
    }

    @Test
    public void testMultipleConsecutiveSTSubstringsAndOthers() {
        assertEquals("6", Judge.run("SSSSSSTTTTT"));
    }
}
