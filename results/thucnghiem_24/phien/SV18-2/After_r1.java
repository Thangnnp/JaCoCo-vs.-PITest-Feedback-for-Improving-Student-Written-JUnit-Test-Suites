package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test_case_1() {
        assertEquals("40", Judge.run("5 3\n-30 -10 10 20 50"));
    }

    @Test
    void test_case_2() {
        assertEquals("20", Judge.run("3 2\n10 20 30"));
    }

    @Test
    void test_case_3() {
        assertEquals("0", Judge.run("1 1\n0"));
    }

    @Test
    void test_case_4() {
        assertEquals("10", Judge.run("8 5\n-9 -7 -4 -3 1 2 3 4"));
    }

    @Test
    void test_case_5() {
        assertEquals("15", Judge.run("6 2\n-5 -2 0 2 5 10"));
    }

    @Test
    void test_case_6() {
        assertEquals("50", Judge.run("10 3\n-40 -20 -10 0 10 20 30 40 50 60"));
    }
}
