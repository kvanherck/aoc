#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

program = []
for opcode, arg in inputRE(r'(.)(\d+)'):
    program.append((opcode, int(arg)))

print(program)

class State(object):
    x, y = 0, 0
    h = 'E'

    turnLeft = {
        'N': 'W',
        'E': 'N',
        'S': 'E',
        'W': 'S',
    }

    turnRight = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N',
    }

    forward = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }

    instructions = {
        'N': lambda s, a: s.move(0, a),
        'S': lambda s, a: s.move(0, -a),
        'E': lambda s, a: s.move(a, 0),
        'W': lambda s, a: s.move(-a, 0),
        'F': lambda s, a: s.move(*s.forward[s.h], a),
        'L': lambda s, a: s.turn(s.turnLeft, a),
        'R': lambda s, a: s.turn(s.turnRight, a),
    }

    def move(self, dx, dy, m=1):
        self.x += dx * m
        self.y += dy * m

    def turn(self, direction, angle):
        if angle == 90:
            self.h = direction[self.h]
        elif angle == 180:
            self.h = direction[direction[self.h]]
        elif angle == 270:
            self.h = direction[direction[direction[self.h]]]

    def step(self, opcode, arg):
        print(opcode, arg)
        i = self.instructions[opcode]
        i(self, arg)
        print(self.x, self.y, self.h)

s = State()
for opcode, arg in program:
    s.step(opcode, arg)

print(abs(s.x) + abs(s.y))
