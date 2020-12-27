#!/usr/bin/env python 
import pdb
stack = []
def psh(*X): stack.extend(X)
def pop(): return stack.pop() if stack else None
def pop2(): return (None, None) if len(stack) < 2 else (stack.pop(), stack.pop())
def rll(x, y):
 x %= y
 if y <= 0 or x == 0: return
 z = -abs(x) + y * (x < 0)
 stack[-y:] = stack[z:] + stack[-y:z]
def x0y0():
 stack.append(10)
 return x1y0

def x1y0():
 stack.append(10)
 return x2y0

def x2y0():
 stack.append(16)
 return x3y0

def x3y0():
 stack.append(3)
 return x4y0

def x4y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x5y0

def x5y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x6y0

def x6y0():
 stack.append(4)
 return x7y0

def x7y0():
 stack.append(16)
 return x8y0

def x8y0():
 stack.append(6)
 return x9y0

def x9y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x10y0

def x10y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x11y0

def x11y0():
 a = pop()
 a is not None and psh(a,a)
 return x12y0

def x12y0():
 stack.append(14)
 return x13y0

def x13y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x14y0

def x14y0():
 a = pop()
 a is not None and psh(a,a)
 return x15y0

def x15y0():
 stack.append(3)
 return x16y0

def x16y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x17y0

def x17y0():
 a = pop()
 a is not None and psh(a,a)
 return x18y0

def x18y0():
 stack.append(8)
 return x19y0

def x19y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x20y0

def x20y0():
 a = pop()
 a is not None and psh(a,a)
 return x21y0

def x21y0():
 stack.append(4)
 return x22y0

def x22y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x23y0

def x23y0():
 a = pop()
 a is not None and psh(a,a)
 return x24y0

def x24y0():
 stack.append(1)
 return x25y0

def x25y0():
 stack.append(16)
 return x26y0

def x26y0():
 stack.append(6)
 return x27y0

def x27y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x28y0

def x28y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x29y0

def x29y0():
 a = pop()
 a is not None and psh(a,a)
 return x30y0

def x30y0():
 stack.append(15)
 return x31y0

def x31y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x32y0

def x32y0():
 stack.append(16)
 return x33y0

def x33y0():
 stack.append(2)
 return x34y0

def x34y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x35y0

def x35y0():
 stack.append(2)
 return x36y0

def x36y0():
 stack.append(16)
 return x37y0

def x37y0():
 stack.append(7)
 return x38y0

def x38y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x39y0

def x39y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x40y0

def x40y0():
 a = pop()
 a is not None and psh(a,a)
 return x41y0

def x41y0():
 stack.append(13)
 return x42y0

def x42y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x43y0

def x43y0():
 a = pop()
 a is not None and psh(a,a)
 return x44y0

def x44y0():
 stack.append(15)
 return x45y0

def x45y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x46y0

def x46y0():
 a = pop()
 a is not None and psh(a,a)
 return x47y0

def x47y0():
 stack.append(6)
 return x48y0

def x48y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x49y0

def x49y0():
 stack.append(5)
 return x50y0

def x50y0():
 stack.append(16)
 return x51y0

def x51y0():
 stack.append(4)
 return x52y0

def x52y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x53y0

def x53y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x54y0

def x54y0():
 stack.append(16)
 return x55y0

def x55y0():
 stack.append(2)
 return x56y0

def x56y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x57y0

def x57y0():
 stack.append(10)
 return x58y0

def x58y0():
 stack.append(16)
 return x59y0

def x59y0():
 stack.append(3)
 return x60y0

def x60y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x61y0

def x61y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x62y0

def x62y0():
 a = pop()
 a is not None and psh(a,a)
 return x63y0

def x63y0():
 stack.append(8)
 return x64y0

def x64y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x65y0

def x65y0():
 stack.append(16)
 return x66y0

def x66y0():
 stack.append(2)
 return x67y0

def x67y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x68y0

def x68y0():
 stack.append(4)
 return x69y0

def x69y0():
 stack.append(16)
 return x70y0

def x70y0():
 stack.append(7)
 return x71y0

def x71y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x72y0

def x72y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x73y0

def x73y0():
 a = pop()
 a is not None and psh(a,a)
 return x74y0

def x74y0():
 stack.append(2)
 return x75y0

def x75y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x76y0

def x76y0():
 stack.append(1)
 return x77y0

def x77y0():
 stack.append(16)
 return x78y0

def x78y0():
 stack.append(6)
 return x79y0

def x79y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x80y0

def x80y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x81y0

def x81y0():
 stack.append(16)
 return x82y0

def x82y0():
 stack.append(5)
 return x83y0

def x83y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x84y0

def x84y0():
 stack.append(10)
 return x85y0

def x85y0():
 a = pop()
 a is not None and psh(a,a)
 return x86y0

def x86y0():
 stack.append(9)
 return x87y0

def x87y0():
 stack.append(16)
 return x88y0

def x88y0():
 stack.append(2)
 return x89y0

def x89y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x90y0

def x90y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x91y0

def x91y0():
 a = pop()
 a is not None and psh(a,a)
 return x92y0

def x92y0():
 stack.append(2)
 return x93y0

def x93y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x94y0

def x94y0():
 stack.append(14)
 return x95y0

def x95y0():
 stack.append(16)
 return x96y0

def x96y0():
 stack.append(6)
 return x97y0

def x97y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x98y0

def x98y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x99y0

def x99y0():
 a = pop()
 a is not None and psh(a,a)
 return x100y0

def x100y0():
 stack.append(13)
 return x101y0

def x101y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x102y0

def x102y0():
 a = pop()
 a is not None and psh(a,a)
 return x103y0

def x103y0():
 stack.append(8)
 return x104y0

def x104y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x105y0

def x105y0():
 a = pop()
 a is not None and psh(a,a)
 return x106y0

def x106y0():
 stack.append(9)
 return x107y0

def x107y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x108y0

def x108y0():
 a = pop()
 a is not None and psh(a,a)
 return x109y0

def x109y0():
 stack.append(14)
 return x110y0

def x110y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x111y0

def x111y0():
 a = pop()
 a is not None and psh(a,a)
 return x112y0

def x112y0():
 stack.append(10)
 return x113y0

def x113y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x114y0

def x114y0():
 return y9X115

def y9X115():
 a = pop()
 a is not None and psh(a,a)
 return y10X115

def y10X115():
 stack.append(1)
 return y11X115

def y11X115():
 a,b = pop2()
 a is not None and psh(b+a)
 return y12X115

def y12X115():
 stack.append(2)
 return y14X115

def y14X115():
 a = pop()
 return [y15X115, Y15x115, Y15X115, y15x115][0 if a is None else (a%4+4)%4]

def y15X115():
 return Y12X117

def Y15x115():
 return X117Y12

def Y15X115():
 return Y12X117

def y15x115():
 return X117Y12

def X117Y12():
 a = pop()
 a is not None and psh(a,a)
 return X117Y11

def X117Y11():
 stack.append(2)
 return X117Y9

def X117Y9():
 a,b = pop2()
 a is not None and psh(b-a)
 return X117Y8

def X117Y8():
 return y0x120

def y0x120():
 stack.append(7)
 return y6x121

def y6x121():
 stack.append(16)
 return x122y0

def x122y0():
 stack.append(2)
 return x123y0

def x123y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x124y0

def x124y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x125y0

def x125y0():
 a = pop()
 a is not None and psh(a,a)
 return x126y0

def x126y0():
 stack.append(1)
 return x127y0

def x127y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x128y0

def x128y0():
 stack.append(12)
 return x129y0

def x129y0():
 stack.append(16)
 return x130y0

def x130y0():
 stack.append(4)
 return x131y0

def x131y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x132y0

def x132y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x133y0

def x133y0():
 a = pop()
 a is not None and psh(a,a)
 return x134y0

def x134y0():
 stack.append(11)
 return x135y0

def x135y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x136y0

def x136y0():
 stack.append(6)
 return x137y0

def x137y0():
 stack.append(16)
 return x138y0

def x138y0():
 stack.append(5)
 return x139y0

def x139y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x140y0

def x140y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x141y0

def x141y0():
 stack.append(1)
 return x142y0

def x142y0():
 stack.append(16)
 return x143y0

def x143y0():
 stack.append(4)
 return x144y0

def x144y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x145y0

def x145y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x146y0

def x146y0():
 a = pop()
 a is not None and psh(a,a)
 return x147y0

def x147y0():
 stack.append(7)
 return x148y0

def x148y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x149y0

def x149y0():
 stack.append(16)
 return x150y0

def x150y0():
 stack.append(2)
 return x151y0

def x151y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x152y0

def x152y0():
 stack.append(10)
 return x153y0

def x153y0():
 stack.append(16)
 return x154y0

def x154y0():
 stack.append(3)
 return x155y0

def x155y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x156y0

