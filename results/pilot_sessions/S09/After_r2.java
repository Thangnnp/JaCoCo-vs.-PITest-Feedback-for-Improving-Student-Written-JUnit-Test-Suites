package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After  {
    @Test
    void test1() {
        assertEquals("0", Judge.run("ST")); // Removes all occurrences of "ST" in the string.
    }
    
    @Test
    void test2() {
        assertEquals("3", Judge.run("SST"));  // Only one occurrence of "ST".
    }

    @Test
    void test3() {
        assertEquals("1", Judge.run("SSSSTTTT")); // Removes all occurrences except the last one.
    }
}
