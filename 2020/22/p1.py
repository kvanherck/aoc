#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
player1 = [int(x) for x in chunks[0][1:]]
player2 = [int(x) for x in chunks[1][1:]]
print(player1)
print(player2)

while player1 and player2:
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    assert p1 != p2
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

print(player1)
print(player2)
cards = player1 + player2
cards.reverse()
scores = [card * (i + 1) for i, card in enumerate(cards)]
print(sum(scores))
