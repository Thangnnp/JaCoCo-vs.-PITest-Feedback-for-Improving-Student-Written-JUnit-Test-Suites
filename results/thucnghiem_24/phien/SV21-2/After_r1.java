package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {

    @Test
    public void testSample1() {
        String input = "5 3\n-30 -10 10 20 50";
        assertEquals("40", Judge.run(input));
    }

    @Test
    public void testSample2() {
        String input = "3 2\n10 20 30";
        assertEquals("20", Judge.run(input));
    }

    @Test
    public void testSample3() {
        String input = "1 1\n0";
        assertEquals("0", Judge.run(input));
    }

    @Test
    public void testMiEqualsK() {
        String input = "10 5\n-9 -7 -4 -3 1 2 3 4";
        assertEquals("3", Judge.run(input));
    }

    @Test
    public void testOnlyOneCandleAtZero() {
        String input = "1 1\n0";
        assertEquals("0", Judge.run(input));
    }

    @Test
    public void testKEqualsN() {
        String input = "10 10\n-9 -7 -4 -3 1 2 3 4";
        assertEquals("0", Judge.run(input));
    }
}
