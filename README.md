# Telegram Machine Learning Contest 2023

The task is to implement a library that detects the programming and markup language of code snippets from message text. [contest link](https://t.me/contest/346)

## Our Method

Our approach is based on word frequency and fully connected neural networks.
We first select about 200 __keywords__, then count the frequency of the keywords in the text.
Then feed this 200-dimension vector into a fully-connection neural network and get the result.

The selection of keywords is done by first selecting many candidates.
We count the frequency of 2-tuple, 3-tuple, ..., and 20-tuple and use the most common 500 words as the candidates.
Then we train a random forest and pick out the __"important"__ ones (there is a defination of 'importance' in random forest methods).
Then we write down the keywords in `constants.py` and never touch it again.

To train the fully connected network, we first label the given dataset and write the result into an SQL database (this is indeed tedious work).
We use the standard routine in PyTorch to train the network.
`classify_fc.py` will write the trained parameters into `parameters.h`, i.e. our model is hard-coded in the .so.
This could make our code super fast.

The complexity of counting the appearance of keywords is O(kn) where n is the length of the text and k is the maximum length of keywords.
The complexity of a neural network is about O(29ml) where 29 is 29 types and m is the number of keywords, l is the number of layers.
We do the matrix multiply by using a for loop.
We believe using BLAS will make the neural network even faster by 200-500 times (because BLAS can take advantage of the vector assemblies).

In the real code, there are 2 neural networks, one is to classify the text into human/codes, and the other will classify which programming language it is.
The reason is that we noticed a huge imbalance in the dataset (see Dataset Properties).
The golden rule in training classifiers is that the ratio #(most common label)/#(most uncommon label) should be smaller than 20.
So we first do a 2-classification, in which the label unbalance is 9:1.
Then we do the 28-classification of programming languages.

The final result is __98.11%__ for code/other classification and __80.47%__ on programming language classification.
The avgeage speed is __1.33ms__ per case (on R7-5800X CPU).
The .so passed test on Fedora33 and Ubuntu20.

## File Descriptions

* `constants.py` is basically `tglang.h`.
* `data_utils.py` loads the dataset into SQLite and reads SQLite out as `[(text, label),...]`, `ml2023dataset.db` is the database it created. It also tests the final `libtglang-tester`
* `determine_keywords.py` outputs keyword candidates using statistics.
* `classify_tree` trains a random forest classifier. This classifier will not be used in C code but help us select important keywords.
* `classify_fc.py` trains the fully-connection classifier and then writes the trained parameters into `parameters.h`.
* `tglang.pyx`,`setup.py`: deprecated. We tried to compile a '.so' directly from Python but failed.

## Todo List

- [x] Wash the dataset and classify them
- [x] Select the keywords candidates by counting the freq of n-tuples.
- [x] Select the keywords using the random forest method.
- [x] Train the neural network using PyTorch.
- [x] Write the trained parameters into C and compile to .so
- [ ] Write the matrix multiplication in BLAS

## Dataset Properties

This time Telegram provided a dataset. There are 21738 text pieces, and among them 1969 are codes. I put them into `ml2023dataset.db`.

The longest human language is 11117; the longest code is 4081. Some very long code ends with '⚠ *message was cropped according to telegram limits!* ⚠'.

We did some simple classification. The languages, their index and #appearing, and the frequency are as follows (sorted by the freq):

|      Lang| ID|Count|Freq|
|----------|---|-----|----|
|      OTHER| 0|41082|91.80%|
|      SHELL|22|  765|1.71%|
|     PYTHON|19|  690|1.54%|
| JAVASCRIPT|11|  400|0.89%|
|       JSON|12|  370|0.83%|
|        C++| 2|  161|0.36%|
|       HTML| 9|  138|0.31%|
|        PHP|17|  134|0.30%|
|          C| 1|  114|0.25%|
|        SQL|24|   98|0.22%|
|       JAVA|10|   96|0.21%|
|       RUST|21|   85|0.19%|
|         C#| 3|   73|0.16%|
| TYPESCRIPT|27|   68|0.15%|
|        LUA|14|   65|0.15%|
|        CSS| 4|   62|0.14%|
|         GO| 8|   60|0.13%|
|     KOTLIN|13|   47|0.11%|
|     DOCKER| 6|   45|0.10%|
|   SOLIDITY|23|   42|0.09%|
|      NGINX|15|   34|0.08%|
|       DART| 5|   29|0.06%|
|        XML|28|   29|0.06%|
|         TL|26|   23|0.05%|
|       RUBY|20|   16|0.04%|
| POWERSHELL|18|   15|0.03%|
|       FUNC| 7|    7|0.02%|
|      SWIFT|25|    4|0.01%|
|OBJECTIVE_C|16|    2|0.00%|