def x156y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x157y0

def x157y0():
 a = pop()
 a is not None and psh(a,a)
 return x158y0

def x158y0():
 stack.append(9)
 return x159y0

def x159y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x160y0

def x160y0():
 stack.append(16)
 return x161y0

def x161y0():
 stack.append(2)
 return x162y0

def x162y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x163y0

def x163y0():
 stack.append(4)
 return x164y0

def x164y0():
 stack.append(16)
 return x165y0

def x165y0():
 stack.append(7)
 return x166y0

def x166y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x167y0

def x167y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x168y0

def x168y0():
 a = pop()
 a is not None and psh(a,a)
 return x169y0

def x169y0():
 stack.append(2)
 return x170y0

def x170y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x171y0

def x171y0():
 stack.append(1)
 return x172y0

def x172y0():
 stack.append(16)
 return x173y0

def x173y0():
 stack.append(6)
 return x174y0

def x174y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x175y0

def x175y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x176y0

def x176y0():
 stack.append(16)
 return x177y0

def x177y0():
 stack.append(5)
 return x178y0

def x178y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x179y0

def x179y0():
 stack.append(10)
 return x180y0

def x180y0():
 stack.append(4)
 return x181y0

def x181y0():
 stack.append(16)
 return x182y0

def x182y0():
 stack.append(3)
 return x183y0

def x183y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x184y0

def x184y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x185y0

def x185y0():
 return x188y0

def x188y0():
 stack.append(2)
 return y2X188

def y2X188():
 stack.append(1)
 return y3X188

def y3X188():
 a,b = pop2()
 a is not None and rll(a,b)
 return y4X188

def y4X188():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return y5X188

def y5X188():
 stack.append(1)
 return y6X188

def y6X188():
 a,b = pop2()
 a is not None and psh(b-a)
 return y7X188

def y7X188():
 a = pop()
 a is not None and psh(a,a)
 return y8X188

def y8X188():
 a = pop()
 a is not None and psh(int(not a))
 return y9X188

def y9X188():
 stack.append(3)
 return y12X188

def y12X188():
 a,b = pop2()
 a is not None and psh(b*a)
 return y13X188

def y13X188():
 a = pop()
 a is not None and psh(a,a)
 return y14X188

def y14X188():
 a = pop()
 return [y15X188, Y15x188, Y15X188, y15x188][0 if a is None else (a%4+4)%4]

def y15X188():
 pop()
 return y16X188

def Y15x188():
 a = pop()
 return [X188Y14, Y14X188][1 if a is None else a&1]

def Y15X188():
 a = pop()
 return [Y14X188, X188Y14][1 if a is None else a&1]

def y15x188():
 breakpoint()
 a = pop()
 return [y15x189, y15X189, Y15x189, Y15X189][0 if a is None else (a%4+4)%4]

def y15x189():
 a = pop()
 return [Y15x188, x188Y15][1 if a is None else a&1]

def y15X189():
 a = pop()
 return [x188Y15, Y15x188][1 if a is None else a&1]

def Y15x189():
 a = pop()
 return [Y15x188, x188Y15][1 if a is None else a&1]

def Y15X189():
 pop()
 return Y14X190

def Y14X190():
 return x191y0

def x191y0():
 stack.append(1)
 return x192y0

def x192y0():
 a = pop()
 a is not None and psh(int(not a))
 return x193y0

def x193y0():
 stack.append(1)
 return x194y0

def x194y0():
 a = pop()
 return [x195y0, X195y0, x195Y0, X195Y0][0 if a is None else (a%4+4)%4]

def x195y0():
 return y3X195

def X195y0():
 return X195y3

def x195Y0():
 a = pop()
 return [x194Y0, Y0x194][1 if a is None else a&1]

def X195Y0():
 return X195y3

def X195y3():
 stack.append(3)
 return X195y6

def X195y6():
 return X195y19

def X195y19():
 return X195y22

def X195y22():
 return X195y24

def X195y24():
 a = pop()
 return [X195y25, x195Y25, X195Y25, x195y25][0 if a is None else (a%4+4)%4]

def X195y25():
 return Y25x188

def x195Y25():
 return x188Y25

def X195Y25():
 a = pop()
 return [X195Y24, Y24X195][1 if a is None else a&1]

def x195y25():
 return x201y25

def x201y25():
 return x210y25

def x210y25():
 return Y22X210

def Y22X210():
 return Y19X210

def Y19X210():
 return x211y0

def x211y0():
 stack.append(1)
 return x212y0

def x212y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x213y0

def x213y0():
 a = pop()
 a is not None and psh(a,a)
 return x214y0

def x214y0():
 a = input()
 breakpoint()
 psh(ord(a))
 return x215y0

def x215y0():
 a = pop()
 a is not None and psh(a,a)
 return x216y0

def x216y0():
 stack.append(8)
 return x217y0

def x217y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x218y0

def x218y0():
 a = pop()
 a is not None and psh(int(not a))
 return x219y0

def x219y0():
 a = pop()
 return [x220y0, X220y0, x220Y0, X220Y0][0 if a is None else (a%4+4)%4]

def x220y0():
 return x222y0

def X220y0():
 pop()
 return X220y1

def x220Y0():
 a = pop()
 return [x219Y0, Y0x219][1 if a is None else a&1]

def X220Y0():
 return y0x222

def y0x222():
 a = pop()
 a is not None and psh(a,a)
 return y0x223

def y0x223():
 stack.append(10)
 return x224y0

def x224y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x225y0

def x225y0():
 a = pop()
 a is not None and psh(int(not a))
 return x226y0

def x226y0():
 a = pop()
 return [x227y0, X227y0, x227Y0, X227Y0][0 if a is None else (a%4+4)%4]

def x227y0():
 return x229y0

def X227y0():
 pop()
 return X227y1

def x227Y0():
 a = pop()
 return [x226Y0, Y0x226][1 if a is None else a&1]

def X227Y0():
 return y0x229

def y0x229():
 stack.append(2)
 return x230y0

def x230y0():
 stack.append(1)
 return x231y0

def x231y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x232y0

def x232y0():
 stack.append(1)
 return x233y0

def x233y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x234y0

def x234y0():
 stack.append(1)
 return x235y0

def x235y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x236y0

def x236y0():
 stack.append(1)
 return x237y0

def x237y0():
 a = pop()
 return [x238y0, X238y0, x238Y0, X238Y0][0 if a is None else (a%4+4)%4]

def x238y0():
 return y19X238

def X238y0():
 return X238y19

def x238Y0():
 a = pop()
 return [x237Y0, Y0x237][1 if a is None else a&1]

def X238Y0():
 return X238y19

def X238y19():
 return X238y22

def X238y22():
 return X238y25

def X238y25():
 return Y25x210

def Y25x210():
 return X210Y22

def X210Y22():
 return X210Y19

def X210Y19():
 return y0x211

def y0x211():
 stack.append(1)
 return y0x212

def y0x212():
 a,b = pop2()
 a is not None and psh(b+a)
 return y0x213

def y0x213():
 a = pop()
 a is not None and psh(a,a)
 return y0x214

def y0x214():
 a = input()
 breakpoint()
 psh(ord(a))
 return y0x215

def y0x215():
 a = pop()
 a is not None and psh(a,a)
 return y0x216

def y0x216():
 stack.append(8)
 return x217y0

def x237Y0():
 pop()
 return x236Y0

def Y0x237():
 pop()
 return Y0x236

def Y0x236():
 a = pop()
 a is not None and psh(int(not a))
 return Y0x235

def Y0x235():
 pop()
 return Y0x234

def Y0x234():
 a = input()
 breakpoint()
 psh(ord(a))
 return Y0x233

def Y0x233():
 pop()
 return Y0x232

def Y0x232():
 a = pop()
 a is not None and psh(int(not a))
 return Y0x231

def Y0x231():
 pop()
 return Y0x230

def Y0x230():
 pop()
 return Y0x229

def Y0x229():
 return Y0x227

def Y0x227():
 a = pop()
 return [Y0x226, x226Y0][1 if a is None else a&1]

def Y0x226():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x225

def x226Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x225Y0

def x225Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x224Y0

def x224Y0():
 pop()
 return x223Y0

def x223Y0():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y0x222

def Y0x222():
 return Y0x220

def Y0x220():
 a = pop()
 return [Y0x219, x219Y0][1 if a is None else a&1]

def Y0x219():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x218

def x219Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x218Y0

def x218Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x217Y0

def x217Y0():
 pop()
 return x216Y0

def x216Y0():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y0x215

def Y0x215():
 a,b = pop2()
 a is not None and psh(b+a)
 return Y0x214

def Y0x214():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y0x213

def Y0x213():
 a = input()
 breakpoint()
 psh(ord(a))
 return Y0x212

def Y0x212():
 pop()
 return Y0x211

def Y0x211():
 return Y0x209

