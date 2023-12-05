import io

from aoc import get_input

result = 0

input = get_input()
_, seeds_string = input.readline().split(": ")
seeds = list(map(int, seeds_string.split()))
print("seeds ", seeds)

for line in input:
    print(line)

print(result)
