package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("4", Judge.run("TSTTSS"));
    }

    @Test
    void test2() {
        assertEquals("0", Judge.run("SSTTST"));
    }

    @Test
    void test3() {
        assertEquals("4", Judge.run("TSSTTTSS"));
    }

    @Test
    void test4() {
        assertEquals("200000", Judge.run("S".repeat(100000) + "T".repeat(100000)));
    }

    @Test
    void test5() {
        assertEquals("6", Judge.run("STSSTS"));
    }

    @Test
    void test6() {
        assertEquals("2", Judge.run("SSSTTT"));
    }

    @Test
    void test7() {
        assertEquals("0", Judge.run("ST".repeat(10000)));
    }

    @Test
    void test8() {
        assertEquals("2", Judge.run("TSSSST"));
    }

    @Test
    void test9() {
        assertEquals("0", Judge.run("ST".repeat(5000)));
    }

    @Test
    void test10() {
        assertEquals("2", Judge.run("TSSTSSTTSS"));
    }

    @Test
    void test11() {
        assertEquals("4", Judge.run("TSTTSSSTTTSS"));
    }

    @Test
    void test12() {
        assertEquals("0", Judge.run("S".repeat(5000) + "T".repeat(5000)));
    }
}
