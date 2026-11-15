package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    
    @Test
    public void testSingleNumber() {
        assertEquals("1", Judge.run("1"));
    }
    
    @Test
    public void testAddition() {
        assertEquals("3", Judge.run("1 2 +"));
    }
    
    @Test
    public void testSubtraction() {
        assertEquals("-3", Judge.run("1 2 -"));
    }
    
    @Test
    public void testMultiplication() {
        assertEquals("6", Judge.run("2 3 *"));
    }
}
