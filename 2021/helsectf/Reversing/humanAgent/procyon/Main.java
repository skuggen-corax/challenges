// 
// Decompiled by Procyon v0.5.36
// 

package agent.human;

import java.util.Random;
import java.io.PrintStream;

public class Main
{
    public static void main(final String[] a) {
        System.out.println(K.ALLATORIxDEMO("h.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A\u0007A-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B.h.B-B-B-B-A.B.B-B.B-B-A.B.A.B.A.B.A-B.A.B-B-B-B-A\u0007A-B-B-B-A-A-A-B-A-B-A-A-B.B-A-A-A-A-B.B-B-B-B-B.h.B-B-B-B.A.B.B-B.B-B.A.B-A-B.B.B.A-B-A-B-B-B-B-A\u0007A-B-B-B-A-A-A.A-A.A-A-A-B.B-A.A-A-A-A.A-B-B-B-B.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\u0007A--o\u0004x\u0011n\u0003y\u000bb\f-\u0000tBL\u000ea\u0003y\r\u007f\u000b--o\u0004x\u0011n\u0003y\r\u007fB{U#U-&H/BB.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\u0007A-B-B-B-B-B-\ny\u0016}X\"Mz\u0015zLl\u000ea\u0003y\r\u007f\u000b#\u0001b\u000f-B-B-B-B-B-B.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\u0007A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.h"));
        System.out.println(K.ALLATORIxDEMO("V#J'C6-1Y#_6D,J?"));
        m.ALLATORIxDEMO();
        new Thread(new c(new K())).start();
        ALLATORIxDEMO(ALLATORIxDEMO(), c.ALLATORIxDEMO);
        int n2;
        int n = n2 = 99;
        while (true) {
            if (n2 < 1) {
                System.out.println(K.ALLATORIxDEMO("B\fhB`\r\u007f\u0007-\u0016d\u000fhC"));
                n = 99;
            }
            final PrintStream out = System.out;
            final int n3 = n--;
            out.println(invokedynamic(makeConcatWithConstants:(II)Ljava/lang/String;, n3, n3));
            System.out.println(invokedynamic(makeConcatWithConstants:(I)Ljava/lang/String;, n));
            try {
                Thread.sleep(1000L);
                n2 = n;
            }
            catch (InterruptedException ex) {
                n2 = n;
            }
        }
    }
    
    public static byte[] c() {
        final String allatorIxDEMO = K.ALLATORIxDEMO("L N&H$J*D(F.@,B2\\0^6X4Z:T8l\u0000n\u0006h\u0004j\nd\bf\u000e`\fb\u0012|\u0010~\u0016x\u0014z\u001at\u0018=S?Q9W;U5[");
        final byte[] array = new byte[16];
        int n;
        int i = n = 0;
        while (i < 16) {
            final byte[] array2 = array;
            final int n2 = n;
            final byte b = allatorIxDEMO.getBytes()[new Random().nextInt(allatorIxDEMO.length())];
            ++n;
            array2[n2] = b;
            i = n;
        }
        return array;
    }
    
    public static String ALLATORIxDEMO(String a) {
        final int n = 5 << 3 ^ 0x3;
        final int n2 = (0x3 ^ 0x5) << 4 ^ 3 << 1;
        final int length = (a = a).length();
        final char[] array = new char[length];
        int n3;
        int i = n3 = length - 1;
        final char[] value = array;
        final char c = (char)n2;
        final int n4 = n;
        while (i >= 0) {
            final char[] array2 = value;
            final String s = a;
            final int index = n3;
            final char char1 = s.charAt(index);
            --n3;
            array2[index] = (char)(char1 ^ n4);
            if (n3 < 0) {
                break;
            }
            final char[] array3 = value;
            final String s2 = a;
            final int index2 = n3--;
            array3[index2] = (char)(s2.charAt(index2) ^ c);
            i = n3;
        }
        return new String(value);
    }
    
    public static byte[] ALLATORIxDEMO(final byte[] a, final byte[] a) {
        final byte[] array = new byte[a.length];
        int n = 0;
        int n2 = 0;
        int n3;
        int i = n3 = 0;
        while (i < a.length) {
            n = (n + 1) % 256;
            n2 = (n2 + (a[n] & 0xFF)) % 256;
            final byte[] array2 = array;
            final byte b = a[n2];
            a[n2] = a[n];
            a[n] = b;
            final byte b2 = a[((a[n] & 0xFF) + (a[n2] & 0xFF)) % 256];
            final int n4 = n3;
            final byte b3 = (byte)(a[n4] ^ b2);
            ++n3;
            array2[n4] = b3;
            i = n3;
        }
        return array;
    }
    
    public static byte[] ALLATORIxDEMO() {
        final byte[] array = new byte[256];
        final byte[] c = c();
        int n;
        int i = n = 0;
        while (i < 256) {
            final byte[] array2 = array;
            final int n2 = n;
            final byte b = (byte)n2;
            ++n;
            array2[n2] = b;
            i = n;
        }
        int n3 = 0;
        int n4;
        int j = n4 = 0;
        while (j < 256) {
            n3 = (n3 + (array[n4] & 0xFF) + c[n4 % 16]) % 256;
            final byte[] array3 = array;
            final byte b2 = array3[n3];
            final int n5 = n3;
            final byte[] array4 = array;
            array3[n5] = array4[n4];
            final int n6 = n4;
            final byte b3 = b2;
            ++n4;
            array4[n6] = b3;
            j = n4;
        }
        return array;
    }
}