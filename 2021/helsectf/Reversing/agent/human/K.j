.version 58 0 
.class public super agent/human/K 
.super java/lang/Object 
.field private F Ljava/lang/String; 
.field private ALLATORIxDEMO I 

.method public ALLATORIxDEMO : ()Ljava/lang/String; 
    .code stack 1 locals 1 
L0:     aload_0 
L1:     getfield Field agent/human/K F Ljava/lang/String; 
L4:     areturn 
L5:     
        .linenumbertable 
            L0 89 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/K; from L0 to L5 
        .end localvariabletable 
    .end code 
.end method 

.method public ALLATORIxDEMO : ()I 
    .code stack 1 locals 1 
L0:     aload_0 
L1:     getfield Field agent/human/K ALLATORIxDEMO I 
L4:     ireturn 
L5:     
        .linenumbertable 
            L0 105 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/K; from L0 to L5 
        .end localvariabletable 
    .end code 
.end method 

.method public <init> : ()V 
    .code stack 5 locals 1 
L0:     sipush 30015 
L3:     aload_0 
L4:     dup_x1 
L5:     ldc 'challenges.ctfd.io' 
L7:     aload_0 
L8:     invokespecial Method java/lang/Object <init> ()V 
L11:    putfield Field agent/human/K F Ljava/lang/String; 
L14:    putfield Field agent/human/K ALLATORIxDEMO I 
L17:    return 
L18:    
        .linenumbertable 
            L0 8 
            L11 120 
            L14 195 
            L17 87 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/K; from L0 to L18 
        .end localvariabletable 
    .end code 
.end method 

.method public static ALLATORIxDEMO : (Ljava/lang/String;)Ljava/lang/String; 
    .code stack 7 locals 5 
L0:     iconst_3 
L1:     iconst_5 
L2:     ixor 
L3:     iconst_4 
L4:     ishl 
L5:     iconst_1 
L6:     dup 
L7:     ishl 
L8:     ixor 
L9:     iconst_1 
L10:    iconst_3 
L11:    ishl 
L12:    iconst_2 
L13:    iconst_5 
L14:    ixor 
L15:    ixor 
L16:    iconst_1 
L17:    iconst_3 
L18:    ishl 
L19:    iconst_5 
L20:    ixor 
L21:    aload_0 
L22:    checkcast java/lang/String 
L25:    dup 
L26:    astore_0 
L27:    invokevirtual Method java/lang/String length ()I 
L30:    dup 
L31:    newarray char 
L33:    iconst_1 
L34:    dup 
L35:    pop2 
L36:    swap 
L37:    iconst_1 
L38:    isub 
L39:    dup_x2 
L40:    istore_3 
L41:    astore_1 
L42:    istore 4 
L44:    dup_x2 
L45:    pop2 
L46:    istore_2 

        .stack full 
            locals Object java/lang/String Object [C Integer Integer Integer 
            stack Integer 
        .end stack 
L47:    iflt L87 
L50:    aload_1 
L51:    aload_0 
L52:    iload_3 
L53:    dup_x1 
L54:    invokevirtual Method java/lang/String charAt (I)C 
L57:    iinc 3 -1 
L60:    iload_2 
L61:    ixor 
L62:    i2c 
L63:    castore 
L64:    iload_3 
L65:    iflt L87 
L68:    aload_1 
L69:    aload_0 
L70:    iload_3 
L71:    iinc 3 -1 
L74:    dup_x1 
L75:    invokevirtual Method java/lang/String charAt (I)C 
L78:    iload 4 
L80:    ixor 
L81:    i2c 
L82:    castore 
L83:    iload_3 
L84:    goto L47 

        .stack same 
L87:    new java/lang/String 
L90:    dup 
L91:    aload_1 
L92:    invokespecial Method java/lang/String <init> ([C)V 
L95:    areturn 
L96:    
        .localvariabletable 
            0 is a Ljava/lang/String; from L0 to L96 
        .end localvariabletable 
    .end code 
.end method 
.sourcefile p 
.end class 
