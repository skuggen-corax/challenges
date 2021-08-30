#!/usr/bin/env python
from pwn import remote, log

def gen_hops(n):
    i = 0
    hop_d = {}

    while i <= n:
        if i == 0:
            hop_d[i] = 0
        elif i == 1:
            hop_d[i] = 1
        elif i == 2:
            hop_d[i] = 2
        else:
            hop_d[i] = hop_d[i-1] + hop_d[i-2]

        i += 1

    return hop_d


hops = gen_hops(1000)


def print_sum(n):
    ssum = hops[n]
    return ssum % 10000


c = remote('hopscotch.hsc.tf', 1337)
case = 0
print(c.recvline())
while True:
    rec = c.recvline().decode().strip()
    if rec[:1] == "b":
        print(rec)
        exit()
    num = int(rec)
    calc = print_sum(num)

    log.info(f"Got {num}, sending {calc})")
    c.sendline(str(calc))
    c.recvuntil(b': ')


print(c.recvall().decode().strip())
