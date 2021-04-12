#!/usr/bin/env python3

# 3 * d ≡ 1 mod 13

# vet at 3^12 E= 1 mod 13
assert 3 ** 12 % 13 == 1

# 3^12 = 3 * 3^11
assert (3 * pow(3, 11)) % 13 == 1

print("flag:", pow(3, 11, 13))

# bonus?
assert pow(3, pow(3, 11), 13) == 1
