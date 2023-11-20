#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import math
from collections import defaultdict, Counter
from constants import *
from datautils import *

def determine_keywords():
    keywords_number = 40
    d = defaultdict(int)
    count = 0
    for text, type29 in read_db():
        if type29 != 11:
            continue
        count += 1
        # text = "".join([c for c in text if c.isascii()])
        text = re.split(r"\s|[\W_]+",text)
        for t in text:
            d[t] += 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(count)
    print([(key,_) for key, _ in d[:keywords_number]])
    print([key for key, _ in d[:keywords_number]])

def filter_keywords(keywords):
    keywords = set(keywords)
    maxlen = max(len(word) for word in keywords)
    code_count, text_count = Counter(), Counter()
    code_length, text_length = 0, 0
    for root, dirs, files in os.walk("ml2023-r1-dataset"):
        for filename in files:
            d = Counter()
            filepath = os.path.join(root, filename)
            f = open(filepath, "r", encoding="utf-8")
            for line in f.readlines():
                for i in range(len(line)):
                    for l in range(1, min(maxlen, len(line)-i)+1):
                        if line[i:i+l] in keywords:
                            d[line[i:i+l]] += 1
            if filename.endswith("-OTHER.txt"):
                text_count += d
                text_length += len(line)
            else:
                code_count += d
                code_length += len(line)
            f.close()
    code_frequency = {k: v/code_length for k, v in code_count.items()}
    text_frequency = {k: v/text_length for k, v in text_count.items()}
    frequency_ratio = {}
    for k in keywords:
        if k in code_frequency and k in text_frequency:
            frequency_ratio[k] = code_frequency[k] / text_frequency[k]
        elif k in code_frequency:
            frequency_ratio[k] = float('inf')
        else:
            frequency_ratio[k] = 0
    code_frequency = sorted(code_frequency.items(),
                            key=lambda x: x[1], reverse=True)
    text_frequency = sorted(text_frequency.items(),
                            key=lambda x: x[1], reverse=True)
    frequency_ratio = sorted(frequency_ratio.items(),
                             key=lambda x: x[1], reverse=True)
    # print(code_frequency)
    # print(text_frequency)
    print(frequency_ratio)
    return frequency_ratio

if __name__=="__main__":
    determine_keywords()