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
    wx, wy = 10, 1

    right2Left = {
        0: 0,
        90: 270,
        180: 180,
        270: 90,
    }

    instructions = {
        'N': lambda s, a: s.moveW(0, a),
        'S': lambda s, a: s.moveW(0, -a),
        'E': lambda s, a: s.moveW(a, 0),
        'W': lambda s, a: s.moveW(-a, 0),
        'F': lambda s, a: s.forward(a),
        'L': lambda s, a: s.turnLeft(a),
        'R': lambda s, a: s.turnLeft(s.right2Left[a]),
    }

    def moveW(self, dx, dy):
        self.wx += dx
        self.wy += dy

    def forward(self, a):
        self.x += self.wx * a
        self.y += self.wy * a

    def turnLeft(self, angle):
        if angle == 90:
            self.wx, self.wy = -self.wy, self.wx
        elif angle == 180:
            self.wx, self.wy = -self.wx, -self.wy
        elif angle == 270:
            self.wx, self.wy = self.wy, -self.wx

    def step(self, opcode, arg):
        print(opcode, arg)
        i = self.instructions[opcode]
        i(self, arg)
        print(self.x, self.y)

s = State()
for opcode, arg in program:
    s.step(opcode, arg)

print(abs(s.x) + abs(s.y))
