package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("40", Judge.run("5 3\n-30 -10 10 20 50"));
    }

    @Test
    void test2() {
        assertEquals("20", Judge.run("3 2\n10 20 30"));
    }

    @Test
    void test3() {
        assertEquals("0", Judge.run("1 1\n0"));
    }

    @Test
    void test4() {
        assertEquals("50", Judge.run("6 3\n-30 -10 10 20 50 50"));
    }

    @Test
    void test5() {
        assertEquals("-10", Judge.run("3 1\n-10 10 20"));
    }

    @Test
    void test6() {
        assertEquals("40", Judge.run("4 3\n-30 -10 10 50"));
    }
}
