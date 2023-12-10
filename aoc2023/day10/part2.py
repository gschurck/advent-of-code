from enum import Enum
from math import inf
from typing import List

from aoc import get_input


class Direction(Enum):
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4


class Step:
    def __init__(self, id_char, id_line, direction, range=1):
        self.id_char = id_char
        self.id_line = id_line
        self.direction = direction
        self.range = range

    def __repr__(self):
        return f"({self.id_char}, {self.id_line})"


tiles_grid = []
paths: List[List[Step]] = []


def add_start(step, expected_symbols):
    print(step.direction)
    print(tiles_grid[step.id_line][step.id_char])
    if not 0 <= step.id_char < len(tiles_grid[0]) or not 0 <= step.id_line < len(tiles_grid):
        return
    if tiles_grid[step.id_line][step.id_char] not in expected_symbols:
        return
    paths.append([step])
    print("ok")


def process_step(next_step: Step, path_id, discovered_pipes_ranges):
    if not 0 <= next_step.id_char < len(tiles_grid[0]) or not 0 <= next_step.id_line < len(tiles_grid):
        raise Exception("out of map")
    next_step_range = discovered_pipes_ranges[next_step.id_line][next_step.id_char]
    if next_step_range != '.':
        return max(next_step.range, next_step_range)
    discovered_pipes_ranges[next_step.id_line][next_step.id_char] = next_step.range
    paths[path_id].append(next_step)
    return 0


def get_next_step(cur_step: Step):
    symbol = tiles_grid[cur_step.id_line][cur_step.id_char]
    print(symbol)
    match symbol:
        case '|':
            if cur_step.direction == Direction.TOP:
                cur_step.id_line -= 1
            elif cur_step.direction == Direction.BOTTOM:
                cur_step.id_line += 1
        case '-':
            if cur_step.direction == Direction.LEFT:
                cur_step.id_char -= 1
            elif cur_step.direction == Direction.RIGHT:
                cur_step.id_char += 1
        case 'L':
            if cur_step.direction == Direction.BOTTOM:
                cur_step.direction = Direction.RIGHT
                cur_step.id_char += 1
            elif cur_step.direction == Direction.LEFT:
                cur_step.direction = Direction.TOP
                cur_step.id_line -= 1
        case 'J':
            if cur_step.direction == Direction.RIGHT:
                cur_step.direction = Direction.TOP
                cur_step.id_line -= 1
            elif cur_step.direction == Direction.BOTTOM:
                cur_step.direction = Direction.LEFT
                cur_step.id_char -= 1
        case '7':
            if cur_step.direction == Direction.RIGHT:
                cur_step.direction = Direction.BOTTOM
                cur_step.id_line += 1
            elif cur_step.direction == Direction.TOP:
                cur_step.direction = Direction.LEFT
                cur_step.id_char -= 1
        case 'F':
            if cur_step.direction == Direction.TOP:
                cur_step.direction = Direction.RIGHT
                cur_step.id_char += 1
            elif cur_step.direction == Direction.LEFT:
                cur_step.direction = Direction.BOTTOM
                cur_step.id_line += 1
        case '.':
            return None, None
        case _:
            raise Exception("case _")
    cur_step.range += 1
    return cur_step


for line in get_input():
    line = line.strip("\n")
    print(line)
    tiles_grid.append(line)

start = None
print("--")
for id_line, line in enumerate(tiles_grid):
    print(line)
    for id_symbol, pipe in enumerate(line):
        if pipe == 'S':
            start = id_symbol, id_line
            break
    if start:
        break

add_start(Step(start[0], start[1] - 1, Direction.TOP), "|7F")
add_start(Step(start[0] + 1, start[1], Direction.RIGHT), "-J7")
add_start(Step(start[0], start[1] + 1, Direction.BOTTOM), "|LJ")
add_start(Step(start[0] - 1, start[1], Direction.LEFT), "-LF")

discovered_pipes_ranges = [['.' for _ in range(0, len(tiles_grid[0]))] for line in range(0, len(tiles_grid))]
for line in discovered_pipes_ranges:
    print("".join(line))
max_range = 0
print("--")
while not max_range:
    print("---")
    for id_path, path in enumerate(paths):
        print("doing path ", id_path)
        print(path[-1])
        next_step = get_next_step(path[-1])
        print("Next step: ", next_step)
        max_range = process_step(next_step, id_path, discovered_pipes_ranges)
        print("MR ", max_range)

print("Max range: ", max_range)
# print(discovered_pipes_ranges)
# for line in discovered_pipes_ranges:
#     print("".join(str(c) for c in line))
