import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
from collections import defaultdict

__author__ = 'nishan'

newlist = list()
testlist = list()

count = 0

counter = 0

# with open('inspect.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         if row['BORO'] == 'MANHATTAN': #or row['BORO'] == 'BROOKLYN' or row['BORO'] == 'QUEENS':
#
#             if row['DBA'].strip():
#                 name = row['DBA']
#             else:
#                 count += 1
#                 continue
#             #grade = row['GRADE']
#             score = row['SCORE']
#             zipcode = row['ZIPCODE']
#             area = row['BORO']
#             gradedate = row['GRADE DATE']
#             newlist.append([name, score,gradedate, zipcode, area])
#             testlist.append(name)
#             #count += 1
#
# print count
#
# print len(set(testlist))
#
# with open("nyc_filter.csv", "wb") as nyc_csv:
#     npr_headers = csv.DictWriter(nyc_csv, fieldnames=["Name", "Score", "Grade Date", "Zipcode", "Area"])
#     npr_headers.writeheader()
#     a = csv.writer(nyc_csv, delimiter=',')
#     a.writerows(newlist)

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

with open("nyc_avg.csv", "wb") as nyc_csv:
    nyc_headers = csv.DictWriter(nyc_csv, fieldnames=["Name", "Avg Score"])
    nyc_headers.writeheader()
    a = csv.writer(nyc_csv, delimiter=',')
    a.writerows(newlist)
