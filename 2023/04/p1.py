#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

score = 0
for line in inputLines():
    fields = line.split(':')
    winning, drawn = fields[1].split('|')
    winnings = list(map(int, winning.split()))
    drawns = list(map(int, drawn.split()))
    s = len([d for d in drawns if d in winnings])
    if s:
        score += 2**(s - 1)
print(score)
