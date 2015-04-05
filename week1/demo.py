#!/usr/bin/python -tt
print "Hello World!"

cool_list=[(1,2),(3,4),(5,6),(0,0)]
print sorted(cool_list,key=lambda x:x[0] +x[1])
