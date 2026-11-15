package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    public void testN1M2() {
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    public void testN3M12() {
        assertEquals("18", Judge.run("3 12"));
    }
    
}
