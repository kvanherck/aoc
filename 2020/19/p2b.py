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

generated = {}

def generateList(ruleNrs):
    assert len(ruleNrs) <= 2, ruleNrs
    if len(ruleNrs) == 1:
        return lookup(ruleNrs[0])
    s = set()
    g1 = lookup(ruleNrs[0])
    g2 = lookup(ruleNrs[1])
    for s1 in g1:
        for s2 in g2:
            s.add(s1 + s2)
    return s

def generate(ruleNr):
    if ruleNr in generated:
        return generated[ruleNr]
    else:
        r = rules[ruleNr]
        if isinstance(r, str):
            return set([r])
        elif isinstance(r, list):
            return generateList(r)
        elif isinstance(r, tuple):
            assert len(r) == 2
            s1 = generateList(r[0])
            s2 = generateList(r[1])
            return s1 | s2

def lookup(ruleNr):
    if ruleNr in generated:
        return generated[ruleNr]
    else:
        g = generate(ruleNr)
        generated[ruleNr] = g
        return g

# Assumption: rules 42 and 31 form two disjoints sets of strings of equal length
g42 = lookup(42)
g31 = lookup(31)
assert len(g42 & g31) == 0
l = len(list(g42)[0])
for s in g42:
    assert len(s) == l
for s in g31:
    assert len(s) == l

# Match rule 0 = 8 11 = 42 {42} 42 {42 31} 31
def match(line):
    n31 = 0
    while len(line) >= l:
        if line[-l:] in g31:
            n31 += 1
            line = line[:-l]
        else:
            break
    n42 = 0
    while len(line) >= l:
        if line[-l:] in g42:
            n42 += 1
            line = line[:-l]
        else:
            break
    if line:
        return False
    if n31 >= 1 and n42 >= n31 + 1:
        return True
    else:
        return False

cnt = 0
for line in chunks[1]:
    m = match(line)
    print(line, m)
    if m:
        cnt += 1

print(cnt)
