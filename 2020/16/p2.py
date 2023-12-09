#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
assert len(chunks) == 3

fields = {}
for line in chunks[0]:
    g = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
    name = g[0]
    x = int(g[1])
    y = int(g[2])
    r = list(range(x, y+1))
    x = int(g[3])
    y = int(g[4])
    r += list(range(x, y+1))
    fields[name] = r

print(fields)

n = len(chunks[2][1].split(','))
fieldOptions = [set(fields.keys()) for _ in range(n)]

for line in chunks[2][1:]:
    values = list(map(int, line.split(',')))
    ticket = []
    valid = True
    for i, x in enumerate(values):
        s = set()
        for field, values in fields.items():
            if x in values:
                s.add(field)
        if not s:
            valid = False
        ticket.append(s)
    if valid:
        for i in range(n):
            fieldOptions[i] &= ticket[i]

for i in range(n):
    print(i, fieldOptions[i])

fieldNames = {}
while True:
    done = True
    for i in range(n):
        if len(fieldOptions[i]) == 1:
            field = list(fieldOptions[i])[0]
            fieldNames[i] = field
            for j in range(n):
                if field in fieldOptions[j]:
                    fieldOptions[j].remove(field)
            done = False
            break
    if done:
        break

for i in range(n):
    assert len(fieldOptions[i]) == 0
    print(i, fieldNames[i])

line = chunks[1][1]
myTicket = list(map(int, line.split(',')))

n = 1
for i, name in fieldNames.items():
    if name.startswith('departure'):
        n *= myTicket[i]

print(n)
