#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

heights = {str(i):i for i in range(10)}
trees = np.asarray(inputArray(heights))
n, m = trees.shape

maxScore = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        height = trees[i, j]
        up = 0
        for k in range(i - 1, -1, -1):
            up += 1
            if trees[k, j] >= height:
                break
        down = 0
        for k in range(i + 1, n):
            down += 1
            if trees[k, j] >= height:
                break
        left = 0
        for k in range(j - 1, -1, -1):
            left += 1
            if trees[i, k] >= height:
                break
        right = 0
        for k in range(j + 1, m):
            right += 1
            if trees[i, k] >= height:
                break
        score = up * down * left * right
        if score > maxScore:
            maxScore = score

print(maxScore)
