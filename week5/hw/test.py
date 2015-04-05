__author__ = 'nishan'

from mrjob.job import MRJob
import re

class BiGramAnalyze(MRJob):

    def mapper(self, _, line):
        line = line.replace('"', ' ')
        l = line.split()
        key_word = l[0]
        following_word = l[1]
        single_count = int(l[2])
        gen = (following_word, single_count)
        yield(key_word, gen)


    def reducer(self, key_word, gen):
        total_count = 0
        gen_list = []
        out_list = []
        for item in gen:                      # gen is an iterative,
            gen_list.append((item[0], item[1])) # because it will be exhausted after used once, put out all the values first
            total_count += item[1]
        for ele in gen_list:
            single_count = ele[1]
            following_word = ele[0]
            ratio = float(single_count)/total_count
            out_list.append([following_word, single_count, ratio])
            out = sorted(out_list, key=lambda out_list: out_list[2], reverse=True)
            # lamda works as following:
            # def getkey (out_list): return out_list[2]
        yield(key_word, out)


if __name__ == '__main__':
    BiGramAnalyze.run()