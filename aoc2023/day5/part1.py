import time
from math import inf

from aoc import get_input

lowest_location = inf
maps = {}

input = get_input()
_, seeds_string = input.readline().split(": ")
seeds = list(map(int, seeds_string.split()))
print("seeds ", seeds)
input.readline()

for id_map, map_start in enumerate(input):
    map_line = ""
    print("new map")
    print(map_start.strip("\n"))
    for map_line in input:
        if map_line == "\n":
            break
        print("new line")
        print(map_line.strip("\n"))
        destination_start, source_start, length = map(int, map_line.split())
        if not id_map in maps:
            maps[id_map] = [(destination_start, source_start, length)]
        maps[id_map].append((destination_start, source_start, length))
    print("-----")
    print("next")
print(maps)
for seed in seeds:
    print("seed ", seed)
    for map_values in maps.values():
        for map_value in map_values:
            destination_start, source_start, length = map_value
            if source_start <= seed <= source_start + length:
                seed += destination_start - source_start
                break
        print("map seed ", seed)
    if seed < lowest_location:
        lowest_location = seed
    print("location ", seed)
print(lowest_location)
