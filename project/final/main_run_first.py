#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
from yelpapi import YelpAPI
from collections import defaultdict

# YELP API Access Details
key = 'cdKLIdRVUr7vnYnsTWbiIA'
secret = 'gujwKmCVeIRDxB1QiWHCK4FPKiQ'
token = 'npddkfvdPPcQP9JtroXIeo6GaWqPIlWR'
token_secret = 'R9TFAp59AbjY8qtBVs0lwlwww3w'


# NYC
newlist = list()

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

# YELP
yelp_api = YelpAPI(key, secret, token, token_secret)

OUT = open(r'combined_results.txt', 'w+')

newdict = {}

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
        test = [id, name, rating, rev_count, zipcode, nyc_rating]
        OUT.write("%s\n" % test)
    except:
        continue

OUT.close()