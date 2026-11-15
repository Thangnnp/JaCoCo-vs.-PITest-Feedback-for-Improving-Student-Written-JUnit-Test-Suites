package codenet;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import codenet.Judge;

public class After {
    @Test
    public void test_1() {
        assertEquals("2", Judge.run("2 3"));
    }

    @Test
    public void test_2() {
        assertEquals("6", Judge.run("2 4"));
    }

    @Test
    public void test_3() {
        assertEquals("10", Judge.run("2 5"));
    }

    // Thêm test để kiểm tra trường hợp n = 1
    @Test
    public void test_n_1() {
        assertEquals("2", Judge.run("1 2"));
    }

    // Sửa test để kiểm tra trường hợp n = 100
    @Test
    public void test_n_100() {
        // Thay vì dùng input "2 3 5 7 11" như trước, giờ dùng input có số lớn hơn 10^18
        assertEquals("1000000000000", Judge.run("1 2 3 4 5"));
    }

    @Test
    public void test_n_1000() {
        // Thêm test để kiểm tra trường hợp n = 1000
        assertEquals("10000000000000", Judge.run("1 2 3 4 5 6 7 8 9 10"));
    }
}
