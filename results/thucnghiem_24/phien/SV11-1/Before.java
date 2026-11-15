package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.Scanner;
import org.junit.jupiter.api.Test;

public class Before {
    @Test
    public void test1() {
        String input = "2\n10 11\n11 12\n2\nN 3";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void test2() {
        String input = "2\n0 15\n5 10\n5 15\n5\nW 20";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void test3() {
        String input = "1\n10 11\n2\nN 1";
        assertEquals("Yes", Judge.run(input));
    }
}
