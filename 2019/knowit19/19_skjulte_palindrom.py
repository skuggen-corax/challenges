

def is_palindrome(num):
    return str(num) == str(num)[::-1]

assert is_palindrome(121) == True
assert is_palindrome(122) == False


def reversed_num(num):
    return int(str(num)[::-1])

assert reversed_num(38) == 83
assert reversed_num(49) == 94
assert reversed_num(120) == 21


total = 0
i = 1
while i <= 123454321:
    summed = i + reversed_num(i)
    
    if is_palindrome(summed) and not is_palindrome(i):
        total += i

    i += 1

print('after', i, 'iterations:', total)