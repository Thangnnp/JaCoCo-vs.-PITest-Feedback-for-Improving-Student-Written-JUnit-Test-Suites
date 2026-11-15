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
        assertEquals("10", Judge.run("8 5\n-9 -7 -4 -3 1 2 3 4"));
    }

    @Test
    void test5() {
        assertEquals("60", Judge.run("10 5\n-20 -10 10 20 30 40 50 60 70 80"));
    }

    @Test
    void test6() {
        assertEquals("50", Judge.run("5 3\n-30 -10 0 20 50"));
    }

    @Test
    void test7() {
        assertEquals("60", Judge.run("10 5\n-8 -4 -2 1 3 4 9 10 20 25"));
    }

    @Test
    void test8() {
        assertEquals("70", Judge.run("5 3\n10 25 35 45 60"));
    }

    @Test
    void test9() {
        assertEquals("5", Judge.run("8 5\n-7 -4 -1 2 3 5 6 7"));
    }

    @Test
    void test10() {
        assertEquals("65", Judge.run("7 3\n-15 -8 2 3 4 5 19"));
    }

    @Test
    void test11() {
        assertEquals("40", Judge.run("4 2\n-4 -3 1 2"));
    }

    @Test
    void test12() {
        assertEquals("50", Judge.run("7 4\n-9 -8 -6 1 3 4 5"));
    }

    @Test
    void test13() {
        assertEquals("40", Judge.run("5 2\n-3 -1 1 2 4"));
    }

    @Test
    void test14() {
        assertEquals("70", Judge.run("8 4\n-9 -6 -2 2 3 4 5 6"));
    }

    @Test
    void test15() {
        assertEquals("60", Judge.run("6 3\n-7 -4 1 3 5 6"));
    }
}
