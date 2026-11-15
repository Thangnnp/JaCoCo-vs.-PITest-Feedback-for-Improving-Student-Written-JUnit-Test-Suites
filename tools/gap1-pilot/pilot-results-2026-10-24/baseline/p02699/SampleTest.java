package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p02699: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            unsafe
            """.strip(), Judge.run("""
            4 5
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            safe
            """.strip(), Judge.run("""
            100 2
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            unsafe
            """.strip(), Judge.run("""
            10 10
            """));
    }
}
