import io

from aoc import get_input

input = get_input()


def get_assignment_data(assignment):
    start, end = assignment.split('-')
    return int(start), int(end), abs(int(start) - int(end))


def get_other_index(id):
    return abs(1 - id)


sum_contained = 0
sum_overlap = 0

for line in io.StringIO(input):
    pair = line.strip('\n')
    assignments = pair.split(',')
    pair_widths = []
    for id, assignment in enumerate(assignments):
        start, end, width = get_assignment_data(assignment)
        pair_widths.append(width)
        assignments[id] = [start, end]
    maxw = max(pair_widths)

    max_id = pair_widths.index(maxw)
    max_assignment = assignments[max_id]
    min_assignment = assignments[get_other_index(max_id)]

    if max_assignment[0] <= min_assignment[0] <= min_assignment[1] <= max_assignment[1]:
        sum_contained += 1

    r = range(int(max_assignment[0]), int(max_assignment[1]) + 1)

    if min_assignment[0] in r or min_assignment[1] in r:
        sum_overlap += 1

print("Fully contained assignment pairs:", sum_contained)
print("Overlapping assignment pairs:", sum_overlap)
