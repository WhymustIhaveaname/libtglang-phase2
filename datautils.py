#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sqlite3
from tqdm import tqdm
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
    c.execute('''CREATE TABLE IF NOT EXISTS datasetd1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT,
        file_text TEXT,
        type01 INT,
        type29 INT,
        len  INT
    )''')
    conn.commit()
    print('inited table')
    conn.close()

def read_db(seglen=512,table='datasetr1'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('select file_text,type29 from %s where type29>=0 and type29<100 order by id;'%(table))
    data = []
    for text,type29 in c.fetchall():
        if type29==0 or len(text)<seglen:
            data.append((text,type29))
        else:
            nseg  = len(text)//seglen + 1
            start = 0
            for _ in range(nseg):
                data.append((text[start:start+seglen],type29))
                start += seglen
    return data

def traverse_folder(dataset="r1"):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    numfile,numcode = 0,0
    for root,dirs,files in os.walk("ml2023-%s-dataset"%(dataset)):
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
            c.execute("INSERT INTO dataset%s (file_path,file_text,type01,type29,len) VALUES (?,?,?,?,?)"%(dataset),(file_path,file_text,iscode,-1 if iscode else 0,len(file_text)))
    conn.commit()
    conn.close()
    print("there are %d files, among them %s are codes"%(numfile,numcode))

def test_libtglang(dataset="r1"):
    cmds = ["cd ./libtglang-tester-r2/build","cmake ..","cmake --build ."]
    os.system(" && ".join(cmds))

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    numfile,numcode = 0,0
    datas = c.execute("select file_path,type01,type29,len from dataset%s where type29>=0 and type29<100;"%(dataset)).fetchall()
    conn.close()
    corr01,corr28 = 0,0
    for file_path,ans01,ans29,length in tqdm(datas):
        numfile += 1
        numcode += ans01
        pred = os.popen("./libtglang-tester-r2/build/tglang-tester ./%s"%(file_path)).read()
        try:
            pred = int(pred.strip().split('\n')[-1])
        except:
            print("error dealing %s (len %d), output is %s"%(file_path,length,pred))
            continue
        if (pred==0)==(ans01==0):
            corr01 += 1
        if ans01>0 and pred==ans29:
            corr28 += 1
    print("numfile, numcode",numfile,numcode)
    print("text/code correct ratio: %.4f"%(corr01/numfile))
    print("code correct ratio: %.4f"%(corr28/numcode))


def stat():
    data = read_db(seglen=1024*1024)+read_db(seglen=1024*1024,table='datasetd1')

    types = [0]*29
    for i,j in data:
        types[j] += 1

    types = [(i,j) for i,j in enumerate(types)]
    types.sort(key=lambda x:x[1],reverse=True)
    for i,j in types:
        print("|%11s|%2d|%5d|%.2f%%|"%(idx2lang[i],i,j,j/len(data)*100))

def count_nonoccr_keyword():
    data = read_db()
    for k in keywords:
        for i,j in data:
            if k in i:
                break
        else:
            print("%s does not occur!"%(k))

if __name__=="__main__":
    # init_db()
    # traverse_folder(dataset='d1')
    # read_db()
    # stat()
    # count_nonoccr_keyword()
    test_libtglang(dataset="d1")
