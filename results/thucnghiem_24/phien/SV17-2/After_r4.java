package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void testEqualCount() {
        assertEquals("8", Judge.run("2 2"));
    }

    @Test
    void testDiffByOneN() {
        assertEquals("12", Judge.run("3 2"));
    }

    @Test
    void testDiffByOneM() {
        assertEquals("12", Judge.run("2 3"));
    }

    @Test
    void testDiffMoreThanOne() {
        assertEquals("0", Judge.run("1 8"));
    }

    @Test
    void testMinimumConstraints() {
        assertEquals("2", Judge.run("1 1"));
    }

    @Test
    void testLargeInput() {
        assertEquals("530123477", Judge.run("100000 100000"));
    }

    @Test
    void testSmallestDiffN() {
        assertEquals("2", Judge.run("2 1"));
    }

    @Test
    void testSmallestDiffM() {
        assertEquals("2", Judge.run("1 2"));
    }

    @Test
    void testDiffTwo() {
        assertEquals("0", Judge.run("4 2"));
    }

    @Test
    void testDiffTwoM() {
        assertEquals("0", Judge.run("2 4"));
    }

    @Test
    void testDiffMoreThanOneReverse() {
        assertEquals("0", Judge.run("8 1"));
    }

    @Test
    void testLargeDiffOneN() {
        // N = 100000, M = 99999
        assertEquals("690321013", Judge.run("100000 99999"));
    }

    @Test
    void testLargeDiffOneM() {
        // N = 99999, M = 100000
        assertEquals("690321013", Judge.run("99999 100000"));
    }

    @Test
    void testLargeDiffMoreThanOne() {
        // N = 100000, M = 1
        assertEquals("0", Judge.run("100000 1"));
    }
}
