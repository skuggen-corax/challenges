# scan string for adjacent case unequal similar characters

# repeat until no more are found/removed

# "aA" => 0
# "abBA" => 0
# "abAB" => 4
# "aabAAB" = 6

def same_type(s1: str, s2: str) -> bool:
    return (s1 != s2) and (s1.lower() == s2.lower())

def reduct(polymer: str) -> str:
    units = list(polymer)
    #idxs = [i for i in range(len(units))]
    deleted = set()

    def next_index(prev_idx: int) -> int:
        for idx in range(prev_idx + 1, len(units)):
            if idx not in deleted:
                return idx
        return len(units)

    did_reduct = True
    while did_reduct:
        did_reduct = False
        lo = next_index(-1)
        hi = next_index(lo)

        while hi< len(units):
            unit1 = units[lo]
            unit2 = units[hi]
            if unit1.lower() == unit2.lower() and unit1 != unit2:
                deleted.add(lo)
                deleted.add(hi)
                lo = next_index(hi)
                hi = next_index(lo)
                did_reduct = True
            else:
                lo = hi
                hi = next_index(hi)
    return "".join(unit for i, unit in enumerate(units) if i not in deleted)

TEST_CASE = "dabAcCaCBAcCcaDA" # => 10

assert(reduct(TEST_CASE) == "dabCBAcaDA")
assert(len(reduct(TEST_CASE)) == 10)

with open('data/05_input.txt') as f:
    polymer = f.read().strip()

#print(len(reduct(polymer))) # 9386

chars = {c.lower() for c in polymer}

best = {}

for c in chars:
    print(c)
    polymer_no_c = polymer.replace(c, "").replace(c.upper(), "")
    best[c] = len(reduct(polymer_no_c))

best_key = min(best, key=lambda c: best[c])
print(best)
print(best_key)