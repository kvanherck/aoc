#!/usr/bin/env python3
import sys
sys.path.append('..')
import functools
import warnings
from common import *

startTime = timer()

cache = {}
calls = 0
hits = 0

def cached(_funcOrEnabled):
    enabled = True
    def decorator(func):
        if not enabled:
            warnings.warn(f"using disabled decorator for '{func.__name__}'")
        @functools.wraps(func)
        def wrapper(pattern, lengths):
            global calls, hits
            calls += 1
            if enabled:
                try:
                    hits += 1
                    return cache[(pattern, tuple(lengths))]
                except KeyError:
                    hits -= 1
            value = func(pattern, lengths)
            cache[(pattern, tuple(lengths))] = value
            return value
        return wrapper

    if type(_funcOrEnabled) is bool:
        enabled = _funcOrEnabled
        return decorator
    else:
        return decorator(_funcOrEnabled)

@cached
def count(pattern, lengths):
    if not lengths:
        if '#' in pattern:
            return 0
        else:
            return 1
    while pattern and pattern[0] == '.':
        pattern = pattern[1:]
    if not pattern and lengths:
        return 0
    if pattern[0] == '#':
        length = lengths[0]
        l = 0
        while pattern and pattern[0] == '#':
            pattern = pattern[1:]
            l += 1
            if l > length:
                return 0
        while l < length:
            if not pattern or pattern[0] == '.':
                return 0
            pattern = pattern[1:]
            l += 1
        if not pattern:
            return count(pattern, lengths[1:])
        else:
            if pattern[0] == '#':
                return 0
            return count(pattern[1:], lengths[1:])
    else:
        n1 = count('.' + pattern[1:], lengths)
        n2 = count('#' + pattern[1:], lengths)
        return n1 + n2

score = 0
for line in inputLines():
    fields = line.split()
    pattern = ','.join([fields[0] for i in range(5)])
    lengths = list(map(int, fields[1].split(','))) * 5
    n = count(pattern, lengths)
    print(line, n)
    score += n

print()
print(f'Finished in {timer() - startTime:.3f} seconds')
print(f'Total calls: {calls}')
print(f'Cache hits: {hits}')
print(f'Cache size: {len(cache)}')
print()
print(score)

# 17788038834082 too low
