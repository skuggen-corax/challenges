"""
https://julekalender.knowit.no/doors/ck48plyxehtde01096odswazu
"""
import math

def trekant(i):
    return (i*(i+1))//2

def er_kvadrat(i):
    root = math.sqrt(i)
    return i == int(root + 0.5) ** 2

antall_tri_kvadrat = 0 # tar med 0
i = 0

while i <= 1000000:
    tre = trekant(i)

    j = 0
    rotations = len(str(tre))
    if er_kvadrat(tre):
        #print(tre, '(tri(',i,'))er kvadrat')
        antall_tri_kvadrat +=1
        i+=1
        continue
    else:
        while j < rotations:
            tre_rot = int(str(tre)[j:] + str(tre)[:j])
            if er_kvadrat(tre_rot):
                #print(tre, '(tri(',i,'))', 'rotasjonen', tre_rot, 'er kvadrat')
                antall_tri_kvadrat +=1
                break   
            j+=1
    i+=1

print(antall_tri_kvadrat)