#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

a = inputArray()

def trees(x, y):
    i, j = 0, 0
    s = 0
    while True:
        i += y
        j += x
        if i >= len(a):
            break
        row = a[i]
        j = j % len(row)
        if row[j]:
            s += 1
    print(f'right {x} down {y} sum {s}')
    return s

p = 1
p *= trees(1, 1)
p *= trees(3, 1)
p *= trees(5, 1)
p *= trees(7, 1)
p *= trees(1, 2)
print(p)
