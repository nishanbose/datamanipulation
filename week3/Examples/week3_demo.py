#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TO DO:
# 1. Grab the page at http://www.themoviedb.org/movie
# 2. Parse the HTML document to get all movie titles on that page
# 3. Save the results in a JSON string and write it to a file

import urllib2
from bs4 import BeautifulSoup
import json

try:
    response = urllib2.urlopen('https://www.themoviedb.org/movie?page=1')
    html = response.read()
except:
    print "Dayuuuum"
    exit()

soup = BeautifulSoup(html)

movielist = []
movielist.append(soup.find(class_="first").a['title'])

for item in soup.find('ul', class_="media_items").find_all(class_="info"):
    movielist.append(item.a.string)

print len(movielist)

json_str = json.dumps(movielist)

print type(json_str)


f = open("movies.json", 'w')
f.write(json_str)
f.close()

IN = open("movies.json", 'rU')
myStr = IN.read()
print myStr
my_movies = json.loads(myStr)
IN.close()

print my_movies