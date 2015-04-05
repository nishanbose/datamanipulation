#!/usr/bin/python

# SI 601 Lab 5
# Partial Credits to Dr. Yuhang Wang

__author__ = 'nishan'

from mrjob.job import MRJob
import re

# Regex for extracting words
word_re = re.compile(r"(\b[\w']+\b)")


class bigram_ratio(MRJob):

    def mapper(self, _, line):
        # Splitting the file by lines
        newline = line.split('\n')

        # Looping through each line
        for l in newline:

            # Extracting words on each line
            word = word_re.findall(l)

            # removing spaces & converting to the right type
            key_ = word[0].strip()  # key word
            value1 = word[1].strip()  # value word
            value2 = int(word[2].strip())  # number of occurances

            # Generating mapped output for reducer.
            yield (key_, (value1, value2) )

    def reducer(self, key, values):

        # initiating variables and lists
        count = 0
        count_list = []
        final_list = []

        # calculating total count value for each key group
        for i in values:
            count_list.append((i[0], i[1]))
            count += i[1]

        # creating a list to be reduced
        for item in count_list:

            w_count = item[1]
            w_bigram = item[0]

            final_list.append([w_bigram, w_count, w_count/float(count)])

            value = sorted(final_list, key=lambda final_list: final_list[2], reverse=True)

        yield(key, value)

if __name__ == '__main__':
    bigram_ratio.run()