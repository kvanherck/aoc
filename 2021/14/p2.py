#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

chunks = list(inputChunks())

template = chunks[0][0]
rules = {}

for line in chunks[1]:
	a, b = line.split(' -> ')
	rules[a] = b

print(template)
print(rules)

def addPair(d, p, n=1):
	d[p] = d.get(p, 0) + n

pairs = {}
for i in range(len(template) - 1):
	p = template[i:i+2]
	addPair(pairs, p)

for step in range(40):
	newPairs = {}
	for p, n in pairs.items():
		if p in rules:
			addPair(newPairs, p[0] + rules[p], n)
			addPair(newPairs, rules[p] + p[1], n)
		else:
			addPair(newPairs, p, n)
	pairs = newPairs

counts = {template[0]: 1}
for p, n in pairs.items():
	counts[p[1]] = counts.get(p[1], 0) + n
print(counts)

l = [n for c, n in counts.items()]
l.sort()
print(l[-1] - l[0])
