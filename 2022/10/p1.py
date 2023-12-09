#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def run(program):
    x = 1
    pc = 0
    cycle = 0
    next = 20
    signal = 0
    while pc < len(program):
        line = program[pc]
        pc += 1
        xx = x
        fields = line.split()
        if fields[0] == 'noop':
            cycle += 1
        elif fields[0] == 'addx':
            cycle += 2
            xx += int(fields[1])
        if cycle >= next:
            signal += next * x
            print(cycle, x, next * x, signal)
            next += 40
        x = xx

program = list(inputLines())
run(program)
