package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void test1() {
        assertEquals("0", Judge.run("5 3 3\n1 2 4"));
    }

    @Test
    void test2() {
        assertEquals("0", Judge.run("7 3 2\n4 5 6"));
    }

    @Test
    void test3() {
        assertEquals("3", Judge.run("10 7 5\n1 2 3 4 6 8 9"));
    }

    @Test
    void test4() {
        assertEquals("1", Judge.run("6 1 3\n4"));
    }

    @Test
    void test5() {
        assertEquals("1", Judge.run("7 1 3\n5"));
    }

    @Test
    void test6() {
        assertEquals("2", Judge.run("8 2 5\n3 7"));
    }

    @Test
    void test7() {
        assertEquals("0", Judge.run("4 1 2\n3"));
    }

    @Test
    void test8() {
        assertEquals("1", Judge.run("6 1 4\n3"));
    }

    @Test
    void test9() {
        assertEquals("1", Judge.run("7 1 5\n4"));
    }
}
