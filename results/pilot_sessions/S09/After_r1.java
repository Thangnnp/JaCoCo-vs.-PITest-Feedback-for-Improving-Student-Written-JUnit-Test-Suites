package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1()  {
        assertEquals("0", Judge.run("S"));
    }
    
    @Test
    void test2()  {
        assertEquals("0", Judge.run("T"));
    }
    
    @Test
    void test3()  {
        assertEquals("5", Judge.run("SSSTT"));
    }
}
