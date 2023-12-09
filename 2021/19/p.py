#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from collections import defaultdict

scanners = []

for block in inputChunks():
	scanner = []
	for line in block[1:]:
		x, y, z = map(int, line.split(','))
		scanner.append((x, y, z))
	scanners.append(scanner)
n = len(scanners)

print(f'Parsed {n} scanners')

def diffVector(v1, v2):
	x1, y1, z1 = v1
	x2, y2, z2 = v2
	return x1 - x2, y1 - y2, z1 - z2

def offsetVector(v, o):
	x1, y1, z1 = v
	x2, y2, z2 = o
	return x1 + x2, y1 + y2, z1 + z2

def manhattan(v1, v2):
	x1, y1, z1 = v1
	x2, y2, z2 = v2
	return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

def rotateVector(v, xTurns, yTurns, zTurns):
	x, y, z = v
	if xTurns:
		y, z = z, -y
	if yTurns:
		x, z = z, -x
	if zTurns:
		x, y = y, -x
	return x, y, z

def rotateScanner(scanner, xTurns, yTurns, zTurns):
	rotated = []
	for v in scanner:
		v = rotateVector(v, xTurns, yTurns, zTurns)
		rotated.append(v)
	return rotated

def distances(scanner):
	dists = set()
	for b1 in scanner:
		for b2 in scanner:
			if b1 < b2:
				dists.add(diffVector(b1, b2))
	return dists

def findOverlap(s1, s2, threshold=12*11/2):
	d1 = distances(s1)
	s2r = s2
	for x in range(2):
		for y in range(4):
			for z in range(4):
				d2 = distances(s2r)
				if len(d1 & d2) >= threshold:
					return s2r
				s2r = rotateScanner(s2r, 0, 0, 1)
			s2r = rotateScanner(s2r, 0, 1, 0)
		s2r = rotateScanner(s2r, 1, 0, 0)
	return None

def findOffset(s1, s2, threshold=12):
	set1 = set(s1)
	for b1 in s1:
		for b2 in s2:
			offset = diffVector(b1, b2)
			s2o = []
			for b in s2:
				s2o.append(offsetVector(b, offset))
			set2 = set(s2o)
			if len(set1 & set2) >= threshold:
				return s2o, offset
	return None, None

def relocate(s1, s2):
	r = findOverlap(s1, s2)
	if r:
		r, o = findOffset(s1, r)
		if r:
			return r, o
	return None, None

located = set([0])
remaining = set(range(1, n))
offsets = [None for i in range(n)]
offsets[0] = (0, 0, 0)
mismatch = set()

while remaining:
	for i in range(n):
		if i in located:
			for j in remaining:
				if (i, j) not in mismatch:
					s, o = relocate(scanners[i], scanners[j])
					if s:
						scanners[j] = s
						located.add(j)
						remaining.remove(j)
						offsets[j] = o
						print(f'Scanner {j} overlaps with {i}: {len(located)}/{n}')
						break
					else:
						mismatch.add((i, j))

beacons = set()
for s in scanners:
	for b in s:
		beacons.add(b)
print(f'Found {len(beacons)} beacons')

d = 0
for o1 in offsets:
	for o2 in offsets:
		m = manhattan(o1, o2)
		d = max(d, m)
print(f'Maximum Manhattan distance = {d}')