def Y0x209():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x208

def Y0x208():
 pop()
 return Y0x207

def Y0x207():
 stack.append(1)
 return Y0x206

def Y0x206():
 a = pop()
 a is not None and psh(int(not a))
 return Y0x205

def Y0x205():
 pop()
 return Y0x204

def Y0x204():
 pop()
 return Y0x203

def Y0x203():
 return Y0x201

def Y0x201():
 a = pop()
 return [Y0x200, x200Y0][1 if a is None else a&1]

def Y0x200():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x199

def x200Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x199Y0

def x199Y0():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return x198Y0

def x198Y0():
 return x198y0

def x198y0():
 a = pop()
 a is not None and psh(a,a)
 return x199y0

def x199y0():
 a = pop()
 a is not None and psh(int(not a))
 return x200y0

def x200y0():
 a = pop()
 return [x201y0, X201y0, x201Y0, X201Y0][0 if a is None else (a%4+4)%4]

def x201y0():
 return x203y0

def X201y0():
 return X201y3

def x201Y0():
 a = pop()
 return [x200Y0, Y0x200][1 if a is None else a&1]

def X201Y0():
 return y0x203

def y0x203():
 stack.append(2)
 return x204y0

def x204y0():
 stack.append(1)
 return x205y0

def x205y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x206y0

def x206y0():
 pop()
 return x207y0

def x207y0():
 stack.append(1)
 return x208y0

def x208y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x209y0

def x209y0():
 return x211y0

def X201y3():
 stack.append(3)
 return X201y6

def X201y6():
 return X201y19

def X201y19():
 return X201y22

def X201y22():
 return X201y24

def X201y24():
 a = pop()
 return [X201y25, x201Y25, X201Y25, x201y25][0 if a is None else (a%4+4)%4]

def X201y25():
 return Y25x195

def x201Y25():
 return x195Y25

def X201Y25():
 a = pop()
 return [X201Y24, Y24X201][1 if a is None else a&1]

def X201Y24():
 return X201Y22

def Y24X201():
 return Y22X201

def Y22X201():
 return Y19X201

def Y19X201():
 return Y6X201

def Y6X201():
 pop()
 return Y5X201

def Y5X201():
 return Y0X201

def Y0X201():
 return x203y0

def x203y0():
 stack.append(2)
 return x204y0

def X201Y22():
 return X201Y19

def X201Y19():
 return X201Y6

def X201Y6():
 pop()
 return X201Y5

def X201Y5():
 return X201Y0

def Y25x195():
 return Y25x188

def Y25x188():
 return Y25x186

def Y25x186():
 return y25x186

def y25x186():
 return y25x188

def y25x188():
 return y25x195

def y25x195():
 return y25x201

def y25x201():
 return y25x210

def y25x210():
 return X210Y22

def Y0x199():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y0x198

def Y0x198():
 return y0x198

def y0x198():
 a = pop()
 a is not None and psh(a,a)
 return y0x199

def y0x199():
 a = pop()
 a is not None and psh(int(not a))
 return y0x200

def y0x200():
 a = pop()
 return [y0x201, y0X201, Y0x201, Y0X201][0 if a is None else (a%4+4)%4]

def y0x201():
 return y0x203

def y0X201():
 return y3X201

def y3X201():
 stack.append(3)
 return y6X201

def y6X201():
 return y19X201

def y19X201():
 return y22X201

def y22X201():
 return y24X201

def y24X201():
 a = pop()
 return [y25X201, Y25x201, Y25X201, y25x201][0 if a is None else (a%4+4)%4]

def y25X201():
 return x195Y25

def Y25x201():
 return Y25x195

def Y25X201():
 a = pop()
 return [Y24X201, X201Y24][1 if a is None else a&1]

def Y0x218():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x217

def Y0x217():
 pop()
 return Y0x216

def Y0x216():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y0x215

def Y0x225():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x224

def Y0x224():
 pop()
 return Y0x223

def Y0x223():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y0x222

def x236Y0():
 a = pop()
 a is not None and psh(int(not a))
 return x235Y0

def x235Y0():
 pop()
 return x234Y0

def x234Y0():
 a = input()
 psh(ord(a))
 return x233Y0

def x233Y0():
 pop()
 return x232Y0

def x232Y0():
 a = pop()
 a is not None and psh(int(not a))
 return x231Y0

def x231Y0():
 pop()
 return x230Y0

def x230Y0():
 pop()
 return x229Y0

def x229Y0():
 return Y0x227

def y19X238():
 return y22X238

def y22X238():
 return y25X238

def y25X238():
 return x210Y25

def x210Y25():
 return Y22X210

def X227y1():
 return X227y3

def X227y3():
 stack.append(3)
 return X227y6

def X227y6():
 return X227y19

def X227y19():
 return X227y21

def X227y21():
 a = pop()
 return [X227y22, x227Y22, X227Y22, x227y22][0 if a is None else (a%4+4)%4]

def X227y22():
 return Y22x220

def x227Y22():
 return x220Y22

def X227Y22():
 a = pop()
 return [X227Y21, Y21X227][1 if a is None else a&1]

def x227y22():
 return x238y22

def x238y22():
 return x240y22

def x240y22():
 return Y19X240

def Y19X240():
 return x241y0

def x241y0():
 pop()
 return x242y0

def x242y0():
 stack.append(1)
 return x243y0

def x243y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x244y0

def x244y0():
 pop()
 return x245y0

def x245y0():
 breakpoint()
 stack.append(4)
 return x246y0

def x246y0():
 stack.append(16)
 return x247y0

def x247y0():
 stack.append(5)
 return x248y0

def x248y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x249y0

def x249y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x250y0

def x250y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x251y0

def x251y0():
 a = pop()
 a is not None and psh(int(not a))
 return x252y0

def x252y0():
 a = pop()
 a is not None and psh(int(not a))
 return x253y0

def x253y0():
 a = pop()
 return [x254y0, X254y0, x254Y0, X254Y0][0 if a is None else (a%4+4)%4]

def x254y0():
 return x256y0

def X254y0():
 return X254y19

def x254Y0():
 a = pop()
 return [x253Y0, Y0x253][1 if a is None else a&1]

def X254Y0():
 return y0x256

def y0x256():
 stack.append(2)
 return y1x257

def y1x257():
 stack.append(16)
 return x258y0

def x258y0():
 stack.append(7)
 return x259y0

def x259y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x260y0

def x260y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x261y0

def x261y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x262y0

def x262y0():
 a = pop()
 a is not None and psh(int(not a))
 return x263y0

def x263y0():
 a = pop()
 a is not None and psh(int(not a))
 return x264y0

def x264y0():
 a = pop()
 return [x265y0, X265y0, x265Y0, X265Y0][0 if a is None else (a%4+4)%4]

def x265y0():
 return x267y0

def X265y0():
 return X265y19

def x265Y0():
 a = pop()
 return [x264Y0, Y0x264][1 if a is None else a&1]

def X265Y0():
 return y0x267

def y0x267():
 stack.append(16)
 return x268y0

def x268y0():
 stack.append(3)
 return x269y0

def x269y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x270y0

def x270y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x271y0

def x271y0():
 a = pop()
 a is not None and psh(int(not a))
 return x272y0

def x272y0():
 a = pop()
 a is not None and psh(int(not a))
 return x273y0

def x273y0():
 a = pop()
 return [x274y0, X274y0, x274Y0, X274Y0][0 if a is None else (a%4+4)%4]

def x274y0():
 return x276y0

def X274y0():
 return X274y19

def x274Y0():
 a = pop()
 return [x273Y0, Y0x273][1 if a is None else a&1]

def X274Y0():
 return y0x276

def y0x276():
 stack.append(5)
 return y4x277

def y4x277():
 stack.append(16)
 return x278y0

def x278y0():
 stack.append(7)
 return x279y0

def x279y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x280y0

def x280y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x281y0

def x281y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x282y0

def x282y0():
 a = pop()
 a is not None and psh(int(not a))
 return x283y0

def x283y0():
 a = pop()
 a is not None and psh(int(not a))
 return x284y0

def x284y0():
 a = pop()
 return [x285y0, X285y0, x285Y0, X285Y0][0 if a is None else (a%4+4)%4]

def x285y0():
 return x287y0

def X285y0():
 return X285y19

def x285Y0():
 a = pop()
 return [x284Y0, Y0x284][1 if a is None else a&1]

def X285Y0():
 return y0x287

def y0x287():
 stack.append(2)
 return y1x288

def y1x288():
 stack.append(16)
 return x289y0

def x289y0():
 stack.append(6)
 return x290y0

def x290y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x291y0

def x291y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x292y0

def x292y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x293y0

def x293y0():
 a = pop()
 a is not None and psh(int(not a))
 return x294y0

def x294y0():
 a = pop()
 a is not None and psh(int(not a))
 return x295y0

