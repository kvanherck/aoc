#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from collections import defaultdict

score = 0
scores = defaultdict(lambda : 1)
for line in inputLines():
    fields = line.split(':')
    card = int(fields[0].split()[1])
    scores[card] = scores[card]
    winning, drawn = fields[1].split('|')
    winnings = list(map(int, winning.split()))
    drawns = list(map(int, drawn.split()))
    s = len([d for d in drawns if d in winnings])
    for c in range(card+1, card+s+1):
        scores[c] = scores[c] + scores[card]

print(sum(scores.values()))
