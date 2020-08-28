import itertools
from intcode import IntcodeComputer
from intcode2 import IntCode
from collections import defaultdict


with open('data/11_input.txt') as f:
    for line in f:
        master = list(map(int, line.strip('\n').split(',')))


#         "<"     "^"     ">"      "v"
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def new_position(position: tuple, turn: int):
    global dirs
    x = position[0]
    y = position[1]
    # hvis turn 0 hent y[0]
    # hvis turn 1 hent y[2]
    if turn == 0:
        new_x = x + dirs[0][0]
        new_y = y + dirs[0][1]
        # rot list left
        dirs = dirs[3:] + dirs[:3]
    elif turn == 1:
        new_x = x + dirs[2][0]
        new_y = y + dirs[2][1]
        # rot list  right
        dirs = dirs[1:] + dirs[:1]
    
    return new_x, new_y

def paint(computer, painted = defaultdict(int), position = (0,0)):
    max_x = min_x = max_y = min_y = 0

    while True:
        run = computer.run()
        #print(run)

        if computer.halt:
            return painted, max_x, min_x, max_y, min_y

        # get color from intcode
        color = computer.outputs.pop(0)
        # add color to dict[position]
        painted[position] = color

        # get turn from intcode
        turn = computer.outputs.pop(0)

        # get new position after turning
        position = new_position(position, turn)
        if position[0] > max_x:
            max_x = position[0]
        if position[1] > max_y:
            max_y = position[1]
        if position[0] < min_x:
            min_x = position[0]
        if position[1] < min_y:
            min_y = position[1]
        
        # get color of new position
        computer.addInput(painted[position])


    return painted


computer = IntcodeComputer(master[:], inputs=[0], storeOutputs=True)
result, max_x, min_x, max_y, min_y = paint(computer)
print('part 1: ', len(result.keys()), '\n\n')


def get_input():
    return color

program2 = master[:]
curr_pos = [0, 0]

# 0 == up
# 1 == right
# 2 == down
# 3 == left
dirs = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
facing = 0
panels = defaultdict(int)
# 0 == black
# 1 == white
color = 1
vm = IntCode(program2, get_input)
while not vm.halted:
    col = vm.run()
    if col is None:
        continue
    turn = vm.run()
    panels[tuple(curr_pos)] = col

    facing += 1 if turn else -1
    facing %= 4
    curr_pos = [curr_pos[0] + dirs[facing][0], curr_pos[1] + dirs[facing][1]]
    col = panels[tuple(curr_pos)]
print(len(panels))

x, y = max(panels, key=lambda p: p[0])[0], max(panels, key=lambda p: p[1])[1]

print(panels)
print(x,y)

# some bug somewhere, but managed to get right answer
# was not AHIAPRAI
# was AHLCPRAL

display = []
for row in range(y+1):
    display.append([])
    for col in range(x+1):
        display[row].append(' ')

for p, v in panels.items():
    x, y = p
    display[y][x] = v

for line in display:
    print(''.join('8' if c == 1 else ' ' for c in line))
