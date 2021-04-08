/*
 * Decompiled with CFR 0.150.
 */
package agent.human;

import agent.human.K;
import agent.human.c;
import agent.human.m;
import java.util.Random;

public class Main {
    public static void main(String[] a) {
        System.out.println(K.ALLATORIxDEMO("h.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A\u0007A-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B.h.B-B-B-B-A.B.B-B.B-B-A.B.A.B.A.B.A-B.A.B-B-B-B-A\u0007A-B-B-B-A-A-A-B-A-B-A-A-B.B-A-A-A-A-B.B-B-B-B-B.h.B-B-B-B.A.B.B-B.B-B.A.B-A-B.B.B.A-B-A-B-B-B-B-A\u0007A-B-B-B-A-A-A.A-A.A-A-A-B.B-A.A-A-A-A.A-B-B-B-B.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\u0007A--o\u0004x\u0011n\u0003y\u000bb\f-\u0000tBL\u000ea\u0003y\r\u007f\u000b--o\u0004x\u0011n\u0003y\r\u007fB{U#U-&H/BB.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\u0007A-B-B-B-B-B-\ny\u0016}X\"Mz\u0015zLl\u000ea\u0003y\r\u007f\u000b#\u0001b\u000f-B-B-B-B-B-B.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\u0007A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.h"));
        System.out.println(K.ALLATORIxDEMO("V#J'C6-1Y#_6D,J?"));
        m.ALLATORIxDEMO();
        Object object = new K();
        object = new c((K)object);
        new Thread((Runnable)object).start();
        Main.ALLATORIxDEMO(Main.ALLATORIxDEMO(), c.ALLATORIxDEMO);
        int n = 99;
        int n2 = n;
        while (true) {
            if (n2 < 1) {
                System.out.println(K.ALLATORIxDEMO("B\fhB`\r\u007f\u0007-\u0016d\u000fhC"));
                n = 99;
            }
            int n3 = n--;
            System.out.println(n3 + " bottles of beer on the wall, " + n3 + " bottles of beer!");
            System.out.println("Take one down, pass it around, " + n + " bottles of beer on the wall!");
            try {
                Thread.sleep(1000L);
                n2 = n;
                continue;
            }
            catch (InterruptedException interruptedException) {
                n2 = n;
                continue;
            }
            break;
        }
    }

    public Main() {
        Main a;
    }

    public static byte[] c() {
        int n;
        String string = K.ALLATORIxDEMO("L N&H$J*D(F.@,B2\\0^6X4Z:T8l\u0000n\u0006h\u0004j\nd\bf\u000e`\fb\u0012|\u0010~\u0016x\u0014z\u001at\u0018=S?Q9W;U5[");
        byte[] arrby = new byte[16];
        int n2 = n = 0;
        while (n2 < 16) {
            arrby[n++] = string.getBytes()[new Random().nextInt(string.length())];
            n2 = n;
        }
        return arrby;
    }

    public static String ALLATORIxDEMO(String a) {
        int n = a.length();
        int n2 = n - 1;
        char[] arrc = new char[n];
        int n3 = (3 ^ 5) << 4 ^ 3 << 1;
        int cfr_ignored_0 = (3 ^ 5) << 4 ^ (3 ^ 5) << 1;
        int n4 = n2;
        int n5 = 5 << 3 ^ 3;
        while (n4 >= 0) {
            int n6 = n2--;
            arrc[n6] = (char)(a.charAt(n6) ^ n5);
            if (n2 < 0) break;
            int n7 = n2--;
            arrc[n7] = (char)(a.charAt(n7) ^ n3);
            n4 = n2;
        }
        return new String(arrc);
    }

    public static byte[] ALLATORIxDEMO(byte[] a, byte[] a2) {
        int n;
        byte[] arrby = new byte[a2.length];
        int n2 = 0;
        int n3 = 0;
        int n4 = n = 0;
        while (n4 < a2.length) {
            n2 = (n2 + 1) % 256;
            n3 = (n3 + (a[n2] & 0xFF)) % 256;
            byte[] arrby2 = a;
            byte by = a[n3];
            arrby2[n3] = a[n2];
            a[n2] = by;
            by = arrby2[((a[n2] & 0xFF) + (a[n3] & 0xFF)) % 256];
            int n5 = n++;
            arrby[n5] = (byte)(a2[n5] ^ by);
            n4 = n;
        }
        return arrby;
    }

    public static byte[] ALLATORIxDEMO() {
        int n;
        int n2;
        byte[] arrby = new byte[256];
        byte[] arrby2 = Main.c();
        int n3 = n2 = 0;
        while (n3 < 256) {
            int n4 = n2++;
            arrby[n4] = (byte)n4;
            n3 = n2;
        }
        n2 = 0;
        int n5 = n = 0;
        while (n5 < 256) {
            n2 = (n2 + (arrby[n] & 0xFF) + arrby2[n % 16]) % 256;
            byte by = arrby[n2];
            arrby[n2] = arrby[n];
            arrby[n++] = by;
            n5 = n;
        }
        return arrby;
    }
}