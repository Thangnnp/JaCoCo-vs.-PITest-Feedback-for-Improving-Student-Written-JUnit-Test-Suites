package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p03196: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            2
            """.strip(), Judge.run("""
            3 24
            """));
    }

    @Test
    void sample2() {
        assertEquals("""
            1
            """.strip(), Judge.run("""
            5 1
            """));
    }

    @Test
    void sample3() {
        assertEquals("""
            111
            """.strip(), Judge.run("""
            1 111
            """));
    }

    @Test
    void sample4() {
        assertEquals("""
            206
            """.strip(), Judge.run("""
            4 972439611840
            """));
    }
}
