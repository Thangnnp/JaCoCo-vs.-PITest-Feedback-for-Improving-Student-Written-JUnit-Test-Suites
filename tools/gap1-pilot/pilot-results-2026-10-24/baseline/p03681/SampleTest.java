package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03681: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            8
            """.strip(), Judge.run("""
            2 2
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            12
            """.strip(), Judge.run("""
            3 2
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            0
            """.strip(), Judge.run("""
            1 8
            """));
    }

    @Test
    void sample4() {
        assertEquals("""
            530123477
            """.strip(), Judge.run("""
            100000 100000
            """));
    }
}
