#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
from yelpapi import YelpAPI
from collections import defaultdict

key = 'cdKLIdRVUr7vnYnsTWbiIA'
secret = 'gujwKmCVeIRDxB1QiWHCK4FPKiQ'
token = 'npddkfvdPPcQP9JtroXIeo6GaWqPIlWR'
token_secret = 'R9TFAp59AbjY8qtBVs0lwlwww3w'


# NYC
newlist = list()
testlist = list()

count = 0

counter = 0

# def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
#     csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
#     for row in csv_reader:
#         yield [unicode(cell, 'utf-8') for cell in row]

# IN = codecs.open(r'inspect.csv', 'rU', encoding='utf-8')
#
# for line in IN:
#     line = IN.next()
#     line = line.split(",")
#     area = line[2]
#     if area == 'MANHATTAN' or area == 'BROOKLYN' or area == 'QUEENS':
#         name = line[1]
#         #grade = row['GRADE']
#         if line[16]) != 0:
#             score = line[16]
#         zipcode = line[5]
#         area = line[2]
#         if not line[18]:
#             gradedate = line[18]
#         newlist.append([name, score, gradedate, zipcode, area])
#         testlist.append(name)


with open('inspect.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['BORO'] == 'MANHATTAN' or row['BORO'] == 'BROOKLYN' or row['BORO'] == 'QUEENS':
            if row['DBA'].strip():
                name = row['DBA']
            else:
                continue
            #grade = row['GRADE']
            score = row['SCORE']
            zipcode = row['ZIPCODE']
            area = row['BORO']
            gradedate = row['GRADE DATE']
            newlist.append([name, score, gradedate, zipcode, area])
            testlist.append(name)
            count += 1

data = defaultdict(list)

for row in newlist:
    n = row[0]
    s = row[1].strip()
    if len(s) == 0:
        s1 = 0
    else:
        s1 = int(s)
    data[n].append(s1)

avglist = defaultdict(list)

for k, v in data.iteritems():
    avglist[k] = (sum(v) / float(len(v)))

print "hello"

#with open("nyc_filter.csv", "wb") as nyc_csv:
#    npr_headers = csv.DictWriter(nyc_csv, fieldnames=["Name", "Score", "Grade Date", "Zipcode", "Area"])
#    npr_headers.writeheader()
#    a = csv.writer(nyc_csv, delimiter=',')
#    a.writerows(newlist)

#print count

boom = set(testlist)

# YELP
yelp_api = YelpAPI(key, secret, token, token_secret)

OUT = open(r'combined_results.txt', 'w+')

newdict = {}

newcount = 0
counterror = 0

for k, v in avglist.items():
    try:
        search_results = yelp_api.search_query(limit=1, term=k, location='NYC')
        a = search_results['businesses']
        id = a[0]['id']
        name = a[0]['name']
        rating = a[0]['rating']
        rev_count = a[0]['review_count']
        zipcode = a[0]['location']['postal_code']
        nyc_rating = avglist[k]
        test = [id,name,rating,rev_count,zipcode, nyc_rating]
        newcount += 1
        OUT.write("%s\n" % test)
    except:
        counterror += 1
        print counterror
        continue

print newcount

OUT.close()