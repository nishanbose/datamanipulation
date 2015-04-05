#!/usr/bin/python -tt
print "Hello World! %s" % ('boom')

cool_list = [(1, 2), (3, 4), (5, 6), (0, 0)]


def mykey(y):
    return y[0] + y[1]

print sorted(cool_list, key=mykey)
