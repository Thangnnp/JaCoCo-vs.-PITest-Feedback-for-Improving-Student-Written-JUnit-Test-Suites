package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class Before {
    @Test
    public void testCase1() {
        String input = "3 24";
        assertEquals("2", Judge.run(input));
    }

    @Test
    public void testCase2() {
        String input = "5 1";
        assertEquals("1", Judge.run(input));
    }

    @Test
    public void testCase3() {
        String input = "1 111";
        assertEquals("111", Judge.run(input));
    }
}
