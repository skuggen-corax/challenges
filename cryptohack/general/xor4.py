from pwn import xor

inpu = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
fform = b'crypto{'

print('xoring cipher with flagformat', fform)
# prints b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
print(xor(inpu, fform))
# tries b'myXORkey'

possible_key = b'myXORkey'

print('trying key:', possible_key)
print(xor(inpu, possible_key).decode())
