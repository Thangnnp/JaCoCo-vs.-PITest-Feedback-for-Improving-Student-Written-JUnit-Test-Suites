package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    void testSample1() {
        // N=2, M=2. |N-M|=0. 2! * 2! * 2 = 2 * 2 * 2 = 8
        assertEquals("8", Judge.run("2 2"));
    }

    @Test
    void testSample2() {
        // N=3, M=2. |N-M|=1. 3! * 2! = 6 * 2 = 12
        assertEquals("12", Judge.run("3 2"));
    }

    @Test
    void testSample3() {
        // N=1, M=8. |N-M|=7 > 1. Output 0
        assertEquals("0", Judge.run("1 8"));
    }

    

    
}
