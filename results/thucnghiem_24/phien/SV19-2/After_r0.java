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
}
