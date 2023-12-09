#!/usr/bin/env python3
import sys
sys.path.append('..')
import copy
from common import *

startTime = timer()

class State:
    minute = 0

    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0

    oreRobots = 1
    clayRobots = 0
    obsidianRobots = 0
    geodeRobots = 0

    factory = 'idle'
    trail = []

    def update(self, build=None):
        self.minute += 1
        self.ore += self.oreRobots
        self.clay += self.clayRobots
        self.obsidian += self.obsidianRobots
        self.geodes += self.geodeRobots
        if self.factory == 'idle':
            if build is not None:
                # print(f'{self.minute} Start building {build} robot')
                self.trail = self.trail + [(self.minute, build)]
                self.factory = build
                if self.factory == 'ore':
                    self.ore -= oreRobotOreCost
                if self.factory == 'clay':
                    self.ore -= clayRobotOreCost
                if self.factory == 'obsidian':
                    self.ore -= obsidianRobotOreCost
                    self.clay -= obsidianRobotClayCost
                if self.factory == 'geode':
                    self.ore -= geodeRobotOreCost
                    self.obsidian -= geodeRobotObsidianCost
        if self.factory != 'idle':
            if self.factory == 'ore':
                self.oreRobots += 1
            if self.factory == 'clay':
                self.clayRobots += 1
            if self.factory == 'obsidian':
                self.obsidianRobots += 1
            if self.factory == 'geode':
                self.geodeRobots += 1
            self.factory = 'idle'

    def __hash__(self):
        return hash((self.minute, self.ore, self.clay, self.obsidian, self.geodes, self.oreRobots, self.clayRobots, self.obsidianRobots, self.geodeRobots))


calls = 0
def find(state):
    global calls
    calls += 1
    # print(f'Minute {state.minute}: {state.ore} ore, {state.clay} clay, {state.obsidian} obsidian, {state.geodes} geodes')
    if state.minute == 24:
        return state
    # s = copy.copy(state)
    # s.update()
    # best = find(s)
    best = None
    if state.factory == 'idle' and state.minute < 23:
        if state.ore >= geodeRobotOreCost and state.obsidian >= geodeRobotObsidianCost:
            s = copy.copy(state)
            s.update('geode')
            n = find(s)
            if best is None or n.geodes > best.geodes:
                best = n
        elif state.ore >= obsidianRobotOreCost and state.clay >= obsidianRobotClayCost:
            s = copy.copy(state)
            s.update('obsidian')
            n = find(s)
            if best is None or n.geodes > best.geodes:
                best = n
        else:
            s = copy.copy(state)
            s.update()
            n = find(s)
            if best is None or n.geodes > best.geodes:
                best = n
            if state.ore >= oreRobotOreCost and state.oreRobots < oreRobotCount:
                s = copy.copy(state)
                s.update('ore')
                n = find(s)
                if best is None or n.geodes > best.geodes:
                    best = n
            if state.ore >= clayRobotOreCost:
                s = copy.copy(state)
                s.update('clay')
                n = find(s)
                if best is None or n.geodes > best.geodes:
                    best = n
    else:
        s = copy.copy(state)
        s.update()
        best = find(s)
    return best

totalQuality = 0
for fields in inputRE(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'):
    blueprint, oreRobotOreCost, clayRobotOreCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = tuple(map(int, fields))
    best = 0
    oreRobotCount = 1
    while True:
        state = find(State())
        # print(f'Blueprint {blueprint} using max {oreRobotCount} ore robots: {state.geodes}')
        # print(f'{state.oreRobots} ore robots, {state.clayRobots} clay robots, {state.obsidianRobots} obsidian robots, {state.geodeRobots} geode robots')
        # print(state.trail)
        if state.geodes >= best:
            best = state.geodes
            if state.oreRobots == oreRobotCount:
                oreRobotCount += 1
            else:
                break
        else:
            break
    quality = blueprint * best
    print(f'Blueprint {blueprint}: {best} geodes, quality = {quality}')
    totalQuality += quality

print(f'Finished in {timer() - startTime:.3f} seconds')
print(f'Total calls: {calls}')
print(totalQuality)

# 1518 is too low!
# 1534 is too low!
# 1573 is too low!
# 1589 = CORRECT = 1573 + 16 (blueprint 16 has 4 geodes instead of 3 in last solution)
