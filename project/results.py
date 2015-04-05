#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
from ast import literal_eval
from collections import defaultdict


__author__ = 'nishan'

# Read filter and create averages
data = defaultdict(list)

for i, row in enumerate(csv.reader(open('nyc_filter.csv', 'rU'))):
    if not i or not row:
        continue
    n = row[0]
    s = row[1].strip()
    if len(s) == 0:
        s1 = 0
    else:
        s1 = int(s)
    data[n].append(s1)

newlist = list()

for k, v in data.iteritems():
    newlist.append((k, sum(v) / float(len(v))))

count = 0

OUT = open(r'match.txt', 'w+')

nycfile = open(r'random.txt', 'rU')
unpack_list = (literal_eval(s) for s in nycfile)
for item in unpack_list:
    for i in newlist:
        if item[1].lower() == i[0].lower():
            count += 1
        else:
            a = [item[1], i[0]]
            OUT.write("%s\n" % a)

print count