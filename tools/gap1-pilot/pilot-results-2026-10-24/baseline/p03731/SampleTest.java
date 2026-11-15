package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03731: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            7
            """.strip(), Judge.run("""
            2 4
            0 3
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            8
            """.strip(), Judge.run("""
            2 4
            0 5
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            2000000000
            """.strip(), Judge.run("""
            4 1000000000
            0 1000 1000000 1000000000
            """));
    }

    @Test
    void sample4() {
        assertEquals("""
            1
            """.strip(), Judge.run("""
            1 1
            0
            """));
    }

    @Test
    void sample5() {
        assertEquals("""
            67
            """.strip(), Judge.run("""
            9 10
            0 3 5 7 100 110 200 300 311
            """));
    }
}
