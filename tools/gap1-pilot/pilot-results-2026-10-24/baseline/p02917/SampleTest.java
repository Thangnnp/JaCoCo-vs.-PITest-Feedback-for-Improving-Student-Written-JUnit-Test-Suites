package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p02917: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            9
            """.strip(), Judge.run("""
            3
            2 5
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            6
            """.strip(), Judge.run("""
            2
            3
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            53
            """.strip(), Judge.run("""
            6
            0 153 10 10 23
            """));
    }
}
