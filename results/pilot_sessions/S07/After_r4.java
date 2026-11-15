package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testSunny() {
        assertEquals("Cloudy", Judge.run("Sunny"));
    }

    @Test
    void testRainy() {
        assertEquals("Sunny", Judge.run("Rainy"));
    }

    @Test
    void testCloudy() {
        assertEquals("Rainy", Judge.run("Cloudy"));
    }

    @Test
    void testNoInput() {
        assertEquals("", Judge.run(""));
    }

    @Test
    void testCaseInsensitive() {
        assertEquals("Cloudy", Judge.run("sunny"));
        assertEquals("Sunny", Judge.run("SUNNY"));
        assertEquals("Rainy", Judge.run("rainy"));
        assertEquals("Cloudy", Judge.run("cloudy"));
    }

    @Test
    void testInvalidInput() {
        assertNull(Judge.run(null)); // Test null input
        assertNull(Judge.run("invalid")); // Test invalid input
    }

    @Test
    void testMultipleConsecutiveInputs() {
        assertEquals("Cloudy", Judge.run("Sunny\nRainy\nCloudy"));
    }

    @Test
    void testLineCoverage() {
        assertNotEquals("", Judge.run("\n\n")); // Test empty line
        assertNotEquals("", Judge.run(" \t ")); // Test whitespace-only input
    }
}
