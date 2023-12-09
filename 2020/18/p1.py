#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def tokenize(s):
    n = ''
    for c in s:
        if c in '0123456789':
            n += c
        else:
            if n:
                yield int(n)
                n = ''
            if c != ' ':
                yield c
    if n:
        yield int(n)

def evaluateExpr(tokens):
    t, tokens = evaluateTerm(tokens)
    acc = t
    while tokens:
        oper = tokens.pop(0)
        t, tokens = evaluateTerm(tokens)
        if oper == '+':
            acc += t
        elif oper == '*':
            acc *= t
    return acc

def evaluateTerm(tokens):
    t = tokens.pop(0)
    if t == '(':
        i = findClosingBracket(tokens)
        t = evaluateExpr(tokens[:i])
        tokens = tokens[i+1:]
    assert isinstance(t, int), t
    return t, tokens

def findClosingBracket(tokens):
    level = 1
    for i in range(len(tokens)):
        if tokens[i] == '(':
            level += 1
        elif tokens[i] == ')':
            level -= 1
        if level == 0:
            return i
    raise ValueError('Closing bracket not found')

def parse(s):
    tokens = list(tokenize(s))
    n = evaluateExpr(tokens)
    print(f'{s} = {n}')
    return n

s = 0
for line in inputLines():
    s += parse(line)

print(s)
