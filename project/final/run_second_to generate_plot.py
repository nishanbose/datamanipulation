#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
from ast import literal_eval

newlist = list()

nycfile = open(r'combined_results.txt', 'rU')
unpack_list = (literal_eval(s) for s in nycfile)
for item in unpack_list:
    newlist.append((item[0],item[2],item[5]))

with open("to_plot.csv", "wb") as nyc_csv:
    nyc_headers = csv.DictWriter(nyc_csv, fieldnames=["Name", "Yelp Rating", "NYC Rating"])
    nyc_headers.writeheader()
    a = csv.writer(nyc_csv, delimiter=',')
    a.writerows(newlist)