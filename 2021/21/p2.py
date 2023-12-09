#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

finish = 21
player1 = 4-1
player2 = 7-1
results = {}

def play(player1, score1, player2, score2):
	try:
		return results[(player1, score1, player2, score2)]
	except KeyError:
		pass
	win1, win2 = 0, 0
	for die1 in (1, 2, 3):
		for die2 in (1, 2, 3):
			for die3 in (1, 2, 3):
				dice = die1 + die2 + die3
				p1 = (player1 + dice) % 10
				s1 = score1 + p1 + 1
				if s1 >= finish:
					win1 += 1
				else:
					w2, w1 = play(player2, score2, p1, s1)
					win1 += w1
					win2 += w2
	results[(player1, score1, player2, score2)] = (win1, win2)
	return win1, win2

start = timer()
print(play(player1, 0, player2, 0))
print(timer() - start)
