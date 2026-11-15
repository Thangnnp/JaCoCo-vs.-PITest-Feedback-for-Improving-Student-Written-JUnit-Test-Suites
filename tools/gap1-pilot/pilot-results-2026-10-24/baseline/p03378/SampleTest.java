package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03378: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            1
            """.strip(), Judge.run("""
            5 3 3
            1 2 4
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            0
            """.strip(), Judge.run("""
            7 3 2
            4 5 6
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            3
            """.strip(), Judge.run("""
            10 7 5
            1 2 3 4 6 8 9
            """));
    }
}
