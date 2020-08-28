#!/usr/bin/env python3
from PIL import Image

print('VolgaCTF 2020: Dissolved')

img = Image.open('stego.png')

extracted_lsbs = []
for i in range(img.height): 
    for j in range(img.width):
        pix = img.getpixel((j,i))
        alph = pix[3]
        if alph != 255: # get pix with disturbance in alpha channel
            extracted_lsbs.append(pix[2]&1) # get lsb of blue

lsb = "".join([str(x) for x in extracted_lsbs]).encode()
print('\nlsb of blue pix:', lsb)

print('\nlsb as string:')
n = 0
while n < len(lsb)-8:
    print(chr(int(lsb[n:n+8], 2)), end="")
    n +=8

