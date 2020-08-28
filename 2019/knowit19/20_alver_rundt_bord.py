import itertools as it
from collections import Counter

def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p

def get_primes_erat(n):
  return set(it.takewhile(lambda p: p<n, erat3()))

def is_28div(num):
    return num % 28 == 0

def is_even(num):
    return num % 2 == 0

def is_7div(num):
    return num % 7 == 0

def get_next_elf(last_elf, rev):
    if not rev:
        next_elf = last_elf+1 if last_elf < 5 else 1
    else:
        next_elf = last_elf-1 if last_elf > 1 else 5
    return next_elf

assert(get_next_elf(4, False)) == 5
assert(get_next_elf(4, True)) == 3
assert(get_next_elf(5, False)) == 1
assert(get_next_elf(1, True)) == 5

rev = False
end = 1_000_740
primes = get_primes_erat(end)

oppgaver = Counter({1:1,2:0,3:0,4:0,5:0})
steg = 1
last_elf = 1

#end = 100
while steg < end:
    next_elf = get_next_elf(last_elf, rev)
    steg += 1

    if steg in primes and oppgaver.most_common()[:-3:-1][0][1]!= oppgaver.most_common()[:-3:-1][1][1]:
        next_elf = oppgaver.most_common()[:-3:-1][0][0]
        #print('regel 1')
    elif is_28div(steg):
        rev ^= True
        next_elf = get_next_elf(last_elf, rev)
        #print('regel 2')
    elif is_even(steg) and next_elf == oppgaver.most_common(1)[0][0] and oppgaver.most_common(2)[0][1] != oppgaver.most_common(2)[1][1]:
        next_elf = get_next_elf(next_elf, rev)
        #print('regel 3')
    elif is_7div(steg):
        next_elf = 5
        #print('regel 4')
    #else:
        #print('regel 5')
    
    oppgaver[next_elf] += 1
    last_elf = next_elf
    #print('elf:', next_elf, 'steg:', steg)

print(oppgaver.most_common(5))
print(oppgaver.most_common(5)[0][1] - oppgaver.most_common(5)[4][1])