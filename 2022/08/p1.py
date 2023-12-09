#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

heights = {str(i):i for i in range(10)}
trees = np.asarray(inputArray(heights))
n, m = trees.shape

score = 0
for i in range(n):
    for j in range(m):
        visible = False
        if i == 0 or i == n - 1:
            visible = True
        elif j == 0 or j == m - 1:
            visible = True
        else:
            height = trees[i, j]
            if trees[i, :j].max() < height:
                visible = True
            if trees[i, j+1:].max() < height:
                visible = True
            if trees[:i, j].max() < height:
                visible = True
            if trees[i+1:, j].max() < height:
                visible = True
        if visible:
            score += 1

print(score)
