package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void sunny() {
        assertEquals("Cloudy", Judge.run("Sunny"));
    }

    @Test
    void cloudy() {
        assertEquals("Rainy", Judge.run("Cloudy"));
    }

    @Test
    void rainy() {
        assertEquals("Sunny", Judge.run("Rainy"));
    }
}
