package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testSunny() {
        assertEquals("Cloudy", Judge.run("Sunny"));
    }

    @Test
    public void testCloudy() {
        assertEquals("Rainy", Judge.run("Cloudy"));
    }

    @Test
    public void testRainy() {
        assertEquals("Sunny", Judge.run("Rainy"));
    }

    @Test
    public void testEmptyInput() {
        assertThrows(RuntimeException.class, () -> Judge.run(""));
    }

    @Test
    public void testInvalidInput() {
        assertThrows(RuntimeException.class, () -> Judge.run("Invalid"));
    }

    @Test
    public void testNullInput() {
        assertThrows(RuntimeException.class, () -> Judge.run(null));
    }
}
