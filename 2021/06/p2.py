#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

lines = list(inputLines())
assert len(lines) == 1
x = list(map(int, lines[0].split(',')))
a = np.asarray(x)

ages = np.zeros(9, dtype=np.ulonglong)
for x in a:
	ages[x] += 1

print(a)
print(ages)

for i in range(256):
	print(i, ages.sum())
	z = ages[0]
	ages[:-1] = ages[1:]
	ages[6] += z
	ages[-1] = z

print(i+1, ages.sum())
