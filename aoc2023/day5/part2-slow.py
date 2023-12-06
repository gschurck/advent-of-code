import time
from collections import OrderedDict
from math import inf

from aoc import get_input

lowest_location = inf
maps = {}

input = get_input()
_, seeds_string = input.readline().split(": ")
seeds_list = list(map(int, seeds_string.split()))
seeds_iter = iter(seeds_list)
seeds = list(zip(seeds_iter, seeds_iter))
print(seeds)

# print("seeds ", seeds)
input.readline()

for id_map, map_start in enumerate(input):
    map_line = ""
    print("new map")
    # print(map_start.strip("\n"))
    lowest_map_diff = inf
    for map_line in input:
        if map_line == "\n":
            break
        # print("new line")
        # print(map_line.strip("\n"))
        destination_start, source_start, length = map(int, map_line.split())
        current_map_diff = source_start - destination_start
        # print("low ", lowest_map_diff)
        # print("cur ", current_map_diff)
        # if not id_map in maps:
        #     maps[id_map] = (destination_start, source_start, length)
        #     lowest_map_diff = current_map_diff
        # else:
        #     min_destination_start, min_source_start, _ = maps[id_map]
        #     if current_map_diff < lowest_map_diff:
        #         lowest_map_diff = current_map_diff
        #         print("ok")
        #         maps[id_map] = (destination_start, source_start, length)
        #     print("-----")
        if not id_map in maps:
            maps[id_map] = [(destination_start, source_start, length)]
        else:
            # destination_start, source_start, _ = maps[id_map]
            maps[id_map].append((destination_start, source_start, length))
    # print("-----")
    # print("next")
print(maps)
print(len(seeds))
for i, seed_tuple in enumerate(seeds):
    seed_start, seed_length = seed_tuple
    print(i)
    for seed in range(seed_start, seed_start + seed_length):
        for map_values in maps.values():
            for map_value in map_values:
                destination_start, source_start, length = map_value
                if source_start <= seed <= source_start + length:
                    seed += destination_start - source_start
                    break
            # print("map seed ", seed)
        if seed < lowest_location:
            lowest_location = seed
        # print

# for seed_id in range(0, len(seeds), 2):
#     seed_start = seeds[seed_id]
#     seed_range = seeds[seed_id + 1]
#     print(seed_id)
#     for seed in range(seeds[seed_id], seeds[seed_id] + seeds[seed_id + 1]):
#         for map_value in maps.values():
#             destination_start, source_start, length = map_value
#             if source_start <= seed <= source_start + length:
#                 seed += destination_start - source_start
#                 break
#             # print("map seed ", seed)
#         if seed < lowest_location:
#             lowest_location = seed
#         # print("location ", seed)
# max_source_start = -inf
# min_source_stop = inf
# for destination_start, source_start, length in reversed(maps.values()):
#     cur_start = source_start
#     cur_stop = source_start + length
#
#     if cur_start > max_source_start:
#         max_source_start = cur_start
#     if cur_stop < min_source_stop:
#         min_source_stop = cur_stop
#
# print("max_start ", max_source_start)
# print("min_stop ", min_source_stop)
print("lowest location: ", lowest_location)
# 475579816
