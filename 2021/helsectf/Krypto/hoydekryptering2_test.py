import numpy as np

from sympy import matrices
# from secret2 import MESSAGE, FLAG


# Super secret alphabet
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;?@[\\]^_`{|}~"
p = len(alphabet)
#print(p)

def encrypt(plaintext, key):
    plaintext = [alphabet.index(l) for l in plaintext]
    assert len(plaintext) % key.shape[0] == 0

    ciphertext = np.array(plaintext)
    ciphertext.resize(int(ciphertext.shape[0]/key.shape[0]), key.shape[0])
    #print("SHAPE:", ciphertext.shape, key.shape)
    ciphertext = np.matmul(ciphertext, key)
    #print("CT shape:",ciphertext.shape)
    ciphertext = np.remainder(ciphertext, len(alphabet)).flatten()

    return "".join([alphabet[int(c)] for c in ciphertext])


import random
KEY = ""
for _ in range(25):
    KEY += random.choice(alphabet)

KEY = "1A234Z567t890!1234f567890"
MESSAGE = list("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
MESSAGE[0:5] = "In_cl"
MESSAGE[15:20] = "yptog"
MESSAGE[60:65] = "subst"
MESSAGE[95:100] = "_alge"
MESSAGE[120:125] = "ter_S"
MESSAGE = "".join(MESSAGE)

FLAG = "EGG{00000000001111111111}"

encrypt_key = np.array([alphabet.index(k) for k in KEY])
encrypt_key.resize(5, 5)

assert encrypt_key.shape[0] == encrypt_key.shape[1]
assert np.linalg.det(encrypt_key) != 0

ciphertext = encrypt(MESSAGE+FLAG, encrypt_key)
print(ciphertext)

ciphertext = """h};&TOOy~aDz52gbB7H.&f'tQFu|J)h&[Pm/'^{6TI)BkE\\\\7qDN~idGXfr`!H#/2$yZS!kf3FS:d\knH3xeYOJ4x6r3y9`0:(.Zr`T^8W{]Cb\KaBHg!kH&U;hx]V$HixrQIt2W}S+IuW|8cra\\0uh)\+"YBL0MDN~idGXfr`eZI'|R?7|Pw-1qquW|8c6PL?[537{)F]j1QW_VfZY5$Xup*_SNhfBJ&EQ1eCZ5Q{#SMY}2jjQaHh4c{js3s*n5VCHH`@M`pC`U$4Jg/z%XBn4SwA*V5{&X/+*\MYxd[gFM)XhrhL\:T5Dxj[EWQ+_UQ-C|u{;jkcxHaGZ+4Rv+-kcyL}l[snbi}_byE-$Ugw\d;*s-_S*l?'d3AUH^U3,32/t+dF&&rz\K;qh#@gbVj4Tks~s9GqKm`u|ikDDbP"""

print("\nLeaked parts of the plaintext ...")
print("index\t leak\t coded\t\t\t\t cipher\t coded")
LEAKS_AT = [        5*0,        5*3,        5*12,        5*19,        5*24,  ]
CODED_MESSAGE = [alphabet.index(l) for l in MESSAGE]
CODED_CIPHER = [alphabet.index(l) for l in ciphertext]
leaked = []
ciphercribs = []
for l in LEAKS_AT:
    leaked.append(CODED_MESSAGE[l:l+5])
    ciphercribs.append(CODED_CIPHER[l:l+5])
    print(l, "\t", MESSAGE[l:l+5], "\t", CODED_MESSAGE[l:l+5], "\t","\t", ciphertext[l:l+5], "\t", CODED_CIPHER[l:l+5])

# solve 25 linear equations with 5 vars, to get inverted key
solved = matrices.Matrix.inv_mod(matrices.Matrix(ciphercribs), len(alphabet))
solved = np.dot(solved,leaked)
solved = np.remainder(solved, len(alphabet))

print("inverted key:\n", solved)

res = encrypt(ciphertext, solved)
print(res)