def x295y0():
 a = pop()
 return [x296y0, X296y0, x296Y0, X296Y0][0 if a is None else (a%4+4)%4]

def x296y0():
 return x298y0

def X296y0():
 return X296y19

def x296Y0():
 a = pop()
 return [x295Y0, Y0x295][1 if a is None else a&1]

def X296Y0():
 return y0x298

def y0x298():
 stack.append(4)
 return y3x299

def y3x299():
 stack.append(16)
 return x300y0

def x300y0():
 stack.append(3)
 return x301y0

def x301y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x302y0

def x302y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x303y0

def x303y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x304y0

def x304y0():
 a = pop()
 a is not None and psh(int(not a))
 return x305y0

def x305y0():
 a = pop()
 a is not None and psh(int(not a))
 return x306y0

def x306y0():
 a = pop()
 return [x307y0, X307y0, x307Y0, X307Y0][0 if a is None else (a%4+4)%4]

def x307y0():
 return x309y0

def X307y0():
 return X307y19

def x307Y0():
 a = pop()
 return [x306Y0, Y0x306][1 if a is None else a&1]

def X307Y0():
 return y0x309

def y0x309():
 stack.append(4)
 return y3x310

def y3x310():
 stack.append(16)
 return x311y0

def x311y0():
 stack.append(6)
 return x312y0

def x312y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x313y0

def x313y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x314y0

def x314y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x315y0

def x315y0():
 a = pop()
 a is not None and psh(int(not a))
 return x316y0

def x316y0():
 a = pop()
 a is not None and psh(int(not a))
 return x317y0

def x317y0():
 a = pop()
 return [x318y0, X318y0, x318Y0, X318Y0][0 if a is None else (a%4+4)%4]

def x318y0():
 return x320y0

def X318y0():
 return X318y19

def x318Y0():
 a = pop()
 return [x317Y0, Y0x317][1 if a is None else a&1]

def X318Y0():
 return y0x320

def y0x320():
 stack.append(16)
 return x321y0

def x321y0():
 stack.append(3)
 return x322y0

def x322y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x323y0

def x323y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x324y0

def x324y0():
 a = pop()
 a is not None and psh(int(not a))
 return x325y0

def x325y0():
 a = pop()
 a is not None and psh(int(not a))
 return x326y0

def x326y0():
 a = pop()
 return [x327y0, X327y0, x327Y0, X327Y0][0 if a is None else (a%4+4)%4]

def x327y0():
 return x329y0

def X327y0():
 return X327y19

def x327Y0():
 a = pop()
 return [x326Y0, Y0x326][1 if a is None else a&1]

def X327Y0():
 return y0x329

def y0x329():
 stack.append(2)
 return y1x330

def y1x330():
 stack.append(16)
 return x331y0

def x331y0():
 stack.append(7)
 return x332y0

def x332y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x333y0

def x333y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x334y0

def x334y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x335y0

def x335y0():
 a = pop()
 a is not None and psh(int(not a))
 return x336y0

def x336y0():
 a = pop()
 a is not None and psh(int(not a))
 return x337y0

def x337y0():
 a = pop()
 return [x338y0, X338y0, x338Y0, X338Y0][0 if a is None else (a%4+4)%4]

def x338y0():
 return x340y0

def X338y0():
 return X338y19

def x338Y0():
 a = pop()
 return [x337Y0, Y0x337][1 if a is None else a&1]

def X338Y0():
 return y0x340

def y0x340():
 stack.append(6)
 return y5x341

def y5x341():
 stack.append(16)
 return x342y0

def x342y0():
 stack.append(2)
 return x343y0

def x343y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x344y0

def x344y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x345y0

def x345y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x346y0

def x346y0():
 a = pop()
 a is not None and psh(int(not a))
 return x347y0

def x347y0():
 a = pop()
 a is not None and psh(int(not a))
 return x348y0

def x348y0():
 a = pop()
 return [x349y0, X349y0, x349Y0, X349Y0][0 if a is None else (a%4+4)%4]

def x349y0():
 return x351y0

def X349y0():
 return X349y19

def x349Y0():
 a = pop()
 return [x348Y0, Y0x348][1 if a is None else a&1]

def X349Y0():
 return y0x351

def y0x351():
 stack.append(3)
 return y2x352

def y2x352():
 stack.append(16)
 return x353y0

def x353y0():
 stack.append(3)
 return x354y0

def x354y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x355y0

def x355y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x356y0

def x356y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x357y0

def x357y0():
 a = pop()
 a is not None and psh(int(not a))
 return x358y0

def x358y0():
 a = pop()
 a is not None and psh(int(not a))
 return x359y0

def x359y0():
 a = pop()
 return [x360y0, X360y0, x360Y0, X360Y0][0 if a is None else (a%4+4)%4]

def x360y0():
 return x362y0

def X360y0():
 return X360y19

def x360Y0():
 a = pop()
 return [x359Y0, Y0x359][1 if a is None else a&1]

def X360Y0():
 return y0x362

def y0x362():
 stack.append(10)
 return x363y0

def x363y0():
 stack.append(5)
 return x364y0

def x364y0():
 stack.append(16)
 return x365y0

def x365y0():
 stack.append(6)
 return x366y0

def x366y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x367y0

def x367y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x368y0

def x368y0():
 a = pop()
 a is not None and psh(a,a)
 return x369y0

def x369y0():
 stack.append(7)
 return x370y0

def x370y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x371y0

def x371y0():
 a = pop()
 a is not None and psh(a,a)
 return x372y0

def x372y0():
 stack.append(4)
 return x373y0

def x373y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x374y0

def x374y0():
 a = pop()
 a is not None and psh(a,a)
 return x375y0

def x375y0():
 stack.append(15)
 return x376y0

def x376y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x377y0

def x377y0():
 stack.append(4)
 return x378y0

def x378y0():
 stack.append(16)
 return x379y0

def x379y0():
 stack.append(7)
 return x380y0

def x380y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x381y0

def x381y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x382y0

def x382y0():
 a = pop()
 a is not None and psh(a,a)
 return x383y0

def x383y0():
 stack.append(1)
 return x384y0

def x384y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x385y0

def x385y0():
 stack.append(16)
 return x386y0

def x386y0():
 stack.append(2)
 return x387y0

def x387y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x388y0

def x388y0():
 stack.append(9)
 return x389y0

def x389y0():
 stack.append(16)
 return x390y0

def x390y0():
 stack.append(7)
 return x391y0

def x391y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x392y0

def x392y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x393y0

def x393y0():
 a = pop()
 a is not None and psh(a,a)
 return x394y0

def x394y0():
 stack.append(7)
 return x395y0

def x395y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x396y0

def x396y0():
 a = pop()
 a is not None and psh(a,a)
 return x397y0

def x397y0():
 stack.append(13)
 return x398y0

def x398y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x399y0

def x399y0():
 a = pop()
 a is not None and psh(a,a)
 return x400y0

def x400y0():
 stack.append(15)
 return x401y0

def x401y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x402y0

def x402y0():
 a = pop()
 a is not None and psh(a,a)
 return x403y0

def x403y0():
 stack.append(1)
 return x404y0

def x404y0():
 stack.append(16)
 return x405y0

def x405y0():
 stack.append(6)
 return x406y0

def x406y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x407y0

def x407y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x408y0

def x408y0():
 a = pop()
 a is not None and psh(a,a)
 return x409y0

def x409y0():
 stack.append(1)
 return x410y0

def x410y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x411y0

def x411y0():
 stack.append(16)
 return x412y0

def x412y0():
 stack.append(2)
 return x413y0

def x413y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x414y0

def x414y0():
 stack.append(5)
 return x415y0

def x415y0():
 stack.append(16)
 return x416y0

def x416y0():
 stack.append(6)
 return x417y0

def x417y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x418y0

def x418y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x419y0

def x419y0():
 a = pop()
 a is not None and psh(a,a)
 return x420y0

def x420y0():
 stack.append(14)
 return x421y0

def x421y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x422y0

def x422y0():
 return y9X423

def y9X423():
 a = pop()
 a is not None and psh(a,a)
 return y10X423

def y10X423():
 stack.append(1)
 return y11X423

def y11X423():
 a,b = pop2()
 a is not None and psh(b-a)
 return y12X423

def y12X423():
 stack.append(2)
 return y14X423

def y14X423():
 a = pop()
 return [y15X423, Y15x423, Y15X423, y15x423][0 if a is None else (a%4+4)%4]

def y15X423():
 return Y12X425

def Y15x423():
 return X425Y12

def Y15X423():
 return Y12X425

def y15x423():
 return X425Y12

def X425Y12():
 a = pop()
 a is not None and psh(a,a)
 return X425Y11

def X425Y11():
 stack.append(3)
 return X425Y8

def X425Y8():
 a,b = pop2()
 a is not None and psh(b-a)
 return X425Y7

