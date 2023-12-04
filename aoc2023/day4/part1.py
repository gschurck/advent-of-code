from aoc import get_input

sum = 0

for id_line, line in enumerate(get_input()):
    line = line.strip('\n')
    print(line)
    line = line.split(":")[1]
    winning_numbers_strings, numbers_strings = map(str.split, line.split("|"))

    winning_numbers = [int(wn) for wn in winning_numbers_strings]
    numbers = [int(n) for n in numbers_strings]

    count = 0

    for number in numbers:
        if number in winning_numbers:
            count += 1

    sum += 2 ** (count - 1) if count else 0

print(sum)
