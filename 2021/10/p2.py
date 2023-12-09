#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

scores = []
def parse(line):
    global totalScore
    print(line)
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if not stack:
                print(f'Extra delimiter: {c}')
                return
            d = stack.pop()
            if c != closing[d]:
                print(f'Invalid delimiter: expected {closing[d]} found {c}')
                return
    if stack:
        s = 0
        m = ''
        while stack:
            d = closing[stack.pop()]
            m += d
            s *= 5
            s += score[d]
        scores.append(s)
        print(f'Incomplete: missing {m} score {s}')

rows = []
for line in inputLines():
    parse(line)

scores.sort()
print(scores[len(scores) // 2])
