#!/usr/bin/env python3

import codecs
import itertools
import string
from base64 import b64decode
from pwn import remote, log, context, xor
# from basecrack.basecrack import BaseCrack


def vigenere(plaintext, key, a_is_zero=True):
    # https://gist.github.com/akonradi/a9637c17fc6452d868ee
    key = key.lower()
    if not all(k in string.ascii_lowercase for k in key):
        raise ValueError("Invalid key {!r}; the key can only consist of English letters".format(key))
    key_iter = itertools.cycle(map(ord, key))
    return "".join(
        chr(ord('a') + (
            (next(key_iter) - ord('a') + ord(letter) - ord('a'))
            + (0 if a_is_zero else 2)
            ) % 26) if letter in string.ascii_lowercase
        else letter
        for letter in plaintext.lower()
    )


def vig(ciphertext, key, a_is_zero=True):
    inverse = "".join(chr(ord('a') +
            ((26 if a_is_zero else 22) -
                (ord(k) - ord('a'))
            ) % 26) for k in key)
    return vigenere(ciphertext, inverse, a_is_zero)


log.info("TG21{} - are ye pirate?")
context.log_level = "info"
c = remote('are-ye-pirate.tghack.no', 1337)
c.recvline(())

level = 0
while True:
    chal = c.recvline()
    if "Level" in chal.decode()[:7]:
        level = int(chal.decode()[6:7])
        # if level == 7:
        #    context.log_level = "debug"

        log.progress("Level:", str(level))
        c.recvuntil("input>")
        c.sendline("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZhhh@[]_/|\\{}`.^~")
        resp = c.recvline()
        chal = c.recvline()
    elif "Wrong" in chal.decode()[:7]:
        print(res)
        print(chal.decode())
        exit()
    elif "flag" in chal.decode()[:35]:
        flag = c.recvline()
        print(flag.decode())
        exit()

    chal = " ".join(chal.decode().split(" ")[2:]).strip()

    if level == 1:
        # base 64
        # res = BaseCrack().decode(chal)
        res = b64decode(chal)
        c.sendline(res)

    elif level == 2:
        # rot13
        res = codecs.decode(chal, 'rot_13')
        c.sendline(res)

    elif level == 3:
        # rot13 + b64d + rot13
        res = codecs.decode(chal, 'rot_13')
        res = b64decode(res)
        res = codecs.decode(res.decode(), 'rot_13')
        c.sendline(res)

    elif level == 4:
        # b64 + xor(0x2a)
        res = b64decode(chal)
        res = xor(res, b"\x2a")
        c.sendline(res)

    elif level == 5:
        # vigene "tghack"
        res = vig(chal, "tghack")
        c.sendline(res)

    elif level == 6:
        # vigene "tghack" + rot13
        res = vig(chal, "tghack")
        res = codecs.decode(res, 'rot_13')
        c.sendline(res)

    elif level == 7:
        # b64d + xor(0x2a) + vigene(tghack)
        res = b64decode(chal)
        res = xor(res, b"\x2a")
        res = vig(res.decode(), "tghack")
        c.sendline(res)

    c.recvuntil("> ")
