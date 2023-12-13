from aoc import get_input

for line in get_input():
    line = line.strip("\n")
    print(line)
    springs, numbers = line.split(" ")
    numbers = [int(nb) for nb in numbers]
    sorted_numbers = sorted(numbers, reverse=True)
    # for number in sorted_numbers:
    #     length = 0

    # for spring_id, spring in enumerate(springs):
    #     if spring not in "#?":
    #         length = 0
    #         break
    #     length += 1
    #     if length
    springs_ranges = springs.split('.')
    for sr_id, spring_range in enumerate(springs_ranges):
        if len(spring_range) == numbers[0]:
            springs_ranges[sr_id] =