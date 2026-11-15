package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    public void testSingleGem() {
        String input = "1\n5 5\n2\nN 5";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void testMultipleGems() {
        String input = "3\n0 0\n10 10\n20 20\n4\nN 10 E 10";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void testAllGemsCollected() {
        String input = "2\n5 5\n15 15\n4\nN 5 E 10 S 10";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void testNoInput() {
        String input = "";
        assertThrows(RuntimeException.class, () -> Judge.run(input));
    }

    @Test
    public void testInvalidInputFormat() {
        String input = "5\n1 1\n2 2\n3 3";
        assertThrows(RuntimeException.class, () -> Judge.run(input));
    }

    @Test
    public void testNegativeGemCoordinates() {
        String input = "-1\n-1 -1";
        assertThrows(RuntimeException.class, () -> Judge.run(input));
    }

    @Test
    public void testGemsOutsideRange() {
        String input = "2\n25 25\n-5 -5\n4\nN 5 E 10 S 10";
        assertThrows(RuntimeException.class, () -> Judge.run(input));
    }
}
