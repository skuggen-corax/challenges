// 
// Decompiled by Procyon v0.5.36
// 

package agent.human;

public class K
{
    private String F;
    private int ALLATORIxDEMO;
    
    public String ALLATORIxDEMO() {
        return this.F;
    }
    
    public int ALLATORIxDEMO() {
        return this.ALLATORIxDEMO;
    }
    
    public K() {
        final int allatorIxDEMO = 30015;
        final String f = "challenges.ctfd.io";
        this.F = f;
        this.ALLATORIxDEMO = allatorIxDEMO;
    }
    
    public static String ALLATORIxDEMO(String a) {
        final int n = (0x3 ^ 0x5) << 4;
        final int n2 = 1;
        final int n3 = n ^ n2 << n2;
        final int n4 = 1 << 3 ^ 0x5;
        final int length = (a = a).length();
        final char[] array = new char[length];
        int n5;
        int i = n5 = length - 1;
        final char[] value = array;
        final char c = (char)n4;
        final int n6 = n3;
        while (i >= 0) {
            final char[] array2 = value;
            final String s = a;
            final int index = n5;
            final char char1 = s.charAt(index);
            --n5;
            array2[index] = (char)(char1 ^ n6);
            if (n5 < 0) {
                break;
            }
            final char[] array3 = value;
            final String s2 = a;
            final int index2 = n5--;
            array3[index2] = (char)(s2.charAt(index2) ^ c);
            i = n5;
        }
        return new String(value);
    }
}