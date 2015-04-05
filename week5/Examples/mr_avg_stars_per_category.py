#!/usr/bin/python

# Written by Dr. Yuhang Wang for SI601
# Calculate the average stars for each business category
# To run locally:  python mr_avg_stars_per_category.py yelp_academic_dataset_business.json > avg_stars_per_category

from mrjob.job import MRJob
import json

class AvgStars(MRJob):

    def mapper(self, _, line):
        data = json.loads(line)
        categories = data.get('categories', None)
        if categories:
            for c in categories:
                stars = data.get('stars', None)
                if stars != None:
                    yield (c, stars)

    def reducer(self, category, stars):
        #    avgstars = sum(stars)/float(len(stars)) # won't work because len() cannot be used on a generator
        l = 0
        s = 0
        for star in stars:
            l = l + 1
            s = s + star

        if l != 0:
            avgstars = s/float(l)
            yield (category, avgstars)


if __name__ == '__main__':
    AvgStars.run()