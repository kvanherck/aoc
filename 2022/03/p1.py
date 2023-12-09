#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def score(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27

s = 0
for line in inputLines():
    n = len(line) // 2
    r1 = set(line[:n])
    r2 = set(line[n:])
    l = list(r1 & r2)
    assert len(l) == 1
    s += score(l[0])

print(s)
