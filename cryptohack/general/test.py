from pwn import xor

print(xor('abc'.encode(), bytes.fromhex('50')).decode())