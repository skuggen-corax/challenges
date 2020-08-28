# input eks: "AIGSAIIFFG"

# 10703437km/t

"""
    G = gress. Senker farten til sleden med 27km/t
    I = is. Øker farten til sleden med 12km/t * antall isområder på rad
    A = asfalt. Senker farten til sleden med 59km/t
    S = skog. Senker farten til sleden med 212km/t
    F = fjell. Kommer alltid i par, der den første er oppover som senker farten med 70km/t mens den andre er nedoverbakke som øker farten med 35km/t.
"""

def brems(terreng, km):
    
    i = 0
    antall_is = 0
    fjell = False

    while km > 0:
        now = terreng[i]
        print(i, km, now)
        new_i = i + 1

        if now != 'I':
            antall_is = 0

        if now == 'G':
            km -= 27
        elif now == 'I':
            antall_is += 1
            km += antall_is * 12
        elif now == "A":
            km -= 59
        elif now == 'S':
            km -= 212
        elif now == 'F':
            if fjell:
                km += 35
                fjell^=True
            else:
                km -= 70
                fjell^=True
        i += 1

    return new_i

with open('data/in11.txt') as f:
    terreng = f.read()

km = 10703437

print(brems(terreng, km))