package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class After {
    @Test
    public void testCase1() {
        String input = "3 24";
        assertEquals("2", Judge.run(input));
    }

    @Test
    public void testCase2() {
        String input = "5 1";
        assertEquals("1", Judge.run(input));
    }

    @Test
    public void testCase3() {
        String input = "1 111";
        assertEquals("111", Judge.run(input));
    }

    @Test
    public void testCase4() {
        String input = "4 972439611840";
        assertEquals("206", Judge.run(input));
    }

    @Test
    public void testCase5() {
        String input = "10 1000000000";
        // Không nên bỏ qua các trường hợp này. Khi n >= N_MAX, thuật toán sẽ không chạy được và output là số NaN (đã bị chặn trong bài)
        assertEquals("1", Judge.run(input));
    }

    @Test
    public void testCase6() {
        String input = "100 12345678901234567890";
        // Thêm trường hợp này để kiểm tra thuật toán đối với n lớn
        assertEquals("2", Judge.run(input));
    }

    @Test
    public void testCase7() {
        String input = "200 98765432109876543210";
        // Thêm trường hợp này để kiểm tra thuật toán đối với n lớn
        assertEquals("3", Judge.run(input));
    }

    @Test
    public void testCase8() {
        String input = "1000 12345678901234567890";
        // Thêm trường hợp này để kiểm tra thuật toán đối với n cực lớn
        assertEquals("2", Judge.run(input));
    }

    @Test
    public void testCase9() {
        String input = "2000 98765432109876543210";
        // Thêm trường hợp này để kiểm tra thuật toán đối với n cực lớn
        assertEquals("3", Judge.run(input));
    }

    @Test
    public void testCase10() {
        String input = "10000 12345678901234567890";
        // Thêm trường hợp này để kiểm tra thuật toán đối với n rất lớn
        assertEquals("2", Judge.run(input));
    }

    @Test
    public void testCase11() {
        String input = "20000 98765432109876543210";
        // Thêm trường hợp này để kiểm tra thuật toán đối với n rất lớn
        assertEquals("3", Judge.run(input));
    }
}
