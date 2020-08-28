from typing import Tuple, List, Set
import re

Req = Tuple[str, str]

RAW = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

LINES = RAW.split('\n')

rgx = r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."

def parse_line(line: str) -> Tuple[str, str]:
    pre, post = re.match(rgx, line).groups()
    return (pre, post)

REQUIREMENTS = [parse_line(line) for line in LINES]

print(REQUIREMENTS)

def allowable(requirements: List[Req], completed: Set[Str]) -> List[str]:
    pass

# https://youtu.be/WtcobWLC2Mo?t=462