with open('data/in9.txt') as f:
    inputs = [int(x) for x in f.read().split('\n')]

def is_krampus(num: int):
    num_sq = num**2
    num_sq_s = str(num_sq)

    i = 1
    while i < len(num_sq_s):
        #print(num_sq_s[:i], num_sq_s[i:])
        a = int(num_sq_s[:i])
        b = int(num_sq_s[i:])
        if a + b == num and a != 0 and b != 0:
            return True
        i += 1
    return False


assert is_krampus(45) == True
assert is_krampus(100) == False

valid = []

for input in inputs:
    if is_krampus(input) == True:
        valid.append(input)

print(sum(valid))
