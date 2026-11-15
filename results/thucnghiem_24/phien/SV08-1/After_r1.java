package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.math.BigInteger;
import org.junit.jupiter.api.Test;
public class After {
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

    @Test
    public void testCase4() {
        String input = "10\n20";
        assertEquals("60", Judge.run(input));
    }

    @Test
    public void testCase5() {
        String input = "3\n6";
        assertEquals("18", Judge.run(input));
    }
}
