package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testMain()  {
        assertEquals("Cloudy", Judge.run("Sunny")); // Kiểm tra ngày mây
        assertEquals("Sunny", Judge.run("Cloudy")); // Kiểm tra lần đám mây tiếp theo
        assertEquals("Rainy", Judge.run("Sunny"));  // Kiểm tra tối nắng
    }
    
    @Test
    void testMain1() {
        assertEquals("Cloudy", Judge.run("Rainy")); // Kiểm tra khi mây sáng
        assertEquals("Sunny", Judge.run("Cloudy")); // Mây tiếp theo là xuất hiện như thế nào
    }
}
