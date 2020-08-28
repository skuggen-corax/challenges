# inspired today by Joel Grus
from typing import List, NamedTuple, Set, Dict

with open('data/03_input.txt') as f:
    one = [x for x in next(f).strip().split(",")]
    two = [x for x in next(f).strip().split(",")]

#print(one)
#print(two)

o1 =['R8','U5','L5','D3']
t1 = ['U7','R6','D4','L4']

o2 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
t2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

o3 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
t3 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

class XY(NamedTuple):
    x: int
    y: int

    #R x + R; L x - L; U y + U; D y - D

def locations(path: List[str]) -> Set[XY]:
    # ['R8','U5','L5','D3']
    x = y = 0

    visited = set()

    for direction in path:
        dire = direction[0]
        dist = int(direction[1:])
        #print(dire, dist)

        for i in range(dist):
            if dire == "U":
                y += 1
            elif dire == "D":
                y -= 1
            elif dire == "R":
                x += 1
            elif dire == "L":
                x -= 1
            else:
                raise RuntimeError(f"bad direction: {dire}")

            visited.add(XY(x, y))

    return visited

def location_steps(path: List[str]) -> Dict[XY, int]:
    # ['R8','U5','L5','D3']
    x = y = num_steps =0

    visited = dict()

    for direction in path:
        dire = direction[0]
        dist = int(direction[1:])
        #print(dire, dist)

        for i in range(dist):
            if dire == "U":
                y += 1
            elif dire == "D":
                y -= 1
            elif dire == "R":
                x += 1
            elif dire == "L":
                x -= 1
            else:
                raise RuntimeError(f"bad direction: {dire}")

            num_steps += 1
            if XY(x, y) not in visited:
                visited[XY(x, y)] = num_steps

    return visited

def all_intersection(path1: List[str], path2: List[str]) -> Set[XY]:
    locations1 = locations(path1)
    locations2 = locations(path2)
    return locations1.intersection(locations2)

def manhattan_dist(xy: XY) -> int:
    return abs(xy.x) + abs(xy.y)

def closest_intersection(path1: List[str], path2: List[str]) -> int:
    all_i = all_intersection(path1, path2)
    return min(manhattan_dist(tup) for tup in all_i if tup != XY(0, 0))

def closest_intersection_steps(path1: List[str], path2: List[str]) -> int:
    distances1 = location_steps(path1)
    distances2 = location_steps(path2)

    all_i = set(locations(path1)).intersection(set(locations(path2)))
    #print(all_i)
    steps = {}

    #for key in all_i:
    #    steps[key] = distances1[key] + distances2[key]
        
    return min(distances1[key] + distances2[key] for key in all_i)

assert (closest_intersection(o1, t1)) == 6
assert (closest_intersection(o2, t2)) == 159
assert (closest_intersection(o3, t3)) == 135

print('part 1: ', closest_intersection(one, two))

assert (closest_intersection_steps(o1, t1)) == 30
assert (closest_intersection_steps(o2, t2)) == 610
assert (closest_intersection_steps(o3, t3)) == 410

print('part 2: ', closest_intersection_steps(one, two))