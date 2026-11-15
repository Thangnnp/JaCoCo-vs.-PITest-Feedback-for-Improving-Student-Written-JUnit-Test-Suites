package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.*;

public class Before {
    @org.junit.jupiter.api.Test
    public void test1() {
        // Tính số lượng các kết nối giữa các nút và sắp xếp lại các giá trị TTL trong từng gói tin
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
        String expectedOutput = "NA\n" +
                "2\n" +
                "2\n" +
                "NA\n" +
                "3\n" +
                "3\n" +
                "3";

        assertEquals(expectedOutput, Judge.run(input));
    }

    @org.junit.jupiter.api.Test
    public void test2() {
        // Tìm kiếm tất cả các kết nối và sắp xếp lại các giá trị TTL trong từng gói tin
        String input = "5\n" +
                "1 0 1\n" +
                "3 0 3\n" +
                "4 0 4\n" +
                "2 0 2\n" +
                "0 0\n" +
                "3\n" +
                "1 2 2\n" +
                "1 3 3\n" +
                "2 4 4";
        String expectedOutput = "NA\n" +
                "2\n" +
                "3\n" +
                "3";

        assertEquals(expectedOutput, Judge.run(input));
    }

    @org.junit.jupiter.api.Test
    public void test3() {
        // Tìm kiếm tất cả các kết nối và sắp xếp lại các giá trị TTL trong từng gói tin
        String input = "10\n" +
                "1 0 1\n" +
                "2 0 2\n" +
                "3 0 3\n" +
                "4 0 4\n" +
                "5 0 5\n" +
                "6 0 6\n" +
                "7 0 7\n" +
                "8 0 8\n" +
                "9 0 9\n" +
                "10 0\n" +
                "10\n" +
                "1 2 2\n" +
                "1 3 3\n" +
                "1 4 4\n" +
                "1 5 5\n" +
                "1 6 6\n" +
                "1 7 7\n" +
                "1 8 8\n" +
                "1 9 9\n";
        String expectedOutput = "";

        assertEquals(expectedOutput, Judge.run(input));
    }
}
