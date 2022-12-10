from pathlib import Path

filepath = Path("./09.txt")

directions = {"D": (0, -1), "U": (0,1), "L": (-1,0), "R": (1,0)}

def touching(hx,hy,tx,ty):
    dx = hx-tx
    dy = hy-ty
    adj = {(1,0), (0,1), (0,0), (1,1)}  
    #touching
    if (abs(dx),abs(dy)) in adj:
        return (True, None)
    #not touching but in same row/col
    if dx == 0 or dy == 0:
        return (False, (dx//abs(dx) if dx else 0,dy//abs(dy) if dy else 0))
    #not touching and diagonal movement
    diagX = 1 if dx >=1 else -1
    diagY = 1 if dy >=1 else -1
    return (False, (diagX,diagY))

def part1():
    hX,hY,tX,tY = 0,0,0,0
    seen = set()
    seen.add((tX,tY))
    with filepath.open() as data:
        for line in data:
            direction, steps = line.rstrip("\n").split()
            #step amounts
            dX, dY = directions[direction]
            for _ in range(int(steps)):
                #move head
                hX += dX
                hY += dY
                #move tail
                is_touching, tail_move = touching(hX,hY,tX,tY)
                if not is_touching:
                    tX += tail_move[0]
                    tY += tail_move[1]
                    #print(direction, hX,hY, tX,tY)
                    seen.add((tX,tY))
    print(len(seen))
def part2():
    knots = {k: {"x":0, "y":0} for k in range(10)}
    seen = set()
    seen.add((knots[9]["x"],knots[9]["y"]))
    with filepath.open() as data:
        for line in data:
            direction, steps = line.rstrip("\n").split()
            #step amounts
            dX, dY = directions[direction]
            for _ in range(int(steps)):
                #move head
                knots[0]["x"] += dX
                knots[0]["y"] += dY
                #move tail
                for t in range(1,10):
                    is_touching, tail_move = touching(knots[t-1]["x"],knots[t-1]["y"],knots[t]["x"],knots[t]["y"])
                    if not is_touching:
                        knots[t]["x"] += tail_move[0]
                        knots[t]["y"] += tail_move[1]
                        #print(direction, hX,hY, tX,tY)
                seen.add((knots[9]["x"],knots[9]["y"]))
    print(len(seen))
part1()
part2()