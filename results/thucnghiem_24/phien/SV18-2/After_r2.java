package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test_case_4() {
        assertEquals("10", Judge.run("8 5\n-9 -7 -4 -3 1 2 3 4"));
    }

    @Test
    void test_case_5() {
        assertEquals("10", Judge.run("6 2\n-5 -2 0 2 5 10"));
    }

    @Test
    void test_case_6() {
        assertEquals("30", Judge.run("10 3\n-40 -20 -10 0 10 20 30 40 50 60"));
    }
}
