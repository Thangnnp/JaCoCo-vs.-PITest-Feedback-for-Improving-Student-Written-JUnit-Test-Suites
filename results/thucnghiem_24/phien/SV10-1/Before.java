package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    void testSimpleAddition() {
        assertEquals("3", Judge.run("1 2 +"));
    }

    @Test
    void testSubtractionAndMultiplication() {
        assertEquals("-3", Judge.run("1 2 + 3 4 - *"));
    }

    @Test
    void testComplexExpression() {
        assertEquals("150", Judge.run("3 9 * 18 / 7 * 2 4 +"));
    }
}
