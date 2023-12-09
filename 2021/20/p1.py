#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
line = chunks[0][0]
algorithm = [1 if c=='#' else 0 for c in line]
print(len(algorithm))

image = {}
border = 0
n, m = 0, 0
for i, line in enumerate(chunks[1]):
	for j, c in enumerate(line):
		if c == '#':
			image[(i, j)] = 1
			n = max(n, i)
			m = max(m, j)

iterations = 2
for iteration in range(iterations):
	newBorder = algorithm[int(str(border) * 9, 2)]
	newImage = {}
	for i in range(-2, n+3):
		for j in range(-2, m+3):
			s = ''
			for k in [-1, 0, 1]:
				for l in [-1, 0, 1]:
					s += str(image.get((i+k, j+l), border))
			x = int(s, 2)
			if algorithm[x] != newBorder:
				newImage[(i, j)] = algorithm[x]
	s = 0
	for i in range(-2, n+3):
		for j in range(-2, m+3):
			s += newImage.get((i, j), newBorder)
	print(iteration, newBorder, s, len(newImage))
	image = newImage
	border = newBorder
