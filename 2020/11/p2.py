#!/usr/bin/env python3
import sys
import numpy as np
sys.path.append('..')
from common import *

i = np.asarray(inputArray(valueMapping={'.': 0, 'L': 1}))
print(i)
n, m = i.shape

newshape = (n, m)
seats = i
occupied = np.zeros(newshape, dtype=int)

def scan(a, i, j, di, dj):
    n, m = a.shape
    s = 0
    # left
    ii = i
    jj = j
    while True:
        ii += di
        jj += dj
        if ii < 0 or ii >= n:
            break
        if jj < 0 or jj >= m:
            break
        if seats[ii, jj]:
            return a[ii, jj]
    return 0

def scanAll(a, i, j):
    s = 0
    s += scan(a, i, j, -1, -1)
    s += scan(a, i, j, -1, 0)
    s += scan(a, i, j, -1, 1)
    s += scan(a, i, j, 0, -1)
    s += scan(a, i, j, 0, 1)
    s += scan(a, i, j, 1, -1)
    s += scan(a, i, j, 1, 0)
    s += scan(a, i, j, 1, 1)
    return s

g = 0
while True:
    g += 1
    print(f'Generation {g}')
    new = np.zeros(newshape, dtype=int)

    for i in range(n):
        for j in range(m):
            if seats[i, j]:
                s = scanAll(occupied, i, j)
                if occupied[i, j] == 0:
                    if s == 0:
                        new[i, j] = 1
                else:
                    if s < 5:
                        new[i, j] = 1
    print(new)
    if np.array_equal(new, occupied):
        break
    occupied = new

print(sum(new.ravel()))
