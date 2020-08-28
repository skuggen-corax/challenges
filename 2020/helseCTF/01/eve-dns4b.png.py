import binascii
import sys

a = '123456789ABC'
a += 'DxFyHJKLMNPQRSTU'
a += 'VWXYZabcdefzhijkmnopqr'
a = a + 'stuvwEGg'

a = a[:13] + a[55] + a[14:55] + a[13] + a[56:]
a = a[:15] + a[56] + a[16:56] + a[15] + a[57:]
a = a[:39] + a[57] + a[40:57] + a[39] + a[58:]

def d(s):
    n = 0
    for c in s:
        n = n*len(a) + a.index(c)
    return binascii.unhexlify(('%x' % n).encode('utf-8'))
print(f"EGG{{{d(sys.argv[1][::-1]).decode('utf-8')}}}")