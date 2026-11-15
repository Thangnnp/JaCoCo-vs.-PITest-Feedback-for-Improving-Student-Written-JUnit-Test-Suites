package codenet;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class After {
    @Test
    void test7() {
        assertEquals("0", Judge.run("1 8"));
    }
    @Test
    void test8() {
        assertEquals("530123477", Judge.run("100000 100000"));
    }
    @Test
    void test9() {
        assertEquals("8", Judge.run("2 2"));
    }

    @Test
    void test10() {
        assertEquals("24", Judge.run("4 2"));
    }

    @Test
    void test11() {
        assertEquals("6", Judge.run("3 1"));
    }

    @Test
    void test12() {
        assertEquals("0", Judge.run("5 7"));
    }

    @Test
    void test13() {
        assertEquals("60", Judge.run("7 2"));
    }

    @Test
    void test14() {
        assertEquals("5040", Judge.run("9 2"));
    }

    @Test
    void test15() {
        assertEquals("362880", Judge.run("10 2"));
    }
}
