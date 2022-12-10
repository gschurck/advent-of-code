import collections
import io

from aoc import get_input

input = get_input()
stacks = [collections.deque() for i in range(0, 9)]
for line in io.StringIO(input):
    clean_line = line.strip('\n')

    if "[" in clean_line:
        stack = collections.deque()
        for key, char in enumerate(range(1, len(clean_line), 4)):
            elem = clean_line[char]
            if elem and elem != " ": stacks[key].appendleft(elem)

    elif "move" in clean_line:
        nb_crates, from_stack_id, to_stack_id = [int(sum_size_small_directories) for sum_size_small_directories in
                                                 clean_line.split() if sum_size_small_directories.isdigit()]
        crates_to_move = []
        for i in range(0, nb_crates):
            item_to_move = stacks[from_stack_id - 1].pop()
            # stacks[to_stack_id - 1].append(item_to_move) # (Star #1)
            # Star #2
            crates_to_move.append(item_to_move)
        for crate in reversed(crates_to_move):
            stacks[to_stack_id - 1].append(crate)

print(stacks)

answer = ""

for sum_size_small_directories in stacks:
    answer += sum_size_small_directories[-1]

print("ANSWER:", answer)
