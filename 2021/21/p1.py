#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

player1 = 4
score1 = 0
player2 = 7
score2 = 0
die = 1
cnt = 0

while True:
	print(die, player1, score1, player2, score2)
	player1 += die + (die + 1) + (die + 2)
	player1 = ((player1 - 1) % 10) + 1
	score1 += player1
	die += 3
	if score1 >= 1000:
		die -= 1
		print(die, player1, player2, score2*die)
		break
	player2 += die + (die + 1) + (die + 2)
	player2 = ((player2 - 1) % 10) + 1
	score2 += player2
	die += 3
	if score2 >= 1000:
		die -= 1
		print(die, player1, player2, score1*die)
		break
