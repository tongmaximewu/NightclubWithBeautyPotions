import java.io.*;
import java.util.*;

/**
 * Nightclub Queue with Beauty Potions
 *
 * This program reads:
 *   n
 *   beauty[0..n-1]
 *   limit[0..n-1]
 *   k
 *
 * and prints the time (number of people admitted before and including k)
 * at which person k enters the club, or -1 if they never enter.
 */
public class Main {

    private static class Person {
        int idx;
        int beauty;
        int limit;

        Person(int idx, int beauty, int limit) {
            this.idx = idx;
            this.beauty = beauty;
            this.limit = limit;
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner(System.in);

        int n;
        try {
            n = fs.nextInt();
        } catch (IOException e) {
            return; // no input
        }

        int[] beauty = new int[n];
        int[] limit = new int[n];

        for (int i = 0; i < n; i++) {
            beauty[i] = fs.nextInt();
        }
        for (int i = 0; i < n; i++) {
            limit[i] = fs.nextInt();
        }

        int k = fs.nextInt();

        final int THRESHOLD = 8;
        final int MAX_BEAUTY = 10;

        Queue<Person> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            queue.offer(new Person(i, beauty[i], limit[i]));
        }

        long time = 0; // number of people admitted so far

        while (!queue.isEmpty()) {
            Person p = queue.poll();

            if (p.beauty >= THRESHOLD) {
                time++;
                if (p.idx == k) {
                    System.out.println(time);
                    return;
                }
                continue;
            }

            if (p.limit == 0) {
                if (p.idx == k) {
                    System.out.println(-1);
                    return;
                }
                continue;
            }

            p.beauty = Math.min(p.beauty + 1, MAX_BEAUTY);
            p.limit--;
            queue.offer(p);
        }

        System.out.println(-1);
    }

    private static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

        FastScanner(InputStream is) {
            in = is;
        }

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
                if (c == -1) throw new EOFException();
            } while (c <= ' ');

            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }

            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }
}
