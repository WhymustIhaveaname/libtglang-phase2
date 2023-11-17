import os
import math
from collections import defaultdict

l = 20
keywords_number = 200  # 候选关键词个数
N = 3586284  # 总字符数
d = defaultdict(int)
for root, dirs, files in os.walk("ml2023-r1-dataset"):
    for filename in files:
        if filename.endswith("-OTHER.txt"):
            continue
        filepath = os.path.join(root, filename)
        f = open(filepath, "r", encoding="utf-8")
        for line in f.readlines():
            for i in range(len(line)-l+1):
                d[line[i:i+l]] += 1
        f.close()

d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print("length:", l)
print([key for key, _ in d[:keywords_number]])
