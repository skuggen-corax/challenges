from pwn import xor

inpu = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(0, 256):
    deco =  xor(inpu, i) 
    if deco[-1:] == b'}':
        print(deco.decode())
        break