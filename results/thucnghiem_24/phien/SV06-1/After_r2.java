package codenet;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class After {
    @Test
    void test7() {
        assertEquals("0", Judge.run("1 8"));
    }
    @Test
    void test8() {
        assertEquals("530123477", Judge.run("100000 100000"));
    }
    @Test
    void test9() {
        assertEquals("8", Judge.run("2 2"));
    }
}
