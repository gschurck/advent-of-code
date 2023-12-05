import io

from aoc import get_input

result = 0

digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def process_char(char, line_part, reversed=False):
    print("new char: ", char)
    if char.isdigit():
        return char, line_part
    line_part = char + line_part if reversed else line_part + char
    print(line_part)
    for dig in digits.keys():
        if dig in line_part:
            print("found ", digits[dig])
            return str(digits[dig]), line_part
    return None, line_part


for line in get_input():
    line = line.strip('\n')
    print(line)
    line_part = ""
    for char in line:
        char1, line_part = process_char(char, line_part)
        if char1:
            break

    line_part = ""
    for char in reversed(line):
        char2, line_part = process_char(char, line_part, True)
        if char2:
            break

    nb = int(char1 + char2)
    print(nb)
    result += nb
print(result)
