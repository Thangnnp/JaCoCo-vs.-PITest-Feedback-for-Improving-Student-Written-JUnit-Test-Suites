package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After extends Before {
    @Test
    public void testSingleSTSubstringAtStart() {
        assertEquals("3", Judge.run("SSTS"));
    }

    @Test
    public void testAllSameChar() {
        assertEquals("0", Judge.run("TTTSSS"));
    }

    @Test
    public void testOneSTAtBeginningAndEnd() {
        assertEquals("1", Judge.run("TTS"));
    }
}
