from collections import defaultdict
from operator import itemgetter

with open('2019/knowit19/data/turer.txt') as f:
    turer = [[tuple(map(int, punkt.split(',')))
                for punkt in tur.strip().split('\n')] 
                for tur in f.read().split('---')]


turplots = [defaultdict(str) for _ in turer]

for i, tur in enumerate(turer):
    for punkt in tur:
        turplots[i][punkt] = 'X'

# 43 turer (0-42)
for n, tur in enumerate(turplots):
    if n in [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22,23,24,25,26,27,28,29, 30,32, 34 , 35 ,36, 37, 38,39,40,41,42]:
        continue
    x_max = max(tur.keys(),key = itemgetter(0))[0]
    y_max = max(tur.keys(),key = itemgetter(1))[1]

    screen = [[' ' for i in range(x_max+1)] for j in range(y_max+1)]
    
    print('\nTur:', n, '\n')
    for k, v in tur.items():
        x, y = k
        screen[y][x] = v
    screen.reverse()
    for line in screen:
        print(''.join(line))
