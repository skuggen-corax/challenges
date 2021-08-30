#!/usr/bin/env python
from pwn import remote, log

def gen_fibs(n):
    i = 0
    fibs_d = {}

    while i<=n:
        if i <= 1:
            fibs_d[i] = i
        else:
            fibs_d[i] = fibs_d[i-1] + fibs_d[i-2]
        i+=1

    return fibs_d


def gen_strange_fibs(n):
    i = 0
    fibs_d = {}

    while i <= n:
        if i == 0:
            fibs_d[i] = 4
        elif i == 1:
            fibs_d[i] = 5
        else:
            fibs_d[i] = fibs_d[i-1] + fibs_d[i-2]

        i += 1

    return fibs_d


fibs = gen_strange_fibs(1000)


def gen_s(n):
    i = 0
    s_d = {}
    
    while i <= n:
        if i == 0:
            s_d[i] = 4
        else:
            s_d[i] = s_d[i-1] + fibs[i]
        i += 1

    return s_d

s = gen_s(1000)


def s_sum(n):
    return sum([s[n] for n in range(n+1)])


def print_sum(n):
    ssum = s_sum(n)
    return str(int(str(ssum)[-10:]))


c = remote('extended-fibonacci-sequence-2.hsc.tf', 1337)
case = 0
while case < 15:
    c.recvuntil(b"Here's case ")
    case = int(c.recvline().decode().split('!')[0])
    log.info(f"Starting with case: {case}")
    num = int(c.recvline().decode().strip())
    calc = print_sum(num)
    print(num, '=>', calc)
    c.sendline(calc)
    print(c.recvline().decode().strip())

print(c.recvall().decode().strip())
