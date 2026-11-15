package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After  {
     @Test
    void testMain()   {
        assertEquals("Rainy", Judge.run("Cloudy")); // Kiểm tra lần mây sau, phải là mùa nắng
    }
} 
