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

for step in range(10):
	newTemplate = ''
	for i in range(len(template) - 1):
		p = template[i:i+2]
		newTemplate += p[0]
		if p in rules:
			newTemplate += rules[p]
	newTemplate += template[-1]
	template = newTemplate
	print(step+1, len(template))

counts = {}
for c in template:
	counts[c] = counts.get(c, 0) + 1
print(counts)

l = [n for c, n in counts.items()]
l.sort()
print(l[-1] - l[0])
