package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

    @Test
    void testSample() {
        String input = "7\n" +
                "1 4 2 5 4 3\n" +
                "2 1 5\n" +
                "3 1 6\n" +
                "4 1 7\n" +
                "5 2 7 6\n" +
                "6 1 1\n" +
                "7 0\n" +
                "6\n" +
                "1 2 2\n" +
                "1 5 3\n" +
                "1 2 1\n" +
                "5 1 3\n" +
                "6 3 3\n" +
                "1 7 4";
        String expected = "2\n2\nNA\n3\n3\n3";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testTTLBoundary() {
        // Kiểm tra trường hợp biên của TTL
        // Đường đi: 1 -> 2 -> 3 (3 router)
        // TTL = 3: Vừa đủ đến 3 (1 giảm còn 2, 2 giảm còn 1, đến 3)
        // TTL = 2: Không đủ đến 3 (1 giảm còn 1, 2 giảm còn 0 -> hủy)
        String input = "3\n" +
                "1 1 2\n" +
                "2 1 3\n" +
                "3 0\n" +
                "2\n" +
                "1 3 3\n" +
                "1 3 2";
        String expected = "3\nNA";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testNoPathAndSmallestN() {
        // Trường hợp n nhỏ nhất và không có đường đi
        String input = "2\n" +
                "1 0\n" +
                "2 0\n" +
                "1\n" +
                "1 2 10";
        String expected = "NA";
        assertEquals(expected, Judge.run(input));
    }
}
