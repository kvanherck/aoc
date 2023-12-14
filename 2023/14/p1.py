#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

grid = inputGrid()
print(grid)
print()

for j in range(grid.m):
    for i in range(grid.n):
        if grid[i, j] == 'O':
            k = i - 1
            while grid[k, j] == '.':
                grid[k, j] = 'O'
                grid[k + 1, j] = '.'
                k -= 1

print(grid)
print()

score = 0
for j in range(grid.m):
    for i in range(grid.n):
        if grid[i, j] == 'O':
            score += grid.n - i
print(score)
