from collections import defaultdict
from math import prod

from aoc import get_input

input = get_input()


def get_line_values(input):
    line = input.readline()
    line = line.strip("\n")
    print(line)
    _, line = line.split(":")
    return list(map(int, line.split()))


times = get_line_values(input)
distances = get_line_values(input)

print(times)
print(distances)

beat_records_ways = defaultdict(int)

for id_race, races in enumerate(zip(times, distances)):
    time, distance_record = races
    print(f"{time} {distance_record}")
    for hold_time in range(1, time):
        traveled_distance = hold_time * (time - hold_time)
        print(f"traveled {traveled_distance}")
        if traveled_distance > distance_record:
            beat_records_ways[id_race] += 1

result = prod(beat_records_ways.values())
print("Result ", result)
