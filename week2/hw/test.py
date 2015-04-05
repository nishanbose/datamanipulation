#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import urlparse
import itertools

#q = urlparse('http://www.searchfeed.com/rd/Clk.jsp?s=wf&k=irs&lnk2=rhhE%3F..iy29%27wBAyekxpr%27fsCqvrkh%27pDB.osC.fsCqvrkh%27qAA%3EpAsplhrxDigr%29t%3DH8441%29w%3DV7n3MAk8uNrngqPi1t%3F5RlJVXufmQNuC7lpJignJo5Pavg3OUliBSBScAnVVUBj3kquCw1IodtDBzlBHknjgyNaFD1u11QQh4a3VmQH3MtcOXQSVnx3SLQ4Ls1Tbuo%3FB3BMuc6QcmoiMq64bhak1D8n8q5n76Jf3QO%22%221%7C2%278G&p=12045&sid=383811&ex=1078895006843')

q = urlparse.urlsplit('http://www.searchfeed.com/rd/Clk.jsp?s=wf&k=irs&lnk2=rhhE%3F..iy29%27wBAyekxpr%27fsCqvrkh%27pDB.osC.fsCqvrkh%27qAA%3EpAsplhrxDigr%29t%3DH8441%29w%3DV7n3MAk8uNrngqPi1t%3F5RlJVXufmQNuC7lpJignJo5Pavg3OUliBSBScAnVVUBj3kquCw1IodtDBzlBHknjgyNaFD1u11QQh4a3VmQH3MtcOXQSVnx3SLQ4Ls1Tbuo%3FB3BMuc6QcmoiMq64bhak1D8n8q5n76Jf3QO%22%221%7C2%278G&p=12045&sid=383811&ex=1078895006843')

h = urlparse.parse_qs(q.query)

g = h.items()

d = [item for sublist in g for item in sublist]

z = list()

for item in d:
    if type(item) == str:
        z.append(item)
    else:
        z.append(item[0])

for item in z:
    if len(item) < 255:
        print "okay"
    else:
        print "not okay"

demo = ([len(key) for key, value in h.iteritems()])

print list

url = 'http://www.abcsearch.com/redirect/?affiliate=searchport2&Terms=transsexual&t=uggc%3A%2F%2Feq9.frk.pbz%2Fwf%3FpyvpxVq%5EE02zXI2XYvc&b=%200.01&e=Frk.pbz&abctime=1078979578&hash=1bf7f635214b875463983ecca9af1288'

result = urlparse.urlparse(url)

a = urlparse.parse_qs(result.query)

for k, v in a.items():
    for i in v:
        print i

print "hello"