from pathlib import Path
from collections import deque
import re

data = Path("./05.txt").read_text().split("\n")

size = (len(data[0]) + 1) // 4

def part1():
    stacks = {k+1: deque() for k in range(size)}

    def move_crates(amount, start, end):
        for _ in range(amount):
            stacks[end].appendleft(stacks[start].popleft())

    for row in data:
        if row.startswith("move"):
            pattern = re.compile(r"(\d+)")
            nums = pattern.findall(row)
            move_crates(*(int(n) for n in nums))
        elif row == "":
            continue
        else:
            for i in range(size):
                start = i*4
                end = start + 3
                crate = row[start:end]
                if crate.startswith("["):
                    stacks[i+1].append(crate[1])          
    print("".join(v[0] for v in stacks.values()))

def part2():
    stacks = {k+1: deque() for k in range(size)}

    def move_crates(amount, start, end):
        temp = [
            stacks[start].popleft()
            for _ in range(amount)
        ]
        stacks[end].extendleft(reversed(temp))

    for row in data:
        if row.startswith("move"):
            pattern = re.compile(r"(\d+)")
            nums = pattern.findall(row)
            move_crates(*(int(n) for n in nums))
        elif row == "":
            continue
        else:
            for i in range(size):
                start = i*4
                end = start + 3
                crate = row[start:end]
                if crate.startswith("["):
                    stacks[i+1].append(crate[1])          
    print("".join(v[0] for v in stacks.values()))
part1()
part2()