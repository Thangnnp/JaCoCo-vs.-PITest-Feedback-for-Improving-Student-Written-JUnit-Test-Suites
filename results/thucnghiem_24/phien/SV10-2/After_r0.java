package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testSingleClock() {
        assertEquals("2", Judge.run("1\n2"));
    }

    @Test
    public void testTwoClocks() {
        assertEquals("6", Judge.run("2\n2\n3"));
    }

    @Test
    public void testThreeClocks() {
        assertEquals("30", Judge.run("3\n5\n10\n15"));
    }
}
