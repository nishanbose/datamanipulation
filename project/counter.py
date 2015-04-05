#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import csv

count = 0

with open('main_file_nyc.csv') as csvfile:
    headerline = csvfile.next()
    reader = csv.reader(csvfile, delimiter=",")
    #reader = csv.DictReader(csvfile)
    for row in reader[:10]:
        count += 1

print count