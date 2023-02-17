import random

width = 10
height = 10
EMPTY = 0
SHIP = 1
grid = []

def grid_output(g):
    for i in range(len(g)):
        strr = ""
        for x in range(len(g[i])):
            out = "."
            if g[i][x] == SHIP:
                out = "#"
            strr = strr + "  " + out
        print(str(i+1) +strr)

for i in range(height):
    row = []
    grid.append(row)
    for x in range(width):
        row.append(EMPTY)

ship_sizes = [5, 4, 3, 3, 2]

for size in ship_sizes:
    while True:
        vertical = random.choice([True, False])
        if vertical:
            start_row = random.randint(0, height - size)
            start_col = random.randint(0, width - 1)
            end_row = start_row + size - 1
            end_col = start_col
        else:
            start_row = random.randint(0, height - 1)
            start_col = random.randint(0, width - size)
            end_row = start_row
            end_col = start_col + size - 1

        saskarsme = False
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                if grid[r][c] == SHIP:
                    saskarsme = True
                    break
            if saskarsme:
                break

        if not saskarsme:
            for r in range(start_row, end_row + 1):
                for c in range(start_col, end_col + 1):
                    grid[r][c] = SHIP
            break

grid_output(grid)