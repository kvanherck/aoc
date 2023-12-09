#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from collections import defaultdict

gears = defaultdict(list)

def isStar(grid, row, col):
    return grid[row, col] == '*'

def isNextToStar(grid, row, start, stop):
    for c in range(start - 1, stop + 2):
        if isStar(grid, row - 1, c):
            return row - 1, c
        if isStar(grid, row + 1, c):
            return row + 1, c
    if isStar(grid, row, start - 1):
        return row, start - 1
    if isStar(grid, row, stop + 1):
        return row, stop + 1
    return None

def testNumber(grid, row, start, stop):
    if isNextToStar(grid, row, start, stop):
        r, c = isNextToStar(grid, row, start, stop)
        gears[(r, c)].append(int(grid[row, start:stop+1]))

grid = inputGrid('.')
grid.expand(right=1)
for row in range(grid.n):
    start = stop = None
    for col in range(grid.m):
        if grid[row, col].isdigit():
            if start is None:
                start = col
        else:
            if start is not None:
                stop = col - 1
                testNumber(grid, row, start, stop)
                start = stop = None

score = 0
for numbers in gears.values():
    if len(numbers) == 2:
        score += numbers[0] * numbers[1]
print(score)
