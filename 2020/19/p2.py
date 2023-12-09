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

rules[8] = ([42], [42, 8])
rules[11] = ([42, 31], [42, 999])
rules[999] = [11, 31]

def parseList(line, ruleNrs, indent=0):
    assert type(line) == str
    assert len(ruleNrs) <= 2
    if len(ruleNrs) == 1:
        return parse(line, ruleNrs[0], indent)
    elif len(ruleNrs) == 2:
        l = parse(line, ruleNrs[0], indent)
        return parseMulti(l, ruleNrs[1], indent)

def parse(line, ruleNr, indent=0):
    assert type(line) == str
    ws = ' ' * indent * 2
    # print(f'{ws}{ruleNr:2}: {line}')
    if not line:
        return []
    r = rules[ruleNr]
    if isinstance(r, str):
        if line[0] == r:
            return [line[1:]]
        else:
            return []
    elif isinstance(r, list):
        return parseList(line, r, indent+1)
    elif isinstance(r, tuple):
        assert len(r) == 2
        l1 = parseList(line, r[0], indent+1)
        l2 = parseList(line, r[1], indent+1)
        return l1 + l2

def parseMulti(lines, ruleNr, indent=0):
    assert type(lines) == list
    matches = []
    for line in lines:
        matches += parse(line, ruleNr, indent)
    return matches

def match(line):
    l = parse(line, 0)
    return '' in l

cnt = 0
for line in chunks[1]:
    m = match(line)
    print(line, m)
    if m:
        cnt += 1

print(cnt)
