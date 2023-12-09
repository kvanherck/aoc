#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

rows = []
for line in inputLines():
    row = [int(c) for c in line]
    rows.append(row)
a = np.asarray(rows)
n, m = a.shape
print(a)

b = 9 * np.ones((n+2, m+2), dtype=int)
b[1:-1, 1:-1] = a

basins = []

def growBasin(i, j):
    size = 0
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if b[i+dx, j+dy] != 9:
            b[i+dx, j+dy] = 9
            size += 1 + growBasin(i+dx, j+dy)
    return size

def findBasin():
    for i in range(1, n+1):
        for j in range(1, m+1):
            if b[i, j] != 9:
                b[i, j] = 9
                size = 1 + growBasin(i, j)
                basins.append(size)
                return True
    return False

while findBasin():
    pass

basins.sort()
basins.reverse()
print(basins)
assert len(basins) >= 3
m = 1
for x in basins[:3]:
    m *= x
print(m)
