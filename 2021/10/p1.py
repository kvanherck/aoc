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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

totalScore = 0
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
                totalScore += score[c]
                return
    if stack:
        print(f'Incomplete')

rows = []
for line in inputLines():
    parse(line)

print(totalScore)
