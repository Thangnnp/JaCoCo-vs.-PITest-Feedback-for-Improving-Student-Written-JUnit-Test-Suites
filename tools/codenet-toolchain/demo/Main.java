import java.util.Scanner;

// DEMO, KHÔNG phải submission CodeNet thật: lời giải tự viết cho bài p02546 (danh từ số nhiều)
// chỉ để thử bộ công cụ. Khi chạy thật, thay bằng file sXXXXXXXXX.java lấy từ Project_CodeNet_Java250.
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        if (s.endsWith("s")) {
            System.out.println(s + "es");
        } else {
            System.out.println(s + "s");
        }
    }
}
