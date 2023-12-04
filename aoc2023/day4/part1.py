from aoc import get_input

sum = 0

for id_line, line in enumerate(get_input()):
    line = line.strip('\n')
    print(line)
    line = line.split(":")[1]
    winning_numbers_strings, numbers_strings = line.split("|")
    winning_numbers_strings = winning_numbers_strings.strip()
    winning_numbers_strings = winning_numbers_strings.split(" ")
    numbers_strings = numbers_strings.strip()
    numbers_strings = numbers_strings.split(" ")

    # remove empty strings
    winning_numbers_strings = list(filter(None, winning_numbers_strings))
    numbers_strings = list(filter(None, numbers_strings))

    winning_numbers = [int(wn) for wn in winning_numbers_strings]
    numbers = [int(n) for n in numbers_strings]

    count = 0

    for number in numbers:
        if number in winning_numbers:
            count += 1

    sum += 2 ** (count - 1) if count else 0

print(sum)
