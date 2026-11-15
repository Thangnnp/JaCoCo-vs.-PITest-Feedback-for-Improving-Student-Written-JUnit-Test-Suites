package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
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
}
