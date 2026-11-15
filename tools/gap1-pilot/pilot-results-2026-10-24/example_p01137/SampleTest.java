package codenet;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/** Bộ test ban đầu của p01137: các cặp Sample Input/Output của đề. */
class SampleTest {
    @Test
    void sample1() {
        assertEquals("""
            1
            2
            2
            3
            18
            44
            """.strip(), Judge.run("""
            1
            2
            4
            27
            300
            1250
            0
            """));
    }
}
