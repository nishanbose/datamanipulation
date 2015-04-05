#!/usr/bin/python

# SI 601 Lab 5
# Written by Dr. Yuhang Wang

# Fill in code where specified to compute bigram counts for the input text file.
# To run in local mode on your own computer:
# python si601_w15_lab5.py pg1268.txt > bigram_counts.txt
# To run in local mode on a login node of Fladoop cluster:
# module load python-hadoop/2.7
# python2.7 si601_w15_lab5.py pg1268.txt > bigram_counts.txt
# To run in Hadoop mode on Fladoop cluster:
# First following instruction at http://caen.github.io/hadoop/user-hadoop.html#mrjob to create your
# .mrjob.conf file, use 'si601w15' as queuename.
# Then run
# module load python-hadoop/2.7
# python2.7 si601_w15_lab5.py -r hadoop --no-output hdfs:///user/yuhangw/pg1268.txt -o hdfs:///user/youraccountname/si601lab5_output

from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"\b[\w']+\b")

class BiGramFreqCount(MRJob):

    def mapper(self, _, line):
        word_list = WORD_RE.findall(line)
        for i in range(0, len(word_list)-1):
            bigram = word_list[i].lower() + ' ' + word_list[i+1].lower()
            yield(bigram, 1)

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    BiGramFreqCount.run()