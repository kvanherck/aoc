#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

print('Part 1')
result = 0
for a, b, c, s in inputRE(r'(\d+)-(\d+) (.): (.*)'):
    a, b = int(a), int(b)
    n = s.count(c)
    if a <= n and n <= b:
        print(f'{n} {a}-{b} {c} OK: {s}')
        result += 1
    else:
        print(f'{n} {a}-{b} {c} NO: {s}')
print(result)

print('Part 2')
result = 0
for a, b, c, s in inputRE(r'(\d+)-(\d+) (.): (.*)'):
    a, b = int(a), int(b)
    matches = 0
    if s[a-1] == c:
        matches += 1
    if s[b-1] == c:
        matches += 1
    if matches == 1:
        print(f'{n} {a}-{b} {c} OK: {s}')
        result += 1
    else:
        print(f'{n} {a}-{b} {c} NO: {s}')
print(result)
