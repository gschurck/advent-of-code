import math
from typing import List, Dict, Tuple

from aoc import get_input


def add_number(new_number_string, new_number_coords, id_char, numbers):
    new_number = [int(new_number_string)]
    for x in range(new_number_coords[0], id_char):
        numbers[x, new_number_coords[1]] = new_number


def get_close_number_value(numbers_dict, symbol_x, symbol_line):
    val_list = numbers_dict.get((symbol_x, symbol_line), [0])
    if not val_list:
        return 0
    val = val_list[0]
    if val > 0:
        numbers_dict[(symbol_x, symbol_line)].clear()
    return val


result = 0

numbers: Dict[Tuple[int, int], List[int]] = {}
symbols = []

for id_line, line in enumerate(get_input()):
    line = line.strip('\n')
    print(line)

    new_number_string = ""
    new_number_coords = None
    last_id_char = None
    for id_char, char in enumerate(line):
        if char.isdigit():  # digit found
            if not new_number_string:  # start of a new number
                new_number_coords = (id_char, id_line)
            new_number_string += char
            last_id_char = id_char
        elif new_number_string:  # end of a number
            add_number(new_number_string, new_number_coords, id_char, numbers)
            new_number_string = ""
            new_number_coords = None

        if not char.isdigit() and char != ".":  # symbol found
            symbols.append((id_char, id_line))

    if new_number_string:
        add_number(new_number_string, new_number_coords, last_id_char, numbers)

for symbol_x, symbol_line in symbols:
    values = [get_close_number_value(numbers, symbol_x - 1, symbol_line - 1) or None,
              get_close_number_value(numbers, symbol_x, symbol_line - 1) or None,
              get_close_number_value(numbers, symbol_x + 1, symbol_line - 1) or None,
              get_close_number_value(numbers, symbol_x + 1, symbol_line) or None,
              get_close_number_value(numbers, symbol_x + 1, symbol_line + 1) or None,
              get_close_number_value(numbers, symbol_x, symbol_line + 1) or None,
              get_close_number_value(numbers, symbol_x - 1, symbol_line + 1) or None,
              get_close_number_value(numbers, symbol_x - 1, symbol_line) or None]
    values = list(filter(None, values))
    print(values)
    if len(values) != 2:
        continue
    result += math.prod(values)

print("Result: ", result)
