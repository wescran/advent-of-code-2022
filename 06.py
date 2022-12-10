from pathlib import Path
from collections import deque
data = Path("./06.txt").read_text().rstrip("\n")

def get_index(size):
    seen = deque(maxlen=size)
    for index, char in enumerate(data, 0):
        seen.append(char)
        if len(set(seen)) == size:
            print(f"index is {index + 1}")
            break
#part 1
print(get_index(4))
# part 2
print(get_index(14))