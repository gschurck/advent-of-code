import sys
import time
from itertools import cycle

from aoc import get_input

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000000)
print(sys.getrecursionlimit())


def get_child_from_instruction(nodes, parents, instruction):
    print("----")
    start = time.time()

    children = [nodes[parent][next(instruction)] for parent in parents]

    # print(children)

    final_children = list(filter(lambda child: child[2] == 'Z', children))
    end = time.time()
    print(end - start)

    if len(final_children) == len(parents):
        return 1

    return 1 + get_child_from_instruction(nodes, children, instruction)


nodes = {}
input = get_input()

instructions = cycle(input.readline().strip("\n"))
input.readline()
for line in input:
    line = line.strip("\n")
    # print(line)

    parent, childs = line.split(" = ")
    childs = childs.strip("()").split(", ")
    # print(childs)
    nodes[parent] = {'L': childs[0], 'R': childs[1]}

print(nodes)
parents = list(filter(lambda parent: parent[2] == 'A', nodes.keys()))
print(parents)
tries_count = get_child_from_instruction(nodes, parents, instructions)
print(tries_count)
