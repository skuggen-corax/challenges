#!/usr/bin/env python3


def ext_gcd(a, b):
    """returns: (gcd, u, v) """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        # print("a:", a, "b:", b)
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return (old_r, old_s, old_t)


p = 26513
q = 32321

g, u, v = ext_gcd(p, q)

print("flag: crypto{" + str(u) + "," + str(v) + "}")
