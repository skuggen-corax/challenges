# 5 keys, need 3

#fav = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151

#k3 = 570999082059702856147787459046280784390391309763131887566210928611371012340016305879778028495709778777
#k4 = 922383132557981536854118203074761267092170577309674587606956115449137789164641724882718353723838873409
#k5 = 1361613195680829887737031633110361870469394661742852962657887598996346260195423498636393760259000241699

# prøver shamir...

#!/usr/bin/env python 
"""
from: https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing
"""

from __future__ import division
from __future__ import print_function

import random
import functools

_PRIME = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151

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


npst = [(3,570999082059702856147787459046280784390391309763131887566210928611371012340016305879778028495709778777), 
         (4, 922383132557981536854118203074761267092170577309674587606956115449137789164641724882718353723838873409), 
         (5, 1361613195680829887737031633110361870469394661742852962657887598996346260195423498636393760259000241699)]


if __name__ == '__main__':
    print('recover flag with sigurd/shamir secret sharing ..')
    secret = recover_secret(npst)
    hexified = hex(secret)
    i = 2
    while i < len(hexified):
        print(chr(int(hexified[i:i+2],16)),end="")
        i +=2

print("")