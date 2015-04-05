#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import json
import sqlite3 as sqlite

IN = open(r'movie_actors_data.txt', 'rU')

with sqlite.connect('test.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS movie_genre")
    cur.execute("CREATE TABLE movie_genre(IMDBID TEXT, GENRE TEXT)")

dict_ = {}

for line in IN:
    jstr = json.loads(line)
    imdbid_ = jstr['imdb_id'].encode('utf-8')
    imdbid_1 = list(str(imdbid_))
    genre_ = jstr['genres']

    for i in genre_:
        a = i.encode('utf-8')
        if not a in dict_:
            dict_[a] = []
            dict_[a].append(imdbid_)
        else:
            dict_[a].append(imdbid_)

for k, v in dict_.items():
    z = ', '.join(v)
    cur.execute("INSERT INTO movie_genre VALUES(?,?)", (k, z))


con.commit()
con.close()
