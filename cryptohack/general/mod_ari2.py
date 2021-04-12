#!/usr/bin/env python3

p = 17

print(pow(3, p, p))
print(pow(5, p, p))
print(pow(7, p, p))

print(pow(7, p-1, p))

p = 65537
print("flag:", pow(27324678765465536, p-1, p))
