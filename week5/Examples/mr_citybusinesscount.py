#!/usr/bin/python

# Written by Dr. Yuhang Wang for SI 601
# Sums up the number of local business in each city in Yelp's Academic Dataset
# To run locally:  python mr_citybusinesscount.py yelp_academic_dataset_business.json > citybusinesscount

from mrjob.job import MRJob
import json

class CityBusinessCount(MRJob):

  def mapper(self, _, line):
    data = json.loads(line)
    city = data.get('city')
    if city:
      yield (city, 1)

  def reducer(self, city, counts):
      yield (city, sum(counts))


if __name__ == '__main__':
    CityBusinessCount.run()