#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def count(pattern, lengths):
    if not lengths:
        if '#' in pattern:
            return 0
        else:
            return 1
    while pattern and pattern[0] == '.':
        pattern = pattern[1:]
    if not pattern and lengths:
        return 0
    if pattern[0] == '#':
        length = lengths[0]
        l = 0
        while pattern and pattern[0] == '#':
            pattern = pattern[1:]
            l += 1
            if l > length:
                return 0
        while l < length:
            if not pattern or pattern[0] == '.':
                return 0
            pattern = pattern[1:]
            l += 1
        if not pattern:
            return count(pattern, lengths[1:])
        else:
            if pattern[0] == '#':
                return 0
            return count(pattern[1:], lengths[1:])
    else:
        n1 = count('.' + pattern[1:], lengths)
        n2 = count('#' + pattern[1:], lengths)
        return n1 + n2

score = 0
for line in inputLines():
    fields = line.split()
    pattern = fields[0]
    lengths = list(map(int, fields[1].split(',')))
    n = count(pattern, lengths)
    print(line, n)
    score += n
print(score)
