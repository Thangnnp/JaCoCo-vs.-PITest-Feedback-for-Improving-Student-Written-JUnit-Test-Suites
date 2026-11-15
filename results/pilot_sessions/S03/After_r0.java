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

}
