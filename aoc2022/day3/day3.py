import io

from aoc import get_input

input = get_input()
sum = 0


def get_priority(item_type):
    if ord('a') <= ord(item_type) <= ord('z'):
        subs = 96
    else:
        subs = 38
    priority = ord(item_type) - subs
    return priority


def get_sets_item_priority(lines):
    sets = []
    for line in lines:
        sets.append(set(line))
    diff = set.intersection(*sets)
    item_type = list(diff)[0]
    return get_priority(item_type)


for group in io.StringIO(input):
    clean_line = group.strip('\n')
    half = int(len(clean_line) / 2)
    first_compart = clean_line[:half]
    second_compart = clean_line[half:]
    priority = get_sets_item_priority([first_compart, second_compart])
    sum += priority

print("1) Priorities sum:", sum)


# Star #2
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


sum = 0
for group in chunks(list(io.StringIO(input)), 3):
    group = [line.strip('\n') for line in group]
    sum += get_sets_item_priority(group)

print("2) Priorities sum:", sum)
