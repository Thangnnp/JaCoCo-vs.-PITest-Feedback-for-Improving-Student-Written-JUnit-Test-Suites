package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
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
}
