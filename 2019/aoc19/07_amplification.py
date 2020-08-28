from typing import List
from itertools import permutations

with open('data/07_input.txt') as f:
    program = [int(x) for x in f.read().split(",")]

#print(program)

def run(instructions: List[int], the_input: List[int] = [0, 0], state = 0):
    #instructions = instructions[:]
    output = None
    
    i = state
    while str(instructions[i])[-2:] != "99":
        #print('current i: ', i)
        instruction = instructions[i]

        # check if opcode has parameters
        in_size = len(str(instruction))
        if in_size > 2: 
            par_mode = True
        else: 
            par_mode = False

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
            # first phase setting, then input
            instructions[instructions[i+1]] = the_input.pop(0)
            i += 2
        elif op_code == 4: # set output
            if par_mode:
                output = instructions[i+1]
            else:
                output = instructions[instructions[i+1]]
            #print(output)
            return output, 4, i + 2
        elif op_code == 5:  # jump-if-true
            if instructions[param1] != 0: 
                i = instructions[param2]
            else: i += 3
        elif op_code == 6:  # jump-if-false
            if instructions[param1] == 0: 
                i = instructions[param2]
            else: i += 3
        elif op_code == 7:  # less-than
            if instructions[param1] < instructions[param2]: 
                instructions[answ] = 1
            else: instructions[answ] = 0
            i += 4
        elif op_code == 8:  # equals
            if instructions[param1] == instructions[param2]: instructions[answ] = 1
            else: instructions[answ] = 0
            i += 4
        # end of opcode cases

    return output, int(str(instructions[i])[-2:]), i

def amplifiers(program: List[int], phase_settings: List[int] = [0,1,2,3,4], input: int = 0):
    last_input = 0

    # set persistent programs
    prog_a = program[:]
    prog_b = program[:]
    prog_c = program[:]
    prog_d = program[:]
    prog_e = program[:]
    state_a = state_b = state_c = state_d = state_e = 0
    op = op_e = 0

    # set first inputs: phases + extra 0 for amplifier A
    a_in = [phase_settings[0], last_input]
    b_in = [phase_settings[1]]
    c_in = [phase_settings[2]]
    d_in = [phase_settings[3]]
    e_in = [phase_settings[4]]

    while op_e != 99:
        # as long as final amplifier dont reach opcode 99, loop trough
        # save current program state when output is produced
        # continue from that state next iteration
        A, op_a, state_a = run(prog_a, a_in, state_a)
        # when opcode is reached output is not set, aka: None
        # in that case, keep last output
        if A != None:
            last_a = A
        else: 
            A = last_a
        b_in.append(A)
        
        #print(A)
        B, op_b, state_b = run(prog_b, b_in, state_b)
        if B != None:
            last_b = B
        else: 
            B = last_b
        c_in.append(B)
        
        C, op_c, state_c = run(prog_c, c_in, state_c)
        if C != None:
            last_c = C
        else: 
            C = last_c
        d_in.append(C)

        D, op_d, state_d = run(prog_d, d_in, state_d)
        if D != None:
            last_d = D
        else: 
            D = last_d        
        e_in.append(D)

        E, op_e, state_e = run(prog_e, e_in, state_e)
        if E != None:
            last_e = E
        else: 
            E = last_e
        a_in.append(E)

        #print(op)
        op = op_e

    return E

def best_combinations(program: List[int], phase_settings: List[int], input: int = 0):
    max_output = 0
    max_phase = []
    # loop trough all permutations of phase_settings
    for phase_order in permutations(phase_settings):
        res = amplifiers(program, phase_order, input)
        if res > max_output:
            max_output = res
            max_phase = phase_order
        
    return max_output, max_phase

initial_input = 0
phase_settings = [0,1, 2,3,4]
print('part 1: ', best_combinations(program, phase_settings, initial_input))

initial_input2 = initial_input
phase_settings2 = [5,6,7,8,9]
print('part 2: ', best_combinations(program, phase_settings2, initial_input))