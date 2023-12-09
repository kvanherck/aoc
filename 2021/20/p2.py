#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
line = chunks[0][0]
algorithm = [1 if c=='#' else 0 for c in line]
print(len(algorithm))

lookup = {}
for i, x in enumerate(algorithm):
	b = f'{i:09b}'
	lookup[b] = str(x)

image = {}
border = '0'
n, m = 0, 0
for i, line in enumerate(chunks[1]):
	for j, c in enumerate(line):
		if c == '#':
			image[(i, j)] = '1'
			n = max(n, i)
			m = max(m, j)

iterations = 50
for iteration in range(iterations):
	newBorder = lookup[border * 9]
	newImage = {}
	for i in range(-iterations, n+iterations+1):
		for j in range(-iterations, m+iterations+1):
			s = ''
			for k in [-1, 0, 1]:
				for l in [-1, 0, 1]:
					s += image.get((i+k, j+l), border)
			if lookup[s] != newBorder:
				newImage[(i, j)] = lookup[s]
	print(iteration, 'inf' if newBorder == '1' else len(newImage))
	image = newImage
	border = newBorder
