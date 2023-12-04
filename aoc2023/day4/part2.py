from collections import defaultdict

from aoc import get_input

copies = defaultdict(lambda: 1)

for id_line, line in enumerate(get_input()):
    card_id = id_line + 1
    copies[card_id].__init__()
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

    print("count ", count)
    for i in range(1, count + 1):
        print(f"add {count} to card {card_id + i}")
        copies[card_id + i] += copies[card_id]

print(copies)
result = sum(copies.values())
print("Result: ", result)
