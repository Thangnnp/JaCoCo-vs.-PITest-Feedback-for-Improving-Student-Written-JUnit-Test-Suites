package codenet;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class After {
    @Test
    void test4() {
        assertEquals("530123477", Judge.run("100000 100000"));
    }
    @Test
    void test5() {
        assertEquals("8", Judge.run("2 2"));
    }
    @Test
    void test6() {
        assertEquals("12", Judge.run("3 2"));
    }
}
