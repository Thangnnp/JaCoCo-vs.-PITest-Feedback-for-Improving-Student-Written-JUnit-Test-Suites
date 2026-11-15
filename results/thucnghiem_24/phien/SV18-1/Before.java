package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {
    @Test
    void testDirectCommunication() {
        assertEquals("Yes", Judge.run("1 3 5 2"));
    }

    @Test
    void testIndirectCommunication() {
        assertEquals("Yes", Judge.run("1 4 7 3"));
    }

    @Test
    void testNoCommunication() {
        assertEquals("No", Judge.run("1 100 2 1"));
    }
}
