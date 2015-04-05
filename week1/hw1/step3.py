#!/usr/bin/env python

# How to
# 1. create a dict containing region, country and population
# 2. find highest 5 population numbers

import csv
import math
from itertools import groupby

"""
line_list = []

fileHeader = open('si601_hw1_step2_nishan.csv', 'rU')
line = fileHeader.next()  # skipping the first header line

for line in fileHeader:
    line = line.strip().split(',')
    info = dict()  # need key and value pairs
    info['region'] = line[1]
    info['country'] = line[0]
    info['highest_avg_pop'] = line[2]
    line_list.append(info)

print line_list
"""

with open("si601_hw1_step2_nishan.csv", "rU") as f:
    headerline = f.next()
    reader = csv.reader(f, delimiter=",")
    d = list(reader)

test = list()

for item in d:
    country = str(item[0])
    if str(item[1]) != 'No region':
        region = str(item[1])
    pop = float(item[2].replace(",", ""))
    combo = (region, (country, pop))
    test.append(combo)

a = list()

for key, group in groupby(sorted(test), lambda x: x[0]):
    test = list(group)
    test = sorted(test, key=lambda x: x[1][1], reverse=True)
    b = (test[0][0], test[0][1][0])
    a.append(b)

a.insert(0, ['region', 'country with highest average population'])
output_file = file('si601_hw1_step3_nishan.csv', 'wb')
write = csv.writer(output_file)
write.writerows(a)

"""
for key, group in groupby(test, lambda x: x[1]):
    listOfThings = " and ".join(["%s" % str(test[0]) for test in group])
    print key + "s:  " + listOfThings + "."

"""
"""
freqs = [(len(list(g)), k) for k, g in groupby(test, lambda x: x[1])]

print freqs

"""
"""
with open("si601_hw1_step2_nishan.csv", "rU") as fin:nishan
    headerline = fin.next()
    total = 0
    for row in csv.reader(fin, delimiter=","):
        print row
"""
