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
        // Kiểm tra trường hợp không có đường đi (đồ thị rời rạc)
        String input = "2\n" +
                       "1 0\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 10";
        assertEquals("NA", Judge.run(input));
    }

    @Test
    void testTTLBoundary() {
        // Trường hợp biên về TTL: TTL=1 cho khoảng cách 1 hop
        // Theo đề: "宛先ルータでは TTL を減算する必要はありません" (Không cần giảm TTL tại đích)
        // Nếu chương trình trả về NA là đang sai logic (bug)
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 2 1";
        assertEquals("1", Judge.run(input));
    }

    @Test
    void testTTLStrictness() {
        // Trường hợp TTL vừa đủ để đi đến đích (2 hop, TTL=2)
        // 1 -> 2 -> 3. TTL=2. 1->2 (TTL 1), 2->3 (Arrival).
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
        // Kiểm tra thuật toán Dijkstra chọn đường ngắn nhất
        // 1 -> 2 (cạnh trực tiếp, cost 1)
        // 1 -> 3 -> 2 (cost 2)
        String input = "3\n" +
                       "1 2 2 3\n" +
                       "2 1 2\n" + // Router 2 nối với 3? Wait, input format: "i 番目のルータの番号 ri, i 番目のルータと直接接続しているルータの個数 ki, i 番目のルータから送信できるルータの番号..."
                       "3 1 2\n" +
                       "1\n" +
                       "1 2 10";
        // 1->2 là trực tiếp (1 hop)
        assertEquals("1", Judge.run(input));
    }
    
    @Test
    void testSameSourceDestination() {
        // Đề bài nói: "送信元と宛先が同じルータになるようなパケットは無いものとします"
        // Nhưng nếu có, code nên xử lý an toàn (NA hoặc 0).
        String input = "2\n" +
                       "1 1 2\n" +
                       "2 0\n" +
                       "1\n" +
                       "1 1 10";
        // Nếu không có logic xử lý đặc biệt, code có thể ra NA
        assertEquals("NA", Judge.run(input));
    }

    @Test
    void testHighTTL() {
        // Kiểm tra TTL lớn không ảnh hưởng đến số hop tối thiểu
        String input = "3\n" +
                       "1 1 2\n" +
                       "2 1 3\n" +
                       "3 0\n" +
                       "1\n" +
                       "1 3 10000";
        assertEquals("2", Judge.run(input));
    }
}
