import time
from collections import OrderedDict
from math import inf

from aoc import get_input

lowest_location = inf
maps = OrderedDict()

input = get_input()
_, seeds_string = input.readline().split(": ")
seeds_list = list(map(int, seeds_string.split()))
seeds_iter = iter(seeds_list)
seeds = list(zip(seeds_iter, seeds_iter))
print(seeds)

min_range = inf
max_range = -inf

# print("seeds ", seeds)
input.readline()

for id_map, map_start in enumerate(input):
    if id_map > 0:
        break
    map_line = ""
    print("new map")
    # print(map_start.strip("\n"))
    lowest_map_diff = inf
    for map_line in input:
        if map_line == "\n":
            break
        # print("new line")
        print(map_line.strip("\n"))
        destination_start, source_start, length = map(int, map_line.split())
        current_map_diff = source_start - destination_start
        print("low ", lowest_map_diff)
        print("cur ", current_map_diff)
        if not id_map in maps:
            maps[id_map] = [(destination_start, source_start, length)]
        else:
            maps[id_map].append((destination_start, source_start, length))
        min_range = min(source_start, min_range)
        max_range = max(source_start + length, max_range)
    # print("-----")
    # print("next")
print(maps)

for seed_start, seed_length in seeds:
    print(f"min diff: {seed_start - min_range} max diff: {seed_start + seed_length - max_range}")

print("lowest location: ", lowest_location)
# 475579816
