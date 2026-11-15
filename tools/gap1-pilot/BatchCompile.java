import javax.tools.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/**
 * Biên dịch hàng loạt trong một JVM (tránh tốn thời gian khởi động javac cho từng file).
 * Đầu vào (stdin): mỗi dòng "đường_dẫn_nguồn<TAB>thư_mục_đầu_ra".
 * Đầu ra (stdout): mỗi dòng "OK<TAB>nguồn" hoặc "CE<TAB>nguồn<TAB>thông báo lỗi đầu tiên".
 */
public class BatchCompile {
    public static void main(String[] args) throws Exception {
        JavaCompiler jc = ToolProvider.getSystemJavaCompiler();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
        String line;
        while ((line = br.readLine()) != null) {
            String[] p = line.split("\t");
            if (p.length < 2) continue;
            Path out = Paths.get(p[1]);
            Files.createDirectories(out);
            DiagnosticCollector<JavaFileObject> dc = new DiagnosticCollector<>();
            try (StandardJavaFileManager fm = jc.getStandardFileManager(dc, null, StandardCharsets.UTF_8)) {
                Iterable<? extends JavaFileObject> units = fm.getJavaFileObjects(new File(p[0]));
                List<String> opts = Arrays.asList("-d", out.toString(), "-nowarn", "-encoding", "UTF-8",
                        "-proc:none", "-Xlint:none");
                boolean ok;
                try {
                    ok = jc.getTask(null, fm, dc, opts, null, units).call();
                } catch (Throwable t) {
                    ok = false;
                }
                if (ok) {
                    System.out.println("OK\t" + p[0]);
                } else {
                    String msg = "";
                    for (Diagnostic<? extends JavaFileObject> d : dc.getDiagnostics()) {
                        if (d.getKind() == Diagnostic.Kind.ERROR) {
                            msg = d.getMessage(Locale.ROOT).replace('\n', ' ').replace('\t', ' ');
                            break;
                        }
                    }
                    System.out.println("CE\t" + p[0] + "\t" + msg);
                }
            }
            System.out.flush();
        }
    }
}
