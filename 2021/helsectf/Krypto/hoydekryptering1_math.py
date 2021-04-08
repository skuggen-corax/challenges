from itertools import product
import numpy as np

from sympy import matrices

# Super secret alphabet
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;?@[\\]^_`{|}~"

def encrypt(plaintext, key):
    plaintext = [alphabet.index(l) for l in plaintext]
    assert len(plaintext) % key.shape[0] == 0

    ciphertext = np.array(plaintext)
    ciphertext.resize(int(ciphertext.shape[0]/key.shape[0]), key.shape[0])
    ciphertext = np.matmul(ciphertext, key)
    ciphertext = np.remainder(ciphertext, len(alphabet)).flatten() # modulus

    return "".join([alphabet[int(c)] for c in ciphertext])

KEY = "super_secret_key"
encrypt_key = np.array([alphabet.index(k) for k in KEY])
encrypt_key.resize(4, 4)

assert encrypt_key.shape[0] == encrypt_key.shape[1]
assert np.linalg.det(encrypt_key) != 0


#FLAG = ""
FLAG = "EGG{polygrafisk_substitusjonskryptering_fra_1929_med_modulAEr_multiplikativ_invers!}"
ciphertext = encrypt(FLAG, encrypt_key)

assert ciphertext == "Q0(Kvx$_o(OB@#$jbZ^[aQR!\e)H?Al\"xC9;?:Pfv-4BXs&NZRp*~O-|Q}AoFCQF+:s)*?^a\'nw?M\"`C^1oH"

print(ciphertext)

inv_key = matrices.Matrix.inv_mod(matrices.Matrix(encrypt_key), len(alphabet))
print(encrypt(ciphertext, inv_key))