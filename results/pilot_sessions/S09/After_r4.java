package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After   {
     @Test
    void test1()  {
        assertEquals("0", Judge.run("TT"));  // string 'x' only contains Ts, so no ST to remove
    }
     
     @Test
    void test2()  {
         assertEquals("5", Judge.run("STTSS")); //string 'x' has multiple instances of "ST" but doesn't start with any Ss or Ts (so length remains unchanged)
     }
}
