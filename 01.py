from pathlib import Path

filepath = Path("./input.txt")

elves = {}
elf_count = 0
calorie_count = 0
with filepath.open() as data:
    for line in data:
        # end of previous elf
        if line == "\n":
            elves[elf_count] = calorie_count
            calorie_count = 0
            elf_count += 1
            continue
        # last line
        elif line == "":
            elves[elf_count] = calorie_count
            continue
        else:
            calorie_count += int(line.rstrip("\n"))
print(sum(sorted(elves.values(), reverse=True)[:3]))