import io

from aoc import get_input

sum = 0
sum2 = 0

for game_id, line in enumerate(get_input()):
    impossible = False
    line = line.strip('\n')
    print(line)
    line = line.split(":")[1].strip()
    cubes_subsets_list = line.split(";")

    color_mins = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for cubes_subset in cubes_subsets_list:
        cubes_colors = cubes_subset.strip().split(",")

        for cubes in cubes_colors:
            cubes = cubes.strip()
            cubes_count_string = ""

            for char in cubes:
                if not char.isdigit():
                    break
                cubes_count_string += char
            cubes_count = int(cubes_count_string)

            color = cubes[len(cubes_count_string) + 1:]
            if cubes_count > color_mins[color]:
                color_mins[color] = cubes_count
                print(f"- set min {color} to {cubes_count}")

            if not impossible:
                if color == "red" and cubes_count > 12:
                    impossible = True
                elif color == "green" and cubes_count > 13:
                    impossible = True
                elif color == "blue" and cubes_count > 14:
                    impossible = True

    cubes_set_power = 1
    for color_min in color_mins.values():
        cubes_set_power *= color_min
    print(cubes_set_power)
    sum2 += cubes_set_power

    if impossible:
        print("Impossible")
        impossible = False
        continue
    print("sum " + str(game_id + 1))
    sum += game_id + 1

# print("\nPart 1: ", sum)
print("\nPart 2: ", sum2)
