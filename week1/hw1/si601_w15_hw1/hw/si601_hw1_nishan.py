#!/usr/bin/env python

import math
import csv
from itertools import groupby

IN = open('world_bank_indicators.txt', 'rU')

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

# initiate lists
list_1 = list()

for country in countries:
    t_pop = u_pop = birthrate = 0.0
    pointer_1 = pointer_2 = pointer_3 = 0
    list_t = list()
    for item in step1_list:
        if country == item[0]:
            t_pop += float(item[1].replace('"', '').replace(',', ''))
            pointer_1 += 1
            if item[2] == '':
                continue
            u_pop += float(item[2].replace(',', '').replace('"', ''))
            pointer_2 += 1
            if item[3] == '':
                continue
            birthrate += float(item[3])
            pointer_3 += 1
    list_t.append(country)
    if pointer_1 != 0:
        list_t.append(t_pop / pointer_1)
    if pointer_2 != 0:
        list_t.append(u_pop / pointer_2)
    list_t.append(u_pop / t_pop)
    if pointer_3 != 0:
        list_t.append(birthrate / (1000 * pointer_3))
    list_1.append(list_t)

# initiate lists
list_2 = list()

for item in list_1:
    if len(item) < 5:
        continue
    list_2.append(item)

for item in list_2:
    item[4] = (-1 * math.log(item[4]))

list_3 = sorted(list_2, key=lambda x: x[4], reverse=True)
list_3 = sorted(list_3, key=lambda x: x[3], reverse=True)

list_3.insert(0, ['country name', 'average population',
                  'average urban population', 'average urban population ratio', 'average birthrate'])

output_file = file('si601_hw1_step1_nishan.csv', 'wb')
write = csv.writer(output_file)
write.writerows(list_3)

IN.close()

# Step 2
IN = open('world_bank_regions.txt', 'rU')

region_list = []

for line in IN.readlines():
    line = line.replace('\n', '').split('\t')
    region_list.append(line)

# removing first row
list_3.pop(0)

for item in list_3:
    for word in region_list:
        if str(item[0]) == str(word[2]):
            item.insert(1, word[0])
        else:
            continue
for item in list_3:
    if len(item) < 6:
        item.insert(1, 'No region')
    else:
        continue

list_3.insert(0, ['country name', 'region', 'average population',
                  'average urban population', 'average urban population ratio', 'average birthrate'])

output_file = file('si601_hw1_step2_nishan.csv', 'wb')
write = csv.writer(output_file)
write.writerows(list_3)

IN.close()

# removing first row
list_3.pop(0)

# initiate lists
list_4 = list()

for item in list_3:
    country = str(item[0])
    if str(item[1]) != 'No region':
        region = str(item[1])
    pop = float(item[2])
    _group = (region, (country, pop))
    list_4.append(_group)

list_5 = list()

for key, group in groupby(sorted(list_4), lambda x: x[0]):
    list_4 = list(group)
    list_4 = sorted(list_4, key=lambda x: x[1][1], reverse=True)
    com_data = (list_4[0][0], list_4[0][1][0])
    list_5.append(com_data)

list_5.insert(0, ['region', 'country with highest average population'])
output_file = file('si601_hw1_step3_nishan.csv', 'wb')
write = csv.writer(output_file)
write.writerows(list_5)

output_file.close()
