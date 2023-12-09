#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from itertools import combinations

startTime = timer()

start = 'AA'
iterations = 26

valves = set()
rates = {}
graph = {}
paths = {}
calls = 0

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

print(f'Number of valves with nonzero flow rate: {len(valves)}')

def simulate(valves):
    def findBest(iteration, position, rate, closedValves):
        global calls
        calls += 1
        if iteration == iterations - 1:
            return rate
        best = 0
        if position in closedValves:
            r = findBest(iteration + 1, position, rate + rates[position], closedValves - set([position]))
            if r >= best:
                best = r
        else:
            found = False
            for newValve, distance in paths[position]:
                if iteration + distance < iterations and newValve in closedValves:
                    r = findBest(iteration + distance, newValve, rate, set(closedValves))
                    r += rate * (distance - 1)
                    if r >= best:
                        found = True
                        best = r
            if not found:
                r = findBest(iteration + 1, position, rate, set(closedValves))
                if r >= best:
                    best = r
        return rate + best

    score = findBest(0, 'AA', 0, valves)

    return score

done = set()
best = 0
for n in range(1, len(valves) // 2 + 1):
    c = list(combinations(valves, n))
    print(f'Processing {len(c)} sets of {n} valves')
    for v1 in c:
        v1 = frozenset(v1)
        done.add(v1)
        v2 = frozenset(valves.difference(v1))
        if v2 in done:
            continue
        s1 = simulate(v1)
        s2 = simulate(v2)
        s = s1 + s2
        if s > best:
            print(s)
            best = s

print()
print(f'Finished in {timer() - startTime:.3f} seconds')
print(f'Total calls: {calls}')
print()
print(best)
