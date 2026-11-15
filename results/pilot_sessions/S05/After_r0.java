package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    public void testSunny() {
        String input = "Sunny";
        String expectedOutput = "Cloudy";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    public void testCloudy() {
        String input = "Cloudy";
        String expectedOutput = "Rainy";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    public void testRainy() {
        String input = "Rainy";
        String expectedOutput = "Sunny";
        assertEquals(expectedOutput, Judge.run(input));
    }
}
