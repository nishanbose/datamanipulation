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
    # Reading and storing HTML responses from IMDB into a file
    response = urllib2.urlopen('http://www.imdb.com/chart/top')
    html = response.read()
    soup = BeautifulSoup(html)

    # Creating a new file
    OUT1 = open(r'step1.html', 'w')

    # Hack for storing unicode characters
    OUT1.write(soup.prettify().encode('utf8'))

    # Closing file
    OUT1.close()

    # Step 2
    # Reading the soup object and extracting specific values

    # Finding the right portion to store in a list
    table = soup.find('tbody', class_='lister-list').find_all('tr')

    # Initiating an empty list
    result = []

    # Iterating through selected list from html response
    for item in table[:100]:

        # Finding URL and extracting ID using regular expression
        imdbid = item.find('td', class_='posterColumn').find('a').get('href')
        idresult = re.search(r'/title/(.+)/', imdbid)

        # Finding title
        title = item.find('td', class_='titleColumn').find('a').string

        # Finding rating
        rating = item.find('td', class_='ratingColumn').find('strong').string

        # Adding to the initiated list
        result.append((idresult.group(1), title, rating))

    # generating output for step2
    OUT2 = open(r'step2.txt', 'w')

    # Iterating through the list of lists
    for i in result:
        # Joining the list and separating by tabs and linebreaks
        line = '\t'.join(i)+'\n'
        # Hack to support unicode
        OUT2.write(unicode(line).encode('utf-8'))
    # Closing file
    OUT2.close()

    # Step 3
    """
    # storing the movie db api key into a variable
    apikey = 'de50cb2ce02bd2e2a108470a496be9b5'

    # Creating a new file for data storage
    OUT3 = open(r'step3.txt', 'w')

    # Iterating thought the data structure created in step 2 to get values from themoviedb
    for item in result:
        # finding the title from the list
        imdbid = item[0]
        # making an api call and storing response
        url = 'http://api.themoviedb.org/3/find/'+imdbid+'?api_key='+apikey+'&external_source=imdb_id'
        response = urllib2.urlopen(url)
        jstr = response.read()
        # writing out to file using tab delimited format
        OUT3.write(imdbid + '\t' + jstr + '\n')
        # added sleep to stay within permitted limits
        sleep(10)

    # Closing file
    OUT3.close()
    """

    # Step 4

    # Opening file created in step 3
    IN = open(r'step3.txt', 'rU')

    # Initiating empty dictionary
    dict_ = {}

    # Iterating through opened file and storing in a data structure
    for line in IN:
        # Splitting line by tab
        line = line.split('\t')
        # Extracting ID
        imdbid = line[0]
        # Extracting JSON and storing into dictionary
        jstr = json.loads(line[1])

        # Storing vote average value in imdbid key
        a = jstr['movie_results']
        b = a[0]['vote_average']
        dict_[imdbid] = b

    # Initiating empty list
    output = []

    # Iterating through list created in step 2
    # Checking for condition if IMDBID matches the dictionary value and storing them  in a list
    for item in result:
        for k, v in dict_.items():
            if k == item[0]:
                x = item[0], unicode(item[1]).encode('utf-8'), item[2], str(v)
                output.append(x)

    # Hack to insert column headings
    output.insert(0, ('IMDB ID', 'title', 'IMDB rating', 'themoviedb rating'))

    # generating output for step 4
    OUT4 = open('step4.csv', 'w')

    # Writing out file using a csv writer
    with OUT4 as f:
        writer = csv.writer(f)
        writer.writerows(output)

    # closing file
    OUT4.close()

# Main Function
def main():

    steps()


# Calling Main Function
if __name__ == '__main__':
    main()