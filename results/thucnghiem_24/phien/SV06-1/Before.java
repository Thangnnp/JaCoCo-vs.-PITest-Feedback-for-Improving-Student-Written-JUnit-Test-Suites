package codenet;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class Before {
    @Test
    void test1() {
        assertEquals("8", Judge.run("2 2"));
    }
    @Test
    void test2() {
        assertEquals("12", Judge.run("3 2"));
    }
    @Test
    void test3() {
        assertEquals("0", Judge.run("1 8"));
    }
}
