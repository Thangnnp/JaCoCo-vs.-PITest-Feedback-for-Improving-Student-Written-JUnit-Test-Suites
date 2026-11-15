package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("2", Judge.run("3 24"));
    }

    @Test
    void test2() {
        assertEquals("1", Judge.run("5 1"));
    }

    @Test
    void test3() {
        assertEquals("111", Judge.run("1 111"));
    }

    @Test
    void test4() {
        assertEquals("0", Judge.run("10 123456789"));
    }

    @Test
    void test5() {
        assertEquals("1", Judge.run("1 2"));
    }

    @Test
    void test6() {
        assertEquals("0", Judge.run("1000000 1000001"));
    }
}
