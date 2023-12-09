#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

startTime = timer()

start = 'AA'
iterations = 30

valves = set()
rates = {}
paths = {}
graph = {}

for fields in inputRE(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)'):
    valve = fields[0]
    rate = int(fields[1])
    rates[valve] = rate
    if rate > 0:
        valves.add(valve)
    graph[valve] = []
    for other in fields[2].split(', '):
        graph[valve].append(other)

for src in valves | set([start]):
    paths[src] = []
    for dst in valves:
        if src == dst:
            continue
        l = len(bfs(src, dst, graph=graph)) - 1
        paths[src].append((dst, l))

cache = {}
calls = 0
def findBest(iteration, position, rate, closedValves):
    global calls
    calls += 1
    if (iteration, position, tuple(closedValves)) in cache:
        return cache[(iteration, position, tuple(closedValves))]
    if iteration == iterations - 1:
        return (rate, [f'finished at {position}: {rate}'])
    best = 0
    if position in closedValves:
        r, t = findBest(iteration + 1, position, rate + rates[position], closedValves - set([position]))
        if r >= best:
            best = r
            trail = ['opening ' + position] + t
    else:
        found = False
        for newValve, distance in paths[position]:
            if iteration + distance < iterations and newValve in closedValves:
                r, t = findBest(iteration + distance, newValve, rate, set(closedValves))
                r += rate * (distance - 1)
                if r >= best:
                    found = True
                    best = r
                    trail = ['moving to ' + newValve] + t
        if not found:
            r, t = findBest(iteration + 1, position, rate, set(closedValves))
            if r >= best:
                best = r
                trail = ['staying at ' + position] + t
    trail[0] += ' ' + str(rate + best)
    cache[(iteration, position, tuple(closedValves))] = (rate + best, trail)
    return rate + best, trail

score, trail = findBest(0, 'AA', 0, valves)

print()
for line in trail:
    print(line)

print()
print(f'Finished in {timer() - startTime:.3f} seconds')
print(f'Total calls: {calls}')
print(f'Cache size: {len(cache)}')
print()
print(score)