def X425Y7():
 return y0x427

def y0x427():
 a = pop()
 a is not None and psh(a,a)
 return y0x428

def y0x428():
 stack.append(7)
 return x429y0

def x429y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x430y0

def x430y0():
 stack.append(16)
 return x431y0

def x431y0():
 stack.append(2)
 return x432y0

def x432y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x433y0

def x433y0():
 stack.append(4)
 return x434y0

def x434y0():
 stack.append(16)
 return x435y0

def x435y0():
 stack.append(7)
 return x436y0

def x436y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x437y0

def x437y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x438y0

def x438y0():
 stack.append(3)
 return x439y0

def x439y0():
 stack.append(16)
 return x440y0

def x440y0():
 stack.append(6)
 return x441y0

def x441y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x442y0

def x442y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x443y0

def x443y0():
 a = pop()
 a is not None and psh(a,a)
 return x444y0

def x444y0():
 stack.append(2)
 return x445y0

def x445y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x446y0

def x446y0():
 a = pop()
 a is not None and psh(a,a)
 return x447y0

def x447y0():
 stack.append(13)
 return x448y0

def x448y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x449y0

def x449y0():
 a = pop()
 a is not None and psh(a,a)
 return x450y0

def x450y0():
 a = pop()
 a is not None and psh(a,a)
 return x451y0

def x451y0():
 stack.append(3)
 return x452y0

def x452y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x453y0

def x453y0():
 a = pop()
 a is not None and psh(a,a)
 return x454y0

def x454y0():
 stack.append(12)
 return x455y0

def x455y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x456y0

def x456y0():
 stack.append(13)
 return x457y0

def x457y0():
 stack.append(16)
 return x458y0

def x458y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x459y0

def x459y0():
 return x462y0

def x462y0():
 stack.append(2)
 return y2X462

def y2X462():
 stack.append(1)
 return y3X462

def y3X462():
 a,b = pop2()
 a is not None and rll(a,b)
 return y4X462

def y4X462():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return y5X462

def y5X462():
 stack.append(1)
 return y6X462

def y6X462():
 a,b = pop2()
 a is not None and psh(b-a)
 return y7X462

def y7X462():
 a = pop()
 a is not None and psh(a,a)
 return y8X462

def y8X462():
 a = pop()
 a is not None and psh(int(not a))
 return y9X462

def y9X462():
 stack.append(3)
 return y12X462

def y12X462():
 a,b = pop2()
 a is not None and psh(b*a)
 return y13X462

def y13X462():
 a = pop()
 a is not None and psh(a,a)
 return y14X462

def y14X462():
 a = pop()
 return [y15X462, Y15x462, Y15X462, y15x462][0 if a is None else (a%4+4)%4]

def y15X462():
 pop()
 return y16X462

def Y15x462():
 a = pop()
 return [X462Y14, Y14X462][1 if a is None else a&1]

def Y15X462():
 a = pop()
 return [Y14X462, X462Y14][1 if a is None else a&1]

def y15x462():
 a = pop()
 return [y15x463, y15X463, Y15x463, Y15X463][0 if a is None else (a%4+4)%4]

def y15x463():
 a = pop()
 return [Y15x462, x462Y15][1 if a is None else a&1]

def y15X463():
 a = pop()
 return [x462Y15, Y15x462][1 if a is None else a&1]

def Y15x463():
 a = pop()
 return [Y15x462, x462Y15][1 if a is None else a&1]

def Y15X463():
 pop()
 return Y14X464

def Y14X464():
 return x465y0

def x465y0():
 return y2X468

def y2X468():
 return
def x462Y15():
 a = pop()
 return [Y14X462, X462Y14][1 if a is None else a&1]

def Y14X462():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y13X462

def X462Y14():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return X462Y13

def X462Y13():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return X462Y12

def X462Y12():
 pop()
 return X462Y11

def X462Y11():
 a,b = pop2()
 a is not None and rll(a,b)
 return X462Y8

def X462Y8():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return X462Y7

def X462Y7():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return X462Y6

def X462Y6():
 pop()
 return X462Y5

def X462Y5():
 a,b = pop2()
 a is not None and psh(b-a)
 return X462Y4

def X462Y4():
 a = pop()
 a is not None and psh(int(not a))
 return X462Y3

def X462Y3():
 pop()
 return X462Y2

def X462Y2():
 pop()
 return X462Y1

def X462Y1():
 stack.append(2)
 return X462y2

def X462y2():
 stack.append(1)
 return X462y3

def X462y3():
 a,b = pop2()
 a is not None and rll(a,b)
 return X462y4

def X462y4():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return X462y5

def X462y5():
 stack.append(1)
 return X462y6

def X462y6():
 a,b = pop2()
 a is not None and psh(b-a)
 return X462y7

def X462y7():
 a = pop()
 a is not None and psh(a,a)
 return X462y8

def X462y8():
 a = pop()
 a is not None and psh(int(not a))
 return X462y9

def X462y9():
 stack.append(3)
 return X462y12

def X462y12():
 a,b = pop2()
 a is not None and psh(b*a)
 return X462y13

def X462y13():
 a = pop()
 a is not None and psh(a,a)
 return X462y14

def X462y14():
 a = pop()
 return [X462y15, x462Y15, X462Y15, x462y15][0 if a is None else (a%4+4)%4]

def X462y15():
 pop()
 return X462y16

def X462Y15():
 a = pop()
 return [X462Y14, Y14X462][1 if a is None else a&1]

def x462y15():
 a = pop()
 return [x463y15, X463y15, x463Y15, X463Y15][0 if a is None else (a%4+4)%4]

def x463y15():
 a = pop()
 return [x462Y15, Y15x462][1 if a is None else a&1]

def X463y15():
 a = pop()
 return [Y15x462, x462Y15][1 if a is None else a&1]

def x463Y15():
 a = pop()
 return [x462Y15, Y15x462][1 if a is None else a&1]

def X463Y15():
 pop()
 return Y14X464

def X462y16():
 return X462y19

def X462y19():
 return X462y22

def X462y22():
 return X462y25

def X462y25():
 return X462y28

def X462y28():
 return Y28x460

def Y28x460():
 return X460Y25

def X460Y25():
 return X460Y22

def X460Y22():
 return X460Y19

def X460Y19():
 return y0x462

def y0x462():
 stack.append(2)
 return X462y2

def Y13X462():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y12X462

def Y12X462():
 pop()
 return Y11X462

def Y11X462():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y8X462

def Y8X462():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y7X462

def Y7X462():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y6X462

def Y6X462():
 pop()
 return Y5X462

def Y5X462():
 a,b = pop2()
 a is not None and psh(b-a)
 return Y4X462

def Y4X462():
 a = pop()
 a is not None and psh(int(not a))
 return Y3X462

def Y3X462():
 pop()
 return Y2X462

def Y2X462():
 pop()
 return Y1X462

def Y1X462():
 stack.append(2)
 return y2X462

def y16X462():
 return y19X462

def y19X462():
 return y22X462

def y22X462():
 return y25X462

def y25X462():
 return y28X462

def y28X462():
 return x460Y28

def x460Y28():
 return Y25X460

def Y25X460():
 return Y22X460

def Y22X460():
 return Y19X460

def Y19X460():
 return x462y0

def Y12X425():
 a = pop()
 a is not None and psh(a,a)
 return Y11X425

def Y11X425():
 stack.append(3)
 return Y8X425

def Y8X425():
 a,b = pop2()
 a is not None and psh(b-a)
 return Y7X425

def Y7X425():
 return x427y0

def x427y0():
 a = pop()
 a is not None and psh(a,a)
 return x428y0

def x428y0():
 stack.append(7)
 return x429y0

def x359Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x358Y0

def Y0x359():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x358

def Y0x358():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x357

def Y0x357():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x356

def Y0x356():
 a = input()
 psh(ord(a))
 return Y0x355

def Y0x355():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x354

def Y0x354():
 pop()
 return Y0x353

def Y0x353():
 pop()
 return Y0x352

def Y0x352():
 pop()
 return Y0x351

def Y0x351():
 return Y0x349

def Y0x349():
 a = pop()
 return [Y0x348, x348Y0][1 if a is None else a&1]

def Y0x348():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x347

def x348Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x347Y0

def x347Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x346Y0

def x346Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x345Y0

def x345Y0():
 a = input()
 breakpoint()
 psh(ord(a))
 return x344Y0

def x344Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x343Y0

def x343Y0():
 pop()
 return x342Y0

def x342Y0():
 pop()
 return x341Y1

def x341Y1():
 pop()
 return Y0x340

def Y0x340():
 return Y0x338

def Y0x338():
 a = pop()
 return [Y0x337, x337Y0][1 if a is None else a&1]

def Y0x337():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x336

def x337Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x336Y0

def x336Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x335Y0

def x335Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x334Y0

