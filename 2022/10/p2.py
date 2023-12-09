#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def run(program):
    x = 1
    pc = 0
    cycle = 0
    delay = False
    for row in range(6):
        line = ''
        for column in range(40):
            if abs(column - x) <= 1:
                line += '#'
            else:
                line += ' '
            if delay:
                x = nextx
                delay = False
            else:
                instr = program[pc]
                pc += 1
                fields = instr.split()
                if fields[0] == 'addx':
                    nextx = x + int(fields[1])
                    delay = True
            cycle += 1
        print(line)

program = list(inputLines())
run(program)
