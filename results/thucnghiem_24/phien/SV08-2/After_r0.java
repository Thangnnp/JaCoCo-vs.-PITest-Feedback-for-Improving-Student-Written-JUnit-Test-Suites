package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    void testSample1() {
        String input = "1 2 +";
        assertEquals("3", Judge.run(input));
    }

    @Test
    void testSample2() {
        String input = "1 2 + 3 4 - *";
        assertEquals("-3", Judge.run(input));
    }

    @Test
    void testEdgeCase() {
        String input = "100000";
        assertEquals("100000", Judge.run(input));
    }
}
