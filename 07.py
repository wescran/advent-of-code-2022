from pathlib import Path
import re

filepath = Path("./07.txt")

class Directory:
    """
    Each class instance represents on directory on the system
    """
    def __init__(self, path, previous=None, size=0, level=0):
        self.path = path
        self.previous = previous
        self.size = size
        self.level = level
    def __repr__(self):
        return f"{self.__class__.__name__}({self.path})"

root_dir = Directory(path="/")
print(root_dir)
directories = {}
directories["/"] = root_dir
current_dir = root_dir

def trickle(directory, size):
    directory.size += size
    if directory.previous:
        trickle(directory.previous, size)

with filepath.open() as data:
    for line in data:
        prompt = line.rstrip("\n")
        if prompt.startswith("$"):
            command = prompt[2:4]
            if command == "cd":
                loc = prompt[5:]
                if loc == "..":
                    current_dir = current_dir.previous if current_dir.previous else root_dir
                elif loc == "/":
                    current_dir = directories["/"]
                else:
                    path = current_dir.path + loc + "/"
                    try:
                        next = directories[path]
                    except KeyError:
                        next = Directory(path=path, previous=current_dir, level=current_dir.level + 1)
                        directories[path] = next
                    current_dir = next
        elif prompt.startswith("dir"):
            path = current_dir.path + prompt[4:] + "/"
            new_dir = Directory(path=path, previous=current_dir, level=current_dir.level + 1)
            directories[path] = new_dir
        else:
            pattern = re.compile(r"^(\d+) (\D+)$")
            file_size, file_name = pattern.match(prompt).groups()
            current_dir.size += int(file_size)
            if current_dir.previous:
                trickle(current_dir.previous, int(file_size))
print(directories)
#part 1
sorted_vals = sorted(directories.values(), key=lambda x: x.level)
current_node = sorted_vals.pop()
res = 0
seen = set()
while True:
    if current_node.path not in seen:
        current_size = current_node.size
        if current_size <= 100000:
            res += current_size
        seen.add(current_node.path)
        if current_node.previous:
            current_node = current_node
            continue
    try:
        current_node = sorted_vals.pop()
    except:
        break
print(res)

#part 2
total_disk_space = 70000000
space_needed = 30000000
total_used = directories["/"].size
space_to_find = space_needed-(total_disk_space - total_used)
sorted_sizes = sorted(directories.values(), key=lambda x: x.size, reverse=True)
current = sorted_sizes.pop()
while True:
    node_size = current.size
    if node_size >= space_to_find:
        print(node_size)
        break
    try:
        current = sorted_sizes.pop()
    except:
        break