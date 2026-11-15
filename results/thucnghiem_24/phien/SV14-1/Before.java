package codenet;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    public void testSimpleCase() {
        assertEquals(2, Main.main(new String[]{"3", "24"}));
    }

    @Test
    public void testSingleElement() {
        assertEquals(1, Main.main(new String[]{"5", "1"}));
    }

    @Test
    public void testLargePWithOneN() {
        long largeP = 10L;
        for (int i = 0; i < 10; i++) {
            largeP *= 10;
        }
        assertEquals(largeP, Main.main(new String[]{"1", String.valueOf(largeP)}));
    }

    

    
}
