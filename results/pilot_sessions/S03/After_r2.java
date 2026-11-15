package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void sampleInput1() {
        assertEquals("4", Judge.run("TSTTSS"));
    }

    @Test
    void sampleInput2() {
        assertEquals("0", Judge.run("SSTTST"));
    }

    @Test
    void sampleInput3() {
        assertEquals("4", Judge.run("TSSTTTSS"));
    }

    // Additional tests
    @Test
    void inputAllSAndT() {
        assertEquals("2", Judge.run("SSTS"));
    }

    @Test
    void inputSingleST() {
        assertEquals("0", Judge.run("ST"));
    }

    @Test
    void inputLongString() {
        String longX = "S".repeat(100) + "T".repeat(100);
        assertEquals(200, Judge.run(longX));
    }

    // Add a test to cover the case when X contains no ST
    @Test
    void inputNoST() {
        assertEquals(200, Judge.run("STSTSSTS"));
    }

}
