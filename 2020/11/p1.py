#!/usr/bin/env python3
import sys
import numpy as np
sys.path.append('..')
from common import *

i = np.asarray(inputArray(valueMapping={'.': 0, 'L': 1}))
print(i)
n, m = i.shape

newshape = (n + 2, m + 2)
seats = np.zeros(newshape, dtype=int)
seats[1:1+n, 1:1+m] = i
occupied = np.zeros(newshape, dtype=int)

g = 0
while True:
    g += 1
    print(f'Generation {g}')
    new = np.zeros(newshape, dtype=int)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if seats[i, j]:
                sa = occupied[i-1:i+2, j-1:j+2]
                s = sum(sa.ravel()) - occupied[i, j]
                if occupied[i, j] == 0:
                    if s == 0:
                        new[i, j] = 1
                else:
                    if s < 4:
                        new[i, j] = 1
    print(new)
    if np.array_equal(new, occupied):
        break
    occupied = new

print(sum(new.ravel()))
