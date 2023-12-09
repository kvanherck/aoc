#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

lines = list(inputLines())
assert len(lines) == 1
x = list(map(int, lines[0].split(',')))
a = np.asarray(x)

for i in range(80):
	print(i, len(a), a)
	z = a == 0
	n = z.sum()
	a -= 1
	a[z] = 6
	a = np.concatenate([a, np.ones(n, dtype=int)*8])

print(i+1, len(a), a)
