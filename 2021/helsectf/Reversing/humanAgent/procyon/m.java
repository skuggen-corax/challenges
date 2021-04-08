// 
// Decompiled by Procyon v0.5.36
// 

package agent.human;

import java.util.Iterator;
import java.util.ArrayList;
import java.io.File;

public class m
{
    public static void c() {
        ProcessHandle.allProcesses().forEach(a -> c(a));
    }
    
    public static void ALLATORIxDEMO() {
        if (new File(K.ALLATORIxDEMO("M")).getTotalSpace() < 85899345920L) {
            System.exit(-1);
        }
    }
    
    public static void c(final ProcessHandle a) {
        final ArrayList<String> list = new ArrayList<String>();
        list.add(K.ALLATORIxDEMO("\u0014`\u0016b\ra\u0011"));
        list.add(Main.ALLATORIxDEMO("\u0010F\u0011J\u0014N"));
        list.add(K.ALLATORIxDEMO("{\u0000b\u001a"));
        list.add(Main.ALLATORIxDEMO("\u0010B\u0014_\u0013J\nI\tS"));
        if (!a.isAlive()) {
            return;
        }
        final String string = a.info().command().toString();
        final Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            if (string.toLowerCase().contains(iterator.next())) {
                System.exit(-1);
            }
        }
    }
}
