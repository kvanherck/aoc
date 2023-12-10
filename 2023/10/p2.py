#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

grid = inputGrid('.')
print(grid)

for i in range(grid.n):
    for j in range(grid.m):
        if grid[i, j] == 'S':
            start = (i, j)
print(f'Starting position: {start}')

northLinks = '|LJ'
southLinks = '|7F'
eastLinks = '-FL'
westLinks = '-J7'

def nextPos(grid, pos, dontMove=None):
    # Try north
    if dontMove != 'N' and grid[pos] in northLinks:
        newPos = (pos[0] - 1, pos[1])
        if grid[newPos] in southLinks:
            return newPos, 'S'
    # Try east
    if dontMove != 'E' and grid[pos] in eastLinks:
        newPos = (pos[0], pos[1] + 1)
        if grid[newPos] in westLinks:
            return newPos, 'W'
    # Try south
    if dontMove != 'S' and grid[pos] in southLinks:
        newPos = (pos[0] + 1, pos[1])
        if grid[newPos] in northLinks:
            return newPos, 'N'
    # Try west
    if dontMove != 'W' and grid[pos] in westLinks:
        newPos = (pos[0], pos[1] - 1)
        if grid[newPos] in eastLinks:
            return newPos, 'E'
    return None, None

for startSymbol in '|-LJ7F':
    loopGrid = Grid(grid.n, grid.m, '.')
    grid[start] = startSymbol
    loopGrid[start] = grid[start]
    pos = start
    steps = 0
    dontMove=None
    while True:
        pos, dontMove = nextPos(grid, pos, dontMove)
        if pos is None:
            steps = 0
            break
        steps += 1
        if pos == start:
            break
        loopGrid[pos] = grid[pos]
    print(startSymbol, steps, steps // 2)
    if steps > 0:
        break

insideCnt = 0
for i in range(grid.n):
    inside = False
    onLoop = None
    for j in range(grid.m):
        if not onLoop:
            if loopGrid[i, j] == '|':
                inside = not inside
            elif loopGrid[i, j] in 'LF':
                onLoop = loopGrid[i, j]
            elif inside and loopGrid[i, j] == '.':
                loopGrid[i, j] = 'I'
                insideCnt += 1
        elif onLoop == 'L':
            if loopGrid[i, j] == '7':
                onLoop = False
                inside = not inside
            elif loopGrid[i, j] in 'J':
                onLoop = False
        elif onLoop == 'F':
            if loopGrid[i, j] == 'J':
                onLoop = False
                inside = not inside
            elif loopGrid[i, j] in '7':
                onLoop = False

print(loopGrid)
print(insideCnt)
