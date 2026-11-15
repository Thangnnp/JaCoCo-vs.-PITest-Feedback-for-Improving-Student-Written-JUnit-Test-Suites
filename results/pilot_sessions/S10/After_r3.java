package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
     @Test
    void testMain()   {
        assertEquals("Cloudy", Judge.run("Sunny"));  // Kiểm tra ngày mây
        assertEquals("Sunny", Judge.run("Cloudy"));  // Kiểm ra lần đám mây tiếp theo
    }
}
