import numpy as np

with open('data/fjord.txt') as f:
    fjord = [char
                for line in f.read().split('\n')
                for char in line]


fjordnp = np.array(fjord).reshape(67, -1).T
end = fjordnp.shape[0] -1

boat = int(np.where(fjordnp[1] == 'B')[0]) # idx 44

turns = 0
progress = 1
syd = False


while progress < end:
    progress += 1

    water = np.nonzero(fjordnp[progress] == ' ')
    nb_diff = (boat-1) - water[0][0]
    sb_diff = water[0][-1] - (boat+1)

    if nb_diff < 2 and not syd:
        syd ^= True
        turns += 1
    elif sb_diff <2 and syd:
        syd ^= True
        turns += 1
    
    if syd:
        boat += 1
    else:
        boat -= 1

    if progress % 25 == 0: print(progress, 'boat:',boat, 'south:', syd, 'turns:', turns)

print(turns)

# oppgitt svar er 3 for høyt, ikke tid til å finne ut hvorfor