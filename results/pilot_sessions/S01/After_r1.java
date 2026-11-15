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
}
