array = [1, 2, 5, 8, 22, 55, "abc", [100, 10000]]

for i in range(10):
    array.append(i)

print(array)

size = 10
board = []

for x in range(size):
    board.append(x)
    print(x, board)

board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

for i in range(len(board)):
    print(board[i])

import random

print(random.randrange(start=7, stop=10))
print(random.uniform(0, 1))

x = "Hello world!"
y = "Goodbye world!"
z = x + y
print(z)

for i in range(10):
    x = x + "a"
    print(x)



import random


def grid_output(g):
    for i in range(len(g)):
        strr = ""
        for x in range(len(g[i])):
            strr = strr + "  " + g[i][x]
        print(str(i + 1) + strr)

width = 10
height = 10
grid = []

for i in range(height):
    row = []
    grid.append(row)
    for x in range(width):
        rng = random.uniform(0, 1)
        if rng < 0.9:
            row.append(".")
        else:
            row.append("#")

grid_output(grid)

import random

EMPTY = 0
SHIP = 1

def grid_output(g):
    for i in range(len(g)):
        strr = ""
        for x in range(len(g[i])):
            out = "."
            if g[i][x] == SHIP:
                out = "#"
            strr = strr + "  " + out
        print(str(i + 1) + strr)


width = 10
height = 10
grid = []

for i in range(height):
    row = []
    grid.append(row)
    for x in range(width):
        rng = random.uniform(0, 1)
        if rng < 0.9:
            row.append(EMPTY)
        else:
            row.append(SHIP)

grid_output(grid)
