package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

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
}
