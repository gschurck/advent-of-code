import io

from aoc import get_input

input = get_input()
reindeers = []
id_renne = 0

for line in io.StringIO(input):
    clean_line = line.strip('\n')
    if clean_line == "":
        id_renne += 1
        continue
    elif len(reindeers) > id_renne:
        reindeers[id_renne] += int(clean_line)
    else:
        reindeers.append(int(clean_line))

reindeers_sorted_cal = sorted(reindeers, reverse=True)
print("#1 Reindeer: ", reindeers_sorted_cal[0])
print("Top 3 : ", sum(reindeers_sorted_cal[:3]))
