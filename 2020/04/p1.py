#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passwd = {}
cnt = 0
for chunk in inputChunks():
    for line in chunk:
        for fieldValue in line.split():
            field = fieldValue.split(':')[0]
            value = fieldValue.split(':')[1]
            passwd[field] = value
    print(passwd)
    valid = True
    for k in required:
        if k not in passwd:
            valid = False
    if valid:
        cnt += 1
    passwd = {}
print(cnt)