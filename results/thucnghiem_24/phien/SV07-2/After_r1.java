package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("YES", Judge.run("3\n4 3 5"));
    }

    @Test
    void test2() {
        assertEquals("NO", Judge.run("3\n4 3 6"));
    }

    @Test
    void test3() {
        assertEquals("NO", Judge.run("3\n8 8 8"));
    }

    @Test
    void test4() {
        assertEquals("YES", Judge.run("3\n5 12 13"));
    }

    @Test
    void test5() {
        assertEquals("NO", Judge.run("3\n6 8 10"));
    }
}
