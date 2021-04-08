from itertools import product
import numpy as np

from tqdm import tqdm 

testalphabet = "abcdefghijklmnopqrstuv_AEGO0123456789!}{"

# Super secret alphabet
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;?@[\\]^_`{|}~"

alle = [p for p in product(testalphabet, repeat=4)]
# print(len(alle)) # alphabeth:     68574961
                 # testalphabeth: 20151121

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


#FLAG =          "EGG{polygrafisk_substitusjonskryptering_fra_1929_med_modulAEr_multiplikativ_invers!}"
FLAG = ""
print(encrypt(FLAG, encrypt_key))
ciphertext = "Q0(Kvx$_o(OB@#$jbZ^[aQR!\e)H?Al\"xC9;?:Pfv-4BXs&NZRp*~O-|Q}AoFCQF+:s)*?^a\'nw?M\"`C^1oH"
print(ciphertext)

index = len(FLAG)

while len(FLAG) < len(ciphertext):

    # print("Leter fra index", index, compare_to)
    compare_to = ciphertext[index:index+4]

    for combination in tqdm(alle, desc=FLAG+"????"):
        test = "".join(combination)
        testcipher = encrypt(FLAG + test, encrypt_key)
        
        # print(testcipher[index:index+4], "equal to", compare_to, testcipher[index:index+4] == compare_to)

        if testcipher[index:index+4] == compare_to:
            break

    if testcipher[index:index+4] == compare_to:
        print("found index", str(index)+"-"+str(index+4), ":", test)
        FLAG = FLAG + test
        index += 4
    else:
        print("something wong..")
        exit()

print(FLAG)