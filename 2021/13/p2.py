#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

chunks = list(inputChunks())

n, m = 0, 0
for line in chunks[0]:
	x, y = map(int, line.split(','))
	n = max(n, y)
	m = max(m, x)
if n % 2 == 1:
	n += 1
if m % 2 == 1:
	m += 1

a = np.zeros((n+1, m+1), dtype=int)
for line in chunks[0]:
	x, y = map(int, line.split(','))
	a[y, x] = 1
print(a.shape)

for line in chunks[1]:
	print(line)
	if line.startswith('fold along y='):
		y = int(line[13:])
		b1 = a[:y, :]
		b2 = a[y+1:, :]
		b = b1 | b2[::-1, :]
	if line.startswith('fold along x='):
		x = int(line[13:])
		b1 = a[:, :x]
		b2 = a[:, x+1:]
		b = b1 | b2[:, ::-1]
	a = b
	print(a.shape)

for row in a:
	s = ''.join(['#' if x else ' ' for x in row])
	print(s)
