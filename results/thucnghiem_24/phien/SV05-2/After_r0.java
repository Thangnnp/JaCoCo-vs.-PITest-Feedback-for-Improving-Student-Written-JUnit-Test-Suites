package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testLCM() {
        assertEquals(BigInteger.valueOf(6), Judge.run("2\n3"));
        assertEquals(BigInteger.valueOf(18), Judge.run("4\n5\n6"));
        // Sử dụng Long.MAX_VALUE cho số lớn hơn 2^31 - 1
        assertEquals(Long.MAX_VALUE, Judge.run("1000000000000000000\n2\n3\n5\n11"));
    }
}
