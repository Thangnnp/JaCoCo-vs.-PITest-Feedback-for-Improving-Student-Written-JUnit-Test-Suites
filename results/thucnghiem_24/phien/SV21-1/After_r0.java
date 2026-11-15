package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    public void testIndirectCommunication() {
        String input = "4 7 9 3";
        String expectedOutput = "Yes";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    public void testDirectCommunication() {
        String input = "100 10 1 2";
        String expectedOutput = "No";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    public void testMultiplePeopleAtSamePosition() {
        String input = "10 10 10 1";
        String expectedOutput = "Yes";
        assertEquals(expectedOutput, Judge.run(input));
    }
}
