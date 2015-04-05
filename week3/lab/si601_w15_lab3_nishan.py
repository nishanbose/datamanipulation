#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The above 'magic comment' is to tell Python that this source code will
# contain unicode literals outside of Latin character set.

# Written by Dr. Yuhang Wang for Lab 3 of UMSI SI 601 Winter 2015 class
# A few lines of code are taken from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# You need to fill in code for the function and let it actually return
# the stuff specified

from bs4 import BeautifulSoup
import json, urllib2
import xml.etree.ElementTree as ET

# this is the HTML document used in this lab
html_doc = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
      "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
  <title>Three Little Pigs</title>
  <meta name="generator" content="Amaya, see http://www.w3.org/Amaya/">
</head>

<body>
<p>Once upon a time, there were <a
href="http://en.wikipedia.org/wiki/Three_Little_Pigs">three little pigs</a>:</p>
<ol>
  <li><h2>Pig A</h2>
  </li>
  <li><h2>Pig B</h2>
  </li>
  <li><h2>Pig C</h2>
  </li>
</ol>

<p>And unfortunately, there was a <a
href="http://en.wikipedia.org/wiki/Big_bad_wolf">big bad wolf</a> too.</p>

<p>There are many stories about them.</p>

<h2>Story 1</h2>

<p>This is story 1.</p>

<h2>Story 2</h2>

<p>This is story 2.</p>

<h2>Story 3</h2>

<p>This is story 3.</p>

<h1>Type of Houses Constructed</h1>

<table border="1" style="width: 100%">
  <caption></caption>
  <col>
  <col>
  <tbody>
    <tr>
      <td>Pig</td>
      <td>House Type</td>
    </tr>
    <tr>
      <td>Pig A</td>
      <td>Straw</td>
    </tr>
    <tr>
      <td>Pig B</td>
      <td>Stick</td>
    </tr>
    <tr>
      <td>Pig C</td>
      <td>Brick</td>
    </tr>
  </tbody>
