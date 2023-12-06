from collections import defaultdict
from math import prod

from aoc import get_input

input = get_input()


def get_line_value(input):
    line = input.readline()
    line = line.strip("\n")
    print(line)
    _, line = line.split(":")
    return int(line.replace(" ", ""))


def iter_from_middle(lst):
    try:
        middle = len(lst) // 2
        yield lst[middle]

        for shift in range(1, middle + 1):
            yield lst[middle - shift]
            yield lst[middle + shift]

    except IndexError:  # occures on lst[len(lst)] or for empty list
        raise StopIteration


time = get_line_value(input)
distance_record = get_line_value(input)

beat_records_ways = 0

hold_times = range(1, time)

for hold_time in iter_from_middle(hold_times):
    traveled_distance = hold_time * (time - hold_time)
    if traveled_distance < distance_record:
        break
    beat_records_ways += 1

print("Result ", beat_records_ways)
