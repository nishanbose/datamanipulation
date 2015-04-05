#!/usr/bin/python

# Written by Dr. Yuhang Wang for SI601
# Mapper only job that only keeps data about local business in Ann Arbor
# To run locally:  python mr_cityfilter.py yelp_academic_dataset_business.json > a2businesses

from mrjob.job import MRJob
import json

class CityFilter(MRJob):

  def mapper(self, _, line):
    data = json.loads(line)
    if data['type'] == 'business':
      if data.get('city', '') == 'Ann Arbor':
          yield ('A2', data)

if __name__ == '__main__':
    CityFilter.run()