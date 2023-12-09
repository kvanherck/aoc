#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

s = 0
for line in inputLines():
    print(line)
    n = ''
    for i, c in enumerate(line):
        if c >= '0' and c <= '9':
            n += c
        for k, v in digits.items():
            if line[i:i+len(k)] == k:
                n += str(v)
    print(n)
    s += int(n[0] + n[-1])
print(s)
