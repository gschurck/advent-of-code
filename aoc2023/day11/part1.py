from typing import List

from aoc import get_input

space: List[str] = []

for line_id, line in enumerate(get_input()):
    line = line.strip("\n")
    print(line)
    space.append(line)
    if line.count('.') == len(line):
        space.append(line)
        
empty_cols = []
for col_id in range(0, len(space[0])):
    empty_line = True
    for row_id in range(0, len(space)):
        if space[row_id][col_id] != '.':
            empty_line = False
            break
    if empty_line:
        empty_cols.append(col_id)

for i, col_id in enumerate(empty_cols):
    for row_id in range(0, len(space)):
        space[row_id] = space[row_id][:col_id + i] + '.' + space[row_id][col_id + i:]

galaxies = []

for row_id, row in enumerate(space):
    for char_id, char in enumerate(row):
        if char == '#':
            galaxies.append((row_id, char_id))

pairs = 0
lengths_sum = 0
calculated = {}
for galaxy_id, galaxy in enumerate(galaxies):
    for galaxy2_id, galaxy2 in enumerate(galaxies):
        key = min(galaxy_id, galaxy2_id), max(galaxy_id, galaxy2_id)
        if galaxy2_id == galaxy_id or key in calculated:
            continue
        pairs += 1
        path_length = abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])
        lengths_sum += path_length
        calculated[key] = True

print("Pairs: ", pairs)
print("Result: ", lengths_sum)
