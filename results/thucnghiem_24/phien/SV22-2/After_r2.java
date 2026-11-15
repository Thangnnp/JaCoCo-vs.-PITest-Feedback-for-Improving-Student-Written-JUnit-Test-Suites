package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testCase1() {
        assertEquals("4", Judge.run("11009 11332"));
    }

    @Test
    public void testCase2() {
        assertEquals("612", Judge.run("31415 92653"));
    }

    @Test
    public void testCase3() {
        assertEquals("1", Judge.run("10000 10000"));
    }

    @Test
    public void testCase4() {
        assertEquals("0", Judge.run("10000 99999"));
    }

    @Test
    public void testCase5() {
        assertEquals("612", Judge.run("31415 99999"));
    }

    @Test
    public void testCase6() {
        assertEquals("12", Judge.run("10000 20000"));
    }

    @Test
    public void testCase7() {
        assertEquals("1089", Judge.run("40000 99999"));
    }

    @Test
    public void testCase8() {
        assertEquals("612", Judge.run("31415 99999"));
    }

    @Test
    public void testCase9() {
        assertEquals("0", Judge.run("10000 99000"));
    }
}
