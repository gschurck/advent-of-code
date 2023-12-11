from aoc import get_input

EXPANSION_SIZE = 1000000

lines = []
for line_id, line in enumerate(get_input()):
    line = line.strip("\n")
    print(line)
    lines.append(line)

print("galaxies")
galaxies = []
for row_id, row in enumerate(lines):
    for col_id, char in enumerate(row):
        if char == '#':
            galaxies.append((row_id, col_id))

print("rows")
added_rows = 0
for row_id, row in enumerate(lines):
    if '#' in row:  # not empty row
        continue
    rows_expansion_size = EXPANSION_SIZE
    cur_row_id = row_id + added_rows
    for galaxy_id, galaxy in enumerate(galaxies):
        galaxy_row, galaxy_col = galaxy
        if galaxy_row > row_id:
            galaxies[galaxy_id] = (galaxy_row + rows_expansion_size - 1, galaxy_col)
    added_rows += rows_expansion_size - 1

print("invert")
inverted_space = zip(*lines)

print("cols")
added_columns = 0
for col_id, col in enumerate(inverted_space):
    if '#' in col:  # not empty col
        continue
    cols_expansion_size = EXPANSION_SIZE
    cur_col_id = col_id + added_columns
    for galaxy_id, galaxy in enumerate(galaxies):
        galaxy_row, galaxy_col = galaxy
        if galaxy_col > cur_col_id:
            galaxies[galaxy_id] = (galaxy_row, galaxy_col + cols_expansion_size - 1)
    added_columns += cols_expansion_size - 1

print("paths")
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
