from codecs import decode

ALPHABETH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ}{ _"

ALPHABYTES = [c.encode() for c in ALPHABETH]

messages = ["6c4a9bbef91506615055fbd4f269003d42e0e0dfc339e574567762bb2b014b28f0126fed115e563496b96ab5e9626d377a8aa1980b",
"664392ce800e1b76505cf3d4da08025d428390abce4f9d01341473cd3d7b4d229b141b9d053d",
"614092a29616076a3730fdc1cc08054651e6f2a7cf509c14337569d63d7e4d3d9b101f9d0449522798cc7cb8914d1e2f1f81b6910c8023fe5ac148248686f016b5",
"685a8cce900f08763143e8c1dc6b175a55e6f2a0c7459715476068a25f76283d8d120d8a122d343385ce11d68a571f217e9dd39c1c9122e95d",
"63468dad96170b76395efbb3ca71014a55e286bac3439815477d74a25275283e89031995183c5a21f7c811a6914d1925718ab6",
"704afea38c121a043455e8d6ca7c635b4fe6f2baca529607331466c1497c5a3de8131d9e183b51559ac80fa5975003447c86be8d138039f241db"]

# shortest message length: 76 hex, aka 38 chars
# longest message length: 130 hex, aka 65 chars
# key length 128 chars urandom

longest_message = min([len(m) for m in messages])//2

def xor(a, b):
    l = min(len(a), len(b))
    return bytes(x ^ y for x, y in zip(a[0: l], b[0: l]))

def find_egg():
    eggfinder = 0
    for n in range(longest_message):
        char = 2 * n
        possible = []
        char_letters = []
        key_letters = []
        for i in range(256):
            key = bytes([i])

            for message in messages:
                msg = decode(message[char:char+2], "hex")
                xord = xor(key, msg)
                if xord in ALPHABYTES:
                    key_letters.append(xord.decode())
                    possible.append(key)

            # hvis alle meldinger har ASCII med denne key
            if len(possible) == len(messages): 
                key_letters.append(key)
                char_letters.append(key_letters)
            key_letters = []
            possible = []
        
        if len(char_letters) > 0:
            search_letters = [item for sublist in char_letters 
                                for item in sublist]

            print(char, ":", [{l[-1:][0]: "".join(l[:-1])} for l in char_letters])

            if eggfinder == 0 and "E" in search_letters:
                eggfinder = 1
            elif eggfinder == 1 and "G" in search_letters:
                eggfinder = 2
            elif eggfinder == 2 and "G" in search_letters:
                eggfinder = 3
            elif eggfinder == 3 and "{" in search_letters:
                print("Possible egg found!", char-8, ":", char)
            else:
                eggfinder = 0
        else:
            eggfinder = 0

find_egg()

# message 0 contains EGG
known = {0:b'\x27', 2: b'\x0f',4: b'\xde', 6: b'\xee', 8: b'\xd9', 
         10: b'\x41', 12: b'\x4e', 14: b'\x24', 
         16: b'\x70', 18: b'\x10', 20: b'\xbc', 22: b'\x93', 24: b'\x89', 
         26: b'\x28', 28: b'\x43', 30: b'\x0f', 32: b'\x07', 34: b'\xa3', 
         36: b'\xd2', 38: b'\xee', 40: b'\x82', 42: b'\x00', 44: b'\xd3',
         46: b'\x46', 48: b'\x67', 50: b'\x34', 52: b'\x27', 54: b'\x82',
         56: b'\x1d', 58: b'\x33', 60: b'\x08', 62: b'\x6e', 64: b'\xc8',
         66: b'\x51', 68: b'\x58', 70: b'\xd8', 72: b'\x57', 74: b'\x69',
         76: b'\x14', 78: b'\x75', 80: b'\xd7', 82: b'\x81', 84: b'\x5c',
         86: b'\xf6', 88: b'\xde', 90: b'\x1f', 92: b'\x4d', 94: b'\x64',
         96: b'\x3f', 98: b'\xc9', 100: b'\xf3', 102: b'\xdd', 104: b'\x5f',
         106: b'\xc5', 108: b'\x6d', 110: b'\xbb', 112: b'\x0e', 114: b'\x95'} 

# decrypt messages using {known}
for message in messages:
    for n in range(min(known.keys()), max(known.keys())+1, 2):
        msg = decode(message[n:n+2], "hex")
        xord = xor(known[n], msg)
        print(" "+xord.decode(), end="")
    print() # newline

    for n in range(min(known.keys()), max(known.keys())+3, 2):
        print(message[n:n+2],end="")
    print() # newline
