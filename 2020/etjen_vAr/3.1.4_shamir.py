#!/usr/bin/env python 
"""
from: https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing
"""

from __future__ import division
from __future__ import print_function

import random
import functools

# 11th Mersenne Prime
_PRIME = 2 ** 107 - 1
# 12th Mersenne Prime is 2**127 -1, 13th is 2**521 - 1

def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1) this can
    be computed via extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    """Compute num / den modulo prime p

    To explain what this means, the return value will be such that
    the following is true: den * _divmod(num, den, p) % p == num
    """
    inv, _ = _extended_gcd(den, p)
    return num * inv

def _lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p

def recover_secret(shares, prime=_PRIME):
    """
    Recover the secret from share points
    (x, y points on the polynomial).
    """
    #print(shares)
    if len(shares) < 2:
        raise ValueError("need at least two shares")
    x_s, y_s = zip(*shares)
    return _lagrange_interpolate(0, x_s, y_s, prime)


etjen = [(1,84657984464390529825364497916194), 
         (2, 73673086149599787963942979835811), 
         (5, 38135776304496424228868822226466)]

etjenk4 = [ (1,154315253502745748263921158136531),
            (7, 50678100992992927876293959379162), 
            (8, 122616934121449585737032791184753), 
            (10, 80773256441241836218608398852592)]

etjenk9 = [ (1, 18431917384105746930902281228572), 
            (2, 47116559448583257145160102856755),
            (3, 43359780976439286737053677319959),
            (4, 42692857761587209442928328545055),
            (5, 116094178794117191280811579355275),
            (7, 158227487577296337342281607135847), 
            (8, 64858484496858151362905892937447), 
            (9, 29731193030541008318265718603098), 
            (10, 33908546822044766120109498310017)]

if __name__ == '__main__':
    print('k=3: ', recover_secret(etjen))
    print('k=4: ', recover_secret(etjenk4))
    print('k=9: ', recover_secret(etjenk9))