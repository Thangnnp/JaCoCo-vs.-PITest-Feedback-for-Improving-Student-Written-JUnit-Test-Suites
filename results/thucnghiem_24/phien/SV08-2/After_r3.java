package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    void testSample1() {
        String input = "1 2 +";
        assertEquals("3", Judge.run(input));
    }

    @Test
    void testSample2() {
        String input = "1 2 + 3 4 - *";
        assertEquals("-3", Judge.run(input));
    }

    @Test
    void testEdgeCase() {
        String input = "100000";
        assertEquals("100000", Judge.run(input));
    }

    @Test
    void testNegativeNumber() {
        String input = "-1 2 -";
        try {
            Judge.run(input);
            fail("Đã không ném ngoại lệ");
        } catch (RuntimeException e) {
            assertTrue(e.getMessage().contains("java.util.NoSuchElementException"));
        }
    }

    @Test
    void testEdgeCaseLargerNumber() {
        String input = "10000000"; // Thay vì 100000
        assertEquals("10000000", Judge.run(input));
    }

    @Test
    void testInvalidOperator() {
        String input = "1 2 ?";
        try {
            Judge.run(input);
            fail("Đã không ném ngoại lệ");
        } catch (RuntimeException e) {
            assertTrue(e.getMessage().contains("Main.main ném ngo?i l?:"));
        }
    }

    @Test
    void testInvalidOperand() {
        String input = "a 2";
        try {
            Judge.run(input);
            fail("Đã không ném ngoại lệ");
        } catch (RuntimeException e) {
            assertTrue(e.getMessage().contains("Main.main ném ngo?i l?:"));
        }
    }

    // Thêm test mới:
    @Test
    void testEmptyInput() {
        String input = "";
        try {
            Judge.run(input);
            fail("Đã không ném ngoại lệ");
        } catch (RuntimeException e) {
            assertTrue(e.getMessage().contains("Main.main ném ngoại lệ:"));
        }
    }

    // Sửa test testNegativeNumber() và testInvalidOperand():
    @Test
    void testNegativeNumberValidated() {
        String input = "-1 2 -";
        try {
            Judge.run(input);
            fail("Đã không ném ngoại lệ");
        } catch (RuntimeException e) {
            assertTrue(e.getMessage().contains("Main.main ném ngo?i l?:"));
        }
    }

    @Test
    void testInvalidOperandValidated() {
        String input = "a 2";
        try {
            Judge.run(input);
            fail("Đã không ném ngoại lệ");
        } catch (RuntimeException e) {
            assertTrue(e.getMessage().contains("Main.main ném ngo?i l?:"));
        }
    }

    // Thêm test mới:
    @Test
    void testMultipleOperators() {
        String input = "1 2 + 3 4 - *";
        assertEquals("-3", Judge.run(input));
    }

    @Test
    void testLargeNumbers() {
        String input = "10000000 10000000 +";
        assertEquals("20000000", Judge.run(input));
    }

    
}
