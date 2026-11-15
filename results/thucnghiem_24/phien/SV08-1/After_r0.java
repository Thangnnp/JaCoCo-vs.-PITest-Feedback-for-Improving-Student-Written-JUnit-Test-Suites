package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import java.math.BigInteger;
class After {
    @Test
    public void testCase1() {
        String input = "2\n3";
        assertEquals("6", Judge.run(input));
    }

    @Test
    public void testCase2() {
        String input = "5\n2\n5\n10\n1000000000000000000\n1000000000000000000";
        assertEquals("1000000000000000000", Judge.run(input));
    }

    @Test
    public void testCase3() {
        String input = "1\n2";
        assertEquals("2", Judge.run(input));
    }
}
