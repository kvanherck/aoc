#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

minx, maxx = 1, 1
miny, maxy = 1, 1
minz, maxz = 1, 1
for line in inputLines():
    x, y, z = tuple(map(int, line.split(',')))
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)
    minz = min(minz, z)
    maxz = max(maxz, z)

print(f'X: {minx}-{maxx}')
print(f'Y: {miny}-{maxy}')
print(f'Z: {minz}-{maxz}')
assert minx >= 0
assert miny >= 0
assert minz >= 0

n, m, l = maxx + 3, maxy + 3, maxz + 3
a = np.zeros((n, m, l), dtype=int)

for line in inputLines():
    x, y, z = tuple(map(int, line.split(',')))
    a[x + 1, y + 1, z + 1] = 1

for i in range(1, n - 1):
    for j in range(1, m - 1):
        for k in range(1, l - 1):
            if a[i, j, k] == 1:
                continue
            if a[0:i, j, k].sum() == 0:
                continue
            if a[i+1:, j, k].sum() == 0:
                continue
            if a[i, 0:j, k].sum() == 0:
                continue
            if a[i, j+1:, k].sum() == 0:
                continue
            if a[i, j, 0:k].sum() == 0:
                continue
            if a[i, j, k+1:].sum() == 0:
                continue
            a[i, j, k] = 1

dx = a[1:,:,:] - a[:-1,:,:]
nx = (abs(dx) == 1).sum()

dy = a[:,1:,:] - a[:,:-1,:]
ny = (abs(dy) == 1).sum()

dz = a[:,:,1:] - a[:,:,:-1]
nz = (abs(dz) == 1).sum()

print(nx + ny + nz)
