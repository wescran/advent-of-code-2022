from pathlib import Path
from collections import deque

filepath = Path("./10.txt")
#filepath = Path("./test.txt")

register = 1
cycle = 1
checks = (c for c in range(20,260,40))
signal = 0
queue = deque()
check = next(checks)
crt = []
row = ""

def draw_pixels(row):
    mod = (cycle - 1) % 40
    if mod in [register - 1, register, register + 1]:
        row += "#"
    else:
        row += "."
    if mod == 39:
        crt.append(row)
        row = ""
    return row

def add_signal(signal, check):
    if cycle == check:
        signal += register * check
        try:
            check = next(checks)
        except StopIteration:
            pass
    return (signal, check)

def add_operation(line):
    operation = line[:4]
    if operation == "noop":
        dur = 1
        inc = 0
    else:
        dur = 2
        inc = int(line[5:])
    queue.append([inc, dur])

def finish_cycles(register):
    stack = queue[0]
    if stack[-1] == 1:
        register += stack[0]
        queue.popleft()
    else:
        stack[-1] -= 1
    return register

with filepath.open() as data:
    # grab initial queue item
    line = data.readline().rstrip("\n")
    add_operation(line)
    while len(queue) > 0:
        try:
            line = data.readline().rstrip("\n")
        except:
            line = None
        row = draw_pixels(row)
        signal, check = add_signal(signal, check)
        register = finish_cycles(register)
        cycle += 1
        if line:
            add_operation(line)
print(signal)
for r in crt:
    print(r)