def x334Y0():
 a = input()
 breakpoint()
 psh(ord(a))
 return x333Y0

def x333Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x332Y0

def x332Y0():
 pop()
 return x331Y0

def x331Y0():
 pop()
 return x330Y6

def x330Y6():
 pop()
 return Y0x329

def Y0x329():
 return Y0x327

def Y0x327():
 a = pop()
 return [Y0x326, x326Y0][1 if a is None else a&1]

def Y0x326():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x325

def x326Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x325Y0

def x325Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x324Y0

def x324Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x323Y0

def x323Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x322Y0

def x322Y0():
 pop()
 return x321Y0

def x321Y0():
 pop()
 return x320Y2

def x320Y2():
 return Y0x318

def Y0x318():
 a = pop()
 return [Y0x317, x317Y0][1 if a is None else a&1]

def Y0x317():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x316

def x317Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x316Y0

def x316Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x315Y0

def x315Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x314Y0

def x314Y0():
 a = input()
 psh(ord(a))
 return x313Y0

def x313Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x312Y0

def x312Y0():
 pop()
 return x311Y0

def x311Y0():
 pop()
 return x310Y5

def x310Y5():
 pop()
 return Y0x309

def Y0x309():
 return Y0x307

def Y0x307():
 a = pop()
 return [Y0x306, x306Y0][1 if a is None else a&1]

def Y0x306():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x305

def x306Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x305Y0

def x305Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x304Y0

def x304Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x303Y0

def x303Y0():
 a = input()
 psh(ord(a))
 return x302Y0

def x302Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x301Y0

def x301Y0():
 pop()
 return x300Y0

def x300Y0():
 pop()
 return x299Y2

def x299Y2():
 pop()
 return Y0x298

def Y0x298():
 return Y0x296

def Y0x296():
 a = pop()
 return [Y0x295, x295Y0][1 if a is None else a&1]

def Y0x295():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x294

def x295Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x294Y0

def x294Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x293Y0

def x293Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x292Y0

def x292Y0():
 a = input()
 psh(ord(a))
 return x291Y0

def x291Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x290Y0

def x290Y0():
 pop()
 return x289Y0

def x289Y0():
 pop()
 return x288Y5

def x288Y5():
 pop()
 return Y0x287

def Y0x287():
 return Y0x285

def Y0x285():
 a = pop()
 return [Y0x284, x284Y0][1 if a is None else a&1]

def Y0x284():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x283

def x284Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x283Y0

def x283Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x282Y0

def x282Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x281Y0

def x281Y0():
 a = input()
 psh(ord(a))
 return x280Y0

def x280Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x279Y0

def x279Y0():
 pop()
 return x278Y0

def x278Y0():
 pop()
 return x277Y6

def x277Y6():
 pop()
 return Y0x276

def Y0x276():
 return Y0x274

def Y0x274():
 a = pop()
 return [Y0x273, x273Y0][1 if a is None else a&1]

def Y0x273():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x272

def x273Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x272Y0

def x272Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x271Y0

def x271Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x270Y0

def x270Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x269Y0

def x269Y0():
 pop()
 return x268Y0

def x268Y0():
 pop()
 return x267Y2

def x267Y2():
 return Y0x265

def Y0x265():
 a = pop()
 return [Y0x264, x264Y0][1 if a is None else a&1]

def Y0x264():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x263

def x264Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x263Y0

def x263Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x262Y0

def x262Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x261Y0

def x261Y0():
 a = input()
 psh(ord(a))
 return x260Y0

def x260Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x259Y0

def x259Y0():
 pop()
 return x258Y0

def x258Y0():
 pop()
 return x257Y6

def x257Y6():
 pop()
 return Y0x256

def Y0x256():
 return Y0x254

def Y0x254():
 a = pop()
 return [Y0x253, x253Y0][1 if a is None else a&1]

def Y0x253():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x252

def x253Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x252Y0

def x252Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x251Y0

def x251Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x250Y0

def x250Y0():
 a = input()
 psh(ord(a))
 return x249Y0

def x249Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x248Y0

def x248Y0():
 pop()
 return x247Y0

def x247Y0():
 pop()
 return x246Y4

def x246Y4():
 pop()
 return Y0x245

def Y0x245():
 stack.append(4)
 return Y0x244

def Y0x244():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x243

def Y0x243():
 pop()
 return Y0x242

def Y0x242():
 stack.append(1)
 return Y0x241

def Y0x241():
 return y0x241

def y0x241():
 pop()
 return y0x242

def y0x242():
 stack.append(1)
 return y0x243

def y0x243():
 a,b = pop2()
 a is not None and psh(b-a)
 return y0x244

def y0x244():
 pop()
 return y0x245

def y0x245():
 stack.append(4)
 return y3x246

def y3x246():
 stack.append(16)
 return x247y0

def Y0x252():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x251

def Y0x251():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x250

def Y0x250():
 a = input()
 psh(ord(a))
 return Y0x249

def Y0x249():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x248

def Y0x248():
 pop()
 return Y0x247

def Y0x247():
 pop()
 return Y0x246

def Y0x246():
 pop()
 return Y0x245

def Y0x263():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x262

def Y0x262():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x261

def Y0x261():
 a = input()
 psh(ord(a))
 return Y0x260

def Y0x260():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x259

def Y0x259():
 pop()
 return Y0x258

def Y0x258():
 pop()
 return Y0x257

def Y0x257():
 pop()
 return Y0x256

def Y0x272():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x271

def Y0x271():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x270

def Y0x270():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x269

def Y0x269():
 pop()
 return Y0x268

def Y0x268():
 pop()
 return Y0x267

def Y0x267():
 return Y0x265

def Y0x283():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x282

def Y0x282():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x281

def Y0x281():
 a = input()
 psh(ord(a))
 return Y0x280

def Y0x280():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x279

def Y0x279():
 pop()
 return Y0x278

def Y0x278():
 pop()
 return Y0x277

def Y0x277():
 pop()
 return Y0x276

def Y0x294():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x293

def Y0x293():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x292

def Y0x292():
 a = input()
 psh(ord(a))
 return Y0x291

def Y0x291():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x290

def Y0x290():
 pop()
 return Y0x289

def Y0x289():
 pop()
 return Y0x288

def Y0x288():
 pop()
 return Y0x287

def Y0x305():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x304

def Y0x304():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x303

def Y0x303():
 a = input()
 psh(ord(a))
 return Y0x302

def Y0x302():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x301

def Y0x301():
 pop()
 return Y0x300

def Y0x300():
 pop()
 return Y0x299

def Y0x299():
 pop()
 return Y0x298

def Y0x316():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x315

def Y0x315():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x314

def Y0x314():
 a = input()
 psh(ord(a))
 return Y0x313

def Y0x313():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x312

def Y0x312():
 pop()
 return Y0x311

def Y0x311():
 pop()
 return Y0x310

def Y0x310():
 pop()
 return Y0x309

def Y0x325():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x324

def Y0x324():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x323

def Y0x323():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x322

def Y0x322():
 pop()
 return Y0x321

def Y0x321():
 pop()
 return Y0x320

def Y0x320():
 return Y0x318

def Y0x336():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x335

def Y0x335():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x334

def Y0x334():
 a = input()
 psh(ord(a))
 return Y0x333

def Y0x333():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x332

def Y0x332():
 pop()
 return Y0x331

def Y0x331():
 pop()
 return Y0x330

def Y0x330():
 pop()
 return Y0x329

def Y0x347():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x346

def Y0x346():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y0x345

def Y0x345():
 a = input()
 psh(ord(a))
 return Y0x344

def Y0x344():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y0x343

def Y0x343():
 pop()
 return Y0x342

def Y0x342():
 pop()
 return Y0x341

def Y0x341():
 pop()
 return Y0x340

def x358Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x357Y0

def x357Y0():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return x356Y0

def x356Y0():
 a = input()
 psh(ord(a))
 return x355Y0

def x355Y0():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return x354Y0

def x354Y0():
 pop()
 return x353Y0

def x353Y0():
 pop()
 return x352Y2

def x352Y2():
 pop()
 return Y0x351

def X360y19():
 return Y19x349

def Y19x349():
 return Y19x338

def Y19x338():
 return Y19x327

def Y19x327():
 return Y19x318

def Y19x318():
 return Y19x307

def Y19x307():
 return Y19x296

def Y19x296():
 return Y19x285

def Y19x285():
 return Y19x274

def Y19x274():
 return Y19x265

def Y19x265():
 return Y19x254

def Y19x254():
 return Y19x240

def Y19x240():
 return Y19x238

def Y19x238():
 return Y19x227

def Y19x227():
 return Y19x220

def Y19x220():
 return Y19x210

def Y19x210():
 return Y19x201

def Y19x201():
 return Y19x197

def Y19x197():
 return Y19x195

def Y19x195():
 return Y19x188

def Y19x188():
 return Y19x186

def Y19x186():
 return y19x186

