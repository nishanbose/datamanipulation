#!/usr/bin/python

# SI601 Winter 2015 Lab 6
# Written by Dr. Yuhang Wang

# Fill in code where specified to compute bigram counts for the input text file.
'''
To run on Fladoop cluster

spark-submit --master yarn-client --queue si601w15 --num-executors 2 --executor-memory 1g --executor-cores 2 si601_w15_lab6.py
'''

import sys, re
from pyspark import SparkContext

sc = SparkContext(appName="PythonBigram")

WORD_RE = re.compile(r"\b[\w']+\b")
input_file = sc.textFile("hdfs:///user/yuhangw/pg1268.txt")

def bigram(line):
    word_list = list(WORD_RE.findall(line))
    bigram_list = []
    for i in range(len(word_list)-1):
        bigram = word_list[i] + " " + word_list[i+1]
        bigram_list.append(bigram)
    return bigram_list

word_counts = input_file.flatMap(lambda line: bigram(line.lower())) \
    .map(lambda word: (word, 1)) \
    .sortByKey(False) \
    .reduceByKey(lambda a, b: a + b)

word_counts_sorted = word_counts.sortBy(lambda x: x[1], ascending=False)

'''
You should get this print out:
of the 2357
in the 970
to the 907
it was 770
on the 719
and the 542
cyrus harding 507
the engineer 494
at the 464
by the 429
'''

# add one line here to save the bigram_counts RDD into HDFS directory 'spark_bigram_output' in your home directory in HDFS
# The saved results must be in TSV format  

word_counts_sorted.map(lambda t:str(t[0]) + "\t" + str(t[1])).saveAsTextFile("spark_bigram_output.tsv")