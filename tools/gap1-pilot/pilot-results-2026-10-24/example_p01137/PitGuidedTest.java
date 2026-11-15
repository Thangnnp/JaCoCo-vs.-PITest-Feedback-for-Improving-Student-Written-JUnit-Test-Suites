package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ ban đầu + 4 test viết theo báo cáo PITest (mutant sống sót ở dòng 15, 24, 34). */
class PitGuidedTest {
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
    void energy8() { // dòng 15: biên <= với lập phương 2^3
        assertEquals("2", Judge.run("8\n0\n"));
    }

    @Test
    void energy9() { // dòng 24: biên <= với bình phương 3^2
        assertEquals("3", Judge.run("9\n0\n"));
    }

    @Test
    void energy16() { // dòng 34: kết quả tốt nhất ở z = 0, cần vòng lặp chạy tới z = 0
        assertEquals("4", Judge.run("16\n0\n"));
    }

    @Test
    void energy28() { // dòng 15: ngay trên lập phương 27
        assertEquals("4", Judge.run("28\n0\n"));
    }
}
