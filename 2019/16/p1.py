#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

phases = 100
repetitions = 1

def generatePatterns(n):
    patterns = []
    for i in range(1, n + 1):
        pattern = [0]*i + [1]*i + [0]*i + [-1]*i
        while len(pattern) < n + 1:
            pattern *= 2
        patterns.append(pattern[1:n+1])
    return patterns

for line in inputLines():
    line = line * repetitions
    n = len(line)
    values = list(map(int, line))
    patterns = generatePatterns(n)
    for phase in range(phases):
        newValues = []
        for i in range(n):
            digit = abs(sum([a * b for a, b in zip(values, patterns[i])])) % 10
            newValues.append(digit)
        values = newValues
        print(phase, ''.join(map(str, values)))
    print(''.join(map(str, values[-10:])))
