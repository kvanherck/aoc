#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

grid = []
for line in inputLines():
    row = [int(c == '#') for c in line]
    grid.append(row)
a = np.array(grid)
n, m = a.shape

expansion = 1000000

rowIndex = []
r = 0
for i in range(n):
    rowIndex.append(r)
    if np.all(a[i] == 0):
        r += expansion
    else:
        r += 1

colIndex = []
c = 0
for i in range(m):
    colIndex.append(c)
    if np.all(a[:,i] == 0):
        c += expansion
    else:
        c += 1

points = []
for i in range(n):
    for j in range(m):
        if a[i, j]:
            points.append((rowIndex[i], colIndex[j]))

s = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        s += d

print(s)
