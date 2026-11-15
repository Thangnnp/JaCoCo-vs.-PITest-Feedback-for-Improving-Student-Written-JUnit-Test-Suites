package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03813: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            ABC
            """.strip(), Judge.run("""
            1000
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            ARC
            """.strip(), Judge.run("""
            2000
            """));
    }
}
