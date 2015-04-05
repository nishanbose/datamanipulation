# -*- coding: utf-8 -*-

import re

def leading_ending(s):
    str = s
    match1 = re.search(r'(?=^(a|b)).*(?=(e|d)$)', str)
    # match = re.search(r'(function|variable)+[0-9]', s)
    if match1:
        print 'found', match1.group()
    else:
        print 'did not find'

leading_ending('apple')

"""
def finding_usa(s):
    match = re.search(r'USA|\xe7\xbe\x8e\xe5\x9b\xbd\xe4\xba\xba', s)
    if match:
        print 'found'
    else:
        print 'did not find'

finding_usa(u'美国人American'.encode('utf-8'))
"""

"""
def push_up_quality_control(s):
    match = re.search(r'(\s[0-9]).+(\s[0-9]|failed)', s)
    set1 = (match.group(1).strip())
    set2 = (match.group(2).strip())
    if match.group(2) == 'failed':
        print (int(set1), set2)
    elif (int(set1) == 1):
        print 'none'
    else:
        print (int(set1), int(set2))

push_up_quality_control('Pull-up set 1 failed.')
"""

"""
def find_all(s):
    a = s.split(",")
    c = set(a)
    count = 0
    f = list()
    for item in a:
        word = a[count].strip()
        match = re.search(r'^(C|D|E).+\\((blah[0-9]\.txt)|(blah\.txt)|(blah\-blah\_blah)|(blah[0-9]))', word)
        _dict = match.group(1), match.group(2)
        count += 1
        f.append(_dict)
    print f

# wordList = re.sub("[^\w]", " ",  .txt).split()

find_all(r'C:\blah-blah_blah, D:\blah2 , E:\blah3.txt')
"""

