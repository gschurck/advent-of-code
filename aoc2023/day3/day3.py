from typing import List, Dict, Tuple

from aoc import get_input


def get_close_number_value(numbers_dict, symbol_x, symbol_line):
    val_list = numbers_dict.get((symbol_x, symbol_line), [0])
    if not val_list:
        return 0
    val = val_list[0]
    if val > 0:
        numbers_dict[(symbol_x, symbol_line)].clear()
        # print("add ", val)
    return val


sum = 0

numbers: Dict[Tuple[int, int], List[int]] = {}
symbols = []

for id_line, line in enumerate(get_input()):
    line = line.strip('\n')
    print(line)

    new_number_string = ""
    new_number_coords = None
    for id_char, char in enumerate(line):
        if char.isdigit():  # digit found
            if not new_number_string:  # start of a new number
                new_number_coords = (id_char, id_line)
            new_number_string += char
        elif new_number_string:  # end of a number
            new_number = [int(new_number_string)]
            for x in range(new_number_coords[0], id_char):
                numbers[x, new_number_coords[1]] = new_number
            new_number_string = ""
            new_number_coords = None

        if not char.isdigit() and char != ".":
            # symbol found
            symbols.append((id_char, id_line))

for symbol_x, symbol_line in symbols:
    sum += get_close_number_value(numbers, symbol_x - 1, symbol_line - 1)
    sum += get_close_number_value(numbers, symbol_x, symbol_line - 1)
    sum += get_close_number_value(numbers, symbol_x + 1, symbol_line - 1)
    sum += get_close_number_value(numbers, symbol_x + 1, symbol_line)
    sum += get_close_number_value(numbers, symbol_x + 1, symbol_line + 1)
    sum += get_close_number_value(numbers, symbol_x, symbol_line + 1)
    sum += get_close_number_value(numbers, symbol_x - 1, symbol_line + 1)
    sum += get_close_number_value(numbers, symbol_x - 1, symbol_line)

print("Part 1 sum: ", sum)
# 542793
print(numbers)
