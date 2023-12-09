#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

nodes = {}
for line in inputLines():
	a, b = line.split('-')
	nodes.setdefault(a, set()).add(b)
	nodes.setdefault(b, set()).add(a)

paths = []
def search(path):
	if path[-1] == 'end':
		paths.append(path)
		print(path)
	else:
		for node in nodes[path[-1]]:
			if node == node.lower() and node in path:
				continue
			search(path + [node])

search(['start'])
print(len(paths))
