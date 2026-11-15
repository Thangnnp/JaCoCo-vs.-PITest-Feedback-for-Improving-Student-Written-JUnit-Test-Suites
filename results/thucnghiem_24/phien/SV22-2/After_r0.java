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
}
