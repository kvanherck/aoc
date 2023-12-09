#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

startTime = timer()

valves = set()
tunnels = {}
rates = {}

for fields in inputRE(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)'):
    valve = fields[0]
    rate = int(fields[1])
    rates[valve] = rate
    if rate > 0:
        valves.add(valve)
    for other in fields[2].split(', '):
        t = tunnels.get(valve, set())
        t.add(other)
        tunnels[valve] = t
        t = tunnels.get(other, set())
        t.add(valve)
        tunnels[other] = t

cache = {}
calls = 0
def findBest(iteration, position, rate, closedValves):
    global calls
    calls += 1
    if (iteration, position, tuple(closedValves)) in cache:
        return cache[(iteration, position, tuple(closedValves))]
    # print(iteration, len(closedValves))
    openValves = list(valves - closedValves)
    openValves.sort()
    # print(f'Minute {iteration+1} @ {position}: open valves = {openValves}, rate = {rate}')
    if iteration == 29:
        cache[(iteration, position, tuple(closedValves))] = (rate, [f'finished at {position}: {rate}'])
        return (rate, [f'finished at {position}: {rate}'])
    best = 0
    if position in closedValves:
        # print('opening', position)
        r, t = findBest(iteration + 1, position, rate + rates[position], closedValves - set([position]))
        if r > best:
            best = r
            trail = ['opening ' + position] + t
    if closedValves:
        for tunnel in tunnels[position]:
            # print('moving to', tunnel)
            r, t = findBest(iteration + 1, tunnel, rate, set(closedValves))
            if r >= best:
                best = r
                trail = ['moving to ' + tunnel] + t
    else:
        r, t = findBest(iteration + 1, position, rate, set(closedValves))
        if r >= best:
            best = r
            trail = ['staying at ' + position] + t
    trail[0] += ' ' + str(rate + best)
    cache[(iteration, position, tuple(closedValves))] = (rate + best, trail)
    return rate + best, trail

# print(findBest(0, 'AA', 0, 0, valves))

# 24 = OK
# print(findBest(24, 'CC', 0, 81, set()))

# 22 = OK
# print(findBest(22, 'DD', 79, set(['CC'])))

# 21 = OK
# score, trail = findBest(21, 'EE', 79, set(['CC']))

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
