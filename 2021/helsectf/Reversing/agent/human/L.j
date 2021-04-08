.version 58 0 
.class super agent/human/L 
.super java/lang/Object 
.implements javax/net/ssl/X509TrustManager 
.field final synthetic ALLATORIxDEMO Lagent/human/c; 

.method public getAcceptedIssuers : ()[Ljava/security/cert/X509Certificate; 
    .code stack 1 locals 1 
L0:     aconst_null 
L1:     areturn 
L2:     
        .linenumbertable 
            L0 56 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/L; from L0 to L2 
        .end localvariabletable 
    .end code 
.end method 

.method public checkClientTrusted : ([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V 
    .code stack 0 locals 3 
L0:     return 
L1:     
        .linenumbertable 
            L0 92 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/L; from L0 to L0 
            1 is a [Ljava/security/cert/X509Certificate; from L0 to L0 
            2 is a Ljava/lang/String; from L0 to L0 
        .end localvariabletable 
    .end code 
.end method 

.method <init> : (Lagent/human/c;)V 
    .code stack 3 locals 2 
L0:     aload_0 
L1:     dup 
L2:     aload_1 
L3:     putfield Field agent/human/L ALLATORIxDEMO Lagent/human/c; 
L6:     invokespecial Method java/lang/Object <init> ()V 
L9:     return 
L10:    
        .linenumbertable 
            L0 20 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/L; from L0 to L10 
            1 is a Lagent/human/c; from L0 to L10 
        .end localvariabletable 
    .end code 
.end method 

.method public checkServerTrusted : ([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V 
    .code stack 0 locals 3 
L0:     return 
L1:     
        .linenumbertable 
            L0 45 
        .end linenumbertable 
        .localvariabletable 
            0 is a Lagent/human/L; from L0 to L0 
            1 is a [Ljava/security/cert/X509Certificate; from L0 to L0 
            2 is a Ljava/lang/String; from L0 to L0 
        .end localvariabletable 
    .end code 
.end method 
.innerclasses 
    agent/human/L [0] [0] 
.end innerclasses 
.enclosing method agent/human/c run ()V 
.sourcefile y 
.nesthost agent/human/c 
.end class 
