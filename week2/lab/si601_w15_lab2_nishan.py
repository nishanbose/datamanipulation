#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Written by Dr. Yuhang Wang for Lab 2 of UMSI SI 601 Winter 2015 class
# A few lines of code are taken from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# You need to fill in code for the function and let it actually return
# the stuff specified

import re

# A. leading and ending letters
# Compile a regular expression to match English words with a leading 'a' or 'b'
# and ends with 'e' or 'd'
# For example:
# leading_ending('apple') should return True
# leading_ending('bad') should return True
# leading_ending('cat') should return False
# leading_ending('be') should return True


def leading_ending(s):
    match = re.search(r'(?=^(a|b)).+(?=(e|d)$)', s)
    if match:
        _result = True
    else:
        _result = False
    return _result


# B. alternate patterns
# Compile a regular expression to match strings that begin with 'variable'
# or 'function' followed by digits
# For example:
# alternate_patterns('variable100') should return True
# alternate_patterns('function2') should return True
# alternate_patterns('variable') should return False because there are no digits after 'variable'
# alternate_patterns('functional40') should return False

def alternate_patterns(s):
    match = re.search(r'(function|variable)+[0-9]', s)
    if match:
        _result = True
    else:
        _result = False
    return _result

# C. Finding the USA
# Given a 8-bit Python string, which is the UTF-8 encoding of some unicode string,
# write a function that returns True if u'美国' (USA in Chinese) or 'USA' is
# found in the unicode string.
# For example:
# finding_usa(u'美国人'.encode('utf-8')) should return True
# finding_usa(u'美国人American'.encode('utf-8')) should return True
# finding_usa('The USA is a great country.') should return True
# finding_usa(u'中美两国'.encode('utf-8')) should return False


def finding_usa(s):
    match = re.search(r'USA|\xe7\xbe\x8e\xe5\x9b\xbd\xe4\xba\xba', s)
    if match:
        _result = True
    else:
        _result = False
    return _result


# D. push_up_quality_control
# Use regular expressions to extract push-up set number and status, which is either
# 'failed' or the number of bad reps found
# For example:
# push_up_quality_control('Push-up set 1 done. Bad rep: 0.') should return (1,0)
# push_up_quality_control('push-up   Set 5 done. bad reps: 3. ') should return (5,3)
# push_up_quality_control("Push-up Set 3 failed.") should return (3,'failed')
# push_up_quality_control("Pull-up set 1 failed.") should return None
# HINT:
# Use re.IGNORECASE for case insensitive matching
# http://docs.python.org/2/library/re.html#re.I
# You may use a couple of regular expressions in this function, or you can use only one
# You may find non-capturing groups handy
# You can use the int() function to convert a string to integer

def push_up_quality_control(s):
    match = re.search(r'(\s[0-9]).+(\s[0-9]|failed)', s)
    set1 = (match.group(1).strip())
    set2 = (match.group(2).strip())
    if (int(set1) == 1) and set2 == 'failed':
        _result = None
    elif set2 == 'failed':
        _result = (int(set1), set2)
    else:
        _result = (int(set1), int(set2))
    return _result

# E. find_all
# Use regular expressions to extract all pairs of drive letter and file name
# from paths on Windows
# For example:
# find_all(r'C:\blah.txt, D:\blah2.txt, E:\blah3.txt') should return [('C', 'blah.txt'), ('D', 'blah2.txt'), ('E', 'blah3.txt')])
# find_all(r'C:\blah.txt , D:\blah2.txt, E:\blah3.txt') should return [('C', 'blah.txt'), ('D', 'blah2.txt'), ('E', 'blah3.txt')])
# find_all(r'C:\blah.txt , D:\blah2.txt, E:\blah3.txt   ') should return [('C', 'blah.txt'), ('D', 'blah2.txt'), ('E', 'blah3.txt')])
# find_all(r'C:\blah-blah_blah, D:\blah2 , E:\blah3.txt') should return [('C', 'blah-blah_blah'), ('D', 'blah2'), ('E', 'blah3.txt')])
# HINT:
# Because '\' is a meta-character in regex, you need to use '\\' to match
# with '\'


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
    return f


#######################################################################
# DO NOT MODIFY ANY CODE BELOW
#######################################################################

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print 'Unit tests:'

    print 'leading_ending'
    test(leading_ending('apple'), True)
    test(leading_ending("bad"), True)
    test(leading_ending("cat"), False)
    test(leading_ending('be'), True)

    print 'alternate_patterns'
    test(alternate_patterns('variable100'), True)
    test(alternate_patterns("function2"), True)
    test(alternate_patterns("variable"), False)
    test(alternate_patterns('functional40'), False)

    print 'finding_usa'
    test(finding_usa(u'美国人'.encode('utf-8')), True)
    test(finding_usa(u'美国人American'.encode('utf-8')), True)
    test(finding_usa('The USA is a great country.'), True)
    test(finding_usa(u'中美两国'.encode('utf-8')), False)

    print 'push_up_quality_control'
    test(push_up_quality_control('Push-up set 1 done. Bad rep: 0.'), (1, 0))
    test(push_up_quality_control(
        'push-up   Set 5 done. bad reps: 3. '), (5, 3))
    test(push_up_quality_control("Push-up Set 3 failed."), (3, 'failed'))
    test(push_up_quality_control("Pull-up set 1 failed."), None)

    print 'find_all'
    test(find_all(r'C:\blah.txt, D:\blah2.txt, E:\blah3.txt'),
         [('C', 'blah.txt'), ('D', 'blah2.txt'), ('E', 'blah3.txt')])
    test(find_all(r'C:\blah.txt , D:\blah2.txt, E:\blah3.txt'),
         [('C', 'blah.txt'), ('D', 'blah2.txt'), ('E', 'blah3.txt')])
    test(find_all(r'C:\blah.txt , D:\blah2.txt, E:\blah3.txt   '),
         [('C', 'blah.txt'), ('D', 'blah2.txt'), ('E', 'blah3.txt')])
    test(find_all(r'C:\blah-blah_blah, D:\blah2 , E:\blah3.txt'),
         [('C', 'blah-blah_blah'), ('D', 'blah2'), ('E', 'blah3.txt')])

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
