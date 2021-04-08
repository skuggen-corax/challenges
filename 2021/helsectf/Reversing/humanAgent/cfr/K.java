/*
 * Decompiled with CFR 0.150.
 */
package agent.human;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public class K {
    private String F;
    private int ALLATORIxDEMO;

    public String ALLATORIxDEMO() {
        K a;
        return a.F;
    }

    public int ALLATORIxDEMO() {
        K a;
        return a.ALLATORIxDEMO;
    }

    public K() {
        K a;
        K k = a;
        k.F = "challenges.ctfd.io";
        k.ALLATORIxDEMO = 30015;
    }

    public static String ALLATORIxDEMO(String a) {
        int n = a.length();
        int n2 = n - 1;
        char[] arrc = new char[n];
        int n3 = 1 << 3 ^ 5;
        int cfr_ignored_0 = 1 << 3 ^ (2 ^ 5);
        int n4 = n2;
        int n5 = (3 ^ 5) << 4 ^ 1 << 1;
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
}