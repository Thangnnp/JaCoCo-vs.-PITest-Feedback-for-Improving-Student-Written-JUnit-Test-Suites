package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

/** Bộ test thử để kiểm tra phép đo: có test sai expected, test assertion yếu, lời gọi trong chú thích. */
class ProbeTest {
    static String costs(int[][] c) {
        StringBuilder sb = new StringBuilder();
        for (int[] r : c) { for (int j = 0; j < 10; j++) sb.append(j == 0 ? "" : " ").append(r[j]); sb.append('\n'); }
        return sb.toString();
    }
    static int[][] uniform(int v) {
        int[][] c = new int[10][10];
        for (int i = 0; i < 10; i++) for (int j = 0; j < 10; j++) c[i][j] = i == j ? 0 : v;
        return c;
    }

    // assertEquals("0", Judge.run("1 1\n" + costs(uniform(5)) + "1\n"));  <- nằm trong chú thích, không được tính
    @Test
    void wrongExpected() {          // expected sai: đúng phải là 5
        assertEquals("6", Judge.run("1 1\n" + costs(uniform(5)) + "3\n"));
    }

    @Test
    void weakAssertion() {          // chỉ kiểm output không rỗng
        assertFalse(Judge.run("1 1\n" + costs(uniform(5)) + "3\n").isEmpty());
    }

    @Test
    void indirectPathCheaper() {    // 2 -> 3 -> 1 rẻ hơn 2 -> 1
        int[][] c = uniform(1000);
        c[2][3] = 1; c[3][1] = 1;
        assertEquals("2", Judge.run("1 1\n" + costs(c) + "2\n"));
    }

    @Test
    void allMinusOneExceptOne() {
        assertEquals("0", Judge.run("2 2\n" + costs(uniform(7)) + "-1 -1\n-1 1\n"));
    }
}
