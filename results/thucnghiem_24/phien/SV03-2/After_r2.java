package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void test1() {
        assertEquals("3", Judge.run("1 2 +"));
    }

    @Test
    void test2() {
        assertEquals("-3", Judge.run("1 2 + 3 4 - *"));
    }

    @Test
    void test3() {
        assertEquals("1000000000", Judge.run("1000000000"));
    }

    @Test
    void test4() {
        assertEquals("9", Judge.run("1 3 + 5 6 * + "));
    }

    @Test
    void test5() {
        assertEquals("-7", Judge.run("2 4 - 3 5 - +"));
    }

    @Test
    void test6() {
        assertEquals("8", Judge.run("3 5 + 2 7 + -"));
    }

    @Test
    void test7() {
        assertEquals("1000000001", Judge.run("100000001 0 "));
    }

    @Test
    void test8() {
        assertEquals("-9", Judge.run("0 0 +  9"));
    }

    @Test
    void test9() {
        assertEquals("13", Judge.run("10 2 + 1"));
    }
}
