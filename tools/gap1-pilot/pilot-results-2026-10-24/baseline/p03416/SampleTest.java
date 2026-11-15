package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03416: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            4
            """.strip(), Judge.run("""
            11009 11332
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            612
            """.strip(), Judge.run("""
            31415 92653
            """));
    }
}
