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
        // 1 -> 2 -> 3 (3 router)
        // TTL = 3: OK (1->2->3)
        // TTL = 2: NA
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
    void testPathSelectionAndCloseArray() {
        // Mutant ở dòng 117, 123 (close[j]) và 119 (ans)
        // Cần đảm bảo PriorityQueue lấy đường ngắn nhất ra trước
        // Đường 1: 1 -> 4 (c=2)
        // Đường 2: 1 -> 2 -> 3 -> 4 (c=4)
        // Nếu PriorityQueue sai hoặc close array không chặn đường dài hơn, 
        // kết quả có thể bị sai nếu code không lấy min.
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

    @Test
    void testComplexPathAndTTL() {
        // Kiểm tra việc cập nhật close array khi tìm thấy đường ngắn hơn sau
        // 1 -> 2 -> 4 (c=3)
        // 1 -> 3 -> 2 (c=3) -> 4 (c=4) - đường này dài hơn nên close[2] phải chặn
        String input = "4\n" +
                "1 2 2 3\n" +
                "2 1 4\n" +
                "3 1 2\n" +
                "4 0\n" +
                "1\n" +
                "1 4 5";
        String expected = "3";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testMultipleQueriesConsistency() {
        // Kiểm tra tính đúng đắn khi thực hiện nhiều query liên tục
        // Đảm bảo các biến ans, close, open được reset
        String input = "3\n" +
                "1 1 2\n" +
                "2 1 3\n" +
                "3 0\n" +
                "3\n" +
                "1 3 3\n" +
                "1 3 2\n" +
                "2 3 2";
        String expected = "3\nNA\n2";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testNoPathWithTTL() {
        // Trường hợp không có đường đi dù TTL rất lớn
        // Hoặc có đường đi nhưng TTL = 1 (không thể đi tiếp từ router đầu tiên)
        String input = "3\n" +
                "1 1 2\n" +
                "2 0\n" +
                "3 0\n" +
                "2\n" +
                "1 3 100\n" +
                "1 2 1";
        String expected = "NA\nNA";
        assertEquals(expected, Judge.run(input));
    }
}

