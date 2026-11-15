package codenet;

import static org.junit.jupiter.api.Assertions.*;
import java.util.*;

public class After {
    @org.junit.jupiter.api.Test
    public void test7() {
        // Tìm kiếm tất cả các kết nối và sắp xếp lại các giá trị TTL trong từng gói tin
        String input = "5\n" +
                "1 0 1\n" +
                "2 0 3\n" +
                "4 0 4\n" +
                "2 0 2\n" +
                "0 0\n" +
                "3\n" +
                "1 2 2\n" +
                "1 3 3\n" +
                "2 4 4";
        String expectedOutput = "";

        assertEquals(expectedOutput, Judge.run(input));
    }

    @org.junit.jupiter.api.Test
    public void test8() {
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

    @org.junit.jupiter.api.Test
    public void test9() {
        // Tìm kiếm tất cả các kết nối và sắp xếp lại các giá trị TTL trong từng gói tin
        String input = "5\n" +
                "1 0 1\n" +
                "2 0 4\n" +
                "3 0 3\n" +
                "4 0 4\n" +
                "2 0 2\n" +
                "3\n" +
                "1 2 2\n" +
                "1 3 3\n" +
                "2 4 4";
        String expectedOutput = "";

        assertEquals(expectedOutput, Judge.run(input));
    }
}
