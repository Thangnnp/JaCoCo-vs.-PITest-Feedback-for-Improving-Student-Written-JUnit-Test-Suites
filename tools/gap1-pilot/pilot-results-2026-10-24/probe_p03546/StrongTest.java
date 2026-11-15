package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

/** Bộ test thử để kiểm tra phép đo: có test sai expected, test assertion yếu, lời gọi trong chú thích. */
class StrongTest {
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

    @Test
    void strongAssertion() {
        assertEquals("5", Judge.run("1 1\n" + costs(uniform(5)) + "3\n"));
    }
}
