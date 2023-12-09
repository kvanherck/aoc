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
cnt = 0
for line in inputLines():
    r = set(line)
    if cnt == 0:
        common = r
    else:
        common = common & r
    cnt += 1
    if cnt == 3:
        l = list(common)
        assert len(l) == 1
        s += score(l[0])
        cnt = 0

print(s)
