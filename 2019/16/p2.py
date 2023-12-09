#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

phases = 100
repetitions = 10000
size = 521000

C = np.zeros(size, dtype=int)
C[0] = 1
for phase in range(phases):
    print(f'Generating phase {phase + 1} array')
    D = np.zeros(size, dtype=int)
    D[0] = C[0]
    for i in range(1, size):
        D[i] = (D[i-1] + C[i]) % 10
    C = D

for line in inputLines():
    print(line)
    digits = []
    values = list(map(int, line))
    n = len(values)
    offset = int(line[:7])
    for pos in range(offset + 1, offset + 9):
        digit = n * repetitions - pos
        if digit > size:
            raise ValueError(f'This input requires a size of at least {digit}')
        s = 0
        for j in range(digit + 1):
            s += C[j] * values[(-digit+j-1) % n]
            s %= 10
        digits.append(s)
    print(''.join(map(str, digits)))
