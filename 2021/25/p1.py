#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

# example: 58 0.005s
# input: 374 3.08s
start = timer()

cells = {}
n, m = 0, 0
for i, line in enumerate(inputLines()):
	n = max(n, i)
	for j, c in enumerate(line):
		m = max(m, j)
		if c != '.':
			cells[(i, j)] = c
n += 1
m += 1
print(n, m)

def show(cells):
	for i in range(n):
		s = ''
		for j in range(m):
			s += cells.get((i, j), '.')
		print(s)

show(cells)

prevCells = {}
steps = 0
while True:
	print(steps)
	if prevCells == cells:
		break
	steps += 1
	prevCells = cells
	newCells = {}
	for (i, j), v in cells.items():
		if v == '>':
			jj = (j + 1) % m
			if (i, jj) not in cells:
				newCells[(i, jj)] = v
			else:
				newCells[(i, j)] = v
		else:
			newCells[(i, j)] = v
	cells = newCells
	newCells = {}
	for (i, j), v in cells.items():
		if v == 'v':
			ii = (i + 1) % n
			if (ii, j) not in cells:
				newCells[(ii, j)] = v
			else:
				newCells[(i, j)] = v
		else:
			newCells[(i, j)] = v
	cells = newCells

show(cells)
print(steps)
print(timer() - start)
