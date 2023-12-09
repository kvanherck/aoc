#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

class Rope:
    def __init__(self):
        self.visited = set()
        self.headX, self.headY = (0, 0)
        self.tailX, self.tailY = (0, 0)
        self.visited.add((0, 0))

    def right(self):
        self.headX += 1
        if self.headX == self.tailX + 2:
            self.tailX += 1
            self.tailY = self.headY
        self.visited.add((self.tailX, self.tailY))

    def left(self):
        self.headX -= 1
        if self.headX == self.tailX - 2:
            self.tailX -= 1
            self.tailY = self.headY
        self.visited.add((self.tailX, self.tailY))

    def up(self):
        self.headY += 1
        if self.headY == self.tailY + 2:
            self.tailY += 1
            self.tailX = self.headX
        self.visited.add((self.tailX, self.tailY))

    def down(self):
        self.headY -= 1
        if self.headY == self.tailY - 2:
            self.tailY -= 1
            self.tailX = self.headX
        self.visited.add((self.tailX, self.tailY))

r = Rope()
for line in inputLines():
    print(line)
    direction, steps = line.split()
    steps = int(steps)
    for i in range(steps):
        if direction == 'R':
            r.right()
        if direction == 'L':
            r.left()
        if direction == 'U':
            r.up()
        if direction == 'D':
            r.down()
        print(r.headX, r.headY, r.tailX, r.tailY)

print(len(r.visited))
