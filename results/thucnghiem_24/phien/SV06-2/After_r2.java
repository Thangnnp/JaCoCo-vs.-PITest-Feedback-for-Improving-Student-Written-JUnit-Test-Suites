package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    @Test
    void test1() {
        assertEquals("2", Judge.run("7\n" +
                "1 4 2 5 4 3\n" +
                "2 1 5\n" +
                "3 1 6\n" +
                "4 1 7\n" +
                "5 2 7 6\n" +
                "6 1 1\n" +
                "7 0\n" +
                "6\n" +
                "1 2 2\n" +
                "1 5 3\n" +
                "1 2 1\n"));
    }

    @Test
    void test2() {
        assertEquals("4", Judge.run("7\n" +
                "1 4 2 5 4 3\n" +
                "2 1 5\n" +
                "3 1 6\n" +
                "4 1 7\n" +
                "5 2 7 6\n" +
                "6 1 1\n" +
                "7 0\n" +
                "6\n" +
                "1 7 4\n"));
    }

    @Test
    void test3() {
        assertEquals("NA", Judge.run("7\n" +
                "1 4 2 5 4 3\n" +
                "2 1 5\n" +
                "3 1 6\n" +
                "4 1 7\n" +
                "5 2 7 6\n" +
                "6 1 1\n" +
                "7 0\n" +
                "6\n" +
                "5 3 3\n"));
    }
}
