#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from collections import defaultdict

cardValue = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}
for i in range(2, 10):
    cardValue[str(i)] = i

typeValue = {
    (1, 1, 1, 1, 1): 0,
    (2, 1, 1, 1): 1,
    (2, 2, 1): 2,
    (3, 1, 1): 3,
    (3, 2): 4,
    (4, 1): 5,
    (5,): 6,
}

def getType(hand):
    cards = defaultdict(int)
    for card in hand:
        cards[card] += 1
    counts = []
    for c, n in cards.items():
        counts.append(n)
    counts.sort()
    counts.reverse()
    return typeValue[tuple(counts)]

def getValues(hand):
    return [cardValue[card] for card in hand]

hands = []
for line in inputLines():
    hand, bid = line.split()
    bid = int(bid)
    hands.append((getType(hand), getValues(hand), hand, bid))
hands.sort()

rank = 1
score = 0
for type, value, hand, bid in hands:
    print(rank, hand, bid, type, value)
    score += rank * bid
    rank += 1
print(score)
