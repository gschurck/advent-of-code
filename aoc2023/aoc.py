import io
from io import StringIO
from pathlib import Path


def get_input() -> StringIO:
    input_path = Path("input.txt")
    return io.StringIO(input_path.read_text())
