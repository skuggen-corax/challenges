import numpy as np

cipher = "44f23b820d2240177475c36842137ca1a84de5664f6a10f9a8b2d551704cf0d078028ab2aaccf5a179a404c2b7b2e6685291fa3db038facd111484f97d54f1f6"

str0m = np.load('luke_22_strømforbruk.npy')
liste = np.load('luke_22_ønskelister.npy')

mapping = dict()
seen = set()
seen_before = set()

equals = set()
unequals = set()
for i in range(len(str0m)):
    for j in range(len(liste[0])):
        item = liste[i][j]
        power = str0m[i][j]

        if item not in seen:    # first time senen
            seen.add(item)
            mapping[item] = power
        else:
            if item not in seen_before:     # second time seen
                seen_before.add(item)
                if mapping[item] == power:
                    equals.add(item)
                else:
                    unequals.add(item)

certain = [hex(num) for num in set(equals)] # 43 f9 59
print('certainly these:',  *zip(equals, certain)) 

not_tested_twice = [hex(num) for num in range(256) if num not in seen_before]
print('unsure about:', not_tested_twice)

not_these = [hex(num) for num in range(256) if num in seen_before and num not in equals]
print('def. not:', not_these)