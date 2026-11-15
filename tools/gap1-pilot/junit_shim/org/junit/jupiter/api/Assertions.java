package org.junit.jupiter.api;

import java.util.Arrays;
import java.util.Objects;
import java.util.function.Supplier;
import org.junit.jupiter.api.function.Executable;
import org.junit.jupiter.api.function.ThrowingSupplier;

/**
 * Bản thay thế TỐI GIẢN của org.junit.jupiter.api.Assertions, chỉ để chạy thử quy trình đo khi không có
 * thư viện JUnit 5 thật. Ngữ nghĩa so sánh giống JUnit 5 cho các overload được hỗ trợ. Thực nghiệm chính
 * dùng JUnit 5 thật (junit_eval.py --junit-jar).
 */
public final class Assertions {
    private Assertions() {}

    private static String m(Object msg) {
        if (msg instanceof Supplier) msg = ((Supplier<?>) msg).get();
        return msg == null ? "" : msg + " ==> ";
    }
    private static void failNotEqual(Object e, Object a, Object msg) {
        throw new AssertionError(m(msg) + "expected: <" + e + "> but was: <" + a + ">");
    }

    public static void assertEquals(Object e, Object a) { assertEquals(e, a, (String) null); }
    public static void assertEquals(Object e, Object a, String msg) { if (!Objects.equals(e, a)) failNotEqual(e, a, msg); }
    public static void assertEquals(Object e, Object a, Supplier<String> msg) { if (!Objects.equals(e, a)) failNotEqual(e, a, msg); }
    public static void assertEquals(long e, long a) { if (e != a) failNotEqual(e, a, null); }
    public static void assertEquals(long e, long a, String msg) { if (e != a) failNotEqual(e, a, msg); }
    public static void assertEquals(int e, int a) { if (e != a) failNotEqual(e, a, null); }
    public static void assertEquals(int e, int a, String msg) { if (e != a) failNotEqual(e, a, msg); }
    public static void assertEquals(double e, double a) { if (Double.doubleToLongBits(e) != Double.doubleToLongBits(a)) failNotEqual(e, a, null); }
    public static void assertEquals(double e, double a, double d) { if (Math.abs(e - a) > d) failNotEqual(e, a, null); }
    public static void assertEquals(double e, double a, double d, String msg) { if (Math.abs(e - a) > d) failNotEqual(e, a, msg); }
    public static void assertEquals(char e, char a) { if (e != a) failNotEqual(e, a, null); }
    public static void assertEquals(boolean e, boolean a) { if (e != a) failNotEqual(e, a, null); }

    public static void assertNotEquals(Object u, Object a) { if (Objects.equals(u, a)) throw new AssertionError("expected: not equal but was: <" + a + ">"); }
    public static void assertNotEquals(Object u, Object a, String msg) { if (Objects.equals(u, a)) throw new AssertionError(m(msg) + "expected: not equal but was: <" + a + ">"); }
    public static void assertNotEquals(long u, long a) { if (u == a) throw new AssertionError("expected: not equal but was: <" + a + ">"); }

    public static void assertTrue(boolean c) { if (!c) throw new AssertionError("expected: <true> but was: <false>"); }
    public static void assertTrue(boolean c, String msg) { if (!c) throw new AssertionError(m(msg) + "expected: <true> but was: <false>"); }
    public static void assertTrue(boolean c, Supplier<String> msg) { if (!c) throw new AssertionError(m(msg) + "expected: <true> but was: <false>"); }
    public static void assertFalse(boolean c) { if (c) throw new AssertionError("expected: <false> but was: <true>"); }
    public static void assertFalse(boolean c, String msg) { if (c) throw new AssertionError(m(msg) + "expected: <false> but was: <true>"); }
    public static void assertNull(Object o) { if (o != null) throw new AssertionError("expected: <null> but was: <" + o + ">"); }
    public static void assertNotNull(Object o) { if (o == null) throw new AssertionError("expected: not <null>"); }
    public static void assertNotNull(Object o, String msg) { if (o == null) throw new AssertionError(m(msg) + "expected: not <null>"); }
    public static void assertArrayEquals(Object[] e, Object[] a) { if (!Arrays.deepEquals(e, a)) failNotEqual(Arrays.deepToString(e), Arrays.deepToString(a), null); }
    public static void assertArrayEquals(int[] e, int[] a) { if (!Arrays.equals(e, a)) failNotEqual(Arrays.toString(e), Arrays.toString(a), null); }
    public static void assertArrayEquals(long[] e, long[] a) { if (!Arrays.equals(e, a)) failNotEqual(Arrays.toString(e), Arrays.toString(a), null); }

    public static <T> T fail(String msg) { throw new AssertionError(msg); }
    public static <T> T fail() { throw new AssertionError(); }

    public static void assertAll(Executable... ex) {
        AssertionError first = null;
        for (Executable e : ex) {
            try { e.execute(); }
            catch (AssertionError err) { if (first == null) first = err; }
            catch (Throwable t) { if (first == null) first = new AssertionError("unexpected exception: " + t, t); }
        }
        if (first != null) throw first;
    }
    public static void assertAll(String heading, Executable... ex) { assertAll(ex); }

    @SuppressWarnings("unchecked")
    public static <T extends Throwable> T assertThrows(Class<T> type, Executable ex) {
        try { ex.execute(); }
        catch (Throwable t) {
            if (type.isInstance(t)) return (T) t;
            throw new AssertionError("Unexpected exception type thrown, expected: <" + type.getName() + "> but was: <" + t.getClass().getName() + ">", t);
        }
        throw new AssertionError("Expected " + type.getName() + " to be thrown, but nothing was thrown.");
    }
    public static <T extends Throwable> T assertThrows(Class<T> type, Executable ex, String msg) { return assertThrows(type, ex); }
    public static void assertDoesNotThrow(Executable ex) {
        try { ex.execute(); } catch (Throwable t) { throw new AssertionError("Unexpected exception thrown: " + t, t); }
    }
    public static <T> T assertDoesNotThrow(ThrowingSupplier<T> s) {
        try { return s.get(); } catch (Throwable t) { throw new AssertionError("Unexpected exception thrown: " + t, t); }
    }
}
