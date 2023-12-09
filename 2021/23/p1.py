#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import heapq

#############
#0123456789X# hallway[i]
###0#1#2#3### rooms[i][1]
  #0#1#2#3#   rooms[i][0]
  #########

# input:     13558 2.27s  97084
# example1:  12521 0.23s  10882

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

def score(rooms):
    s = 0
    for i in range(4):
        if rooms[i][0] == expected[i]:
            s += 1
            if rooms[i][1] == expected[i]:
                s += 1
    return s

def heuristic(rooms, hallway):
    s = 0
    for i in range(4):
        if rooms[i][0] is not None and rooms[i][0] != expected[i]:
            j = destination[rooms[i][0]]
            s += moveCost[rooms[i][0]] * (3 + abs(i - j) * 2)
        if rooms[i][1] is not None and rooms[i][1] != expected[i]:
            j = destination[rooms[i][1]]
            s += moveCost[rooms[i][1]] * (2 + abs(i - j) * 2)
    for i in range(11):
        if hallway[i] is not None:
            j = destination[hallway[i]] * 2 + 2
            s += moveCost[hallway[i]] * (1 + abs(i - j))
    return s

def processRooms(rooms, hallway, cost):
    moves = set()
    for i in range(4):
        room = rooms[i]
        if room[1] is not None:
            if room[0] != expected[i] or room[1] != expected[i]:
                new = list(rooms)
                new[i] = (room[0], None)
                moves |= moveFrom(tuple(new), hallway, i*2+2, room[1], cost + moveCost[room[1]])
        elif room[0] is not None:
            if room[0] != expected[i]:
                new = list(rooms)
                new[i] = (None, None)
                moves |= moveFrom(tuple(new), hallway, i*2+2, room[0], cost + moveCost[room[0]]*2)
    return moves

def processHallway(rooms, hallway, cost):
    moves = set()
    if hallway[0] is not None and hallway[1] is None:
        new = list(hallway)
        new[0] = None
        moves |= moveFrom(rooms, tuple(new), 1, hallway[0], cost + moveCost[hallway[0]])
    for i in (1, 3, 5, 7, 9):
        if hallway[i] is not None:
            new = list(hallway)
            new[i] = None
            moves |= moveFrom(rooms, tuple(new), i, hallway[i], cost)
    if hallway[10] is not None and hallway[9] is None:
        new = list(hallway)
        new[10] = None
        moves |= moveFrom(rooms, tuple(new), 9, hallway[10], cost + moveCost[hallway[10]])
    return moves

def moveFrom(rooms, hallway, pos, value, cost):
    moves = set()
    i = pos
    while i > 0:
        i -= 1
        if hallway[i] is not None:
            break
        if i in (2, 4, 6, 8):
            moves |= tryRoom(rooms, hallway, i // 2 - 1, value, cost + moveCost[value]*(pos - i))
        else:
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
        else:
            new = list(hallway)
            new[i] = value
            moves.add((cost + moveCost[value]*(i - pos), rooms, tuple(new)))
    return moves

def tryRoom(rooms, hallway, i, value, cost):
    moves = set()
    if value != expected[i]:
        return moves
    if rooms[i][1] is not None:
        return moves
    if rooms[i][0] is None:
        new = list(rooms)
        new[i] = (value, None)
        moves.add((cost + moveCost[value]*2, tuple(new), hallway))
    elif rooms[i][0] == expected[i]:
        new = list(rooms)
        new[i] = (value, value)
        moves.add((cost + moveCost[value], tuple(new), hallway))
    return moves

def printPositions(rooms, hallway):
    s = ['.' if x is None else x for x in hallway]
    print(''.join(s))
    r = ['.' if x[1] is None else x[1] for x in rooms]
    print(f'  {r[0]} {r[1]} {r[2]} {r[3]}')
    r = ['.' if x[0] is None else x[0] for x in rooms]
    print(f'  {r[0]} {r[1]} {r[2]} {r[3]}')
    print()

def dijkstra(rooms, hallway):
    cnt = 0
    visited = set()
    queue = [(0, 0, cnt, rooms, hallway)]
    while True:
        f, cost, _, rooms, hallway = heapq.heappop(queue)
        if (rooms, hallway) in visited:
            continue
        print(len(visited), score(rooms), f, cost)
        moves = processRooms(rooms, hallway, cost)
        moves |= processHallway(rooms, hallway, cost)
        s = score(rooms)
        for c, r, h in moves:
          if (r, h) not in visited:
              if score(r) > s:
                  cnt += 1
                  g = heuristic(r, h)
                  heapq.heappush(queue, (c+g, c, cnt, r, h))
                  moves = []
                  break
        for c, r, h in moves:
            if (r, h) not in visited:
                cnt += 1
                g = heuristic(r, h)
                heapq.heappush(queue, (c+g, c, cnt, r, h))
        visited.add((rooms, hallway))
        if score(rooms) == 8:
            print(f'Finished after {cnt} iterations')
            return cost

lines = list(inputLines(stripWhitespace=False))
assert len(lines) == 5
row0 = lines[1][1:12]
row0 = [None if x == '.' else x for x in row0]
row1 = lines[2][3:11:2]
row1 = [None if x == '.' else x for x in row1]
row2 = lines[3][3:11:2]
row2 = [None if x == '.' else x for x in row2]

hallway = tuple(row0)
rooms = tuple([(row2[i], row1[i]) for i in range(4)])
printPositions(rooms, hallway)
start = timer()
print(dijkstra(rooms, hallway))
print(f'Finished in {timer() - start}s')
