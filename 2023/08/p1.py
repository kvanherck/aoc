#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from collections import defaultdict

chunks = list(inputChunks())
path = chunks[0][0]
graph = {}

for line in chunks[1]:
    fields = line.split()
    source = fields[0]
    dest1 = fields[2][1:-1]
    dest2 = fields[3][:-1]
    graph[source] = (dest1, dest2)

steps = 0
node = 'AAA'
index = 0
while node != 'ZZZ':
    if path[index] == 'L':
        node = graph[node][0]
    else:
        node = graph[node][1]
    index = (index + 1) % len(path)
    steps += 1
    print(steps, node)

print(steps)
