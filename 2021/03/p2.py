#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

lines = list(inputLines())
values = [int(x, 2) for x in lines]
n = len(values)
m = len(lines[0])

a = np.asarray(values)
p2 = (2 ** np.arange(m))[::-1]

def select(a, invert):
    a = a.copy()
    i = 0
    while i < m and len(a) > 1:
        x = a & p2[i] != 0
        if (sum(x) >= len(a)/2) != invert:
            a = a[x]
        else:
            a = a[~x]
        i += 1
    return a[0]

oxy = select(a, False)
co2 = select(a, True)

print(oxy, co2, oxy*co2)
