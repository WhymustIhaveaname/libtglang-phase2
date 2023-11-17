def keywords_frequency(text, keywords):
    if type(keywords) == list:
        keywords = set(keywords)
    k = max(len(word) for word in keywords)
    n = len(text)
    d = dict.fromkeys(keywords, 0)
    # 如果text[i:j]是关键词，那么把inkeywords[i:j]设为True，以后就不考虑他们了
    inkeywords = [False for _ in range(n)]
    for l in range(k, 0, -1):
        i = 0
        while i <= n-l:
            while i <= n-l and (any(inkeywords[j] for j in range(i, i+l)) or text[i:i+l] not in keywords):
                i += 1
            if i > n-l:
                break
            d[text[i:i+l]] += 1
            for j in range(i, i+l):
                inkeywords[j] = True
            i = i+l
    return d
