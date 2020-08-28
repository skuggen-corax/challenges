# helpful hints from https://www.reddit.com/user/naclmolecule/
import numpy as np

with open('data/08_input.txt') as f:
    input = f.read()

image = np.array(list(input)).reshape((-1, 150)) # reshape to (100, (6, 25))

min_z_layer = min(image, key=lambda layer:np.sum(layer == '0')) # find layer with min sum of '0'

print('part 1: ', np.sum(min_z_layer == '1') * np.sum(min_z_layer == '2')) # print product of '1's and '2' in the min(0) layer

decoded = image[0]

for layer in image:
    decoded = np.where(decoded == '2', layer, decoded) # replace '2' from layer, keep '0' and '1'
    
    if np.sum(decoded == '2') == 0: # possible early stopping
        break    

decoded = np.where(decoded == '1', 'X', ' ') # To make it easier to see (1,2) => (X, )
decoded = decoded.reshape((6, 25))

print('part 2: \n')
for row in decoded:
    print(*row)
