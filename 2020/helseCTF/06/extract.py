#!/usr/bin/env python3
from PIL import Image

print('helseCTF: Vertikal forskyvning')

img1 = Image.open('2_image.png')
img2 = Image.open('EGG{946ad89061dc82d12249d3195853c685}.png')

extracted_lsbs = []

print('w', img1.width, 'h', img1.height)

antall = 0
for j in range(img1.width): 
#i = 0
    for i in range(img1.height):
        #j = 0
        pix1 = img1.getpixel((j,i))
        pix2 = img2.getpixel((j,i))
        #if img1.getpixel((j,0)) > img2.getpixel((j,0)) and pix1[0] < pix2[0]:
        if pix1[0] > pix2[0]:
        #if pix1[0] < pix2[0]:
            print(antall, '(i,j):', (i,j), '1:', pix1[0], ' 2:', pix2[0])
            antall += 1

            forskyvning = 1
            f = i + forskyvning % 527 - forskyvning

            extracted_lsbs.append(img2.getpixel((j,f))[0]&1) # get of red +1 vertical
            #extracted_lsbs.append(img2.getpixel((j,f))[1]&1)
            #extracted_lsbs.append(img2.getpixel((j,f))[2]&1)

print('antall:', antall)


lsb = "".join([str(x) for x in extracted_lsbs]).encode()
#print('\nlsb of blue pix:', lsb)

#print('\nlsb as string:')
#n = 0
#while n < len(lsb)-8:
#    print(chr(int(lsb[n:n+8], 2)), end="")
#    n +=8

