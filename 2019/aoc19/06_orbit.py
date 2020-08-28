from typing import List
import re
from anytree import Node, RenderTree, PreOrderIter, find_by_attr, Walker
# input: lines of "373)6C9"

with open('data/06_input.txt') as f:
    orbit_map = [(line.strip()) for line in f]

rgx = "(...)\)(...)"

def parse_map(orbit_item: str):
    return re.match(rgx, orbit_item).groups()
    
assert  parse_map("373)6C9") == ('373', '6C9')

def build_tree(orbit_map: List[str]):
    # add root/parent nodes to tree
    nodes = set()

    root = None

    for orbit_item in orbit_map:
        a, b = parse_map(orbit_item)
        if a in nodes and b not in nodes:
            locals()[b] = Node(b, parent=locals()[a])
            nodes.add(b)
        elif a not in nodes and b in nodes:
            locals()[a] = Node(a)
            locals()[b].parent = locals()[a]
            nodes.add(a)
        elif a in nodes and b in nodes:
            locals()[b].parent = locals()[a]
        else:
            locals()[a] = Node(a)
            locals()[b] = Node(b, parent=locals()[a])
            nodes.add(a)
            nodes.add(b)
        
        root = locals()[a].root

    #print(nodes)
    return root

def count_edges(orbit_map: List[str]):
    # sum all node depths
    tot_height = 0
    root = build_tree(orbit_map)
    tot_height = sum([node.depth for node in PreOrderIter(root)])

    return tot_height
#RAW = ["PQ6)WX4", "5DD)FFZ", "COM)PQ6", "WX4)5DD"]
#asd = build_tree(RAW)
#print(RenderTree(asd))

print('part 1: ', count_edges(orbit_map))

def distance_between(orbit_map: List[str]): 
    # walk from start to finish node with walker()
    root = build_tree(orbit_map)

    y = find_by_attr(root, "YOU")
    s = find_by_attr(root, "SAN")

    w = Walker()
    steps = 0

    """ walk return: 
    steps up to common
    common node
    steps down from common
    """
    return w.walk(y, s)

x,_,z = distance_between(orbit_map)

print('part 2: ', len(x) + len(z) - 2) # sub 2 because we want distance from what YOU is orbiting to what SAN is orbiting