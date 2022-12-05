from pathlib import Path
from string import ascii_letters

filepath = Path("./03.txt")
priority = {letter: index for index, letter in enumerate(ascii_letters, 1)}

def part1():
    res = 0
    with filepath.open() as data:
        for line in data:
            sack = line.rstrip("\n")
            size = len(sack) // 2
            comp_1 = set(sack[:size])
            comp_2 = set(sack[size:])
            same = comp_1 & comp_2
            res += sum(priority[letter] for letter in same)
    print(res)

def part2():
    res = 0
    line_num = 0
    seen = []
    with filepath.open() as data:
        for line in data:
            line_num += 1
            sack = line.rstrip("\n")
            seen.append(set(sack))
            if line_num == 3:
                badge = seen[0] & seen[1] & seen[2]
                print(badge)
                res += sum(priority[letter] for letter in badge)
                seen = []
                line_num = 0
    print(res)

part1()
part2()