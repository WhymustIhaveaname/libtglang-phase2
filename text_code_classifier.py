import os
from collections import Counter
from constants import keywords
from keywords_frequency import keywords_frequency

keywords = {k[0] for k in keywords if k[1] == float('inf')}

text_count, code_count = 0, 0
text_score, code_score = 0, 0

for root, dirs, files in os.walk("ml2023-r1-dataset"):
    for filename in files:
        if filename.endswith("-OTHER.txt"):
            text_count += 1
        else:
            code_count += 1
        filepath = os.path.join(root, filename)
        d = Counter()
        f = open(filepath, "r", encoding="utf-8")
        for line in f.readlines():
            d += Counter(keywords_frequency(line, keywords))
        f.close()
        if d:
            # 认为是代码
            if filename.endswith("-CODE.txt"):
                code_score += 1
        else:
            if filename.endswith("-OTHER.txt"):
                text_score += 1
print(code_score, code_count)
print(text_score, text_count)
