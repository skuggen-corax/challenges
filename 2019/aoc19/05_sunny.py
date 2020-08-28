from typing import List

with open('data/05_input.txt') as f:
    program = [int(x) for x in f.read().split(",")]

#print(program)

def run(instructions: List[int], the_input = 1):
    instructions = instructions[:]
    output = None
    
    i = 0
    while str(instructions[i])[-2:] != "99":
        #print('current i: ', i)
        instruction = instructions[i]

        # check if opcode has parameters
        in_size = len(str(instruction))
        if in_size > 2: par_mode = True
        else: par_mode = False

        if par_mode: op_code = int(str(instruction)[-2:])
        else: op_code = instruction

        # extract opcode parameters
        pars = [] 
        if par_mode:
            j = in_size -3
            while j >= 0: 
                pars.append(int(str(instruction)[j]))
                j -= 1

        # set parametars according to mode found in opcode
        if par_mode and pars[0] == 1: param1 = i + 1
        else: param1 = instructions[i + 1]
        if op_code < 10 and op_code != 3 and op_code != 4:
            if par_mode and len(pars)>1:
                if pars[1] == 1: param2 = i + 2
                else: param2 = instructions[i+2]
            else: param2 = instructions[i+2]
            answ = instructions[i+3]
        
        #print('in: ', instruction, 'op: ', op_code, 'i: ', i, 'param1: ', param1)
        
        # cases for different opcodes
        if op_code == 1: # add
            instructions[answ] = instructions[param1] + instructions[param2]
            i += 4
        elif op_code == 2: # multiply
            instructions[answ] = instructions[param1] * instructions[param2]
            i += 4
        elif op_code == 3: # read input
            instructions[instructions[i+1]] = the_input
            i += 2
        elif op_code == 4: # set output
            if par_mode:
                output = instructions[i+1]
            else:
                output = instructions[instructions[i+1]]
            print(output)
            i += 2
        elif op_code == 5:  # jump-if-true
            if instructions[param1] != 0:
                i = instructions[param2]
            else:
                i += 3
        elif op_code == 6:  # jump-if-false
            if instructions[param1] == 0:
                i = instructions[param2]
            else:
                i += 3
        elif op_code == 7:  # less-than
            if instructions[param1] < instructions[param2]:
                instructions[answ] = 1
            else:
                instructions[answ] = 0
            i += 4
        elif op_code == 8:  # equals
            if instructions[param1] == instructions[param2]:
                instructions[answ] = 1
            else:
                instructions[answ] = 0
            i += 4
        # end of opcode cases

    return output

# assert run([3,0,4,0,99], 13) == 13
# assert run([1101,100,-96,4,0,6,99]) == 99

# assert run([3,9,8,9,10,9,4,9,99,-1,8], 8) == 1
# assert run([3,9,8,9,10,9,4,9,99,-1,8], 7) == 0

# assert run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0) == 0
# assert run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1) == 1
# assert run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0) == 0
# assert run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1) == 1

print('part 1: ', run(program, 1))
print('part 2: ', run(program, 5))