</table>
</body>
</html>
"""

# this is the json string used in this lab
# For example, "apple": [3.0, 0.99] means we bought 3.0 pounds of apples at 0.99 per pound
json_str = '{"apple": [3.0, 1.0], "pear": [2.0, 1.5], "orange": [1.0, 0.9], "star fruit": [2.2, 3.0], "watermelon": [10, 0.2]}'

# this is the XML document used in this lab
xml_doc ='''<?xml version="1.0" encoding="ISO-8859-1"?>
<catalog>
	<cd>
		<title>Empire Burlesque</title>
		<artist sex="male">Bob Dylan</artist>
		<country>USA</country>
		<company>Columbia</company>
		<price>10.90</price>
		<year>1985</year>
	</cd>
	<cd>
		<title>Hide your heart</title>
		<artist sex="female">Bonnie Tyler</artist>
		<country>UK</country>
		<company>CBS Records</company>
		<price>9.90</price>
		<year>1988</year>
	</cd>
	<cd>
		<title>Greatest Hits</title>
		<artist sex="female">Dolly Parton</artist>
		<country>USA</country>
		<company>RCA</company>
		<price>9.90</price>
		<year>1982</year>
	</cd>
	<cd>
		<title>Still got the blues</title>
		<artist sex="male">Gary Moore</artist>
		<country>UK</country>
		<company>Virgin records</company>
		<price>10.20</price>
		<year>1990</year>
	</cd>
	<cd>
		<title>Eros</title>
		<artist sex="male">Eros Ramazzotti</artist>
		<country>EU</country>
		<company>BMG</company>
		<price>9.90</price>
		<year>1997</year>
	</cd>
	<cd>
		<title>One night only</title>
		<artist sex="male">Bee Gees</artist>
		<country>UK</country>
		<company>Polydor</company>
		<price>10.90</price>
		<year>1998</year>
	</cd>
	<cd>
		<title>Sylvias Mother</title>
		<artist sex="male">Dr.Hook</artist>
		<country>UK</country>
		<company>CBS</company>
		<price>8.10</price>
		<year>1973</year>
	</cd>
	<cd>
		<title>Maggie May</title>
		<artist sex="male">Rod Stewart</artist>
		<country>UK</country>
		<company>Pickwick</company>
		<price>8.50</price>
		<year>1990</year>
	</cd>
	<cd>
		<title>Romanza</title>
		<artist sex="male">Andrea Bocelli</artist>
		<country>EU</country>
		<company>Polydor</company>
		<price>10.80</price>
		<year>1996</year>
	</cd>
	<cd>
		<title>When a man loves a woman</title>
		<artist sex="male">Percy Sledge</artist>
		<country>USA</country>
		<company>Atlantic</company>
		<price>8.70</price>
		<year>1987</year>
	</cd>
	<cd>
		<title>Black angel</title>
		<artist sex="mixed">Savage Rose</artist>
		<country>EU</country>
		<company>Mega</company>
		<price>10.90</price>
		<year>1995</year>
	</cd>
	<cd>
		<title>1999 Grammy Nominees</title>
		<artist sex="mixed">Many</artist>
		<country>USA</country>
		<company>Grammy</company>
		<price>10.20</price>
		<year>1999</year>
	</cd>
	<cd>
		<title>For the good times</title>
		<artist sex="male">Kenny Rogers</artist>
		<country>UK</country>
		<company>Mucik Master</company>
		<price>8.70</price>
		<year>1995</year>
	</cd>
	<cd>
		<title>Big Willie style</title>
		<artist sex="male">Will Smith</artist>
		<country>USA</country>
		<company>Columbia</company>
		<price>9.90</price>
		<year>1997</year>
	</cd>
	<cd>
		<title>Tupelo Honey</title>
		<artist sex="male">Van Morrison</artist>
		<country>UK</country>
		<company>Polydor</company>
		<price>8.20</price>
		<year>1971</year>
	</cd>
	<cd>
		<title>Soulsville</title>
		<artist sex="male">Jorn Hoel</artist>
		<country>Norway</country>
		<company>WEA</company>
		<price>7.90</price>
		<year>1996</year>
	</cd>
	<cd>
		<title>The very best of</title>
		<artist sex="male">Cat Stevens</artist>
		<country>UK</country>
		<company>Island</company>
		<price>8.90</price>
		<year>1990</year>
	</cd>
	<cd>
		<title>Stop</title>
		<artist sex="male">Sam Brown</artist>
		<country>UK</country>
		<company>A and M</company>
		<price>19.95</price>
		<year>1988</year>
	</cd>
	<cd>
		<title>Bridge of Spies</title>
		<artist sex="male">T'Pau</artist>
		<country>UK</country>
		<company>Siren</company>
		<price>7.90</price>
		<year>1987</year>
	</cd>
	<cd>
		<title>Private Dancer</title>
		<artist sex="female">Tina Turner</artist>
		<country>UK</country>
		<company>Capitol</company>
		<price>8.90</price>
		<year>1983</year>
	</cd>
	<cd>
		<title>Midt om natten</title>
		<artist sex="male">Kim Larsen</artist>
		<country>EU</country>
		<company>Medley</company>
		<price>7.80</price>
		<year>1983</year>
	</cd>
	<cd>
		<title>Pavarotti Gala Concert</title>
		<artist sex="male">Luciano Pavarotti</artist>
		<country>UK</country>
		<company>DECCA</company>
		<price>9.90</price>
		<year>1991</year>
	</cd>
	<cd>
		<title>The dock of the bay</title>
		<artist sex="male">Otis Redding</artist>
		<country>USA</country>
		<company>Atlantic</company>
		<price>7.90</price>
		<year>1987</year>
	</cd>
	<cd>
		<title>Picture book</title>
		<artist sex="mixed">Simply Red</artist>
		<country>EU</country>
		<company>Elektra</company>
		<price>7.20</price>
		<year>1985</year>
	</cd>
	<cd>
		<title>Red</title>
		<artist sex="male">The Communards</artist>
		<country>UK</country>
		<company>London</company>
		<price>7.80</price>
		<year>1987</year>
	</cd>
	<cd>
		<title>Unchain my heart</title>
		<artist sex="male">Joe Cocker</artist>
		<country>USA</country>
		<company>EMI</company>
		<price>8.20</price>
		<year>1987</year>
	</cd>
</catalog>
'''

# A. get_title (1 point)
# When called in the test coding, the get_title function will be passed the
# HTML document stored in the global variable html_doc. It should return
# the title of the page in a unicode string.
# get_title(html_doc) should return u'Three Little Pigs'
def get_title(html_doc):
    soup = BeautifulSoup(html_doc)
    return soup.title.string


# B. process_json (2 points)
# When called in the test coding, the process_json function will be passed the
# JSON string stored in the global variable json_str. You should implement this
# function such that it will return the total amount money needed to buy the fruits
# stored in json_str.
# process_json(json_str) should return 15.5
def process_json(json_str):
    a = json.loads(json_str)
    total = 0.0
    for k, v in a.items():
        for item in v:
            b = v[0] * v[1]
        total = total + b

    return total


# C. get_pigs (2 points)
# When called in the test coding, the get_pigs function will be passed the
# HTML document stored in the global variable html_doc.
# It should return the three pigs listed below 'there were three little pigs'
# in a JSON string.
# Note that it should return a string, not a list. 
# get_pigs(html_doc) should return '["Pig A", "Pig B", "Pig C"]'
def get_pigs(html_doc):
    soup = BeautifulSoup(html_doc)

    result = []

    for item in soup.find("table").find_all('tr')[1:]:
        b = item.select("td:nth-of-type(1)")
        result.append(str(b[0].string))

    return json.dumps(result)


# D. get_story_headings (2 points)
# When called in the test coding, the get_story_headings function will be passed the
# HTML document stored in the global variable html_doc.
# It should return the three story headings in a JSON string.
# Note that it should return a string, not a list. 
# get_story_headings(html_doc) should return '["Story 1", "Story 2", "Story 3"]'
def get_story_headings(html_doc):
    soup = BeautifulSoup(html_doc)

    result = []

    for item in soup.find_all('h2'):
        if item.parent.name == 'body':
            result.append(item.string)

    return json.dumps(result)


# E. get_houses (2 points)
# When called in the test coding, the get_houses function will be passed the
# HTML document stored in the global variable html_doc.
# It should return information in the house table in a JSON string.
# Note that it should return a string, not a list.
# get_houses(html_doc) should return '[["Pig A", "Straw"], ["Pig B", "Stick"], ["Pig C", "Brick"]]'
# HINT: contruct a list of tuples first, and then convert it to a JSON string.
def get_houses(html_doc):
    soup = BeautifulSoup(html_doc)

    result_1 = []

    for item in soup.find('table').find_all('tr')[1:]:
        result_2 = []
        b = item.select("td")
        for i in b:
            result_2.append(str(i.string))
        result_1.append(result_2)

    return json.dumps(result_1)


# F. get_links (2 points)
# When called in the test coding, the get_links function will be passed the
# HTML document stored in the global variable html_doc.
# It should return all url links in the page in a JSON string.
# Note that it should return a string, not a list.
# get_links(html_doc) should return '["http://en.wikipedia.org/wiki/Three_Little_Pigs", "http://en.wikipedia.org/wiki/Big_bad_wolf"]'
def get_links(html_doc):
    soup = BeautifulSoup(html_doc)

    result = []

    for item in soup.find_all('a'):
        link = item.get('href')
        result.append(link)

    return json.dumps(result)


# G. treasure_hunting (3 points)
# The treasure_hunting function should first visit http://www.example.com, and
# then find the only url link on that page, and then visit that url link.
# On this page, there is a table under 'Test IDN top-level domains'. In the first
# column (Domain), there are a list of foreign characters.
# I want you to fetch the content of the cell in column 1 and row 3, and return it
# in a unicode string.
# treasure_hunting() should return u'测试'
def treasure_hunting():
    response = urllib2.urlopen('http://example.com')
    html = response.read()
    soup = BeautifulSoup(html)

    result = soup.find('a')
    result = result.get('href')

    response_final = urllib2.urlopen(result)
    html_1 = response_final.read()
    soup_1 = BeautifulSoup(html_1)

    result_2 = soup_1.find('table', class_='iana-table').find('tbody')

    row = result_2.find_all('tr')[2]
    data = row.find_all('td')[0]

    return data.string


# H. get_last_title (1 point)
# The get_last_title function will be passed a string containing the XML document
# in the file 'cd_catalog.xml', and it should return the title of the last CD as
# a string.
def get_last_title(xmlstr):
    root = ET.fromstring(xmlstr)
    query = root.findall("./cd/title")

    for item in query:
        result = item.text

    return result


# I. find_first_girl (1 point)
# The find_first_girl function will be passed a string containing the XML document
# in the file 'cd_catalog.xml', and it should return the name of the first female
# artist
def find_first_girl(xmlstr):
    root = ET.fromstring(xmlstr)

    result = root.find(".//artist[@sex='female']")

    return result.text


# J. find_most_pricy (2 points)
# The find_most_pricy function will be passed a string containing the XML document
# in the file 'cd_catalog.xml', and it should return the price of the most expensive
# CD as a float value
def find_most_pricy(xmlstr):
    root = ET.fromstring(xmlstr)
    query = root.findall('.//price')

    max_price = 0.0

    for item in query:
        if max_price < float(item.text):
            max_price = float(item.text)

    return max_price


# K. get_uk_artists (2 points)
# The get_uk_artists function will be passed a string containing the XML document
# in the file 'cd_catalog.xml', and it should return a list of all UK artists in
# alphabetical order
def get_uk_artists(xmlstr):
    root = ET.fromstring(xmlstr)
    query = root.findall('.//cd')

    result = []

    for item in query:
        q = item.find('country')
        if q.text == 'UK':
            name = item.find('artist').text
            result.append(name)

    return sorted(result)


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

def test2(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, got, expected)

# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'get_title'

  test(get_title(html_doc), u'Three Little Pigs')
  
  print 'process_json'

  test(process_json(json_str), 15.5)

  print 'get_pigs'

  test(get_pigs(html_doc),  '["Pig A", "Pig B", "Pig C"]' )
  
  print 'get_story_headings'

  test(get_story_headings(html_doc),  '["Story 1", "Story 2", "Story 3"]' )

  print 'get_houses'

  test(get_houses(html_doc), '[["Pig A", "Straw"], ["Pig B", "Stick"], ["Pig C", "Brick"]]')

  print 'get_links'

  test(get_links(html_doc), '["http://en.wikipedia.org/wiki/Three_Little_Pigs", "http://en.wikipedia.org/wiki/Big_bad_wolf"]')

  print 'treasure_hunting'

  test2(treasure_hunting(), u'测试')
  
  print 'get_last_title'
  test(get_last_title(xml_doc), 'Unchain my heart')

  print 'find_first_girl'
  test(find_first_girl(xml_doc), 'Bonnie Tyler')

  print 'find_most_pricy'
  test(find_most_pricy(xml_doc), 19.95 )

  print 'get_uk_artists'
  test(get_uk_artists(xml_doc),  ['Bee Gees', 'Bonnie Tyler', 'Cat Stevens', 'Dr.Hook', 'Gary Moore', 'Kenny Rogers', 'Luciano Pavarotti', 'Rod Stewart', 'Sam Brown', "T'Pau", 'The Communards', 'Tina Turner', 'Van Morrison'] )

  
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()