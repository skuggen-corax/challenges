import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode

img = Image.open('luke_23_julekort.png', 'r')

imgarray = np.array(img)

xor_bitplanes_0 = ((imgarray[...,0] ^ imgarray[...,1] ^ imgarray[...,2]) & 0x01) * 255

decoded_qr = decode(xor_bitplanes_0)

print(decoded_qr[0][0].decode())

# PST{4ll_th3s3_d3l1c10us_l4y3rs}