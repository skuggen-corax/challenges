"""Gitt et alfabet {2, 3, 5, 7, 11}, hva er summen av alle 7ere i sekvensen når lengden på sekvensen = 217532235?"""

alph = [3, 5, 7, 11, 2] # flytter 2 til slutten siden første 2-tall blir lagt inn manuelt
end_len = 217532235

results = [2, 2]
added = 1

i = 2 # lengden på sekvensen
while i < end_len:

    for num in alph:
        antall = results[added]
        for _ in range(antall):
            results.append(num)
        i += antall
        added += 1

        if added % 3000000 == 0:
            print('lengde: ', i)

#print(len(results))
print(results[:end_len-1].count(7)*7)