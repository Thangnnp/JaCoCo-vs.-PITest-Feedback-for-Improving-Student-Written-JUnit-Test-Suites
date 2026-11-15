package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("Yes", Judge.run("4 7 9 3"));
    }

    @Test
    void test2() {
        assertEquals("No", Judge.run("100 10 1 2"));
    }

    @Test
    void test3() {
        assertEquals("Yes", Judge.run("10 10 10 1"));
    }

    @Test
    void test4() {
        assertEquals("Yes", Judge.run("1 100 2 98"));
    }

    @Test
    void test5() {
        assertEquals("No", Judge.run("3 6 10 2"));
    }

    @Test
    void test6() {
        assertEquals("Yes", Judge.run("9 7 4 3"));
    }

    @Test
    void test7() {
        assertEquals("No", Judge.run("100 50 2 25"));
    }

    @Test
    void test8() {
        assertEquals("Yes", Judge.run("3 6 9 4"));
    }
}
