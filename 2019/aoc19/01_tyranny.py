
def fuel_for_module(fuel: int):
    return fuel // 3 - 2

def all_modules(x):
    sum = 0
    for module in x:
        #print(module)
        sum += fuel_for_module(module)
    return sum

assert(fuel_for_module(12) == 2)
assert(fuel_for_module(14) == 2)
assert(fuel_for_module(1969) == 654)
assert(fuel_for_module(100756) == 33583)

with open('data/01_input.txt') as f:
    numbers = [int(line.strip()) for line in f]

sum = all_modules(numbers)
print('part 1: ',sum)

def all_modules2(x):
    sum = 0
    for module in x:
        #print(module)
        first_fuel = fuel_for_module(module)
        sum += fuel_of_fuel(first_fuel)
    return sum

def fuel_of_fuel(x):
    if x < 1:
        return 0
    #print(x)
    return x + fuel_of_fuel((x // 3) - 2)

#assert(fuel_of_fuel(14) == 0)
#assert(fuel_of_fuel(1969) == 966)

sum2 = all_modules2(numbers)
print('part 2: ',sum2)