from collections import Counter

inputa = 382345
inputb = 843167

def increase(current: int):
    while True:
        current = current + 1
        # one = (current % 10)
        # two =(current % 100 // 10)
        # three = (current % 1000 // 100)
        # four = (current % 10000 // 1000)
        # five = (current % 100000 // 10000)
        # six = (current % 1000000 // 100000)
        six, five, four, three, two, one = [c for c in str(current)] # replace the above commented stuff

        # clunky way of skipping a lot of iterations  (although these iterations are cheap)
        if six > five: 
            return int(str(six) + str(six) + str(six) + str(six) + str(six) + str(six))
        if five > four:
            return int(str(six) + str(five) + str(five) + str(five) + str(five) + str(five))
        if four > three:
            return int(str(six) + str(five) + str(four) + str(four) + str(four) + str(four))
        if three > two:
            return int(str(six) + str(five) + str(four) + str(three) + str(three) + str(three))
        if two > one:
            return int(str(six) + str(five) + str(four) + str(three) + str(two) + str(two))
        else:
            if six == five or five == four or four == three or three == two or two == one: # all the aboves already contain equal neighbours
                return int(str(six) + str(five) + str(four) + str(three) + str(two) + str(one))
    


def iterate_input(first: int, next: int):
    i = first
    results = []
    while i < next:
        next_i = increase(i)
        if next_i < next:
            results.append(str(next_i))
        
        i = next_i
    
    return results

print('part 1: ', len(iterate_input(inputa, inputb)))

def stronger(first: int, next: int):
    results = iterate_input(first, next)
    strong_results = []

    for result in results:
        num_letters = Counter([c for c in result])
        if 2 in num_letters.values():
            strong_results.append(result)
    
    return len(strong_results)


print('part 2: ', stronger(inputa, inputb))