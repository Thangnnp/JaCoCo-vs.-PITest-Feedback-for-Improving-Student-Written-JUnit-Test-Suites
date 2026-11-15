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

    @Test
    void test7() {
        assertEquals("80", Judge.run("5 4\n-10 -20 10 20 50"));
    }

    @Test
    void test8() {
        assertEquals("-30", Judge.run("4 2\n-30 -10 10 50"));
    }

    @Test
    void test9() {
        assertEquals("60", Judge.run("5 4\n-10 -20 10 20 50"));
    }

    @Test
    void test10() {
        assertEquals("100", Judge.run("6 3\n-10 -30 10 20 50 100"));
    }

    @Test
    void test11() {
        assertEquals("-50", Judge.run("4 2\n-10 -30 10 50"));
    }

    @Test
    void test12() {
        assertEquals("90", Judge.run("6 3\n-10 -30 10 20 50 100"));
    }

    @Test
    void test13() {
        assertEquals("140", Judge.run("7 4\n-10 -20 -30 10 20 50 60"));
    }

    @Test
    void test14() {
        assertEquals("-60", Judge.run("4 2\n-10 -60 10 60"));
    }

    @Test
    void test15() {
        assertEquals("130", Judge.run("7 4\n-10 -20 -30 10 20 50 60"));
    }
}
