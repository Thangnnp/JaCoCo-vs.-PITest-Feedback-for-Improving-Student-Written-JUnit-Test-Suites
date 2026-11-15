package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testCase1() {
        assertEquals("YES", Judge.run("3 4 5"));
    }

    @Test
    public void testCase2() {
        assertEquals("NO", Judge.run("4 3 6"));
    }
    
    @Test
    public void testCase3() {
        assertEquals("NO", Judge.run("8 8 8"));
    }
    
    @Test
    public void testCase4() {
        assertEquals("YES", Judge.run("5 12 13"));
    }

    @Test
    public void testCase5() {
        assertEquals("NO", Judge.run("5 13 12"));
    }
    
    @Test
    public void testCase6() {
        assertEquals("NO", Judge.run("8 9 10"));
    }
}
