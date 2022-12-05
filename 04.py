from pathlib import Path

filepath = Path("./04.txt")

def part1():
    found = 0
    with filepath.open() as data:
        for line in data:
            pair_1, pair_2 = line.rstrip("\n").split(",")
            start_1, stop_1 = pair_1.split("-")
            start_2, stop_2 = pair_2.split("-")
            range_1 = set(range(int(start_1), int(stop_1) + 1))
            range_2 = set(range(int(start_2), int(stop_2) + 1))
            if range_1 & range_2 == range_1 or range_1 & range_2 == range_2:
                found += 1
    print(found)
def part2():
    found = 0
    with filepath.open() as data:
        for line in data:
            pair_1, pair_2 = line.rstrip("\n").split(",")
            start_1, stop_1 = pair_1.split("-")
            start_2, stop_2 = pair_2.split("-")
            range_1 = set(range(int(start_1), int(stop_1) + 1))
            range_2 = set(range(int(start_2), int(stop_2) + 1))
            if range_1 & range_2:
                found += 1
    print(found)
part1()
part2()