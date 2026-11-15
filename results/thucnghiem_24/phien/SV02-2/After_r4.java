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

    @Test
    public void test7() {
        assertEquals("1", Judge.run("11009 11009"));
    }

    @Test
    public void test8() {
        assertEquals("1", Judge.run("11010 11010"));
    }

    @Test
    public void test9() {
        assertEquals("3", Judge.run("11008 11012"));
    }

    @Test
    public void test10() {
        assertEquals("4", Judge.run("11111 11332"));
    }

    @Test
    public void test11() {
        assertEquals("610", Judge.run("31413 92653"));
    }

    @Test
    public void test12() {
        assertEquals("0", Judge.run("99999 10000"));
    }

    @Test
    public void test13() {
        assertEquals("1", Judge.run("11009 11111"));
    }

    @Test
    public void test14() {
        assertEquals("9", Judge.run("11111 11219"));
    }

    @Test
    public void test15() {
        assertEquals("0", Judge.run("10000 99999"));
    }
}
