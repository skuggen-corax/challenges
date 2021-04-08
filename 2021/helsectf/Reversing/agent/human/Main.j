.version 58 0 
.class public super agent/human/Main 
.super java/lang/Object 

.method public static main : ([Ljava/lang/String;)V 
    .code stack 3 locals 3 
L0:     getstatic Field java/lang/System out Ljava/io/PrintStream; 
L3:     ldc [s22] 
L5:     invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L8:     invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
L11:    getstatic Field java/lang/System out Ljava/io/PrintStream; 
L14:    ldc "V#J'C6-1Y#_6D,J?" 
L16:    invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L19:    invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
L22:    invokestatic Method agent/human/m ALLATORIxDEMO ()V 
L25:    new agent/human/K 
L28:    dup 
L29:    invokespecial Method agent/human/K <init> ()V 
L32:    astore_1 
L33:    new agent/human/c 
L36:    dup 
L37:    aload_1 
L38:    invokespecial Method agent/human/c <init> (Lagent/human/K;)V 
L41:    astore_1 
L42:    new java/lang/Thread 
L45:    dup 
L46:    aload_1 
L47:    invokespecial Method java/lang/Thread <init> (Ljava/lang/Runnable;)V 
L50:    invokevirtual Method java/lang/Thread start ()V 
L53:    invokestatic Method agent/human/Main ALLATORIxDEMO ()[B 
L56:    getstatic Field agent/human/c ALLATORIxDEMO [B 
L59:    invokestatic Method agent/human/Main ALLATORIxDEMO ([B[B)[B 
L62:    bipush 99 
L64:    istore_1 
L65:    pop 
L66:    iload_1 

        .stack full 
            locals Object [Ljava/lang/String; Integer 
            stack Integer 
        .end stack 
L67:    iconst_1 
L68:    if_icmpge L85 
L71:    getstatic Field java/lang/System out Ljava/io/PrintStream; 
L74:    ldc 'B\x0chB`\r\x7f\x07-\x16d\x0fhC' 
L76:    invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L79:    invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
L82:    bipush 99 
L84:    istore_1 

        .stack same 
L85:    getstatic Field java/lang/System out Ljava/io/PrintStream; 
L88:    iload_1 
L89:    iinc 1 -1 
L92:    dup 
L93:    invokedynamic [id80] 
L98:    invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
L101:   getstatic Field java/lang/System out Ljava/io/PrintStream; 
L104:   iload_1 
L105:   invokedynamic [id85] 
L110:   invokevirtual Method java/io/PrintStream println (Ljava/lang/String;)V 
        .catch java/lang/InterruptedException from L113 to L119 using L124 
L113:   ldc2_w 1000L 
L116:   invokestatic Method java/lang/Thread sleep (J)V 
L119:   iload_1 
L120:   goto L67 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L123:   athrow 

        .stack full 
            locals Object [Ljava/lang/String; Integer 
            stack Object java/lang/InterruptedException 
        .end stack 
L124:   astore_2 
L125:   iload_1 
L126:   goto L67 
L129:   
        .linenumbertable 
            L11 134 
            L22 120 
            L25 87 
            L33 5 
            L42 89 
            L50 153 
            L53 163 
            L56 20 
            L62 105 
            L66 138 
            L71 78 
            L82 112 
            L85 92 
            L89 16 
            L101 119 
            L113 45 
            L120 193 
            L124 172 
            L126 193 
        .end linenumbertable 
        .localvariabletable 
            0 is a [Ljava/lang/String; from L0 to L129 
        .end localvariabletable 
    .end code 
.end method 

.method public <init> : ()V 
    .code stack 1 locals 1 
L0:     aload_0 
L1:     invokespecial Method java/lang/Object <init> ()V 
L4:     return 
L5:     
        .linenumbertable 
            L0 76 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/Main; from L0 to L5 
        .end localvariabletable 
    .end code 
.end method 

.method public static c : ()[B 
    .code stack 5 locals 3 
L0:     ldc 'L N&H$J*D(F.@,B2\\0^6X4Z:T8l\x00n\x06h\x04j\nd\x08f\x0e`\x0cb\x12|\x10~\x16x\x14z\x1at\x18=S?Q9W;U5[' 
L2:     invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L5:     astore_0 
L6:     bipush 16 
L8:     newarray byte 
L10:    iconst_1 
L11:    dup 
L12:    pop2 
L13:    astore_1 
L14:    iconst_0 
L15:    dup 
L16:    istore_2 

        .stack full 
            locals Object java/lang/String Object [B Integer 
            stack Integer 
        .end stack 
L17:    bipush 16 
L19:    if_icmpge L52 
L22:    aload_1 
L23:    iload_2 
L24:    aload_0 
L25:    invokevirtual Method java/lang/String getBytes ()[B 
L28:    new java/util/Random 
L31:    dup 
L32:    invokespecial Method java/util/Random <init> ()V 
L35:    aload_0 
L36:    invokevirtual Method java/lang/String length ()I 
L39:    invokevirtual Method java/util/Random nextInt (I)I 
L42:    baload 
L43:    iinc 2 1 
L46:    bastore 
L47:    iload_2 
L48:    goto L17 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L51:    athrow 

        .stack append Object java/lang/String Object [B Integer 
L52:    aload_1 
L53:    areturn 
L54:    
        .linenumbertable 
            L0 147 
            L6 39 
            L14 71 
            L22 91 
            L47 71 
            L52 170 
        .end linenumbertable 
    .end code 
.end method 

.method public static ALLATORIxDEMO : (Ljava/lang/String;)Ljava/lang/String; 
    .code stack 7 locals 5 
L0:     iconst_5 
L1:     iconst_3 
L2:     ishl 
L3:     iconst_3 
L4:     ixor 
L5:     iconst_3 
L6:     iconst_5 
L7:     ixor 
L8:     iconst_4 
L9:     ishl 
L10:    iconst_3 
L11:    iconst_5 
L12:    ixor 
L13:    iconst_1 
L14:    ishl 
L15:    ixor 
L16:    iconst_3 
L17:    iconst_5 
L18:    ixor 
L19:    iconst_4 
L20:    ishl 
L21:    iconst_3 
L22:    iconst_1 
L23:    ishl 
L24:    ixor 
L25:    aload_0 
L26:    checkcast java/lang/String 
L29:    dup 
L30:    astore_0 
L31:    invokevirtual Method java/lang/String length ()I 
L34:    dup 
L35:    newarray char 
L37:    iconst_1 
L38:    dup 
L39:    pop2 
L40:    swap 
L41:    iconst_1 
L42:    isub 
L43:    dup_x2 
L44:    istore_3 
L45:    astore_1 
L46:    istore 4 
L48:    dup_x2 
L49:    pop2 
L50:    istore_2 

        .stack full 
            locals Object java/lang/String Object [C Integer Integer Integer 
            stack Integer 
        .end stack 
L51:    iflt L91 
L54:    aload_1 
L55:    aload_0 
L56:    iload_3 
L57:    dup_x1 
L58:    invokevirtual Method java/lang/String charAt (I)C 
L61:    iinc 3 -1 
L64:    iload_2 
L65:    ixor 
L66:    i2c 
L67:    castore 
L68:    iload_3 
L69:    iflt L91 
L72:    aload_1 
L73:    aload_0 
L74:    iload_3 
L75:    iinc 3 -1 
L78:    dup_x1 
L79:    invokevirtual Method java/lang/String charAt (I)C 
L82:    iload 4 
L84:    ixor 
L85:    i2c 
L86:    castore 
L87:    iload_3 
L88:    goto L51 

        .stack same 
L91:    new java/lang/String 
L94:    dup 
L95:    aload_1 
L96:    invokespecial Method java/lang/String <init> ([C)V 
L99:    areturn 
L100:   
        .localvariabletable 
            0 is a Ljava/lang/String; from L0 to L100 
        .end localvariabletable 
    .end code 
.end method 

.method public static ALLATORIxDEMO : ([B[B)[B 
    .code stack 8 locals 7 
L0:     aload_1 
L1:     arraylength 
L2:     newarray byte 
L4:     iconst_1 
L5:     dup 
L6:     pop2 
L7:     astore_2 
L8:     iconst_0 
L9:     istore_3 
L10:    iconst_0 
L11:    istore 4 
L13:    iconst_0 
L14:    dup 
L15:    istore 6 

        .stack full 
            locals Object [B Object [B Object [B Integer Integer Top Integer 
            stack Integer 
        .end stack 
L17:    aload_1 
L18:    arraylength 
L19:    if_icmpge L107 
L22:    iload_3 
L23:    iconst_1 
L24:    iadd 
L25:    sipush 256 
L28:    irem 
L29:    istore_3 
L30:    iload 4 
L32:    aload_0 
L33:    iload_3 
L34:    baload 
L35:    sipush 255 
L38:    iand 
L39:    iadd 
L40:    sipush 256 
L43:    irem 
L44:    istore 4 
L46:    aload_2 
L47:    aload_0 
L48:    dup 
L49:    dup2 
L50:    iload 4 
L52:    baload 
L53:    istore 5 
L55:    iload 4 
L57:    aload_0 
L58:    dup_x2 
L59:    iload_3 
L60:    baload 
L61:    bastore 
L62:    iload_3 
L63:    iload 5 
L65:    bastore 
L66:    iload_3 
L67:    baload 
L68:    sipush 255 
L71:    iand 
L72:    aload_0 
L73:    iload 4 
L75:    baload 
L76:    sipush 255 
L79:    iand 
L80:    iadd 
L81:    sipush 256 
L84:    irem 
L85:    baload 
L86:    istore 5 
L88:    aload_1 
L89:    iload 6 
L91:    dup_x1 
L92:    baload 
L93:    iload 5 
L95:    ixor 
L96:    i2b 
L97:    iinc 6 1 
L100:   bastore 
L101:   iload 6 
L103:   goto L17 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L106:   athrow 

        .stack full 
            locals Object [B Object [B Object [B Integer Integer Top Integer 
            stack 
        .end stack 
L107:   aload_2 
L108:   areturn 
L109:   
        .linenumbertable 
            L0 117 
            L8 207 
            L10 90 
            L13 96 
            L22 68 
            L30 124 
            L47 47 
            L55 144 
            L62 32 
            L66 36 
            L88 33 
            L101 96 
            L107 59 
        .end linenumbertable 
        .localvariabletable 
            0 is a [B from L0 to L109 
            1 is a [B from L0 to L109 
        .end localvariabletable 
    .end code 
.end method 

.method public static ALLATORIxDEMO : ()[B 
    .code stack 5 locals 5 
L0:     sipush 256 
L3:     newarray byte 
L5:     iconst_1 
L6:     dup 
L7:     pop2 
L8:     astore_0 
L9:     invokestatic Method agent/human/Main c ()[B 
L12:    astore_1 
L13:    iconst_0 
L14:    dup 
L15:    istore_2 

        .stack full 
            locals Object [B Object [B Integer 
            stack Integer 
        .end stack 
L16:    sipush 256 
L19:    if_icmpge L35 
L22:    aload_0 
L23:    iload_2 
L24:    dup 
L25:    i2b 
L26:    iinc 2 1 
L29:    bastore 
L30:    iload_2 
L31:    goto L16 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L34:    athrow 

        .stack append Object [B Object [B Integer 
L35:    iconst_0 
L36:    istore_2 
L37:    iconst_0 
L38:    dup 
L39:    istore 4 

        .stack full 
            locals Object [B Object [B Integer Top Integer 
            stack Integer 
        .end stack 
L41:    sipush 256 
L44:    if_icmpge L96 
L47:    iload_2 
L48:    aload_0 
L49:    iload 4 
L51:    baload 
L52:    sipush 255 
L55:    iand 
L56:    iadd 
L57:    aload_1 
L58:    iload 4 
L60:    bipush 16 
L62:    irem 
L63:    baload 
L64:    iadd 
L65:    sipush 256 
L68:    irem 
L69:    istore_2 
L70:    aload_0 
L71:    dup 
L72:    iload_2 
L73:    baload 
L74:    istore_3 
L75:    iload_2 
L76:    aload_0 
L77:    dup_x2 
L78:    iload 4 
L80:    baload 
L81:    bastore 
L82:    iload 4 
L84:    iload_3 
L85:    i2b 
L86:    iinc 4 1 
L89:    bastore 
L90:    iload 4 
L92:    goto L41 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L95:    athrow 

        .stack full 
            locals Object [B Object [B Integer Top Integer 
            stack 
        .end stack 
L96:    aload_0 
L97:    areturn 
L98:    
        .linenumbertable 
            L0 190 
            L9 41 
            L13 125 
            L22 102 
            L30 125 
            L35 184 
            L37 129 
            L47 21 
            L70 146 
            L75 175 
            L82 108 
            L90 129 
            L96 171 
        .end linenumbertable 
    .end code 
.end method 
.innerclasses 
    java/lang/invoke/MethodHandles$Lookup java/lang/invoke/MethodHandles Lookup public static final 
.end innerclasses 
.sourcefile c 
.const [s22] = String [u21] 
.const [id80] = InvokeDynamic invokeStatic Method java/lang/invoke/StringConcatFactory makeConcatWithConstants (Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite; String '\x01 bottles of beer on the wall, \x01 bottles of beer!' : makeConcatWithConstants (II)Ljava/lang/String; 
.const [id85] = InvokeDynamic invokeStatic Method java/lang/invoke/StringConcatFactory makeConcatWithConstants (Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite; String 'Take one down, pass it around, \x01 bottles of beer on the wall!' : makeConcatWithConstants (I)Ljava/lang/String; 
.const [u21] = Utf8 'h.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A\x07A-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B.h.B-B-B-B-A.B.B-B.B-B-A.B.A.B.A.B.A-B.A.B-B-B-B-A\x07A-B-B-B-A-A-A-B-A-B-A-A-B.B-A-A-A-A-B.B-B-B-B-B.h.B-B-B-B.A.B.B-B.B-B.A.B-A-B.B.B.A-B-A-B-B-B-B-A\x07A-B-B-B-A-A-A.A-A.A-A-A-B.B-A.A-A-A-A.A-B-B-B-B.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\x07A--o\x04x\x11n\x03y\x0bb\x0c-\x00tBL\x0ea\x03y\r\x7f\x0b--o\x04x\x11n\x03y\r\x7fB{U#U-&H/BB.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\x07A-B-B-B-B-B-\ny\x16}X"Mz\x15zLl\x0ea\x03y\r\x7f\x0b#\x01b\x0f-B-B-B-B-B-B.h.B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-B-A\x07A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.A.h' 
.end class 
