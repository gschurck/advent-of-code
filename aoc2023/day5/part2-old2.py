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
        print(map_line.strip("\n"))
        destination_start, source_start, length = map(int, map_line.split())
        current_map_diff = source_start - destination_start
        print("low ", lowest_map_diff)
        print("cur ", current_map_diff)
        if not id_map in maps:
            maps[id_map] = [(destination_start, source_start, length)]
        else:
            maps[id_map].append((destination_start, source_start, length))

    # print("-----")
    # print("next")
print(maps)
# print(len(seeds))
# for seed_id in range(0, len(seeds), 2):
#     print(seed_id)
#     for seed in range(seeds[seed_id], seeds[seed_id] + seeds[seed_id + 1]):
#         for map_values in maps.values():
#             for map_value in map_values:
#                 destination_start, source_start, length = map_value
#                 if source_start <= seed <= source_start + length:
#                     seed += destination_start - source_start
#                     break
#             # print("map seed ", seed)
#         if seed < lowest_location:
#             lowest_location = seed
#         # print

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

for id_map, maps_values in enumerate(maps.values()):
    maps_values_sorted = sorted(
        maps_values,
        key=lambda x: x[1] - x[0]
    )
    for destination_start, source_start, length in maps_values_sorted:
        if not id_map + 1 in maps:
            break
        for next_ maps[id_map + 1]
        if source_start > next_map


print("lowest location: ", lowest_location)
# 475579816
