#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

lines = list(inputLines(ignoreBlanks=False))

numbers = list(map(int, lines[0].split(',')))

boards = []
board = []
for line in lines[2:] + ['']:
	line = line.strip()
	if line:
		r = list(map(int, line.split()))
		board.append(r)
	else:
		b = np.asarray(board)
		boards.append(b)
		board = []

n, m = boards[0].shape

marked = [np.zeros((n, m)) for _ in range(len(boards))]

def markAll(boards, marked, x):
	for i in range(len(boards)):
		mark(boards[i], marked[i], x)

def mark(board, marked, x):
	found = board == x
	marked[found] = 1

def isWinner(marked):
	if np.any(np.sum(marked, 0) == 5) or np.any(np.sum(marked, 1) == 5):
		return True
	else:
		return False

def findWinner():
	for i, x in enumerate(numbers):
		markAll(boards, marked, x)
		for j, m in enumerate(marked):
			if isWinner(m):
				print(f'Board {j+1} wins with {x} at turn {i+1}')
				score = boards[j][m == 0].sum()
				print(f'Score = {score} * {x} = {score * x}')
				return

findWinner()
