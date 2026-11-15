package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.NoSuchElementException;
import org.junit.jupiter.api.Test;

public class After {
    @Test
    public void testEmptyString() {
        String input = "";
        assertThrows(RuntimeException.class, () -> Judge.run(input));
    }

    @Test
    public void testInvalidInput() {
        String input = "Invalid";
        try {
            Judge.run(input);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // Expected exception thrown
        }
    }

    @Test
    public void testNullInput() {
        String input = null;
        try {
            Judge.run(input);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            // Expected exception thrown
        }
    }

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
