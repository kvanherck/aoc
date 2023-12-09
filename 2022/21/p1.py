#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

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

def evaluate(label):
    try:
        return values[label]
    except KeyError:
        label1, operator, label2 = expressions[label]
        value = operators[operator](evaluate(label1), evaluate(label2))
        values[label] = value
        return value

print(int(evaluate('root')))
