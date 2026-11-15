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
}
