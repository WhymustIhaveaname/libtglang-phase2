# Telegram Machine Learning Contest 2023

The task is to implement a library that detects the programming and markup language of code snippets from message text. [contest link](https://t.me/contest/346)

## Dataset Properties

This time telegram provided a dataset. There are 21738 text pieces and among them 1969 are codes. I put them into `ml2023dataset.db`.

The longest human language is 11117; the longest code is 4081. Some very long code end with '⚠ *message was cropped according to telegram limits!* ⚠'.

We did some simple classification. The languages, its index and #appearing and the frequency are as follows (sort by the freq):

|Language   |idx |count|freq|
|-----------|----|-----|----|
|      OTHER| 0|19769|91.56%|
|      SHELL|22|  386|1.79%|
|     PYTHON|19|  344|1.59%|
| JAVASCRIPT|11|  201|0.93%|
|       JSON|12|  159|0.74%|
|        C++| 2|   72|0.33%|
|          C| 1|   69|0.32%|
|       HTML| 9|   69|0.32%|
|        PHP|17|   68|0.31%|
|       RUST|21|   49|0.23%|
|       JAVA|10|   47|0.22%|
|        SQL|24|   42|0.19%|
|        CSS| 4|   40|0.19%|
|        LUA|14|   37|0.17%|
| TYPESCRIPT|27|   35|0.16%|
|         C#| 3|   34|0.16%|
|     KOTLIN|13|   27|0.13%|
|         GO| 8|   25|0.12%|
|   SOLIDITY|23|   23|0.11%|
|      NGINX|15|   22|0.10%|
|       DART| 5|   15|0.07%|
|        XML|28|   14|0.06%|
|     DOCKER| 6|   13|0.06%|
|         TL|26|   13|0.06%|
|       FUNC| 7|    5|0.02%|
|       RUBY|20|    5|0.02%|
| POWERSHELL|18|    4|0.02%|
|      SWIFT|25|    3|0.01%|
|OBJECTIVE_C|16|    2|0.01%|

