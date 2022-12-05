from pathlib import Path

wins = {"X": "C", "Y": "A", "Z": "B"}
loses = {"X": "B", "Y": "C", "Z": "A"}
scoring = {"X": 1, "Y": 2, "Z": 3}
loss, draw, win = 0,3,6
opp_wins = {"A": "Z", "B": "X", "C": "Y"}
opp_loses = {"A": "Y", "B": "Z", "C": "X"}
opp_draw = {"A": "X", "B": "Y", "C": "Z"}

filepath = Path("./02.txt")
def part1():
    score = 0
    with filepath.open() as data:
        for line in data:
            opp, you = tuple(line.rstrip("\n").split())
            score += scoring[you]
            if wins[you] == opp:
                score += win
            elif loses[you] == opp:
                score += loss
            else:
                score += draw
    print(score)

def part2():
    score = 0
    with filepath.open() as data:
        for line in data:
            opp, you = tuple(line.rstrip("\n").split())
            if you == "X":
                score += loss + scoring[opp_wins[opp]]
            elif you== "Y":
                score += draw + scoring[opp_draw[opp]]
            else:
                score += win + scoring[opp_loses[opp]]
    print(score)
part1()
part2()