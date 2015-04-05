#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json, urllib2

response = urllib2.urlopen('http://python.org/')
html = response.read()

soup = BeautifulSoup(html)

print "hello"