def y19x186():
 return y19x188

def y19x188():
 return y19x195

def y19x195():
 return y19x197

def y19x197():
 return y19x201

def y19x201():
 return y19x210

def y19x210():
 return y19x220

def y19x220():
 return y19x227

def y19x227():
 return y19x238

def y19x238():
 return y19x240

def y19x240():
 return y19x254

def y19x254():
 return y19x265

def y19x265():
 return y19x274

def y19x274():
 return y19x285

def y19x285():
 return y19x296

def y19x296():
 return y19x307

def y19x307():
 return y19x318

def y19x318():
 return y19x327

def y19x327():
 return y19x338

def y19x338():
 return y19x349

def y19x349():
 return y19x360

def y19x360():
 return y19x460

def y19x460():
 return y19x462

def y19x462():
 return y19x471

def y19x471():
 return y0x472

def y0x472():
 stack.append(10)
 return x473y0

def x473y0():
 stack.append(1)
 return x474y0

def x474y0():
 stack.append(16)
 return x475y0

def x475y0():
 stack.append(2)
 return x476y0

def x476y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x477y0

def x477y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x478y0

def x478y0():
 stack.append(4)
 return x479y0

def x479y0():
 stack.append(16)
 return x480y0

def x480y0():
 stack.append(7)
 return x481y0

def x481y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x482y0

def x482y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x483y0

def x483y0():
 stack.append(3)
 return x484y0

def x484y0():
 stack.append(16)
 return x485y0

def x485y0():
 stack.append(6)
 return x486y0

def x486y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x487y0

def x487y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x488y0

def x488y0():
 a = pop()
 a is not None and psh(a,a)
 return x489y0

def x489y0():
 stack.append(2)
 return x490y0

def x490y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x491y0

def x491y0():
 a = pop()
 a is not None and psh(a,a)
 return x492y0

def x492y0():
 stack.append(13)
 return x493y0

def x493y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x494y0

def x494y0():
 a = pop()
 a is not None and psh(a,a)
 return x495y0

def x495y0():
 a = pop()
 a is not None and psh(a,a)
 return x496y0

def x496y0():
 stack.append(3)
 return x497y0

def x497y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x498y0

def x498y0():
 a = pop()
 a is not None and psh(a,a)
 return x499y0

def x499y0():
 stack.append(12)
 return x500y0

def x500y0():
 a,b = pop2()
 a is not None and psh(b-a)
 return x501y0

def x501y0():
 a = pop()
 a is not None and psh(a,a)
 return x502y0

def x502y0():
 stack.append(11)
 return x503y0

def x503y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x504y0

def x504y0():
 stack.append(9)
 return x505y0

def x505y0():
 stack.append(16)
 return x506y0

def x506y0():
 stack.append(4)
 return x507y0

def x507y0():
 a,b = pop2()
 a is not None and psh(b*a)
 return x508y0

def x508y0():
 a,b = pop2()
 a is not None and psh(b+a)
 return x509y0

def x509y0():
 stack.append(11)
 return x510y0

def x510y0():
 return x513y0

def x513y0():
 stack.append(2)
 return y2X513

def y2X513():
 stack.append(1)
 return y3X513

def y3X513():
 a,b = pop2()
 a is not None and rll(a,b)
 return y4X513

def y4X513():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return y5X513

def y5X513():
 stack.append(1)
 return y6X513

def y6X513():
 a,b = pop2()
 a is not None and psh(b-a)
 return y7X513

def y7X513():
 a = pop()
 a is not None and psh(a,a)
 return y8X513

def y8X513():
 a = pop()
 a is not None and psh(int(not a))
 return y9X513

def y9X513():
 stack.append(3)
 return y12X513

def y12X513():
 a,b = pop2()
 a is not None and psh(b*a)
 return y13X513

def y13X513():
 a = pop()
 a is not None and psh(a,a)
 return y14X513

def y14X513():
 a = pop()
 return [y15X513, Y15x513, Y15X513, y15x513][0 if a is None else (a%4+4)%4]

def y15X513():
 pop()
 return y16X513

def Y15x513():
 a = pop()
 return [X513Y14, Y14X513][1 if a is None else a&1]

def Y15X513():
 a = pop()
 return [Y14X513, X513Y14][1 if a is None else a&1]

def y15x513():
 a = pop()
 return [y15x514, y15X514, Y15x514, Y15X514][0 if a is None else (a%4+4)%4]

def y15x514():
 a = pop()
 return [Y15x513, x513Y15][1 if a is None else a&1]

def y15X514():
 a = pop()
 return [x513Y15, Y15x513][1 if a is None else a&1]

def Y15x514():
 a = pop()
 return [Y15x513, x513Y15][1 if a is None else a&1]

def Y15X514():
 pop()
 return Y14X515

def Y14X515():
 return x516y0

def x516y0():
 return y2X519

def y2X519():
 return
def x513Y15():
 a = pop()
 return [Y14X513, X513Y14][1 if a is None else a&1]

def Y14X513():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y13X513

def X513Y14():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return X513Y13

def X513Y13():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return X513Y12

def X513Y12():
 pop()
 return X513Y11

def X513Y11():
 a,b = pop2()
 a is not None and rll(a,b)
 return X513Y8

def X513Y8():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return X513Y7

def X513Y7():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return X513Y6

def X513Y6():
 pop()
 return X513Y5

def X513Y5():
 a,b = pop2()
 a is not None and psh(b-a)
 return X513Y4

def X513Y4():
 a = pop()
 a is not None and psh(int(not a))
 return X513Y3

def X513Y3():
 pop()
 return X513Y2

def X513Y2():
 pop()
 return X513Y1

def X513Y1():
 stack.append(2)
 return X513y2

def X513y2():
 stack.append(1)
 return X513y3

def X513y3():
 a,b = pop2()
 a is not None and rll(a,b)
 return X513y4

def X513y4():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return X513y5

def X513y5():
 stack.append(1)
 return X513y6

def X513y6():
 a,b = pop2()
 a is not None and psh(b-a)
 return X513y7

def X513y7():
 a = pop()
 a is not None and psh(a,a)
 return X513y8

def X513y8():
 a = pop()
 a is not None and psh(int(not a))
 return X513y9

def X513y9():
 stack.append(3)
 return X513y12

def X513y12():
 a,b = pop2()
 a is not None and psh(b*a)
 return X513y13

def X513y13():
 a = pop()
 a is not None and psh(a,a)
 return X513y14

def X513y14():
 a = pop()
 return [X513y15, x513Y15, X513Y15, x513y15][0 if a is None else (a%4+4)%4]

def X513y15():
 pop()
 return X513y16

def X513Y15():
 a = pop()
 return [X513Y14, Y14X513][1 if a is None else a&1]

def x513y15():
 a = pop()
 return [x514y15, X514y15, x514Y15, X514Y15][0 if a is None else (a%4+4)%4]

def x514y15():
 a = pop()
 return [x513Y15, Y15x513][1 if a is None else a&1]

def X514y15():
 a = pop()
 return [Y15x513, x513Y15][1 if a is None else a&1]

def x514Y15():
 a = pop()
 return [x513Y15, Y15x513][1 if a is None else a&1]

def X514Y15():
 pop()
 return Y14X515

def X513y16():
 return X513y19

def X513y19():
 return X513y22

def X513y22():
 return X513y25

def X513y25():
 return X513y28

def X513y28():
 return Y28x511

def Y28x511():
 return X511Y25

def X511Y25():
 return X511Y22

def X511Y22():
 return X511Y19

def X511Y19():
 return y0x513

def y0x513():
 stack.append(2)
 return X513y2

def Y13X513():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y12X513

def Y12X513():
 pop()
 return Y11X513

def Y11X513():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y8X513

def Y8X513():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y7X513

def Y7X513():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y6X513

def Y6X513():
 pop()
 return Y5X513

def Y5X513():
 a,b = pop2()
 a is not None and psh(b-a)
 return Y4X513

def Y4X513():
 a = pop()
 a is not None and psh(int(not a))
 return Y3X513

def Y3X513():
 pop()
 return Y2X513

def Y2X513():
 pop()
 return Y1X513

def Y1X513():
 stack.append(2)
 return y2X513

def y16X513():
 return y19X513

def y19X513():
 return y22X513

def y22X513():
 return y25X513

def y25X513():
 return y28X513

def y28X513():
 return x511Y28

def x511Y28():
 return Y25X511

def Y25X511():
 return Y22X511

def Y22X511():
 return Y19X511

def Y19X511():
 return x513y0

def x362y0():
 stack.append(10)
 return x363y0

def X349y19():
 return Y19x338

def x351y0():
 stack.append(3)
 return x352y0

def x352y0():
 stack.append(16)
 return x353y0

def X338y19():
 return Y19x327

def x340y0():
 stack.append(6)
 return x341y0

def x341y0():
 stack.append(16)
 return x342y0

