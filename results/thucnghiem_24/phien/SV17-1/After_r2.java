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
        // 1 -> 2 -> 3 (độ dài 3 router)
        // TTL = 3: 1 (TTL 3->2), 2 (TTL 2->1), đến 3 (OK)
        // TTL = 2: 1 (TTL 2->1), 2 (TTL 1->0, hủy) -> NA
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
    void testMultiplePathsAndPriority() {
        // Kiểm tra việc tìm đường ngắn nhất khi có nhiều lựa chọn
        // Và kiểm tra logic PriorityQueue (compareTo)
        // 1 -> 2 -> 4 (chi phí 3)
        // 1 -> 3 -> 4 (chi phí 3)
        // 1 -> 4 (chi phí 2)
        // 1 -> 5 -> 6 -> 7 -> 4 (chi phí 5)
        String input = "7\n" +
                "1 4 2 3 4 5\n" +
                "2 1 4\n" +
                "3 1 4\n" +
                "4 0\n" +
                "5 1 6\n" +
                "6 1 7\n" +
                "7 1 4\n" +
                "1\n" +
                "1 4 10";
        String expected = "2";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testCloseArrayAndRevisit() {
        // Mutant ở dòng 117, 123 liên quan đến close[j]
        // Kiểm tra xem chương trình có bỏ qua đường dài hơn đến cùng một node không
        // 1 -> 2 (c=2)
        // 1 -> 3 -> 2 (c=3, phải bị loại bởi close[2])
        String input = "3\n" +
                "1 2 2 3\n" +
                "3 1 2\n" +
                "2 0\n" +
                "1\n" +
                "1 2 5";
        String expected = "2";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testTTLZeroAndOne() {
        // Kiểm tra TTL cực nhỏ
        // Đề bài: vi >= 0. Nếu vi = 0 hoặc 1, ngay tại router đầu tiên TTL-1 <= 0
        String input = "2\n" +
                "1 1 2\n" +
                "2 0\n" +
                "2\n" +
                "1 2 1\n" +
                "1 2 0";
        String expected = "NA\nNA";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testLargeNetworkReset() {
        // Kiểm tra việc reset dữ liệu giữa các query
        // Query 1: có đường đi
        // Query 2: không có đường đi (NA)
        String input = "4\n" +
                "1 1 2\n" +
                "2 1 3\n" +
                "3 0\n" +
                "4 0\n" +
                "2\n" +
                "1 3 10\n" +
                "1 4 10";
        String expected = "3\nNA";
        assertEquals(expected, Judge.run(input));
    }
}
