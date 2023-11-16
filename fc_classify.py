#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import time
import sqlite3
from constants import *
from datautils import *

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
    stat()