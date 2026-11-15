package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
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
}
