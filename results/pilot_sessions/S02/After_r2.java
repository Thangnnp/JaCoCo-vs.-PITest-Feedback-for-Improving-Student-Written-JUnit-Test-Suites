package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void sunny2() {
        assertEquals("Cloudy", Judge.run("Sunny"));
    }

    @Test
    void cloudy2() {
        assertEquals("Rainy", Judge.run("Cloudy"));
    }

    @Test
    void rainy2() {
        assertEquals("Sunny", Judge.run("Rainy"));
    }

    @Test
    void sunny3() {
        assertEquals("Cloudy", Judge.run("Sunny"));
    }

    @Test
    void cloudy3() {
        assertEquals("Rainy", Judge.run("Cloudy"));
    }

    @Test
    void rainy3() {
        assertEquals("Sunny", Judge.run("Rainy"));
    }

    @Test
    void sunny4() {
        assertEquals("Cloudy", Judge.run("Sunny"));
    }

    @Test
    void cloudy4() {
        assertEquals("Rainy", Judge.run("Cloudy"));
    }

    @Test
    void rainy4() {
        assertEquals("Sunny", Judge.run("Rainy"));
    }
}
