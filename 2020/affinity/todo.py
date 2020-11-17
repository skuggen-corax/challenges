#!/usr/bin/env python3

# solution for "TODO" chall of affinity ctf 2020

def encode(msg):
    output = ''

    for i in range(len(msg)):
        temp = ord(msg[i]) * 0x40
        #print(msg[i], " =1>", temp, end="")
        temp = temp >> 4
        #print(" =2>", temp, end="")
        if 0xc0 <= temp < 0xe8:
            #print(" =3> str(int())", str(int(msg[i]) * 0x1234))
            output = str(int(msg[i]) * 0x1234) + output
        else:
            #print(" =3> chr(ord())", chr(ord(msg[i])  * 0x10).encode())
            output = chr(ord(msg[i]) * 0x10) + output
    return output


def decode(msg):
    i = 0
    output = ""
    while(i < len(msg)):
        if msg[i] in ["4"]:
            output = str(int(msg[i:i+4])//0x1234) + output
            i += 4
        if msg[i] in ["2", "1"]:
            output = str(int(msg[i:i+5])//0x1234) + output
            i += 5
        else:
            output = chr(ord(msg[i:i+1])//0x10) + output
            i += 1
    return output

def shift(msg):
    j = len(msg) - 1
    output = ''

    for i in range(len(msg)//2):
        output += msg[i] + msg[j]
        j -= 1

    return output

def unshift(msg):
    left = right = ''
    i = 0
    while i < len(msg):
        left += msg[i]
        right = msg[i+1] + right
        i+=2
    
    print(left + right)


if __name__ == '__main__':
    # shifted = shift('<REDACTED>')
    # hashed = encode(shifted)

    hashed = '4660۠ܰ4660ڀ٠װװސ23300۰ސݐ18640ܠݰװۀڠ18640۰ްؠѠȐՀȐа4660ѠȐѠߐА'

    unshift(decode(hashed))
