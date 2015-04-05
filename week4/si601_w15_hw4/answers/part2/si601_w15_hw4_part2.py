#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

# Initial code for SI 601 W15 Homework 4 Part 2
# Partial Credits to Yuhang Wang

import oauth2 as oauth
import json
import pydot
import os

# Twitter API documentation
# https://dev.twitter.com/overview/documentation

# Get access tokens from https://dev.twitter.com/oauth/overview/application-owner-access-tokens
# These are Yuhang's access tokens. Please do not distribute. 
consumer_key = 'eJ8D3x8bY9BeR0oKqQZtewppu'
consumer_secret = 'oHUR60rtACnXAw2xY3Ca5OGXoALQO08oggNUo7hzRIhyG2OxoO'
access_token = '613687133-tjeJnMyY6qupRPItlXJwj2LajXL4ntgh68ZdQsjo'
access_secret = 'V0kiGJJ5FXNOLouj6rwTIlZX5L2obbVM9eIQWhtiNANlU'

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth.Token(key=access_token, secret=access_secret)
client = oauth.Client(consumer, token)

# Get up to 200 tweets on your own home timeline
# Doc: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
header, response = client.request('https://api.twitter.com/1.1/statuses/home_timeline.json?count=200', method="GET")

# print response

############################################################################
# add more code below to
# 1. load the response JSON string into a Python data structure
# 2. a graph in the DOT language using pydot such that if there is a tweet from
# user A, and the tweet mentions users B, C, D, then the directed edges A->B, A->C,
# A->D are added to the graph. Note that self-mentions should not count. 
# The results should be saved in a file like twitter_example_output.dot.
############################################################################

# Loading json into variable
jstr = json.loads(response)

# Initiating graph variable and defining type
graph = pydot.Dot(graph_type='digraph')

# Initiating empty data structure
dict_ = {}

# Iterating through items in json variable
for item in jstr:
    # selecting user mentions from item
    umentions_dict = item['entities']
    umentions = umentions_dict['user_mentions']

    # selecting usernames from item
    uname_dict = item['user']
    uname = uname_dict['screen_name']

    # Checking if number of mentions is more than 1
    if len(umentions) > 1: #and uname != (x for v in umentions for k, x in v.items()):
        # Iterating through user mentions dictionary
        for i in umentions:
            # Selecting user mention
            mention = unicode(i['screen_name']).encode('utf-8')
            # Building dictionary by using username as key and user mentions as list of values
            # Checking username is not equal to user mention
            if uname != mention:
                # continue
                # Checking if key already exists
                if not uname in dict_:
                    dict_[uname] = []
                    dict_[uname].append(mention)
                # Checking if duplicate user mentions are present
                elif mention not in dict_[uname]:
                    dict_[uname].append(mention)

                # Iterating through dictionary items to add edge data
for k, v in dict_.items():
    # Iterating through list of values (user mentions)
    for i in v:
        edge = pydot.Edge(unicode(k).encode('utf-8'), unicode(i).encode('utf-8'))
        edge.set_color("blue")
        graph.add_edge(edge)

# creating dot file for output
graph.write('twitter_output.dot')

# creating pdf output using dot file
#cmd = 'dot -Tps twitter_output.dot -o twitter_output.pdf'
#os.system(cmd)