from Cryptodome.Util.number import long_to_bytes
 
# vi vil finne m
# vi vet at m^(2^x) (mod p) = a


def legendre_symbol(a, p):
    """
    Legendre symbol
    Define if a is a quadratic residue modulo odd prime
    http://en.wikipedia.org/wiki/Legendre_symbol
    """
    ls = pow(a, p >> 1, p)
    if ls == p - 1:
        return -1
    return ls


def prime_mod_sqrt(a, p):
    """
    Square root modulo prime number
    Solve the equation
        x^2 = a mod p
    and return list of x solution
    http://en.wikipedia.org/wiki/Tonelli-Shanks_algorithm
    """
    a %= p

    # Simple case
    if a == 0:
        return [0]
    if p == 2:
        return [a]

    # Check solution existence on odd prime
    if legendre_symbol(a, p) != 1:
        return []

    # Simple case
    if p & 3 == 3:
        x = pow(a, (p >> 2) +1, p)
        return [x, p-x]

    # Factor p-1 on the form q * 2^s (with Q odd)
    q, s = p - 1, 0
    while q & 1 == 0:
        s += 1
        q >>= 1

    # Select a z which is a quadratic non resudue modulo p
    z = 1
    while legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, q, p)

    # Search for a solution
    x = pow(a, (q + 1)//2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        # Find the lowest i such that t^(2^i) = 1
        e = 2
        for i in range(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2

        # Update next value to iterate
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return [x, p-x]


a = 283849800649093313510494175418755497823945890813696818393522811641016385469212918363581359374155332176958058700548924862371286274930622752510028849706134
p = 9124597104758540080509291029676122374984377441887824449832944547628900282228841849713949013869826508940227230479894829537848432784148500372100266463819447

# a ≡ m^n (mod p)
# vi vil ha m
# a = pow(m, n, p)


def printable(nums):
    for num in nums:
        egg = long_to_bytes(num)
    try:
        print(egg.decode())
        return 1
    except:
        pass 

m = prime_mod_sqrt(a, p)


#assert pow(m, 2, p) == a

# modular kvadratrot av a er m:

printable(m)

x = 1
while True:
    for element in m:
        m.extend(prime_mod_sqrt(element, p))
        if printable(m) == 1:
            print("Foud egg when x =", x, "element:", element)
            exit()
    x+=1