

def program(input):
    input[1] = noun
    input[2] = verb

    i = 0
    while input[i] != 99:
        #print('next operation: ', input[i], ' at: ', i, ' : ')#, end="")
        if input[i] == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]

        i += 4

    return input[0]

assert program([1, 9, 10, 3,2,3,11,0,99,30,40,50], 9, 10) == 3500

noun = 12
verb = 2
with open('data/02_input.txt') as f:
    file_input = [int(x) for x in next(f).split(",")]

print('part 1: ', program(file_input.copy(), noun, verb))


# find noun + verb that produce output: 19690720

def find_words():
    #file_input2 = file_input.copy()
    noun = 0

    while noun < 100:
        verb = 0
        while verb < 100:
            file_input2 = file_input[:]
            if noun + verb > len(file_input2):
                print('breaks at: ', noun, verb)
                break
            current = program(file_input2, noun, verb)
            #if current >= 0:
                #print(noun, verb, ' : ', current) 
            if current == 19690720:
                return noun, verb
            verb += 1
        
        noun += 1
    
    return -1, -1

    
    

noun, verb = find_words()


# part 2
print('part 2: ', 100*noun + verb)