def X327y19():
 return Y19x318

def x329y0():
 stack.append(2)
 return x330y0

def x330y0():
 stack.append(16)
 return x331y0

def X318y19():
 return Y19x307

def x320y0():
 stack.append(16)
 return x321y0

def X307y19():
 return Y19x296

def x309y0():
 stack.append(4)
 return x310y0

def x310y0():
 stack.append(16)
 return x311y0

def X296y19():
 return Y19x285

def x298y0():
 stack.append(4)
 return x299y0

def x299y0():
 stack.append(16)
 return x300y0

def X285y19():
 return Y19x274

def x287y0():
 stack.append(2)
 return x288y0

def x288y0():
 stack.append(16)
 return x289y0

def X274y19():
 return Y19x265

def x276y0():
 stack.append(5)
 return x277y0

def x277y0():
 stack.append(16)
 return x278y0

def X265y19():
 return Y19x254

def x267y0():
 stack.append(16)
 return x268y0

def X254y19():
 return Y19x240

def x256y0():
 stack.append(2)
 return x257y0

def x257y0():
 stack.append(16)
 return x258y0

def X227Y21():
 return X227Y19

def Y21X227():
 return Y19X227

def Y19X227():
 return Y6X227

def Y6X227():
 pop()
 return Y5X227

def Y5X227():
 return Y1X227

def Y1X227():
 stack.append(1)
 return Y0X227

def Y0X227():
 return x229y0

def x229y0():
 stack.append(2)
 return x230y0

def X227Y19():
 return X227Y6

def X227Y6():
 pop()
 return X227Y5

def X227Y5():
 return X227Y1

def X227Y1():
 stack.append(1)
 return X227Y0

def x220Y22():
 return x210Y22

def x210Y22():
 return x201Y22

def x201Y22():
 return x197Y22

def x197Y22():
 return Y19X197

def Y19X197():
 return x198y0

def Y22x220():
 return Y22x210

def Y22x210():
 return Y22x201

def Y22x201():
 return Y22x197

def Y22x197():
 return X197Y19

def X197Y19():
 return y0x198

def X220y1():
 return X220y19

def X220y19():
 return X220y22

def X220y22():
 return Y22x210

def x222y0():
 a = pop()
 a is not None and psh(a,a)
 return x223y0

def x223y0():
 stack.append(10)
 return x224y0

def X195Y24():
 return X195Y22

def Y24X195():
 return Y22X195

def Y22X195():
 return Y19X195

def Y19X195():
 return Y6X195

def Y6X195():
 pop()
 return Y5X195

def Y5X195():
 return Y0X195

def Y0X195():
 return y3X195

def y3X195():
 stack.append(3)
 return y6X195

def y6X195():
 return y19X195

def y19X195():
 return y22X195

def y22X195():
 return y24X195

def y24X195():
 a = pop()
 return [y25X195, Y25x195, Y25X195, y25x195][0 if a is None else (a%4+4)%4]

def y25X195():
 return x188Y25

def Y25X195():
 a = pop()
 return [Y24X195, X195Y24][1 if a is None else a&1]

def x188Y25():
 return x186Y25

def x186Y25():
 return x186y25

def x186y25():
 return x188y25

def x188y25():
 return x195y25

def X195Y22():
 return X195Y19

def X195Y19():
 return X195Y6

def X195Y6():
 pop()
 return X195Y5

def X195Y5():
 return X195Y0

def x194Y0():
 pop()
 return x193Y0

def Y0x194():
 pop()
 return Y0x193

def Y0x193():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y0x192

def Y0x192():
 pop()
 return Y0x191

def Y0x191():
 return y0x191

def y0x191():
 stack.append(1)
 return y0x192

def y0x192():
 a = pop()
 a is not None and psh(int(not a))
 return y0x193

def y0x193():
 stack.append(1)
 return y0x194

def y0x194():
 a = pop()
 return [y0x195, y0X195, Y0x195, Y0X195][0 if a is None else (a%4+4)%4]

def y0x195():
 return X195y3

def y0X195():
 return y3X195

def Y0x195():
 a = pop()
 return [Y0x194, x194Y0][1 if a is None else a&1]

def x193Y0():
 a,b = pop2()
 a is not None and rll(a,b)
 return x192Y0

def x192Y0():
 pop()
 return x191Y0

def x191Y0():
 return x191y0

def x188Y15():
 a = pop()
 return [Y14X188, X188Y14][1 if a is None else a&1]

def Y14X188():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y13X188

def X188Y14():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return X188Y13

def X188Y13():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return X188Y12

def X188Y12():
 pop()
 return X188Y11

def X188Y11():
 a,b = pop2()
 a is not None and rll(a,b)
 return X188Y8

def X188Y8():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return X188Y7

def X188Y7():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return X188Y6

def X188Y6():
 pop()
 return X188Y5

def X188Y5():
 a,b = pop2()
 a is not None and psh(b-a)
 return X188Y4

def X188Y4():
 a = pop()
 a is not None and psh(int(not a))
 return X188Y3

def X188Y3():
 pop()
 return X188Y2

def X188Y2():
 pop()
 return X188Y1

def X188Y1():
 stack.append(2)
 return X188y2

def X188y2():
 stack.append(1)
 return X188y3

def X188y3():
 a,b = pop2()
 a is not None and rll(a,b)
 return X188y4

def X188y4():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return X188y5

def X188y5():
 stack.append(1)
 return X188y6

def X188y6():
 a,b = pop2()
 a is not None and psh(b-a)
 return X188y7

def X188y7():
 a = pop()
 a is not None and psh(a,a)
 return X188y8

def X188y8():
 a = pop()
 a is not None and psh(int(not a))
 return X188y9

def X188y9():
 stack.append(3)
 return X188y12

def X188y12():
 a,b = pop2()
 a is not None and psh(b*a)
 return X188y13

def X188y13():
 a = pop()
 a is not None and psh(a,a)
 return X188y14

def X188y14():
 a = pop()
 return [X188y15, x188Y15, X188Y15, x188y15][0 if a is None else (a%4+4)%4]

def X188y15():
 pop()
 return X188y16

def X188Y15():
 a = pop()
 return [X188Y14, Y14X188][1 if a is None else a&1]

def x188y15():
 a = pop()
 return [x189y15, X189y15, x189Y15, X189Y15][0 if a is None else (a%4+4)%4]

def x189y15():
 a = pop()
 return [x188Y15, Y15x188][1 if a is None else a&1]

def X189y15():
 a = pop()
 return [Y15x188, x188Y15][1 if a is None else a&1]

def x189Y15():
 a = pop()
 return [x188Y15, Y15x188][1 if a is None else a&1]

def X189Y15():
 pop()
 return Y14X190

def X188y16():
 return X188y19

def X188y19():
 return X188y22

def X188y22():
 return X188y25

def X188y25():
 return X188y28

def X188y28():
 return Y28x186

def Y28x186():
 return X186Y25

def X186Y25():
 return X186Y22

def X186Y22():
 return X186Y19

def X186Y19():
 return y0x188

def y0x188():
 stack.append(2)
 return X188y2

def Y13X188():
 a = pop()
 a is not None and print(a, sep='', end='', flush=1)
 return Y12X188

def Y12X188():
 pop()
 return Y11X188

def Y11X188():
 a,b = pop2()
 a is not None and rll(a,b)
 return Y8X188

def Y8X188():
 a,b = pop2()
 a is not None and a!=0 and psh(b//a)
 return Y7X188

def Y7X188():
 a = pop()
 a is not None and print(chr(a&255), sep='', end='', flush=1)
 return Y6X188

def Y6X188():
 pop()
 return Y5X188

def Y5X188():
 a,b = pop2()
 a is not None and psh(b-a)
 return Y4X188

def Y4X188():
 a = pop()
 a is not None and psh(int(not a))
 return Y3X188

def Y3X188():
 pop()
 return Y2X188

def Y2X188():
 pop()
 return Y1X188

def Y1X188():
 stack.append(2)
 return y2X188

def y16X188():
 return y19X188

def y19X188():
 return y22X188

def y22X188():
 return y25X188

def y25X188():
 return y28X188

def y28X188():
 return x186Y28

def x186Y28():
 return Y25X186

def Y25X186():
 return Y22X186

def Y22X186():
 return Y19X186

def Y19X186():
 return x188y0

def Y12X117():
 a = pop()
 a is not None and psh(a,a)
 return Y11X117

def Y11X117():
 stack.append(2)
 return Y9X117

def Y9X117():
 a,b = pop2()
 a is not None and psh(b-a)
 return Y8X117

def Y8X117():
 return x120y0

def x120y0():
 stack.append(7)
 return x121y0

def x121y0():
 stack.append(16)
 return x122y0

if __name__ == "__main__":
    bounce = x0y0
    while bounce is not None:
        bounce = bounce()
