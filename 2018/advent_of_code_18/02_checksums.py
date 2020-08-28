from typing import Set, List
from collections import Counter

# read file
with open('data/02_input.txt') as f:
    package_ids = [line.strip() for line in f]


def char_count_values(word: str) -> Set[int]:
    char_count = Counter(word)
    return set(char_count.values())

assert(char_count_values("aaab") == {1,3})

def checksum(ids: List[str]) -> int:
    """
    returns (# strings with a character with a char occuring exactly twice) *
            (# strings with a character with a char occuring exactly thrice)

    """
    num_twos = 0
    num_threes = 0

    for box_id in ids:
        ccv = char_count_values(box_id)
        if 2 in ccv:
            num_twos += 1
        if 3 in ccv:
            num_threes += 1
    
    return num_twos * num_threes


print(checksum(package_ids))


# common characters of strings who differ by exactly one char

def characters_in_common(ids: List[str]) -> str:
    leave_one_outs = Counter()

    for box_id in ids:
        for i in range(len(box_id)):
            leave_one_out = tuple(box_id[:i] + "_" + box_id[(i+1):])
            leave_one_outs[leave_one_out] += 1
    
    [(best, best_count), (not_best, not_best_count)] = leave_one_outs.most_common(2)

    assert best_count == 2
    assert not_best_count == 1
    return "".join([c for c in best if c !="_"])

print(characters_in_common(package_ids))