package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    public void testCase1() {
        String input = "2\n" +
                      "10 11\n" +
                      "11 12\n" +
                      "2\n" +
                      "N 2\n" +
                      "E 1";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void testCase2() {
        String input = "2\n" +
                      "10 11\n" +
                      "11 12\n" +
                      "2\n" +
                      "N 2\n" +
                      "W 1";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void testCase3() {
        String input = "3\n" +
                      "0 15\n" +
                      "5 10\n" +
                      "5 15\n" +
                      "5\n" +
                      "W 10\n" +
                      "S 10\n" +
                      "N 20\n" +
                      "E 10\n" +
                      "S 10";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void testCase4() {
        String input = "0";
        assertEquals("", Judge.run(input));
    }

    @Test
    public void testCase5() {
        String input = "2\n" +
                      "20 0\n" +
                      "0 20\n" +
                      "1\n" +
                      "N 40";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void testCase6() {
        String input = "2\n" +
                      "5 5\n" +
                      "5 5\n" +
                      "2\n" +
                      "S 1\n" +
                      "E 1";
        assertEquals("No", Judge.run(input));
    }

}
