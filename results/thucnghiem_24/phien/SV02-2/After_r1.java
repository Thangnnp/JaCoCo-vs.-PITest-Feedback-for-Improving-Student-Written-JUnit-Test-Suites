package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    public void test1() {
        assertEquals("4", Judge.run("11009 11332"));
    }

    @Test
    public void test2() {
        assertEquals("612", Judge.run("31415 92653"));
    }

    @Test
    public void test3() {
        assertEquals("0", Judge.run("10000 10000"));
    }

    @Test
    public void test4() {
        assertEquals("1", Judge.run("11001 11002"));
    }

    @Test
    public void test5() {
        assertEquals("9", Judge.run("11111 11119"));
    }

    @Test
    public void test6() {
        assertEquals("0", Judge.run("99999 100000"));
    }
}
