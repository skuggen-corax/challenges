import itertools
from intcode import IntcodeComputer
from collections import defaultdict
from enum import Enum
import numpy as np
from intcode2 import IntCode

with open('data/13_input.txt') as f:
    for line in f:
        program = list(map(int, line.strip().split(',')))

program1 = program[:]
computer = IntcodeComputer(program1, inputs=[], storeOutputs=True)
computer.run()

#print(len(computer.outputs))
output = computer.outputs[2::3]
result1 = output.count(2)
print('part 1: ',result1)

def get_input():
    for pos, v in screen.items():
        if v == 4:  # Ball
            ball_x = pos[0]
        elif v == 3:  # Paddle
            paddle_x = pos[0]
    if paddle_x < ball_x:
        return 1  # Move right
    elif paddle_x > ball_x:
        return -1  # Move left
    elif paddle_x == ball_x:
        return 0  # Don't move


def display(grid):
    max_x = max(x for x,y in grid)
    max_y = max(y for x,y in grid)
    # print(max_x, max_y)
    screen = [[' ' for i in range(max_x+1)] for j in range(max_y+1)]
    for k, v in grid.items():
        x, y = k
        screen[y][x] = tile_ids[v]
    for line in screen:
        print(''.join(line))


# print(data)
tile_ids = {0: ' ', 1: '|', 2: '*', 3: '=', 4: '0'}
program2 = program[:]
program2[0] = 2
vm2 = IntCode(program2, get_input)
screen = {}
i = 0
inp = 0
ball_x = 0
paddle_x = 0
score = 0
steps = 0
while not vm2.halted:
    x, y, t_id = [vm2.run() for _ in range(3)]
    if any(i is None for i in [x, y, t_id]):
        continue
    if x == -1 and y == 0:
        score = t_id
    else:
        screen[(x, y)] = t_id

    # if steps % 100 == 0:
    #     display(screen)
    steps += 1
print(score)

    
