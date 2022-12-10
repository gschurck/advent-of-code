import io

from aoc import get_input


class Directory:
    parent: 'Directory'
    directories: dict[str, 'Directory']
    size: int

    def __init__(self, parent):
        self.parent = parent
        self.directories = {}
        self.files_sizes = []

    def get_directory_size(self) -> int:
        directory_size: int = self.get_subdirectories_size() + sum(self.files_sizes)
        CmdParser.sum_size_small_directories += directory_size if directory_size <= 100000 else 0
        self.size = directory_size
        CmdParser.directories_sizes.append(directory_size)
        return directory_size

    def get_subdirectories_size(self) -> int:
        subdirectories_size: int = 0
        for subdirectory in self.directories.values():
            subdirectories_size += subdirectory.get_directory_size()
        return subdirectories_size


class CmdParser:
    cwd: Directory = Directory(None)
    is_ls: bool = False
    sum_size_small_directories = 0
    size_dir_to_delete: int
    directories_sizes: [int] = []

    @staticmethod
    def cd(directory_name: str):
        match directory_name:
            case "/":
                CmdParser.cd_root()
            case "..":
                CmdParser.cwd = CmdParser.cwd.parent
            case _:
                CmdParser.cwd = CmdParser.cwd.directories[directory_name]

    @staticmethod
    def ls(line):
        splitted_line = line.split(" ")
        if line[:3] == "dir":
            directory_name: str = splitted_line[1]
            CmdParser.cwd.directories[directory_name] = Directory(CmdParser.cwd)
        else:
            file_size: int = int(splitted_line[0])
            CmdParser.cwd.files_sizes.append(file_size)

    @staticmethod
    def get_root_recursive(dir: Directory):
        return CmdParser.get_root_recursive(dir.parent) if dir.parent else dir

    @staticmethod
    def cd_root():
        CmdParser.cwd = CmdParser.get_root_recursive(CmdParser.cwd)

    # Star 2 **
    @staticmethod
    def get_size_directory_to_delete() -> int:
        CmdParser.directories_sizes.sort()
        unused_space: int = 70000000 - CmdParser.get_root_total_size()
        min_size_dir_to_del: int = 30000000 - unused_space
        return next(size for size in CmdParser.directories_sizes if size > min_size_dir_to_del)

    @staticmethod
    def get_root_total_size():
        CmdParser.cd_root()
        root = CmdParser.cwd
        return sum([directory.size for directory in root.directories.values()]) + sum(root.files_sizes)


line_input = io.StringIO(get_input())

for line in line_input:
    clean_line = line.strip('\n')
    if clean_line[0] == '$':
        CmdParser.is_ls = False
        match clean_line[2:4]:
            case "cd":
                CmdParser.cd(clean_line[5:])
            case "ls":
                CmdParser.is_ls = True
    elif CmdParser.is_ls:
        CmdParser.ls(clean_line)

CmdParser.cd_root()
_ = CmdParser.cwd.get_subdirectories_size()

# Star 1 *
print("Small directories size sum:", CmdParser.sum_size_small_directories)

# Star 2 **
print("Total size of directory to delete:", CmdParser.get_size_directory_to_delete())
