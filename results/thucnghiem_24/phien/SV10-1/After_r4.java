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
    
    @Test
    void testDivisionByZero() {
        // PITest should catch this mutation that results in a division by zero
        assertThrows(ArithmeticException.class, () -> {
            Judge.run("10 0 /");
        });
    }

    @Test
    void testNegativeOperand() {
        assertEquals("-5", Judge.run("-5"));
    }
    
    @Test
    void testSubtraction() {
        assertEquals("1", Judge.run("5 4 -"));
    }
    
    @Test
    void testLargeNumbers() {
        // PITest should catch this mutation that results in incorrect result due to integer overflow
        assertEquals((int) (2147483647L * 2), Judge.run("2147483647 2 *"));
    }
}
