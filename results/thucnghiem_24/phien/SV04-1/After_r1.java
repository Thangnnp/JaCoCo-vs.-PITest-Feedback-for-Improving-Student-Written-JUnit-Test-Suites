package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void test1() {
        assertEquals("40", Judge.run("5 3\n-30 -10 10 20 50"));
    }
    
    @Test
    void test2() {
        assertEquals("20", Judge.run("3 2\n10 20 30"));
    }
    
    @Test
    void test3() {
        assertEquals("0", Judge.run("1 1\n0"));
    }

    @Test
    void test4() {
        assertEquals("10", Judge.run("8 5\n-9 -7 -4 -3 1 2 3 4"));
    }

    @Test
    void test5() {
        assertEquals("60", Judge.run("10 5\n-20 -10 10 20 30 40 50 60 70 80"));
    }

    @Test
    void test6() {
        assertEquals("50", Judge.run("5 3\n-30 -10 0 20 50"));
    }
}
