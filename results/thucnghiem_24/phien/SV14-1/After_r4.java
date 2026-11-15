package codenet;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

class After {

    @Test
    void testModPow() {
        assertEquals(1L, Main.modPow(3L, 0L, 5L));
        assertEquals(8L, Main.modPow(2L, 3L, 9L));
    }
    
    // Define nCk function to return number of subsets and sum of them
    @Test
    void testNcK() {
        int[] array = {1, 2, 3};
        Pair<Set<Long>, Long> result = Main.nCk(array.length);

        Set<Long> subsets = result.f;
        Long sumOfSubsets = result.s;

        assertEquals((long)Math.pow(2, array.length), subsets.size());

        for (Long subsetSum : subsets) {
            assertTrue(subsetSum >= 0);
        }

        assertEquals(sumOfSubsets, subsets.stream().mapToLong(Long::longValue).sum());
    }
}
