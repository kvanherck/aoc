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

b = np.zeros((n+2, m+2), dtype=int)
b[1:-1,1:-1] = a
print(b)

incr = np.zeros((n+2, m+2), dtype=int)
incr[1:-1,1:-1] = np.ones((n, m), dtype=int)
print(incr)

incr3 = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

flashes = 0
for step in range(100):
	b += incr
	zeros = np.ones((n+2, m+2), dtype=int)
	done = False
	while not done:
		done = True
		for i in range(1, n+1):
			for j in range(1, m+1):
				if b[i, j] > 9:
					b[i-1:i+2, j-1:j+2] += incr3
					b[i, j] = 0
					zeros[i, j] = 0
					flashes += 1
					done = False
	b *= zeros
	print(step + 1, flashes)

print(flashes)
