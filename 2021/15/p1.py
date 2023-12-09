#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np
import heapq

def readInput():
	rows = []
	for line in inputLines():
	    row = [int(c) for c in line]
	    rows.append(row)
	a = np.asarray(rows)
	print(a.shape)
	print(a)
	return a

infinity = 1000000

def neighbours(x, y, n, m):
	l = []
	if x > 0:
		l.append((x-1, y))
	if x < n-1:
		l.append((x+1, y))
	if y > 0:
		l.append((x, y-1))
	if y < m-1:
		l.append((x, y+1))
	return l

def dijkstra(weights, start, destination):
	costs = np.ones(weights.shape, dtype=int) * infinity
	costs[start] = 0
	queue = [(0, start)]
	while True:
		c0, current = heapq.heappop(queue)
		for i, j in neighbours(*current, *weights.shape):
			if costs[i, j] == infinity:
				c = c0 + weights[i, j]
				costs[i, j] = c
				heapq.heappush(queue, (c, (i, j)))
		if current == destination:
			print(costs)
			return costs[current]

def main():
	a = readInput()
	n, m = a.shape
	print(dijkstra(a, (0, 0), (n-1, m-1)))

if __name__ == '__main__':
	main()
