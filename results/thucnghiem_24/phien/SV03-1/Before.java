package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import codenet.Judge;

public class Before {
    @Test
    public void test_1() {
        assertEquals("2", Judge.run("2 3"));
    }

    @Test
    public void test_2() {
        assertEquals("6", Judge.run("2 4"));
    }

    @Test
    public void test_3() {
        assertEquals("10", Judge.run("2 5"));
    }
}
