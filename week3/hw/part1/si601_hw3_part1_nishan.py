#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created for SI601 - Homework Assignment 3 - Part 1
Partial Credits to GSI Ming Jiang for code
"""

__author__ = 'nishan'

import xml.etree.ElementTree as ET

# Parsing XML file into variable
tree = ET.parse('Rom.xml')
root = tree.getroot()

# Defining Namespaces
namespace1 = '{http://www.tei-c.org/ns/1.0}'
namespace2 = '{http://www.w3.org/XML/1998/namespace}'

# Creating output file
OUT1 = open('si601_hw3_part1_nishan_output.txt', 'w+')

# Iterating through all matching elements
for item in root.iter(namespace1 + 'milestone'):

    # Skipping invalid entries
    if item.attrib[namespace2 + 'id'].startswith("ms") or item.attrib[namespace2 + 'id'].startswith("stz") or item.attrib['n'].startswith("2.CH") or item.attrib['n'].startswith("P"):
         continue
    output = item.attrib['n'] + '\t' + item.attrib[namespace2 + 'id']

    # Writing out to file
    OUT1.write(output+'\n')

# Closing file
OUT1.close()


