package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }
}

class After {
    @Test
    public void testN1M2() {
        assertEquals("4", Judge.run("2 6"));
    }

    @Test
    public void testN3M12() {
        assertEquals("18", Judge.run("3 12"));
    }
    
    @Test
    public void testN4M24() {
        assertEquals("60", Judge.run("4 24"));
    }

    @Test
    public void testN5M60() {
        assertEquals("2784", Judge.run("5 60"));
    }
    
    @Test
    public void testN10M3628800() {
        assertEquals("3628800", Judge.run("10 3628800"));
    }

    @Test
    public void testN2M4() {
        assertEquals("5", Judge.run("2 4"));
    }

    @Test
    public void testN6M720() {
        assertEquals("96", Judge.run("6 720"));
    }
    
    @Test
    public void testN100M3628800() {
        assertEquals("3628800", Judge.run("100 3628800"));
    }

    @Test
    public void testN5M120() {
        assertEquals("720", Judge.run("5 120"));
    }

    @Test
    public void testN7M2520() {
        assertEquals("420", Judge.run("7 2520"));
    }
    
    @Test
    public void testN10M3628800() {
        assertEquals("3628800", Judge.run("10 3628800"));
    }

    @Test
    public void testN2M5() {
        assertEquals("6", Judge.run("2 5"));
    }

    
    
    

    
}
