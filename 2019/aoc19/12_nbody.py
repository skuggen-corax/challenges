import re
from typing import NamedTuple, List
from dataclasses import dataclass
import copy
from math import gcd

# x, y, z = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', l).groups() 

@dataclass
class XYZ():
    x: int
    y: int
    z: int

    def energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

class Moon:
    def __init__(self, position: XYZ, velocity: XYZ = None):
        self.position = position
        self.velocity = velocity or XYZ(0,0,0)

    def __repr__(self) -> str:
        return f"Moon(p:{self.position.x, self.position.y, self.position.z}, v:{self.velocity.x, self.velocity.y, self.velocity.z})"

    def potential_energy(self) -> int:
        return self.position.energy()

    def kinetic_energy(self) -> int:
        return self.velocity.energy()

    def total_energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()

    def apply_velocity(self) -> None:
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    def sig_x(self):
        return (self.position.x, self.velocity.x)

    def sig_y(self):
        return (self.position.y, self.velocity.y)

    def sig_z(self):
        return (self.position.z, self.velocity.z)
        

def time_step(moons: List[Moon]) -> None:
    # update velocity from gravity
    for moon in moons:
        for moon2 in moons:
            if moon != moon2:
                if moon.position.x > moon2.position.x:
                    moon.velocity.x -= 1
                elif moon.position.x < moon2.position.x:
                    moon.velocity.x += 1
                
                if moon.position.y > moon2.position.y:
                    moon.velocity.y -= 1
                elif moon.position.y < moon2.position.y:
                    moon.velocity.y += 1
                
                if moon.position.z > moon2.position.z:
                    moon.velocity.z -= 1
                elif moon.position.z < moon2.position.z:
                    moon.velocity.z += 1

    # update position from velocity
    for moon in moons:
        moon.apply_velocity()


INPUT = [
    Moon(XYZ(-9,10,-1)),
    Moon(XYZ(-14,-8,14)),
    Moon(XYZ(1,5,6)),
    Moon(XYZ(-19,7,8))
]

TEST1 = [
    Moon(XYZ(-1, 0,  2)),
    Moon(XYZ(2,-10,-7)),
    Moon(XYZ(4,-8,  8)),
    Moon(XYZ(3, 5, -1))
]

# for n in range(10):
#     time_step(TEST1)

# tot = 0
# for moon in TEST1:
#     #print(moon.kinetic_energy, moon.potential_energy, moon.total_energy())
#     tot += moon.total_energy()

# assert tot == 179


for _ in range(1000):
    time_step(INPUT)

print('part 1: ', sum(moon.total_energy() for moon in INPUT))

INPUT = [
    Moon(XYZ(-9,10,-1)),
    Moon(XYZ(-14,-8,14)),
    Moon(XYZ(1,5,6)),
    Moon(XYZ(-19,7,8))
]

def sigs_x(moons: List[Moon]):
    return tuple(moon.sig_x() for moon in moons)

def sigs_y(moons: List[Moon]):
    return tuple(moon.sig_y() for moon in moons)

def sigs_z(moons: List[Moon]):
    return tuple(moon.sig_z() for moon in moons)

def steps_to_repeat(moons: List[Moon], sig_fn) -> int:
    moons = copy.deepcopy(moons)

    seen = set()
    seen.add(sig_fn(moons))

    n_steps = 0

    while True:
        n_steps += 1
        time_step(moons)
        sig = sig_fn(moons)
        if sig in seen:
            return n_steps
        else:
            seen.add(sig)

a = steps_to_repeat(INPUT, sigs_x)
b = steps_to_repeat(INPUT, sigs_y)
c = steps_to_repeat(INPUT, sigs_z)

ab = a * b // gcd(a, b)
abc = ab * c // gcd(ab, c)
print('part 2: ', abc)