package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testRightTriangle() {
        assertEquals("YES", Judge.run("4\n3 4 5"));
    }

    @Test
    void testNotRightTriangle() {
        assertEquals("NO", Judge.run("4\n1 2 3"));
    }
    
    @Test
    void testSingleInput() {
        assertEquals("NO", Judge.run("1\n8 8 8"));
    }
    
    @Test
    void testBoundaryValues() {
        assertEquals("YES", Judge.run("4\n600 550 700"));
        assertEquals("NO", Judge.run("4\n999 1 1"));
    }
    
    @Test
    void testOneSideZero() {
        assertEquals("NO", Judge.run("4\n0 3 4"));
        assertEquals("NO", Judge.run("4\n3 0 4"));
        assertEquals("NO", Judge.run("4\n3 4 0"));
    }
    
    @Test
    void testNegativeInputs() {
        assertThrows(RuntimeException.class, () -> Judge.run("4\n-1 -2 -3"));
    }
}
