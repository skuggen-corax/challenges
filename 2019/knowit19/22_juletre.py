import numpy as np

with open('2019/knowit19/data/forest.txt') as f:
    skog = [[char for char in line]
                for line in f.read().split('\n')]

dropp = skog.pop(-1)

skognp = np.array(skog).reshape(35, -1).T
skoghoyd = len(skognp[0])

sumtre = 0
for col in skognp:
    if col[-1] == '#':
        idx = np.nonzero(col == '#')
        sumtre += (skoghoyd - idx[0][0])

print(sumtre*40)