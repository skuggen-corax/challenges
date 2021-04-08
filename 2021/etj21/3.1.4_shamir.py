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

etjenk4 = [ (1, 103897326758549940055925588924916),
            (2, 10340134542888813646404431216601),
            (8, 152164276776809363141295407085942), 
            (10, 46833376042454306127670627241261),
            (11, 118513551624680702545283450296591)]

etjenk9 = [ (1, 78416662352898028738456380336979), 
            (2, 54512220361155434109080573852585),
            (3, ),
            (4, 22896490884629287279847925445605),
            (5, ),
            (7, 129588987433539636912903729062440), 
            (8, 20207262580225677916488220830573), 
            (9, 31266589518595858674009820958195), 
            (10, 116256089605332522308483017004116),
            (11, 66405607367904648551344286239019)]

if __name__ == '__main__':
    print('k=3: ', recover_secret(etjen))
    print('k=4: ', recover_secret(etjenk4))
    print('k=9: ', recover_secret(etjenk9))