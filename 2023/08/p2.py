#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

chunks = list(inputChunks())
path = chunks[0][0]
graph = {}
nodes = []

for line in chunks[1]:
    fields = line.split()
    source = fields[0]
    dest1 = fields[2][1:-1]
    dest2 = fields[3][:-1]
    graph[source] = (dest1, dest2)
    assert source not in nodes
    if source.endswith('A'):
        nodes.append(source)

durations = []
for node in nodes:
    steps = 0
    index = 0
    while not node.endswith('Z'):
        if path[index] == 'L':
            node = graph[node][0]
        else:
            node = graph[node][1]
        index = (index + 1) % len(path)
        steps += 1
    durations.append(steps)
    print(node, steps, index)
    assert index == 0

total = 1
for duration in durations:
    total = lcm(total, duration)

print(total)
