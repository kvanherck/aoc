#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import copy

values = {}
expressions = {}
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

for line in inputLines():
    label, expression = line.split(':')
    fields = expression.split()
    if len(fields) == 1:
        value = int(fields[0])
        values[label] = value
    elif len(fields) == 3:
        expression = (fields[0], fields[1], fields[2])
        expressions[label] = expression

original = copy.copy(values)

def evaluate(label):
    try:
        return values[label]
    except KeyError:
        label1, operator, label2 = expressions[label]
        value = operators[operator](evaluate(label1), evaluate(label2))
        values[label] = value
        return value

def solve(x):
    global values
    values = copy.copy(original)
    values['humn'] = x
    expression = expressions['root']
    label1, operator, label2 = expression
    value1 = evaluate(label1)
    value2 = evaluate(label2)
    return value1 - value2

def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

low = 1
high = 1 << 64
slow = sign(solve(low))
shigh = sign(solve(high))
assert slow != shigh

while True:
    mid = (low + high) // 2
    r = solve(mid)
    if r == 0:
        print(mid)
        break
    if sign(r) == shigh:
        high = mid
    else:
        low = mid
