import io

from aoc import get_input

input = get_input()

rules = ['A', 'B', 'C']
points = 0


def get_id(letter: str) -> int:
    i = ord(letter) - 65
    return i % 23


def wins_against(letter: str) -> str:
    i = get_id(letter)
    return rules[(i - 1) % 3]


def loses_against(letter: str) -> str:
    i = get_id(letter)
    return rules[(i + 1) % 3]


def process_round(letter1: str, letter2: str):
    global points
    letter2_id: int = get_id(letter2)
    letter2: str = rules[letter2_id]
    loser_letter: str = wins_against(letter2)
    if loser_letter == letter1:
        points += 6
    elif letter1 == letter2:
        points += 3
    points += letter2_id + 1


print("Rules:")

for r in ['A', 'B', 'C']:
    print(f"{rules[get_id(r)]} wins against {wins_against(r)}")
    print(f"{rules[get_id(r)]} loses against {loses_against(r)}")

for r in ['X', 'Y', 'Z']:
    print(f"{rules[get_id(r)]} wins against {wins_against(r)}")
    print(f"{rules[get_id(r)]} loses against {loses_against(r)}")

for line in io.StringIO(input):
    clean_line = line.strip('\n')
    process_round(clean_line[0], clean_line[2])

print("\nPoints: ", points)
