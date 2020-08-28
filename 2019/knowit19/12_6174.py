
# sortere stigende = liten
# sorter synkende = stor
# stor - liten

n_7 = 0
i = 1000
dont = [1111,2222,3333,4444,5555,6666,7777,8888,9999]

def sort_split_sub(num):
    liten = list(str(num).zfill(4))
    liten.sort()
    
    stor = list(str(num).zfill(4))
    stor.sort(reverse = True)
    
    liten = int("".join(liten))
    stor = int("".join(stor))

    #print(num, liten, stor)
    return stor - liten

while i <= 9999:
    if i not in dont:
        j = 0
        num = i
        while num != 6174:
            j += 1
            num = sort_split_sub(num)
        
        if j == 7:
            n_7 += 1

    i += 1

print(n_7)