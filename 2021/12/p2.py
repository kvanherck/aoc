#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

nodes = {}
for line in inputLines():
	a, b = line.split('-')
	nodes.setdefault(a, set()).add(b)
	nodes.setdefault(b, set()).add(a)

paths = []
def search(path, revisited=False):
	if path[-1] == 'end':
		paths.append(path)
		print(path)
	else:
		for node in nodes[path[-1]]:
			if node.islower() and node in path:
				if not revisited and node not in ['start', 'end']:
					search(path + [node], True)
			else:
				search(path + [node], revisited)

search(['start'])
print(len(paths))
