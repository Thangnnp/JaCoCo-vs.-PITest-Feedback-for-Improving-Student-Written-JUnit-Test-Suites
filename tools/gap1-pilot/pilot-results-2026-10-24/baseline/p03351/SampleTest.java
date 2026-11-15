package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03351: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            Yes
            """.strip(), Judge.run("""
            4 7 9 3
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            No
            """.strip(), Judge.run("""
            100 10 1 2
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            Yes
            """.strip(), Judge.run("""
            10 10 10 1
            """));
    }

    @Test
    void sample4() {
        assertEquals("""
            Yes
            """.strip(), Judge.run("""
            1 100 2 10
            """));
    }
}
