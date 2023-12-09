#!/usr/bin/env python3
import sys
import re
import heapq
from timeit import default_timer as timer

DEFAULT_INPUT = 'input.txt'

def inputLines(ignoreBlanks=True, stripWhitespace=True):
    if len(sys.argv) == 1:
        inputFile = DEFAULT_INPUT
    elif len(sys.argv) == 2:
        inputFile = sys.argv[1]
    else:
        sys.exit(f'Usage: {sys.argv[0]} [{DEFAULT_INPUT}]')
    n = 0
    with open(inputFile) as f:
        for line in f.readlines():
            if stripWhitespace:
                line = line.strip()
            if ignoreBlanks and not line:
                continue
            yield line
            n += 1
    print(f'Parsed {n} lines')


def inputInts():
    for line in inputLines():
        yield int(line)


def inputRE(pattern):
    r = re.compile(pattern)
    for line in inputLines():
        m = r.match(line)
        if m:
            yield m.groups()


def inputChunks():
    n = 0
    chunk = []
    for line in inputLines(ignoreBlanks=False):
        if line:
            chunk.append(line)
        else:
            if chunk:
                yield chunk
                n += 1
                chunk = []
    if chunk:
        yield chunk
        n += 1
    print(f'Parsed {n} chunks')


def inputArray(valueMapping={'.': 0, '#': 1}):
    rows = []
    for line in inputLines():
        values = [valueMapping[x] for x in line]
        rows.append(values)
    return rows


def inputGrid(defaultValue=None):
    g = Grid.fromListOfLists(inputLines())
    g.defaultValue = defaultValue
    return g


def bfs(start, destination=None, destFunc=None, graph=None, edgeFunc=None):
    if destFunc is None:
        assert destination is not None
        destFunc = lambda node: node == destination
    if edgeFunc is None:
        assert graph is not None
        edgeFunc = lambda node: graph[node]
    queue = [start]
    prev = {}
    while True:
        if not queue:
            return None
        currentNode = queue.pop(0)
        if destFunc(currentNode):
            node = currentNode
            trail = [node]
            while node != start:
                node = prev[node]
                trail.append(node)
            trail.reverse()
            return trail
        for newNode in edgeFunc(currentNode):
            if newNode not in prev:
                prev[newNode] = currentNode
                queue.append(newNode)


def dijkstra(start, destination=None, destFunc=None, graph=None, costFunc=None, returnTrail=False):
    if destFunc is None:
        assert destination is not None
        destFunc = lambda node: node == destination
    if costFunc is None:
        assert graph is not None
        costFunc = lambda node: graph[node]
    costs = {}
    queue = [(0, start)]
    prev = {}
    while True:
        if not queue:
            return None
        currentCost, currentNode = heapq.heappop(queue)
        if destFunc(currentNode):
            if returnTrail:
                node = currentNode
                trail = [node]
                while node != start:
                    node = prev[node]
                    trail.append(node)
                trail.reverse()
                return currentCost, trail
            else:
                return currentCost
        for newNode, weight in costFunc(currentNode):
            newCost = currentCost + weight
            if newNode not in costs or newCost < costs[newNode]:
                costs[newNode] = newCost
                prev[newNode] = currentNode
                heapq.heappush(queue, (newCost, newNode))


class Grid:
    def __init__(self, n, m, defaultValue=None):
        self.n = n
        self.m = m
        self.defaultValue = defaultValue
        self.data = [[defaultValue] * m for _ in range(n)]

    @classmethod
    def fromListOfLists(cls, lol):
        lol = list(lol)
        n = len(lol)
        m = len(lol[0])
        g = cls(n, m)
        for i, r in enumerate(lol):
            for j, c in enumerate(r):
                g[i, j] = c
        return g

    def __getitem__(self, key):
        if type(key) != tuple:
            raise TypeError
        if len(key) != 2:
            raise TypeError
        r, c = key
        if type(r) != int:
            raise TypeError
        if type(c) == slice:
            a = [self[r, i] for i in range(c.start, c.stop, c.step or 1)]
            if type(self.defaultValue) == str:
                return ''.join(a)
            return a
        if type(c) != int:
            raise TypeError
        if r < 0 or r >= self.n:
            return self.defaultValue
        if c < 0 or c >= self.m:
            return self.defaultValue
        return self.data[r][c]

    def __setitem__(self, key, value):
        if type(key) != tuple:
            raise TypeError
        if len(key) != 2:
            raise TypeError
        r, c = key
        if type(r) != int:
            raise TypeError
        if type(c) != int:
            raise TypeError
        if r < 0 or r >= self.n:
            raise IndexError
        if c < 0 or c >= self.m:
            raise IndexError
        self.data[r][c] = value

    def expand(self, left=None, right=None, bottom=None, top=None, value=None):
        if value is None:
            value = self.defaultValue
        if left:
            for i in range(self.n):
                self.data[i] = [value] * left + self.data[i]
            self.m += left
        if right:
            for i in range(self.n):
                self.data[i] = self.data[i] + [value] * right
            self.m += right
        if bottom:
            self.data = [[value] * self.m for _ in range(bottom)] + self.data
            self.n += bottom
        if top:
            self.data = self.data + [[value] * self.m for _ in range(top)]
            self.n += top

    def __str__(self):
        lines = []
        for row in self.data:
            line = ''.join([str(c) for c in row])
            lines.append(line)
        return '\n'.join(lines)
