import numpy as np
import matplotlib.pyplot as plt
import itertools

from pwn import remote

interesting_tps = []

c = remote('challenges.ctfd.io', 30030)

lines = c.recvall().decode().strip().split("\n")
pts = []
for line in lines:
    line = line.strip().split(" ")
    pts.append((int(line[0]), 0.01*(6-int(line[1]))))


plt.scatter(*zip(*pts), marker='o', s=3, color='red')
plt.show()
