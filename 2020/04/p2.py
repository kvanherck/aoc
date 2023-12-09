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
        if int(passwd['byr']) < 1920 or int(passwd['byr']) > 2002:
            valid = False
        if int(passwd['iyr']) < 2010 or int(passwd['iyr']) > 2020:
            valid = False
        if int(passwd['eyr']) < 2020 or int(passwd['eyr']) > 2030:
            valid = False
        h = passwd['hgt']
        if h.endswith('cm'):
            hc = int(h[:-2])
            if hc < 150 or hc > 193:
                valid = False
        elif h.endswith('in'):
            hi = int(h[:-2])
            if hi < 59 or hi > 76:
                valid = False
        else:
            valid = False
        if not re.match('#[0-9a-f]{6}$', passwd['hcl']):
            valid = False
        if passwd['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False
        if not re.match('[0-9]{9}$', passwd['pid']):
            valid = False
    if valid:
        cnt += 1
    passwd = {}
print(cnt)
