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
}
