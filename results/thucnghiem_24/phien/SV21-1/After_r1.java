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

    @Test
    public void testCaseAAndCCannotCommunicate() {
        String input = "100 0 101 1";
        String expectedOutput = "No";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    public void testEdgeCaseADistantFromCButABandBCCanBeCommunicate() {
        String input = "99 100 2 3";
        String expectedOutput = "Yes";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    public void testCaseAIsAtTheSamePositionAsBAndCCannotCommunicate() {
        String input = "10 10 11 1";
        String expectedOutput = "No";
        assertEquals(expectedOutput, Judge.run(input));
    }
}
