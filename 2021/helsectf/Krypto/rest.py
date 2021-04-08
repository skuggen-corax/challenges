from Cryptodome.Util.number import long_to_bytes
from sympy.ntheory.modular import crt

n = [954557211877289119789, 838313404031611232357, 875707149083085815411]
s = [730185355840085704378, 311836825142240843993, 77245018134820932374]

res = crt(n, s)

print(long_to_bytes(str(res[0])).decode())