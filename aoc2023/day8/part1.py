import sys
import time
from itertools import cycle

from aoc import get_input

sys.setrecursionlimit(20000)


def get_child_from_instruction(nodes, parent, instruction):
    child = nodes[parent][next(instruction)]
    if child == "ZZZ":
        return 1
    return 1 + get_child_from_instruction(nodes, child, instruction)


nodes = {}
input = get_input()
instructions = cycle(input.readline().strip("\n"))
input.readline()

for line in input:
    line = line.strip("\n")
    parent, childs = line.split(" = ")
    childs = childs.strip("()").split(", ")
    nodes[parent] = {'L': childs[0], 'R': childs[1]}

print(nodes)
start = time.time()
tries_count = get_child_from_instruction(nodes, "AAA", instructions)
end = time.time()
print(end - start)
print("Result ", tries_count)
