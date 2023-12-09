#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
assert len(chunks) == 2

rules = {}
for line in chunks[0]:
    a, b = line.split(': ')
    a = int(a)
    if b.startswith('"'):
        rules[a] = b[1]
    elif '|' in b:
        l, r = b.split(' | ')
        x = list(map(int, l.split(' ')))
        y = list(map(int, r.split(' ')))
        rules[a] = (x, y)
    else:
        x = list(map(int, b.split(' ')))
        rules[a] = x

def parseList(line, ruleNrs):
    for sr in ruleNrs:
        m, line = parse(line, sr)
        if not m:
            return False, None
    # print('match', ruleNrs)
    return True, line

def parse(line, ruleNr):
    # print(ruleNr, line)
    r = rules[ruleNr]
    if isinstance(r, str):
        if line[0] == r:
            # print('match', ruleNr)
            return True, line[1:]
        else:
            return False, None
    elif isinstance(r, list):
        return parseList(line, r)
    elif isinstance(r, tuple):
        m1, l1 = parseList(line, r[0])
        if m1:
            return True, l1
        return parseList(line, r[1])

def match(line):
    m, l = parse(line, 0)
    return m and l == ''

cnt = 0
for line in chunks[1]:
    m = match(line)
    print(line, m)
    if m:
        cnt += 1

print(cnt)
