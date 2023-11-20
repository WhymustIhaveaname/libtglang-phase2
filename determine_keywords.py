#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import math
from collections import defaultdict
from constants import *
from datautils import *

keywords_number = 1000  # 候选关键词个数
d = defaultdict(int)
count = 0
for text, type29 in read_db():
    if type29 != 22:
        continue
    count += 1
    # text = "".join([c for c in text if c.isascii()])
    text = text.split(' ')
    for t in text:
        d[t] += 1

d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(count)
print([key for key, _ in d[:keywords_number]])
