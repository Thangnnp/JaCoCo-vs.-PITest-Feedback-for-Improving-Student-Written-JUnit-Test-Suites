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
}
