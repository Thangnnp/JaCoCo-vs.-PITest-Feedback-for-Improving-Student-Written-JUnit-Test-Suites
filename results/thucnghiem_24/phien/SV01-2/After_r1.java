package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    void test1() {
        String input = "2 2";
        assertEquals("8", Judge.run(input));
    }

    @Test
    void test2() {
        String input = "3 2";
        assertEquals("12", Judge.run(input));
    }

    @Test
    void test3() {
        String input = "1 8";
        assertEquals("0", Judge.run(input));
    }

    @Test
    void test4() {
        String input = "10 20";
        assertEquals("0", Judge.run(input));
    }

    @Test
    void test5() {
        String input = "200000 10000";
        assertEquals("0", Judge.run(input));
    }
}
