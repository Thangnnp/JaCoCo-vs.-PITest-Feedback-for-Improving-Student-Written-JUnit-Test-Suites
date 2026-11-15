package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testSample1() {
        // 5 3 3
        // 1 2 4
        // Bên trái 3 có: 1, 2 (2 cổng)
        // Bên phải 3 có: 4 (1 cổng)
        // Min(2, 1) = 1
        assertEquals("1", Judge.run("5 3 3\n1 2 4"));
    }

    @Test
    void testSample2() {
        // 7 3 2
        // 4 5 6
        // Bên trái 2 có: (0 cổng)
        // Bên phải 2 có: 4, 5, 6 (3 cổng)
        // Min(0, 3) = 0
        assertEquals("0", Judge.run("7 3 2\n4 5 6"));
    }

    @Test
    void testSample3() {
        // 10 7 5
        // 1 2 3 4 6 8 9
        // Bên trái 5 có: 1, 2, 3, 4 (4 cổng)
        // Bên phải 5 có: 6, 8, 9 (3 cổng)
        // Min(4, 3) = 3
        assertEquals("3", Judge.run("10 7 5\n1 2 3 4 6 8 9"));
    }
    
    
    
    
}
