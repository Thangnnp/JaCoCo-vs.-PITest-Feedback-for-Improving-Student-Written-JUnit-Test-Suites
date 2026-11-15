package codenet;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

class After {

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

    @Test
    public void testSimpleCase_moi() {
        Map<Long, Long> primeFactors = Main.primeFactor(24);
        assertEquals(2L, primeFactors.get(2L));
        assertEquals(1L, primeFactors.get(3L));
    }

    @Test
    public void testSingleElement_moi() {
        Map<Long, Long> primeFactors = Main.primeFactor(1);
        assertTrue(primeFactors.isEmpty());
    }

    @Test
    public void testGCDCalculation() {
        long P = 24;
        for (Map.Entry<Long, Long> entry : Main.primeFactor(P).entrySet()) {
            while (P % entry.getKey() == 0) {
                P /= entry.getKey();
            }
        }
        assertEquals(1L, P);
    }

    

    
}
