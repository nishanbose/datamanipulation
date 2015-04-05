#!/usr/bin/env python

# open the file containing data for each representative
IN = open('si601_w15_hw1/world_bank_indicators.txt', 'rU')

country = set()

line = IN.next()

info = dict()

for line in IN:
    line = line.replace('"', '')
    line = line.replace(',', '')
    # remove the head and tail spaces and split into list by delimiter '\t'
    line = line.strip().split('\t')
    year = line[1].split('/')
    year = int(year[2])

    info = dict()  # need key and value pairs
    info['country'] = line[0]
    info['date'] = year
    info['population'] = int(line[9])
    info['mobile_sub'] = int(line[4])
    info['health'] = int(line[6])
    info['internetUser'] = int(line[5])
    info['gdp_per_cap'] = int(line[19])
    info['mobile_per_cap'] = float(line[4]) / float(line[9])
    line_list.append(info)

