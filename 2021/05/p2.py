#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

points = []
for x1,y1,x2,y2 in inputRE(r'(\d+),(\d+) -> (\d+),(\d+)'):
	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	points.append((x1, y1, x2, y2))

size = np.asarray(points).max() + 1
grid = np.zeros((size,size))
print(size)

for x1,y1,x2,y2 in points:
	if x1 == x2:
		if y1 > y2:
			y1, y2 = y2, y1
		grid[x1,y1:y2+1] += 1
	elif y1 == y2:
		if x1 > x2:
			x1, x2 = x2, x1
		grid[x1:x2+1:,y1] += 1
	elif x2 - x1 == y2 - y1:
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		for i in range(x2 - x1 + 1):
			grid[x1+i,y1+i] += 1
	elif x2 - x1 == y1 - y2:
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		for i in range(x2 - x1 + 1):
			grid[x1+i,y1-i] += 1

print(grid.transpose())
print(np.sum(grid >= 2))
