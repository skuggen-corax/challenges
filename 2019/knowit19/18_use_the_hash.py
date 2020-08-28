from functools import reduce
from operator import mul
from collections import Counter
from math import ceil
from string import ascii_lowercase

with open('data/names.txt') as f:
    names = [[name for name in namelist.strip().split('\n')]
                   for namelist in f.read().split('---')]


with open('data/employees.csv') as f:
    employees = [[name for name in employee.strip().split(',')]
                       for employee in f.read().split('\n')]


alpha = dict(zip(ascii_lowercase + 'æøå', range(1,30)))

def ascii_char_sum(word):
    return sum([ord(c) for c in word])

def ascii_char_prod(word):
    return reduce(mul, [ord(c) for c in word], 1)

def half_name(name):
    split = ceil(len(name) / 2)
    return name[:split], name[split:]

def alphabet_sum_mod(word):
    return sum([alpha[c.lower()] for c in word if c not in [' ', "'"]]) % len(names[2])

def count_chars(word):
    return len([c for c in word if c not in [' ', "'"]])


head = employees.pop(0)
n_m = len(names[0])
n_f = len(names[1])
n_b = len(names[3])


sw_names = []
for name in employees:
    male = True if name[2] == 'M' else False

    if male:
        first = names[0][ascii_char_sum(name[0]) % n_m]
    else:
        first = names[1][ascii_char_sum(name[1]) % n_f]

    lasta, lastb = half_name(name[1])
    
    lasta_sw = names[2][alphabet_sum_mod(lasta)]
    
    nevner = count_chars(name[0]) if male else count_chars(name[0]) + count_chars(name[1])
    lastb_str = list(str(ascii_char_prod(lastb) * nevner))
    lastb_str.sort(reverse = True)
    lastb_sw = names[3][int("".join(lastb_str)) % n_b]

    sw_name = "".join([first, ' ', lasta_sw, lastb_sw])
    sw_names.append(sw_name)


print('Most common: ', Counter(sw_names).most_common(1)[0][0])