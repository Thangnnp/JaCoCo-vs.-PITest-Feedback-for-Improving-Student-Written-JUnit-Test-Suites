package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

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

    @Test
    void testSingleOperand() {
        assertEquals("5", Judge.run("5"));
    }

    @Test
    void testMultipleMultiplications() {
        assertEquals("72", Judge.run("6 3 * 4 *"));
    }
}
