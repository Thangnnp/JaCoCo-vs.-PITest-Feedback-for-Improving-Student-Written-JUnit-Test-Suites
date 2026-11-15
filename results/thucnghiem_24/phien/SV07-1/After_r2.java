package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("4", Judge.run("11009 11332"));
    }

    @Test
    void test2() {
        assertEquals("612", Judge.run("31415 92653"));
    }

    @Test
    void test3() {
        assertEquals("0", Judge.run("1 9"));
    }

    @Test
    void test4() {
        assertEquals("0", Judge.run("10000 10000"));
    }

    @Test
    void test5() {
        assertEquals("899", Judge.run("10001 99999"));
    }

    @Test
    void test6() {
        assertEquals("732", Judge.run("40000 99999"));
    }

    @Test
    void test7() {
        assertEquals("189", Judge.run("80000 99999"));
    }
}
