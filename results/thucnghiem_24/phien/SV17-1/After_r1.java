package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

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

    @Test
    void testPathSelectionAndCloseArray() {
        // Kiểm tra việc chọn đường ngắn nhất và cập nhật mảng close
        // 1 -> 2 -> 4 (3 router)
        // 1 -> 3 -> 4 (3 router)
        // 1 -> 4 (2 router)
        String input = "4\n" +
                "1 3 2 3 4\n" +
                "2 1 4\n" +
                "3 1 4\n" +
                "4 0\n" +
                "1\n" +
                "1 4 5";
        String expected = "2";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testMultipleQueriesAndLargeTTL() {
        // Kiểm tra nhiều truy vấn cùng lúc và TTL lớn
        // Đảm bảo trạng thái (close array) được reset cho mỗi truy vấn
        String input = "3\n" +
                "1 1 2\n" +
                "2 1 3\n" +
                "3 1 1\n" +
                "3\n" +
                "1 3 100\n" +
                "3 2 100\n" +
                "2 1 2";
        String expected = "3\n3\nNA";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testCompareToInPriorityQueue() {
        // Ép PriorityQueue sử dụng compareTo bằng cách đưa vào các đường có độ dài khác nhau
        // 1 -> 4 (trực tiếp, c=2)
        // 1 -> 2 -> 3 -> 4 (c=4)
        String input = "4\n" +
                "1 2 2 4\n" +
                "2 1 3\n" +
                "3 1 4\n" +
                "4 0\n" +
                "1\n" +
                "1 4 10";
        String expected = "2";
        assertEquals(expected, Judge.run(input));
    }
}
