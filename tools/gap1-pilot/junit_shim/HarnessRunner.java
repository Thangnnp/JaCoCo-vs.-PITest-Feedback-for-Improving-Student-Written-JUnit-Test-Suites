import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Chạy các phương thức @Test của MỘT lớp test. Dùng được với JUnit 5 API thật (junit-jupiter-api.jar)
 * hoặc với bản thay thế tối giản trong thư mục này.
 * AssertionError (gồm AssertionFailedError của JUnit 5) là FAIL; ngoại lệ khác là ERROR.
 *
 *   java HarnessRunner <tên lớp đầy đủ> [chỉ số bắt đầu] [chỉ số kết thúc, không gồm]
 *
 * In ra stdout, mỗi test hai dòng:
 *   START <i> <tên>
 *   RESULT <i> <tên> PASS|FAIL|ERROR|HARNESS <thông báo một dòng>   (HARNESS: lỗi của bộ chấm)
 * Thứ tự chạy: theo tên phương thức (cố định giữa các lần chạy). Nếu JVM dừng giữa chừng
 * (System.exit, quá thời gian), driver chạy lại từ test kế tiếp bằng [chỉ số bắt đầu].
 */
public class HarnessRunner {
    private static List<Method> annotated(Class<?> c, Class<? extends java.lang.annotation.Annotation> a) {
        List<Method> ms = new ArrayList<>();
        for (Method m : c.getDeclaredMethods()) if (m.isAnnotationPresent(a)) { m.setAccessible(true); ms.add(m); }
        ms.sort(Comparator.comparing(Method::getName));
        return ms;
    }

    private static String oneLine(Throwable t) {
        String s = t.getClass().getName() + (t.getMessage() == null ? "" : ": " + t.getMessage());
        s = s.replace('\n', ' ').replace('\r', ' ');
        return s.length() > 300 ? s.substring(0, 300) : s;
    }

    private static boolean isHarness(Throwable t) {
        for (; t != null; t = t.getCause()) if (t.getMessage() != null && t.getMessage().startsWith("HARNESS:")) return true;
        return false;
    }

    public static void main(String[] args) throws Exception {
        java.io.PrintStream out = new java.io.PrintStream(new java.io.FileOutputStream(java.io.FileDescriptor.out), true, "UTF-8");
        Class<?> c = Class.forName(args[0]);
        int from = args.length > 1 ? Integer.parseInt(args[1]) : 0;
        List<Method> tests = annotated(c, org.junit.jupiter.api.Test.class);
        out.println("COUNT " + tests.size());
        for (Method m : annotated(c, org.junit.jupiter.api.BeforeAll.class)) {
            if (Modifier.isStatic(m.getModifiers())) m.invoke(null);
        }
        List<Method> before = annotated(c, org.junit.jupiter.api.BeforeEach.class);
        List<Method> after = annotated(c, org.junit.jupiter.api.AfterEach.class);
        int to = args.length > 2 ? Math.min(Integer.parseInt(args[2]), tests.size()) : tests.size();
        for (int i = from; i < to; i++) {
            Method m = tests.get(i);
            out.println("START " + i + " " + m.getName());
            System.setProperty("judge.current", m.getName());
            String status = "PASS", msg = "";
            try {
                java.lang.reflect.Constructor<?> k = c.getDeclaredConstructor();
                k.setAccessible(true);
                Object inst = k.newInstance();
                try {
                    for (Method b : before) b.invoke(inst);
                    m.invoke(inst);
                } finally {
                    for (Method a : after) a.invoke(inst);
                }
            } catch (InvocationTargetException e) {
                Throwable t = e.getCause();
                status = isHarness(t) ? "HARNESS" : (t instanceof AssertionError) ? "FAIL" : "ERROR";
                msg = oneLine(t);
            } catch (Throwable t) {
                status = "ERROR";
                msg = oneLine(t);
            }
            out.println("RESULT " + i + " " + m.getName() + " " + status + " " + msg);
        }
        for (Method m : annotated(c, org.junit.jupiter.api.AfterAll.class)) {
            if (Modifier.isStatic(m.getModifiers())) m.invoke(null);
        }
        out.println("DONE");
    }
}
