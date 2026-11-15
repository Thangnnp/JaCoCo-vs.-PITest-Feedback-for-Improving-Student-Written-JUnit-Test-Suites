package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    void test1() {
        String input = "3 4 5";
        String expectedOutput = "YES";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    void test2() {
        String input = "3 4 6";
        String expectedOutput = "NO";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    void test3() {
        String input = "8 8 8";
        String expectedOutput = "NO";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    void test4() {
        String input = "1 2 3\n";
        String expectedOutput = "YES";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    void test5() {
        String input = "9 10 11\n";
        String expectedOutput = "NO";
        assertEquals(expectedOutput, Judge.run(input));
    }

    @Test
    void test6() {
        String input = "1000 1 1\n";
        String expectedOutput = "YES";
        assertEquals(expectedOutput, Judge.run(input));
    }
}
