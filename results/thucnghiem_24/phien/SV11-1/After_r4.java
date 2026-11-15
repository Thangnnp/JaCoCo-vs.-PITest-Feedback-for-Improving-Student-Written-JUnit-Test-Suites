package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.Scanner;
import org.junit.jupiter.api.Test;

public class After {
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

    @Test
    public void test4() {
        String input = "0";
        assertEquals("", Judge.run(input));
    }

    @Test
    public void test5() {
        String input = "1\n10 11\n2\nS 3";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void test6() {
        String input = "2\n10 11\n11 12\n2\nE 3";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void test7() {
        String input = "1\n0 0\n2\nN 20";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void test8() {
        String input = "1\n10 11\n2\nE 10";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void test9() {
        String input = "2\n5 0\n15 20\n2\nW 3";
        assertEquals("No", Judge.run(input));
    }

    @Test
    public void test10() {
        String input = "1\n5 15\n2\nS 20";
        assertEquals("Yes", Judge.run(input));
    }

    @Test
    public void test11() {
        String input = "3\n0 0\n10 10\n20 20\n3\nN 10";
        assertEquals("No", Judge.run(input));
    }
}
