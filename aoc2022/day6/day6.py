import collections
import io

from aoc import get_input

input = get_input()


def get_start_of_nb(nb):
    buffer = collections.deque()

    for id, c in enumerate(io.StringIO(input).readlines()[0]):
        if c in [' ', '\n']:
            continue
        if len(buffer) > len(set(buffer)):
            buffer.popleft()
        elif len(buffer) == nb:
            print("Character before start-of-packet:", id)
            break

        buffer.append(c)


# Star #1
print("start-of-packet")
get_start_of_nb(4)

# Star #2
print("start-of-message")
get_start_of_nb(14)
