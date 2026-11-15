package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After   {
     @Test
    void test1()  {
        assertEquals("0", Judge.run("")); // empty string, no "ST" to remove
    }
    
     @Test
    void test2() {
         assertEquals("3", Judge.run("SSTT")); // all occurrences of "ST" in the string
    }
     
     @Test
    void test3()  {
        assertEquals("1", Judge.run("SSSTTT")); // not all occurrences of "ST", but after removing one, it's reduced by three characters (each occurrence of 'ST' is two characters long)
    }
}
