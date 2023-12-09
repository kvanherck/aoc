#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

stacks = []
for line in inputLines(ignoreBlanks=False, stripWhitespace=False):
    if line.startswith(' 1'):
        break
    letters = line[1::4]
    for i, c in enumerate(letters):
        if i == len(stacks):
            stacks.append([])
        if c == ' ':
            continue
        stacks[i].insert(0, c)

for fields in inputRE(r'move (\d+) from (\d+) to (\d+)'):
    cnt, x, y = map(int, fields)
    for i in range(cnt):
        c = stacks[x-1].pop()
        stacks[y-1].append(c)

tops = [stack[-1] for stack in stacks]
print(''.join(tops))
