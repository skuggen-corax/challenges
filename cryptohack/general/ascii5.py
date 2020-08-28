from pwn import remote
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs

r = remote('socket.cryptohack.org', 13377) #, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

j = 0
run = True
while run:
    j += 1
    print('Level:', j, '', end="") if j <= 100 else print('Here comes the FLAG:')
    received = json_recv()

    if 'flag' in received:
        print(received['flag'])
        run = False
        break

    codetype = received["type"]
    encoded = received["encoded"]

    #print("Received type: ", codetype, "with encoded value: ", encoded)

    decoded = ""

    if codetype == 'rot13':
        decoded = codecs.encode(encoded, 'rot_13')
    elif codetype == 'utf-8':
        decoded = "".join([chr(c) for c in encoded])
    elif codetype == 'base64':
        decoded = base64.b64decode(encoded.encode()).decode()
    elif codetype == 'bigint':
        decoded = long_to_bytes(int(encoded, 0)).decode()
    elif codetype == 'hex':
        for i in range(0, len(encoded), 2):
            decoded += chr(int(encoded[i:i+2],16))

    print(codetype, ':', encoded, '=>', decoded)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)
