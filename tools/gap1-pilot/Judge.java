package codenet;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

/**
 * Chạy Main.main với input cho trước (thay cho stdin) và trả về output (stdout) đã chuẩn hoá.
 * Sinh viên viết test dạng:  assertEquals("8", Judge.run("2"));
 */
public final class Judge {
    private Judge() {}

    public static String run(String input) {
        InputStream oldIn = System.in;
        PrintStream oldOut = System.out;
        ByteArrayOutputStream buf = new ByteArrayOutputStream();
        try {
            System.setIn(new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8)));
            System.setOut(new PrintStream(buf, true, StandardCharsets.UTF_8));
            Main.main(new String[0]);
        } catch (Exception e) {
            throw new RuntimeException("Main.main ném ngoại lệ: " + e, e);
        } finally {
            System.out.flush();
            System.setIn(oldIn);
            System.setOut(oldOut);
        }
        return normalize(buf.toString(StandardCharsets.UTF_8));
    }

    /** Bỏ khác biệt \r\n, khoảng trắng cuối dòng và dòng trống cuối — giống cách online judge so output. */
    public static String normalize(String s) {
        String[] lines = s.replace("\r\n", "\n").replace('\r', '\n').split("\n", -1);
        StringBuilder sb = new StringBuilder();
        for (String line : lines) {
            sb.append(line.replaceAll("\\s+$", "")).append('\n');
        }
        return sb.toString().replaceAll("\\n+$", "");
    }
}
