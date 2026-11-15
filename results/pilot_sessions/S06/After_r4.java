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
        // Kiểm tra xem khi có nhiều TST liên tiếp, chỉ số mảng sẽ đưa ra kết quả như thế nào
        String input = "TSSTTSS";
        assertEquals("4", Judge.run(input));
    }

    @Test
    public void testCaseEmptyString() {
        // Kiểm tra xem khi chuỗi trống được đưa vào, chương trình sẽ xử lý ra sao
        String input = "";
        assertEquals(0, Integer.parseInt(Judge.run(input)));
    }

    @Test
    public void testCaseValidInput() {
        // Kiểm tra xem với các trường hợp nhập liệu hợp lệ, chương trình sẽ đưa ra kết quả chính xác
        String[] inputs = {"TSTTSS", "SSTTST", "TSSTTTSS"};
        for (String input : inputs) {
            assertEquals(input.length(), Integer.parseInt(Judge.run(input)));
        }
    }

    @Test
    public void testCaseInvalidInput() {
        // Kiểm tra xem với các trường hợp nhập liệu không hợp lệ, chương trình sẽ đưa ra kết quả chính xác
        String[] inputs = {"TST", "SSTS", "TS"};
        for (String input : inputs) {
            assertEquals(0, Integer.parseInt(Judge.run(input)));
        }
    }

    @Test
    public void testCaseLongInput() {
        // Kiểm tra xem với các trường hợp nhập liệu dài, chương trình sẽ đưa ra kết quả chính xác
        String input = "TSSTTTSS";
        for (int i = 0; i < 10000; i++) {
            input += "TSSTTTSS";
        }
        assertEquals(40004, Integer.parseInt(Judge.run(input)));
    }

    @Test
    public void testCaseEdgeCase() {
        // Kiểm tra xem với các trường hợp rìa (ví dụ: chuỗi có một ký tự), chương trình sẽ đưa ra kết quả chính xác
        String[] inputs = {"T", "S", ""};
        for (String input : inputs) {
            assertEquals(0, Integer.parseInt(Judge.run(input)));
        }
    }

    @Test
    public void testCaseConsecutiveST() {
        // Kiểm tra xem với các trường hợp có nhiều ST liên tiếp, chương trình sẽ đưa ra kết quả chính xác
        String input = "TSSTTSTS";
        assertEquals(8, Integer.parseInt(Judge.run(input)));
    }

    @Test
    public void testCaseMiddleCharactersRemoved() {
        // Kiểm tra xem khi các ký tự ở giữa được loại bỏ, chương trình sẽ đưa ra kết quả chính xác
        String input = "TSSSST";
        assertEquals(4, Integer.parseInt(Judge.run(input)));
    }

    @Test
    public void testCaseNoSTFound() {
        // Kiểm tra xem khi không tìm thấy chuỗi ST, chương trình sẽ đưa ra kết quả chính xác
        String input = "TTTSSTS";
        assertEquals(7, Integer.parseInt(Judge.run(input)));
    }
}
