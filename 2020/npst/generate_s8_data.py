# eksperiment med å generere .DATA segment for selde8-programmer (ikke spesielt vellykket)
numbers = dict()

def as_hex(number):
    result = ""
    if len(str(number)) == 2:
        result += '0x00, '
    elif len(str(number)) == 1:
        result += '0x00, 0x00, '

    for char in str(number):
        result += "0x3" + char + ", "
    return result[:-2]

for i in range (0,256):
    for j in range (0, 256):
        numbers['{:02X}'.format(i) + '{:02X}'.format(j)] = as_hex((i+j) % 256)

for key in sorted(numbers): 
    print(numbers[key], end=", ")