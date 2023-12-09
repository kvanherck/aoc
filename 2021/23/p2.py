#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import heapq

#############
#0123456789X# hallway[i]
###0#1#2#3### rooms[i][3]
  #0#1#2#3#   rooms[i][2]
  #0#1#2#3#   rooms[i][1]
  #0#1#2#3#   rooms[i][0]
  #########

# input:     56982 10.2s
# example1:  44169 5.4s

expected = 'ABCD'
destination = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}

moveCost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

scoreCache = {}
def score(rooms):
    try:
        return scoreCache[rooms]
    except KeyError:
        pass
    s = 0
    for i in range(4):
        for k in range(4):
            if rooms[i][k] == expected[i]:
                s += 1
            else:
                break
    scoreCache[rooms] = s
    return s

heuristicCache = {}
def heuristic(rooms, hallway):
    try:
        return heuristicCache[(rooms, hallway)]
    except KeyError:
        pass
    s = 0
    for i in range(4):
        for k in range(4):
            x = rooms[i][k]
            if x is not None and x != expected[i]:
                j = destination[x]
                s += moveCost[x] * (5 - k + abs(i - j) * 2)
    for i in range(11):
        if hallway[i] is not None:
            j = destination[hallway[i]] * 2 + 2
            s += moveCost[hallway[i]] * (1 + abs(i - j))
    heuristicCache[(rooms, hallway)] = s
    return s

leaveCache = {}
def mayLeave(rooms, i):
    try:
        return leaveCache[(rooms, i)]
    except KeyError:
        pass
    for k in range(4):
        if rooms[i][k] is not None and rooms[i][k] != expected[i]:
            leaveCache[(rooms, i)] = True
            return True
    leaveCache[(rooms, i)] = False
    return False

enterCache = {}
def mayEnter(rooms, i):
    try:
        return enterCache[(rooms, i)]
    except KeyError:
        pass
    for k in range(4):
        if rooms[i][k] is not None and rooms[i][k] != expected[i]:
            enterCache[(rooms, i)] = False
            return False
    enterCache[(rooms, i)] = True
    return True

def processRooms(rooms, hallway, cost):
    moves = set()
    for i in range(4):
        if mayLeave(rooms, i):
            room = rooms[i]
            for k in [3, 2, 1, 0]:
                if room[k] is not None:
                    newRoom = list(room)
                    newRoom[k] = None
                    new = list(rooms)
                    new[i] = tuple(newRoom)
                    moves |= moveFrom(tuple(new), hallway, i*2+2, room[k], cost + moveCost[room[k]] * (4-k), True)
                    break
    return moves

def processHallway(rooms, hallway, cost):
    moves = set()
    if hallway[0] is not None and hallway[1] is None:
        new = list(hallway)
        new[0] = None
        moves |= moveFrom(rooms, tuple(new), 1, hallway[0], cost + moveCost[hallway[0]], False)
    for i in (1, 3, 5, 7, 9):
        if hallway[i] is not None:
            new = list(hallway)
            new[i] = None
            moves |= moveFrom(rooms, tuple(new), i, hallway[i], cost, False)
    if hallway[10] is not None and hallway[9] is None:
        new = list(hallway)
        new[10] = None
        moves |= moveFrom(rooms, tuple(new), 9, hallway[10], cost + moveCost[hallway[10]], False)
    return moves

def moveFrom(rooms, hallway, pos, value, cost, allowHallway):
    moves = set()
    i = pos
    while i > 0:
        i -= 1
        if hallway[i] is not None:
            break
        if i in (2, 4, 6, 8):
            moves |= tryRoom(rooms, hallway, i // 2 - 1, value, cost + moveCost[value]*(pos - i))
        elif allowHallway:
            new = list(hallway)
            new[i] = value
            moves.add((cost + moveCost[value]*(pos - i), rooms, tuple(new)))
    i = pos
    while i < 10:
        i += 1
        if hallway[i] is not None:
            break
        if i in (2, 4, 6, 8):
            moves |= tryRoom(rooms, hallway, i // 2 - 1, value, cost + moveCost[value]*(i - pos))
        elif allowHallway:
            new = list(hallway)
            new[i] = value
            moves.add((cost + moveCost[value]*(i - pos), rooms, tuple(new)))
    return moves

def tryRoom(rooms, hallway, i, value, cost):
    moves = set()
    if value != expected[i]:
        return moves
    if not mayEnter(rooms, i):
        return moves
    for k in range(4):
        if rooms[i][k] is None:
            newRoom = list(rooms[i])
            newRoom[k] = value
            new = list(rooms)
            new[i] = tuple(newRoom)
            moves.add((cost + moveCost[value]*(4-k), tuple(new), hallway))
            return moves
    return moves

def printPositions(rooms, hallway):
    s = ['.' if x is None else x for x in hallway]
    print(''.join(s))
    for j in [3, 2, 1, 0]:
        r = ['.' if x[j] is None else x[j] for x in rooms]
        print(f'  {r[0]} {r[1]} {r[2]} {r[3]}')
    print()

def dijkstra(rooms, hallway):
    cnt = 0
    visited = set()
    queue = [(0, 0, cnt, rooms, hallway, None, None)]
    trail = {}
    while True:
        f, cost, _, rooms, hallway, pr, ph = heapq.heappop(queue)
        if (rooms, hallway) in visited:
            continue
        print(len(visited), score(rooms), f, cost)
        trail[(rooms, hallway)] = (pr, ph)
        moves = processRooms(rooms, hallway, cost)
        moves |= processHallway(rooms, hallway, cost)
        s = score(rooms)
        for c, r, h in moves:
          if (r, h) not in visited:
              if score(r) > s:
                  cnt += 1
                  g = heuristic(r, h)
                  heapq.heappush(queue, (c+g, c, cnt, r, h, rooms, hallway))
                  moves = []
                  break
        for c, r, h in moves:
            if (r, h) not in visited:
                cnt += 1
                g = heuristic(r, h)
                heapq.heappush(queue, (c+g, c, cnt, r, h, rooms, hallway))
        visited.add((rooms, hallway))
        if score(rooms) == 16:
            print(f'Finished after {cnt} iterations')
            while rooms is not None:
                printPositions(rooms, hallway)
                rooms, hallway = trail[(rooms, hallway)]
            return cost

lines = list(inputLines(stripWhitespace=False))
assert len(lines) == 5
row0 = lines[1][1:12]
row0 = [None if x == '.' else x for x in row0]
row1 = lines[2][3:11:2]
row1 = [None if x == '.' else x for x in row1]
row2 = ['D', 'C', 'B', 'A']
row3 = ['D', 'B', 'A', 'C']
row4 = lines[3][3:11:2]
row4 = [None if x == '.' else x for x in row4]
hallway = tuple(row0)
rooms = tuple([(row4[i], row3[i], row2[i], row1[i]) for i in range(4)])
printPositions(rooms, hallway)

start = timer()
print(dijkstra(rooms, hallway))
print(f'Finished in {timer() - start}s')
