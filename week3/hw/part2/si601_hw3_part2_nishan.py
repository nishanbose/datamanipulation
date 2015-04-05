#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import urllib2
from bs4 import BeautifulSoup
import json
from time import sleep
import re
import csv

def steps():

    # Step 1
    response = urllib2.urlopen('http://www.imdb.com/chart/top')
    html = response.read()
    soup = BeautifulSoup(html)
    OUT1 = open(r'step1.html', 'w')
    OUT1.write(soup.prettify().encode('utf8'))
    OUT1.close()

    # Step 2
    table = soup.find('tbody', class_='lister-list').find_all('tr')

    result = []

    for item in table[:100]:

        imdbid = item.find('td', class_='posterColumn').find('a').get('href')
        idresult = re.search(r'/title/(.+)/', imdbid)

        title = item.find('td', class_='titleColumn').find('a').string
        rating = item.find('td', class_='ratingColumn').find('strong').string

        result.append((idresult.group(1), title, rating))

    # generating output for step2
    OUT2 = open(r'step2.txt', 'w')
    for i in result:
        line = '\t'.join(i)+'\n'
        OUT2.write(unicode(line).encode('utf-8'))
    OUT2.close()

    # Step 3
    apikey = 'de50cb2ce02bd2e2a108470a496be9b5'

    OUT3 = open(r'step3.txt', 'w')
    for item in result:
        imdbid = item[0]
        url = 'http://api.themoviedb.org/3/find/'+imdbid+'?api_key='+apikey+'&external_source=imdb_id'
        response = urllib2.urlopen(url)
        jstr = response.read()
        OUT3.write(imdbid + '\t' + jstr + '\n')
        sleep(5)
    OUT3.close()


    # Step 4
    """
    IN = open(r'step3.txt', 'rU')

    dict_ = {}

    for line in IN:
        line = line.split('\t')
        imdbid = line[0]
        jstr = json.loads(line[1])
        a = jstr['movie_results']
        b = a[0]['vote_average']
        dict_[imdbid] = b

    output = []

    for item in result:
        for k, v in dict_.items():
            if k == item[0]:
                x = item[0], unicode(item[1]).encode('utf-8'), item[2], str(v)
                output.append(x)

    output.insert(0, ('IMDB ID', 'title', 'IMDB rating', 'themoviedb rating'))

    # generating output for step4
    OUT4 = open('step4.csv', 'w')

    with OUT4 as f:
        writer = csv.writer(f)
        writer.writerows(output)

    OUT4.close()
    """

def main():

    steps()



# Calling Main Function

if __name__ == '__main__':
    main()