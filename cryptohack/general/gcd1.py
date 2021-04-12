#!/usr/bin/env python3


def gcd(a, b):
    if b > a:
        a, b = b, a
    while True:
        # print("a:", a, "b:", b)
        if a >= 2 * b:
            a = a - b
        else:
            a, b = b, a - b

        if b == 0:
            return a


def nicer_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = 12
b = 8

assert gcd(a, b) == 4
assert nicer_gcd(b, a) == 4

a = 66528
b = 52920
print("flag:", nicer_gcd(a, b))
