#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

def toArray(lines, valueMapping={'.': 0, '#': 1}):
    rows = []
    for line in lines:
        values = [valueMapping[x] for x in line]
        rows.append(values)
    return np.array(rows)

chunks = inputChunks()
score = 0
for chunk in chunks:
    a = toArray(chunk)
    print(a)
    n, m = a.shape
    reflections = 0
    for i in range(1, n):
        k = min(i, n - i)
        a1 = a[i-k:i]
        a2 = a[i+k-1:i-1:-1]
        if np.sum(a1 != a2) == 1:
            print(f'vertical reflection below row {i}')
            reflections += 1
            score += 100 * i
    for j in range(1, m):
        k = min(j, m - j)
        a1 = a[:,j-k:j]
        a2 = a[:,j+k-1:j-1:-1]
        if np.sum(a1 != a2) == 1:
            print(f'horizontal reflection after column {j}')
            reflections += 1
            score += j
    print(f'Found {reflections} reflection')
    assert reflections == 1

print(score)
