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

b = a[0:1]
for i in range(1, n):
    b = np.concatenate((b, a[i:i+1]))
    if np.all(a[i] == 0):
        b = np.concatenate((b, a[i:i+1]))
a = b
n, m = a.shape

b = a[:,0:1]
for i in range(1, m):
    b = np.concatenate((b, a[:,i:i+1]), 1)
    if np.all(a[:,i] == 0):
        b = np.concatenate((b, a[:,i:i+1]), 1)
a = b
n, m = a.shape

points = []
for i in range(n):
    for j in range(m):
        if a[i, j]:
            points.append((i, j))

s = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        s += d

print(s)
