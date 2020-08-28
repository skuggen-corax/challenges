# top left: 0,0
from math import atan2, sqrt, degrees
import operator

starmap = dict()


def find_roids(starmap):
    roids = dict()
    
    r = len(starmap)
    c = len(starmap[0])

    i = 0
    while i < r:
        j = 0
        while j < c:
            if starmap[i][j] == "#":
                roids[(j,i)] = 0
            j += 1
        i += 1


    return roids

def line_of_sight(starmap):
    roids = find_roids(starmap)
    
    # lineære streker
    # kan ekskludere alle som er multipler av allerede 
    # ex: hvis posisjon(0,0) og roid1(2,1) alle (2x, 1x) er blokkert
    # hvis posisjon (3,1) og roid(4,4) er alle (1x, 3x) blokkert
    for roid in roids:
        vectors = []
        for roid_in_sight in roids:
            if roid != roid_in_sight:
                radian = atan2(roid_in_sight[1] - roid[1], roid_in_sight[0] - roid[0])
                if radian not in vectors:
                    vectors.append(radian)
                    #print(radian)
                    roids[roid] += 1

    return roids

with open('data/10_input.txt') as f:
    starmap = f.read().split('\n')

# RAW = [".#..#",".....","#####","....#","...##"]
# #roids = find_roids(RAW)

# v1 = ["......#.#.","#..#.#....","..#######.",".#.#.###..",".#..#.....","..#....#.#","#..#....#.",".##.#..###","##...#..#.",".#....####"]
# v11 = (line_of_sight(v1) )
# v111 = max(v11, key=(lambda k: v11[k])) # point of asteroid with highest los-count
# assert v111 == (5, 8)
# assert v11[v111] == 33

roids = line_of_sight(starmap) # dict with asteroids and number of other asteroids in line of sight
max_in_sight = max(roids, key=(lambda k: roids[k])) # point of asteroid with highest los-count
print('part 1: ', max_in_sight, ' : ', roids[max_in_sight])

def vaporizer(starmap, point, nth):
    roids = find_roids(starmap)

    relative_targets = []
    
    for roid in roids:
        if roid != point:
            radian = atan2(roid[1] - point[1], roid[0] - point[0])
            degree = degrees(radian) + 450
            if degree >= 720:
                degree -= 720
            if degree >= 360:
                degree -= 360

            dist = sqrt((roid[1] - point[1])**2 + (roid[0] - point[0])**2)


            #print(roid, degree, dist)

            relative_targets.append((degree, dist, roid))

    relative_targets.sort()
    #return relative_targets

    vaporized = []
    size = len(relative_targets) - 1
    largest_degree = max(relative_targets)
    i = 0
    popped = 0
    last_degree = -1

    while popped < nth:
        degree = relative_targets[i][0]
        largest_degree = max(relative_targets)[0]
        
        #print(i, size, popped, last_degree, largest_degree)
        if degree > last_degree:
            vaporized.append(relative_targets.pop(i))
            last_degree = degree
            popped += 1
        else:
            i += 1

        if largest_degree == last_degree:
            last_degree = -1
            i = 0

    return vaporized


# v2 = [".#..##.###...#######","##.############..##.",".#.######.########.#",
# ".###.#######.####.#.","#####.##.#.##.###.##","..#####..#.#########"
# "####################","#.####....###.#.#.##","##.#################"
# "#####.##.###..####..","..######..##.#######","####.##.####...##..#"
# ".#####..#.######.###","##...#.##########...","#.##########.#######"
# ".####.#.###.###.#.##","....##.##.###..#####",".#.#.###########.###"
# "#.#.#.#####.####.###","###.##.####.##.#..##"]
# v2_bes = (11, 13)
# v2_val = vaporizer(v2, v2_bes, 200)
# print(v2_val[0:19])


vaped = vaporizer(starmap, max_in_sight, 200)
print(len(vaped))
vap_200 = vaped[-1][2]
print(vap_200)
print('part 2: ', 100 * vap_200[0] + vap_200[1])