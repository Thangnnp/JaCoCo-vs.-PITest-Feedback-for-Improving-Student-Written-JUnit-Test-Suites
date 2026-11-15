package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ ban đầu + 4 test viết theo báo cáo JaCoCo (nhánh chưa phủ ở dòng 15 và 24). */
class JacocoGuidedTest {
    @Test
    void sample1() {
        assertEquals("""
            1
            2
            2
            3
            18
            44
            """.strip(), Judge.run("""
            1
            2
            4
            27
            300
            1250
            0
            """));
    }

    @Test
    void energy63() { // dòng 15: ngay dưới lập phương 64, (int)cbrt có thể lệch
        assertEquals("9", Judge.run("63\n0\n"));
    }

    @Test
    void energy64() { // dòng 15: lập phương đúng 4^3
        assertEquals("4", Judge.run("64\n0\n"));
    }

    @Test
    void energy999999() { // dòng 24: căn bậc hai sát giới hạn
        assertEquals("387", Judge.run("999999\n0\n"));
    }

    @Test
    void energy1000000() { // dòng 15/24: giá trị lớn nhất, 100^3 = 10^6
        assertEquals("100", Judge.run("1000000\n0\n"));
    }
}
