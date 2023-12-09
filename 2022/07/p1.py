#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

tree = {}
cwd = []
for line in inputLines():
    if line.startswith('$ cd '):
        subdir = line[5:]
        if subdir == '/':
            cwd = []
        elif subdir == '..':
            cwd.pop()
        else:
            cwd.append(subdir)
    elif line.startswith('$ ls'):
        pass
    else:
        size, name = line.split()
        if size != 'dir':
            size = int(size)
            subtree = tree
            for dir in cwd:
                try:
                    subtree = subtree[dir]
                except KeyError:
                    subtree[dir] = {}
                    subtree = subtree[dir]
            subtree[name] = size

total = 0
def treesize(tree, cwd=[]):
    global total
    size = 0
    for name, item in tree.items():
        if isinstance(item, int):
            size += item
        else:
            size += treesize(item, cwd + [name])
    if size <= 100000:
        total += size
    return size

treesize(tree)
print('Total size of dirs <= 100000:', total)
