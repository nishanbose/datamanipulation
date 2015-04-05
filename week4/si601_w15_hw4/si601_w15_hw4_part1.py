#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import json
import sqlite3 as sqlite
import sys

IN = open(r'movie_actors_data.txt', 'rU')

with sqlite.connect('si601_hw4.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS movie_genre")
    cur.execute("DROP TABLE IF EXISTS movies")
    cur.execute("DROP TABLE IF EXISTS movie_actor")
    cur.execute("CREATE TABLE movie_genre(IMDB_ID TEXT, GENRE TEXT)")
    cur.execute("CREATE TABLE movies(IMDB_ID TEXT, TITLE TEXT, YEAR INT, RATING REAL)")
    cur.execute("CREATE TABLE movie_actor(IMDB_ID TEXT, ACTOR TEXT)")

for line in IN:
    # Creatig Common Structures
    jstr = json.loads(line)
    imdbid = jstr['imdb_id'].encode('utf-8')

    # Table 1
    genre = jstr['genres']
    if len(genre) > 0:
        for item in genre:
            cur.execute("INSERT INTO movie_genre VALUES(?,?)", (imdbid, item))

    # Table 2
    title = jstr['title']
    year = jstr['year']
    rating = jstr['rating']
    cur.execute("INSERT INTO movies VALUES(?,?,?,?)", (imdbid, title, year, rating))

    # Table 3
    actor = jstr['actors']
    for item in actor:
        cur.execute("INSERT INTO movie_actor VALUES(?,?)", (imdbid, item))

con.commit()
con.close()

with sqlite.connect('si601_hw4.db') as con2:
    cur2 = con2.cursor()
    cur2.execute("SELECT GENRE FROM movie_genre GROUP BY genre ORDER BY COUNT(GENRE) DESC LIMIT 10")
    row1 = cur2.fetchall()

    cur2.execute("SELECT title, year, rating FROM movie_genre AS G JOIN movies AS M ON (M.imdb_id=G.imdb_id) WHERE G.genre = 'Fantasy' ORDER BY RATING DESC, YEAR DESC")
    row2 = cur2.fetchall()

    cur2.execute("SELECT A.ACTOR, count(g.genre) FROM movie_actor as A JOIN movie_genre as G on (A.IMDB_ID = G.IMDB_ID) WHERE G.GENRE = 'Comedy' GROUP BY A.ACTOR ORDER BY count(g.genre) DESC LIMIT 10")
    row3 = cur2.fetchall()

    cur2.execute("SELECT m1.actor AS first, m2.actor AS second, count(*) AS count FROM movie_actor AS m1 JOIN movie_actor AS m2 ON (m1.imdb_id=m2.imdb_id) WHERE m1.actor < m2.actor GROUP BY m1.actor, m2.actor ORDER BY COUNT DESC LIMIT 20")
    row4 = cur2.fetchall()

con2.close()

# For output to a file
OUT = open('si601_hw4_part1_nishan_output.txt', 'w+')
sys.stdout = OUT

# row1.insert(0, ((u"Top 10 Genres:"),))
print "Top 10 genres:"
for i in row1:
    print i[0]

print
print "Fantasy movies:"
print "Title, Year, Rating"
#row2.insert(0, ((u"Title, Year, Rating"),))
for i in row2:
    print ", ".join([unicode(x).encode('utf-8') for x in i])

print
print "Top 10 most productive comedy actors:"
print "Actor, Movies"
#row3.insert(0, ((u"Actor, Movies"),))
for i in row3:
    print ", ".join([unicode(x).encode('utf-8') for x in i])

print
print "Top 10 most frequent pairs of actors who co-stared in the same movie:"
print "Actor A, Actor B, Co-stared Movies"
# row3.insert(0, ((u"Actor A, Actor B, Co-stared Movies"),))
for i in row4:
    print ", ".join([unicode(x).encode('utf-8') for x in i])

OUT.close()