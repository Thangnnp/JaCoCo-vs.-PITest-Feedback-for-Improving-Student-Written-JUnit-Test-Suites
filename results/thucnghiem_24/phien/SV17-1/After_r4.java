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
    void testPriorityQueueAndShortestPath() {
        // Mutant dòng 117, 119, 123, 137, 138
        // Mục tiêu: Ép PriorityQueue phải so sánh các node có 'c' (số router) khác nhau
        // Đảm bảo đường ngắn nhất được chọn kể cả khi nó được phát hiện sau hoặc qua nhiều nhánh
        // 1 -> 2 -> 3 -> 4 (c=4)
        // 1 -> 5 -> 4 (c=3)
        // 1 -> 6 -> 7 -> 8 -> 9 -> 4 (c=6)
        String input = "9\n" +
                "1 3 2 5 6\n" +
                "2 1 3\n" +
                "3 1 4\n" +
                "4 0\n" +
                "5 1 4\n" +
                "6 1 7\n" +
                "7 1 8\n" +
                "8 1 9\n" +
                "9 1 4\n" +
                "1\n" +
                "1 4 10";
        String expected = "3";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testCloseArrayPruning() {
        // Mutant 117: now.c+1 < close[j]
        // Kiểm tra xem nếu một lộ trình đến node j dài hơn hoặc bằng lộ trình đã biết 
        // thì nó có bị loại bỏ không.
        // 1 -> 2 (c=2)
        // 1 -> 3 -> 2 (c=3) - đường này phải bị chặn bởi close[2]=2
        String input = "3\n" +
                "1 2 2 3\n" +
                "2 0\n" +
                "3 1 2\n" +
                "1\n" +
                "1 2 5";
        String expected = "2";
        assertEquals(expected, Judge.run(input));
    }

    @Test
    void testMultipleQueriesAndReset() {
        // Đảm bảo tính độc lập giữa các query (ans reset, close reset)
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
    void testTTLOneAndZero() {
        // Đề bài: 0 <= vi <= 10000.
        // Nếu TTL = 1, router đầu tiên giảm TTL xuống 0 và hủy ngay lập tức.
        String input = "2\n" +
                "1 1 2\n" +
                "2 0\n" +
                "2\n" +
                "1 2 1\n" +
                "1 2 0";
        String expected = "NA\nNA";
        assertEquals(expected, Judge.run(input));
    }
}
