#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

rows = []
for i, line in enumerate(inputLines()):
    row = []
    for j, char in enumerate(line):
        if char == 'S':
            height = 0
            start = i, j
        elif char == 'E':
            height = 25
            end = i, j
        else:
            height = ord(char) - ord('a')
        row.append(height)
    rows.append(row)

def isValidMove(i, j, k, l):
    if k < 0 or k >= len(rows):
        return False
    if l < 0 or l >= len(rows[0]):
        return False
    if rows[k][l] <= rows[i][j] + 1:
        return True
    return False

def edgeFunc(node):
    i, j = node
    moves = []
    for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if isValidMove(i, j, k, l):
            moves.append((k, l))
    return moves

print(len(bfs(start, end, edgeFunc=edgeFunc)) - 1)
