package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.*;
import org.junit.jupiter.api.Test;
public class After {
    @Test
    public void testCase1() {
        String input = "TSTTSS";
        assertEquals("4", Judge.run(input));
    }

    @Test
    public void testCase2() {
        String input = "SSTTST";
        assertEquals("0", Judge.run(input));
    }

    @Test
    public void testCase3() {
        String input = "TSSTTTSS";
        assertEquals("4", Judge.run(input));
    }

    @Test
    public void testCaseScannerClosed() {
        // Kiểm tra xem khi Scanner không được đóng, có ảnh hưởng gì đến kết quả không?
        String input = "TSTTSS";
        String output = Judge.run(input);
        Judge.run("TSTTSS"); // Chạy một lần nữa để kiểm tra
        assertEquals(output, Judge.run(input));
    }

    @Test
    public void testCaseArrayCondition() {
        String input = "TTTTSS";
        assertEquals("4", Judge.run(input));
    }

    @Test
    public void testCaseArrayIndex() {
        String input = "TSSTTSS";
        assertEquals("4", Judge.run(input));
    }
}
