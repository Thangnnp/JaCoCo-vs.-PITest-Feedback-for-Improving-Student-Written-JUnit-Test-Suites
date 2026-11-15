package codenet;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

class After {

    @Test
    public void testSimpleCase() {
        assertEquals("2", Judge.run("3 24"));
    }

    @Test
    public void testSingleElement() {
        assertEquals("1", Judge.run("5 1"));
    }
    
    @Test
    public void testLargePWithOneN() {
        long largeP = 10L;
        for (int i = 0; i < 10; i++) {
            largeP *= 10;
        }
        assertEquals(String.valueOf(largeP), Judge.run("1 " + largeP));
    }

    @Test
    void testModPow() {
        assertEquals(1, Main.modPow(3, 0, 5));
        assertEquals(8, Main.modPow(2, 3, 9));
    }

    @Test
    void testNcK() {
        int[] array = {1, 2, 3};
        Pair<Set<Long>, Long> result = Main.nCk(array.length);
        Set<Long> subsets = result.f;
        Long sumOfSubsets = result.s;

        assertEquals(8, subsets.size());
        for (long subsetSum : subsets) {
            assertTrue(subsetSum >= 0 && subsetSum <= array.length * (array.length + 1L) / 2);
        }

        assertEquals(sumOfSubsets, subsets.stream().mapToLong(Long::longValue).sum());
    }

    @Test
    public void testModPow_moi() {
        assertEquals(1L, Main.modPow(3L, 0L, 5L));
        assertEquals(8L, Main.modPow(2L, 3L, 9L));
    }

    @Test
    public void testNcK_moi() {
        int[] array = {1, 2};
        Pair<Set<Long>, Long> result = Main.nCk(array.length, (int)Math.pow(2, array.length), 1L);

        Set<Long> subsets = result.f;
        Long sumOfSubsets = result.s;

        assertEquals((long)Math.pow(2, array.length), subsets.size());
        
        for(Long subset : subsets) {
            assertTrue(subset >= 0);
        }

        assertEquals(sumOfSubsets, subsets.stream().mapToLong(Long::longValue).sum());
    }
}
