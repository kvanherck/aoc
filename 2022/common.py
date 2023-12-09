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
