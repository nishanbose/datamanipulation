#!/usr/bin/env python

import math
import csv
from itertools import groupby

IN = open('si601_w15_hw1/world_bank_indicators.txt', 'rU')

# Step 1

# initiate lists
countries = list()
step1_list = list()

# Skip first line
line = IN.next()

for line in IN:
    line = line.split('\t')
    country = line[0]
    tot_pop = line[9]
    urban_pop = line[10]
    birthrate = line[11]
    countries.append(country)
    countries = sorted(set(countries))
    _group = (country, tot_pop, urban_pop, birthrate)
    _group = list(_group)
    step1_list.append(_group)

newlist = list()

for country in countries:
    totalpopulation = urbanpopulation = birthrate = 0.0
    count1 = count2 = count3 = 0
    temp = list()
    for item in step1_list:
        if country == item[0]:
            totalpopulation += float(item[1].replace('"', '').replace(',', ''))
            count1 += 1
            if item[2] == '':
                continue
            urbanpopulation += float(item[2].replace(',', '').replace('"', ''))
            count2 += 1
            if item[3] == '':
                continue
            birthrate = birthrate + float(item[3])
            count3 += 1
            # print s/float(1000*count)
    temp.append(country)
    if count1 != 0:
        temp.append(totalpopulation / count1)
    if count2 != 0:
        temp.append(urbanpopulation / count2)
    temp.append(urbanpopulation / totalpopulation)
    if count3 != 0:
        temp.append(birthrate / (1000 * count3))
    newlist.append(temp)

newlist2 = list()
for item in newlist:
    if len(item) < 5:
        continue
    newlist2.append(item)

for item in newlist2:
    item[4] = -1 * math.log(item[4])

newlist3 = sorted(newlist2, key=lambda x: x[4], reverse=True)
newlist3 = sorted(newlist3, key=lambda x: x[3], reverse=True)
newlist3.insert(0, ['country name', 'average population',
                    'average urban population', 'average urban population ratio', 'average birthrate'])

output_file = file('si601_hw1_step1_nishan.csv', 'wb')
write = csv.writer(output_file)
write.writerows(newlist3)

IN.close()

# Step 2
IN = open('si601_w15_hw1/world_bank_regions.txt', 'rU')
regions = []
for line in IN.readlines():
    name = line.replace('\n', '').split('\t')
    regions.append(name)

newlist3.pop(0)

for item in newlist3:
    for word in regions:
        if str(item[0]) == str(word[2]):
            item.insert(1, word[0])
        else:
            continue
for item in newlist3:
    if len(item) < 6:
        item.insert(1, 'No region')
    else:
        continue

newlist3.insert(0, ['country name', 'region', 'average population',
                    'average urban population', 'average urban population ratio', 'average birthrate'])

output_file = file('si601_hw1_step2_nishan.csv', 'wb')
write = csv.writer(output_file)
write.writerows(newlist3)

IN.close()

newlist3.pop(0)

test = list()

for item in newlist3:
    country = str(item[0])
    if str(item[1]) != 'No region':
        region = str(item[1])
    pop = float(item[2])
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

output_file.close()
