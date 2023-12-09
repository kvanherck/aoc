#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2,
}

def decimal(s):
    d = 0
    for c in s:
        d *= 5
        d += digits[c]
    return d

def snafu(d):
    s = ''
    while d > 0:
        x = d % 5
        if x <= 2:
            s = str(x) + s
            d = d // 5
        elif x == 3:
            s = '=' + s
            d = d // 5 + 1
        elif x == 4:
            s = '-' + s
            d = d // 5 + 1
    return s

s = 0
for line in inputLines():
    d = decimal(line)
    s += d
    print(f'{line} = {d}')

print(s)
print(snafu(s))
