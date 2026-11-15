package codenet;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class After {
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

    @Test
    void test7() {
        assertEquals("", Judge.run("-5 -3"));
    }

    @Test
    void test8() {
        assertEquals("9", Judge.run("2 9"));
    }

    @Test
    void test9() {
        assertEquals("4", Judge.run("4 20"));
    }

    @Test
    void test10() {
        assertEquals("-5", Judge.run("-7 -5"));
    }

    @Test
    void test11() {
        assertEquals("2", Judge.run("5 3"));
    }

    @Test
    void test12() {
        assertEquals("12", Judge.run("3 36"));
    }
}
