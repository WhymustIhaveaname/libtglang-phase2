#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sqlite3
from constants import *

db_name = 'ml2023dataset.db'

def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS datasetr1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT,
        file_text TEXT,
        type01 INT,
        type29 INT,
        len  INT
    )''')
    conn.commit()
    conn.close()
    print('inited table datasetr1')

def read_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('select file_text,type29 from datasetr1 where type29>=0 and type29<100 order by id;')
    data = []
    for text,type29 in c.fetchall():
        data.append((text,type29))
    return data

def traverse_folder():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    numfile,numcode = 0,0
    for root,dirs,files in os.walk("ml2023-r1-dataset"):
        for file in files:
            numfile += 1
            file_path = os.path.join(root, file)
            iscode = 1 if file_path.endswith('CODE.txt') else 0
            if iscode:
                numcode += 1
            else:
                assert file_path.endswith('OTHER.txt'), 'file name abnormal: %s'%(file_path)

            with open(file_path,'r') as f:
                file_text = f.read().strip()
            c.execute("INSERT INTO datasetr1 (file_path,file_text,type01,type29,len) VALUES (?,?,?,?,?)",(file_path,file_text,iscode,-1 if iscode else 0,len(file_text)))
    conn.commit()
    conn.close()
    print("there are %d files, among them %s are codes"%(numfile,numcode))

def stat():
    data = read_db()

    types = [0]*29
    for i,j in data:
        types[j] += 1

    types = [(i,j) for i,j in enumerate(types)]
    types.sort(key=lambda x:x[1],reverse=True)
    for i,j in types:
        print("|%11s|%2d|%5d|%.2f%%|"%(idx2lang[i],i,j,j/len(data)*100))

if __name__=="__main__":
    # init_db()
    # traverse_folder()
    # read_db()
    stat()
