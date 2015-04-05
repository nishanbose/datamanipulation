#!/usr/bin/env python

""" import math
f h = open("si601_w15_hw1/world_bank_indicators.txt", "r")

 count = 0
 for line in fh:
    count = count + 1
 print 'Line Count:', count


import csv
with open("si601_w15_hw1/world_bank_indicators.txt", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
print d[1][1]


import csv

import math

fileHeader = open("si601_w15_hw1/world_bank_indicators.txt", "rU")

with open("si601_w15_hw1/world_bank_indicators.txt", "rU") as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)

count = 0
line = fileHeader.next()
a = []
for line in fileHeader:
    count = count + 1
    b = d[count][2].replace('"', '')
    b = d[count][2].replace(',', '')
    b = d[count][2].strip()
    if len(b) != 0:
        a.append(d[count][2])

print a
print "\n" + str(count)


import csv

import math

fileHeader = open("si601_w15_hw1/world_bank_indicators.txt", "rU")

line_list = []
line = fileHeader.next()
for line in fileHeader:
    line = line.replace('"', '')
    line = line.replace(',', '')
    line = line.strip().split('\t')
    if len(line) != 0:
        a = int(line[2])
        line_list.append(a)

print sum(line_list)


import csv

import math

with open("si601_w15_hw1/world_bank_indicators.txt", "rU") as f:
    reader = csv.reader(f, delimiter="\t")
    reader.next()
    a = sum(int(x[2]) for x in reader)

print a

import csv

with open("si601_w15_hw1/world_bank_indicators.txt", "rU") as fin:
    headerline = fin.next()
    total = 0
    for row in csv.reader(fin, delimiter="\t"):
        total += int(row[2])
    print total
"""

"""
import csv

import math

fileHeader = open("si601_w15_hw1/world_bank_indicators.txt", "rU")

with open("si601_w15_hw1/world_bank_indicators.txt", "rU") as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
    print d

count = 0
line = fileHeader.next()
a = []

for line in fileHeader:
    count = count + 1
    b = d[count][2].replace(",","")
    if len(b) != 0:
        c = int(b)
        a.append(b)

# print a, count
"""

# open the file containing data for each representative
IN = open('representativesparty.txt', 'rU')

