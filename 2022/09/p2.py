#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

class Rope:
    def __init__(self, length):
        self.knots = [(0, 0) for i in range(length)]
        self.visited = set()
        self.visited.add(self.knots[-1])

    def move(self, direction):
        x, y = self.knots[0]
        x, y = self.moveKnot(x, y, direction)
        self.knots[0] = x, y
        for i in range(1, len(self.knots)):
            self.updateKnot(i)
        self.visited.add(self.knots[-1])

    def moveKnot(self, x, y, direction):
        if direction == 'R':
            x += 1
        if direction == 'L':
            x -= 1
        if direction == 'U':
            y += 1
        if direction == 'D':
            y -= 1
        return x, y

    def updateKnot(self, i):
        headX, headY = self.knots[i - 1]
        tailX, tailY = self.knots[i]
        if abs(headX - tailX) == 2 or abs(headY - tailY) == 2:
            if headX > tailX:
                tailX += 1
            elif headX < tailX:
                tailX -= 1
            if headY > tailY:
                tailY += 1
            elif headY < tailY:
                tailY -= 1
        self.knots[i] = tailX, tailY

r = Rope(10)
for line in inputLines():
    print(line)
    direction, steps = line.split()
    steps = int(steps)
    for i in range(steps):
        r.move(direction)
        print(r.knots)

print(len(r.visited))
