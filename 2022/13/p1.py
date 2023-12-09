#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def compare(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return True
        elif l1 > l2:
            return False
        else:
            return None
    if isinstance(l1, list) and isinstance(l2, list):
        i = 0
        while True:
            if i == len(l1) and i == len(l2):
                return None
            if i == len(l1):
                return True
            if i == len(l2):
                return False
            c = compare(l1[i], l2[i])
            if c is not None:
                return c
            i += 1
    if isinstance(l1, int) and isinstance(l2, list):
        return compare([l1], l2)
    if isinstance(l1, list) and isinstance(l2, int):
        return compare(l1, [l2])
    assert False

if __name__ == '__main__':
    score = 0
    index = 1
    for chunk in inputChunks():
        l1 = eval(chunk[0])
        l2 = eval(chunk[1])
        print(l1)
        print(l2)
        c = compare(l1, l2)
        print(index, c)
        if c is None:
            c = True
        if c:
            score += index
        print()
        index += 1

    print(score)
