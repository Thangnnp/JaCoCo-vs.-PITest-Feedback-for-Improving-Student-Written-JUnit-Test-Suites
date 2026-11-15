package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p02263: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            3
            """.strip(), Judge.run("""
            1 2 +
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            -3
            """.strip(), Judge.run("""
            1 2 + 3 4 - *
            """));
    }
}
