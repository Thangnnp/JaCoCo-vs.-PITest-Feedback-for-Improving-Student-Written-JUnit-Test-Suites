package codenet;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Paths;

/**
 * Judge dùng khi CHẤM (junit_eval.py), cùng API với Judge.java sinh viên dùng: run(String), normalize(String).
 * Khác Judge.java ở ba điểm, để kết quả trong JVM giống khi chạy chương trình như một tiến trình (`java Main`):
 *  1. Mỗi lần gọi run() nạp lại codenet.Main trong ClassLoader mới: biến static không mang từ lần gọi trước.
 *  2. Chờ các luồng không phải daemon mà chương trình tạo ra kết thúc rồi mới lấy output.
 *  3. Không flush System.out do chương trình tự thay: output nằm trong bộ đệm chưa flush bị mất như khi chạy thật.
 * Thư mục chứa codenet/Main*.class truyền qua -Djudge.main.dir=...
 */
public final class Judge {
    private Judge() {}

    public static String run(String input) {
        InputStream oldIn = System.in;
        PrintStream oldOut = System.out;
        ByteArrayOutputStream buf = new ByteArrayOutputStream();
        PrintStream cap = new PrintStream(buf, true, StandardCharsets.UTF_8);
        try {
            URL dir = Paths.get(System.getProperty("judge.main.dir")).toUri().toURL();
            try (URLClassLoader cl = new URLClassLoader(new URL[]{dir}, ClassLoader.getPlatformClassLoader())) {
                Method main = cl.loadClass("codenet.Main").getDeclaredMethod("main", String[].class);
                main.setAccessible(true); // lớp Main không public vẫn chạy được, như khi chạy `java Main`
                log(input);
                java.util.Set<Thread> before = Thread.getAllStackTraces().keySet();
                System.setIn(new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8)));
                System.setOut(cap);
                main.invoke(null, (Object) new String[0]);
                // chương trình chạy phần chính trong luồng riêng (new Thread(...).start()): chờ các luồng
                // không phải daemon do nó tạo kết thúc, như JVM chờ trước khi thoát
                for (Thread t : Thread.getAllStackTraces().keySet()) {
                    if (!before.contains(t) && !t.isDaemon() && t != Thread.currentThread()) t.join();
                }
            }
        } catch (InvocationTargetException e) {
            Throwable t = e.getCause();
            if (t instanceof Error) throw (Error) t;           // giống Judge.java: Error không bị bọc
            throw new RuntimeException("Main.main ném ngoại lệ: " + t, t);
        } catch (Exception e) {
            // lỗi của bộ chấm, không phải của chương trình: HarnessRunner ghi trạng thái HARNESS
            throw new IllegalStateException("HARNESS: không nạp được codenet.Main: " + e, e);
        } finally {
            // Chỉ flush luồng của bộ chấm. KHÔNG flush System.out: nếu chương trình tự bọc System.out bằng
            // bộ đệm mà không flush, khi chạy thật output đó bị mất, nên ở đây cũng không được cứu lại.
            cap.flush();
            System.setIn(oldIn);
            System.setOut(oldOut);
        }
        return normalize(buf.toString(StandardCharsets.UTF_8));
    }

    /** Ghi lại đầu vào thực tế mà test truyền vào (để đếm số đầu vào độc lập và kiểm ràng buộc). */
    private static synchronized void log(String input) {
        String f = System.getProperty("judge.log");
        if (f == null) return;
        try {
            java.nio.file.Files.writeString(Paths.get(f),
                    System.getProperty("judge.current", "?") + "\t"
                    + java.util.Base64.getEncoder().encodeToString(input.getBytes(StandardCharsets.UTF_8)) + "\n",
                    StandardCharsets.UTF_8, java.nio.file.StandardOpenOption.CREATE, java.nio.file.StandardOpenOption.APPEND);
        } catch (java.io.IOException ignored) { }
    }

    /** Giống hệt Judge.normalize của bộ công cụ nhóm. */
    public static String normalize(String s) {
        String[] lines = s.replace("\r\n", "\n").replace('\r', '\n').split("\n", -1);
        StringBuilder sb = new StringBuilder();
        for (String line : lines) {
            sb.append(line.replaceAll("\\s+$", "")).append('\n');
        }
        return sb.toString().replaceAll("\\n+$", "");
    }
}
