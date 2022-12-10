from pathlib import Path

filepath = Path("./08.txt")
#filepath = Path("./test.txt")
# create grid, use dictionaries for faster lookup
grid = {}
with filepath.open() as data:
    for row, line in enumerate(data):
        row_dict = {}
        for col, h in enumerate(line.rstrip("\n")):
            row_dict[int(col)] = int(h)
        grid[int(row)] = row_dict

# initial visible value includes outside border of trees
grid_len = len(grid)
row_len = len(grid[0])
visible = 0

def check_trees(row, col):
    h = grid[row][col]
    false_check = 0
    view_l, view_r, view_u, view_d = 0,0,0,0
    #check left
    for i in range(col-1, -1, -1):
        view_l += 1
        if grid[row][i] >= h:
            false_check += 1
            break
    #check right
    for i in range(col + 1,row_len):
        view_r += 1
        if grid[row][i] >= h:
            false_check += 1
            break
    # check up
    for i in range(row - 1, -1, -1):
        view_u += 1
        if grid[i][col] >= h:
            false_check += 1
            break
    #check down
    for i in range(row + 1,grid_len):
        view_d += 1
        if grid[i][col] >= h:
            false_check += 1
            break
    
    return (False if false_check == 4 else True, view_l * view_r * view_u * view_d)

view_scores = []
for r in range(grid_len):
    for c in range(row_len):
        is_visible, view_score = check_trees(r,c)
        if is_visible:
            visible += 1
        view_scores.append(view_score)


print(visible)
print(max(view_scores))