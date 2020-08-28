"""
Ny pr053dyr3 f0r kryp73ring
NI553N h4r få77 på p1455 ny PPK. K4n ni553n3 hj31p3r3 v3rifi53r3 4t k0d3n 3r ukn3kk31ig?
KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11
PST krøllparentes                                  krøllparentes slutt

1 => t : 
3 =>  :
4 =>  :
5 => l : 
6 =>  :
7 => e : 
8 => a : 
9 => s : 

z98øyåz8æy67aåy0å6æ7aø1å1438åa5a
 sa    a   e       e  t t  a  l 
"""

#rotor = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å','A','B','C','D','E',   # v encode
#                             'a','b','c','d','e','f','5','h','i','j','k','l','m','n','1','p','q','r','s','t','u','v','w','x','y','z','æ','ø','å','a','b','c','d','e'] # ^ decode

# tatt bort: g o 
#input =     "KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11"
#ppk3result "PST krøllparentes                                  krøllparentes slutt

#ppk3input  "KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo"
#ppk3result "PST krøllparantes 30e6d8432ce54710f9c09f305e7b9829 krøllparantes slutt"

from string import ascii_lowercase, ascii_uppercase, digits


def transpose(char, key):
    if char.isupper():
        alph = ascii_uppercase + 'ÆØÅ'
    elif char.islower():
        alph = ascii_lowercase + 'æøå'
    elif char.isdigit():
        alph = digits
        return alph[(alph.index(char) - 4) % len(alph)]
    else:
        return char
    return alph[(alph.index(char) + key) % len(alph)]


def print_flag(s):
    if 'PST' in s:
        print('\nSolution is probably:')
        s = s.replace(' krø11p4r3n735 51u77', '}')
        s = s.replace(' krø11p4r3n735 ', '{')
        print(s)
        print()


cipher = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11'
plain = ''

for c in cipher:
    plain += transpose(c, 5)

# Print probable solution
print_flag(plain)