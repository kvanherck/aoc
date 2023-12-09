#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

score = 0

def isSymbol(grid, row, col):
    return grid[row, col] != '.'

def isNextToSymbol(grid, row, start, stop):
    for c in range(start - 1, stop + 2):
        if isSymbol(grid, row - 1, c):
            return True
        if isSymbol(grid, row + 1, c):
            return True
    if isSymbol(grid, row, start - 1):
        return True
    if isSymbol(grid, row, stop + 1):
        return True
    return False

def testNumber(grid, row, start, stop):
    if isNextToSymbol(grid, row, start, stop):
        global score
        score += int(grid[row, start:stop+1])

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

print(score)
