package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
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

    @Test
    void testEdgeCaseSamePositions() {
        assertEquals("Yes", Judge.run("10 10 10 1"));
    }

    @Test
    void testFarApartDirectlyCommunicate() {
        assertEquals("No", Judge.run("1 98 99 2"));
    }

    @Test
    void testCloseButIndirectFail() {
        assertEquals("No", Judge.run("1 5 6 3"));
    }

    @Test
    void testBoundaryCondition() {
        assertEquals("Yes", Judge.run("0 1 2 1"));
    }
}
