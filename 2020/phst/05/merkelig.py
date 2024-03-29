import sys, os
import pdb
import string

digits = {"🎲": 0, "🍫": 1,  "🎮": 2, "🎧": 3, "🎨": 4, "🍬": 5}
base = len(digits)


def parse_num(code):
    num = 0
    for i,c in enumerate(code):
        num += digits[c] * base**i
    return num

#if len(sys.argv) < 2:
#    print("Mangler programfil!")
#    exit(1)

code = open('underfundig', "rt", encoding="utf8").read() # sys.argv[1]

def runp():
    pc = 0
    stack = [0] * 256
    sp = 0
    riktige = 0 
    while pc < len(code):
        op = code[pc]
        pc += 1
        if op == "🐰":
            stack[sp] = parse_num(code[pc:pc+4])
            #print('\nparse:', stack[sp], '\t\t', end="")
            sp += 1
            pc += 4
        elif op == "🐥":
            stack[sp] = stack[sp-1]
            sp += 1
        elif op == "🌱":
            sp -= 1
            #print(stack)
            stack[sp-1] += stack[sp]
            stack[sp-1] %= base**4
        elif op == "🌻":
            sp -= 1
            #print('sub', stack[sp-1], stack[sp])
            stack[sp-1] -= stack[sp]
            stack[sp-1] %= base**4
        elif op == "🐇":
            sp -= 1
            if stack[sp] != 0:
                pc += parse_num(code[pc:pc+4])
                #print('something wrong, jumpout')
            else:
                riktige += 1
                pc += 4
        elif op == "🥚":
            sp -= 1
            stack[sp-1] ^= stack[sp]
        elif op == "🐤":
            sp -= 1
            #os.write(1, bytes([stack[sp]]))
        elif op == "🐣":
            #line = sys.stdin.buffer.readline().strip()
            for c in line:
                #print(chr(c), end="")
                stack[sp] = c
                sp += 1
            stack[sp] = len(line)
            sp += 1
        elif op == "🌞":
            #exit(0)
            return riktige

length = 34
inpu = ["0"] * length
inpu[33] = "}"
inpu[32] = "."

for i in range(31, -1, -1):
    next_c = i
    for j in string.printable:
        #print(j)
        inpu[next_c] = j
        #print(i, next_c, inpu[next_c], j)
        line = "".join(inpu).encode()
        if runp() > length - i:
            #print(line)
            break

    #print('found:', j)

print(line.decode())
