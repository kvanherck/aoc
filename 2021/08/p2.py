#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

segmentOptions = {
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set(),
    7: set(),
}

def sortWord(w):
    letters = [c for c in w]
    letters.sort()
    return ''.join(letters)

def perm3(l):
    p = []
    for a in l:
        for b in l:
            if b == a:
                continue
            for c in l:
                if c == a or c == b:
                    continue
                p.append((a, b, c))
    return p

def intersect(x, y):
    sx = set(x)
    sy = set(y)
    si = sx ^ sy
    if len(si) == 1:
        return list(si)[0]
    else:
        return None

def equal(x, y):
    sx = set(x)
    sy = set(y)
    si = sx ^ sy
    return len(si) == 0

def check(d0, d1, d2, d3, d4, d5, d6, d7, d8, d9):
    a = intersect(d1, d7)
    if a is None:
        return None
    d = intersect(d0, d8)
    if d is None:
        return None
    c = intersect(d6, d8)
    if c is None:
        return None
    e = intersect(d9, d8)
    if e is None:
        return None
    f = intersect(d1, c)
    if f is None:
        return None
    b = intersect(d4, c+d+f)
    if b is None:
        return None
    g = intersect(d2, a+c+d+e)
    if g is None:
        return None
    if not equal(d3, a+c+d+f+g):
        return None
    if not equal(d5, a+b+d+f+g):
        return None
    s = {}
    s[0] = sortWord(a+b+c+e+f+g)
    s[1] = sortWord(c+f)
    s[2] = sortWord(a+c+d+e+g)
    s[3] = sortWord(a+c+d+f+g)
    s[4] = sortWord(b+c+d+f)
    s[5] = sortWord(a+b+d+f+g)
    s[6] = sortWord(a+b+d+e+f+g)
    s[7] = sortWord(a+c+f)
    s[8] = sortWord(a+b+c+d+e+f+g)
    s[9] = sortWord(a+b+c+d+f+g)
    d = {}
    for k, v in s.items():
        d[v] = k
    return d

answer = 0
for line in inputLines():
    print(line)
    for k in segmentOptions:
        segmentOptions[k] = set()
    parts = line.split('|')
    assert len(parts) == 2
    words1 = parts[0].split()
    words2 = parts[1].split()
    words = words1 + words2
    for word in words:
        word = sortWord(word)
        segmentOptions[len(word)].add(word)
    assert len(segmentOptions[2]) == 1
    assert len(segmentOptions[3]) == 1
    assert len(segmentOptions[4]) == 1
    assert len(segmentOptions[5]) == 3
    assert len(segmentOptions[6]) == 3
    assert len(segmentOptions[7]) == 1
    d1 = list(segmentOptions[2])[0]
    d4 = list(segmentOptions[4])[0]
    d7 = list(segmentOptions[3])[0]
    d8 = list(segmentOptions[7])[0]
    for d2, d3, d5 in perm3(segmentOptions[5]):
        for d0, d6, d9 in perm3(segmentOptions[6]):
            digits = check(d0, d1, d2, d3, d4, d5, d6, d7, d8, d9)
            if digits:
                number = 0
                for word in words2:
                    word = sortWord(word)
                    number *= 10
                    number += digits[word]
                print(number)
                answer += number

print(answer)
