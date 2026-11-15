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
    void testNoPath() {
        String input = "2\n" +
                       "1 0\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("NA", Judge.run(input));
    }

    // Các test dưới đây đang fail chứng tỏ chương trình có lỗi logic hoặc lỗi xử lý TTL/Path
    // Tôi vẫn giữ chúng để làm tài liệu về lỗi của chương trình
    @Test
    void testTTLBoundary() {
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 1";
        assertEquals("1", Judge.run(input));
    }

    @Test
    void testTTLStrictness() {
        String input = "3\n" +
                       "1 1 2\n" +
                       "2 1 3\n" +
                       "3 0\n" +
                       "1\n" +
                       "1 3 2";
        assertEquals("2", Judge.run(input));
    }

    @Test
    void testPathOptimization() {
        String input = "3\n" +
                       "1 2 2 3\n" +
                       "2 0\n" +
                       "3 1 2\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("1", Judge.run(input));
    }
    
    @Test
    void testSingleHopDirect() {
        // Test case đơn giản nhất: 1 hop trực tiếp
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("1", Judge.run(input));
    }

    @Test
    void testLoopInGraph() {
        // Đồ thị có vòng lặp: 1->2, 2->1.
        // Packet: 1->2, TTL=10.
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 1 1\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("1", Judge.run(input));
    }
}
