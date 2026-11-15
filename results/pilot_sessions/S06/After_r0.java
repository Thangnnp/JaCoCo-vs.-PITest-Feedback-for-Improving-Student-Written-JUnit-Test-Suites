package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
import org.junit.jupiter.api.Test;

public class After {
    @Test
    public void testCase1() {
        String input = "TSTTSS";
        assertEquals("4", Judge.run(input));
    }

    @Test
    public void testCase2() {
        String input = "SSTTST";
        assertEquals("0", Judge.run(input));
    }

    @Test
    public void testCase3() {
        String input = "TSSTTTSS";
        assertEquals("4", Judge.run(input));
    }
}
