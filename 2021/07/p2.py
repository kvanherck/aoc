#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

lines = list(inputLines())
assert len(lines) == 1
x = list(map(int, lines[0].split(',')))
a = np.asarray(x)

f = None
for i in range(min(a), max(a)+1):
	d = np.abs(a - i)
	c = d * (d + 1) // 2
	s = np.sum(c)
	if f is None or s < f:
		f = s
print(f)
