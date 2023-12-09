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

b = 10 * np.ones((n+2, m+2), dtype=int)
b[1:-1,1:-1] = a

s = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        x = b[i, j]
        b[i, j] = 10
        if x < np.min(b[i-1:i+2, j-1:j+2]):
            print(i, j, x)
            s += x + 1
        b[i, j] = x

print(s)
