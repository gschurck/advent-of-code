from collections import defaultdict

from aoc import get_input

result = 0

for line in get_input():
    line = line.strip("\n")
    print(line)
    values_dict = defaultdict(list)
    values_dict[0] = list(map(int, line.split()))

    step = 0
    while values_dict[step].count(0) != len(values_dict[step]):
        step += 1
        for id_val, value in enumerate(values_dict[step - 1][1:]):
            diff = value - values_dict[step - 1][id_val]
            values_dict[step].append(diff)
    values_dict[len(values_dict) - 1].insert(0, 0)
    for id_line, diff_line in enumerate(reversed(list(values_dict.values())[1:])):
        id_line = len(values_dict) - id_line - 1
        values_dict[id_line - 1].insert(0, values_dict[id_line - 1][0] - values_dict[id_line][0])
    print(values_dict)
    result += values_dict[0][0]
    print("add ", values_dict[0][0])

print("Result ", result)
