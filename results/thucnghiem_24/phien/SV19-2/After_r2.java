package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    
    @Test
    public void testAandCCanCommunicateDirectly() {
        assertEquals("Yes", Judge.run("4 7 9 3"));
    }
    
    @Test
    public void testAandCCanCommunicateIndirectly() {
        assertEquals("Yes", Judge.run("10 10 10 1"));
    }
    
    @Test
    public void testACCannotCommunicate() {
        assertEquals("No", Judge.run("1 100 2 10"));
    }
    
    @Test
    public void testBandCCanCommunicateDirectly() {
        assertEquals("Yes", Judge.run("4 7 9 5"));
    }
    
    @Test
    public void testABandACanCommunicateIndirectly() {
        assertEquals("Yes", Judge.run("10 8 12 3"));
    }
    
    @Test
    public void testBCannotCommunicate() {
        assertEquals("No", Judge.run("9 12 15 4"));
    }
    
    @Test
    public void testAandBCanCommunicateDirectly() {
        assertEquals("Yes", Judge.run("10 8 12 6"));
    }
    
    @Test
    public void testACannotCommunicateIndirectly() {
        assertEquals("No", Judge.run("9 15 20 7"));
    }
    
    @Test
    public void testBAndCCannotCommunicate() {
        assertEquals("No", Judge.run("8 10 13 4"));
    }
}
