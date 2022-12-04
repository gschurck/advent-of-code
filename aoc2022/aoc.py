from pathlib import Path


def get_input() -> str:
    # cwd = Path(__file__).parents[1].__str__()
    input = Path("input.txt")
    return input.read_text()
