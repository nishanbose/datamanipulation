__author__ = 'nishan'

import sys, re
from pyspark import SparkContext

sc = SparkContext(appName="PythonBigramProb")
WORD_RE = re.compile(r"\b[\w']+\b")

text_file = sc.textFile("hdfs:///user/yuhangw/pg1268.txt")
bigram_input = sc.textFile("hdfs:///user/nishan/si601_w15_hw6_lab6")

word_counts = text_file.flatMap(lambda line: [x.lower() for x in WORD_RE.findall(line)])\
                        .map(lambda x: (str(unicode(x)),1))\
                        .reduceByKey(lambda a, b: a + b)
# add more Spark RDD operators here to compute bigram
sortedwordCounts = word_counts.sortBy(lambda v:v[0])

bigram = bigram_input.map(lambda x: str(unicode(x)))\
                    .map(lambda x: (x.split('\t')[0],x.split('\t')[1]))\
                    .map(lambda x: ( x[0].split('\s')[0] ,  (x[0].split('\s')[1],x[1])  ))

prob = bigram.join(word_counts).map(lambda x: ( x[0],\
                x[1][0][0],\
                x[1][0][1],\
                float(x[1][0][1])/float(x[1][1]) ) )
prob.take(10)
sortedProb = prob.sortBy(lambda x: (x[0],-x[3]) )
sortedProb.take(10)
sortedProb.map(lambda t : t[0] + '\s' + t[1] + '\t' + t[2] + '\t' + str(t[3])).saveAsTextFile('output_si601_nishan_hw6')