import itertools as it

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

start = 1
end = 98765432

primes = get_primes_erat(9+9+9+9+9+9+9+9)

ant_harshad = 0

i = start
while i < end:

    siffersum = 0
    for c in str(i):
        siffersum += int(c)
    
    if i % siffersum == 0:
        if siffersum in primes:
            ant_harshad += 1

    i += 1

print(ant_harshad)