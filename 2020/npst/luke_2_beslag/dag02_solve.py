#!/usr/bin/env python

filename = 'pen_gwyn_greatest_hits.mid'
old_byte = b''
annenhver = True
solution = ""

with open(filename, "rb") as f:
    while (byte := f.read(1)):
        if (byte == b'@' and annenhver and old_byte not in [b'\x90', b'\x80']):
            solution += old_byte.decode()
        annenhver ^= True
        old_byte = byte

print("PST{" + solution.split('{')[1].split('}')[0] + '}')