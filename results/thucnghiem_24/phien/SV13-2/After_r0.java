package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testRightTriangle() {
        assertEquals("YES", Judge.run("4\n3 4 5"));
    }

    @Test
    void testNotRightTriangle() {
        assertEquals("NO", Judge.run("4\n1 2 3"));
    }
}
