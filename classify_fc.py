#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import time
import pickle
import copy
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from tqdm import tqdm
from constants import *
from datautils import *

torch.manual_seed(2023)


class FClassifier(nn.Module):
    def __init__(self, output_size, hidden_size=32):
        super().__init__()
        self.input_size = len(keywords)
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.fc = nn.Sequential(
            nn.Linear(self.input_size, self.hidden_size),
            nn.LeakyReLU(),
            nn.Linear(self.hidden_size, self.output_size),
        )

    def forward(self, x):
        return self.fc(x)


def load_data(ratio=10, elim={}):
    data = read_db()+read_db(table='datasetd1')
    print('totally %d datas' % (len(data)))
    trainset = []
    testset = []
    counter = {i: 0 for i in range(29)}
    for text, type29 in tqdm(data):
        if type29 in elim:
            continue
        counter[type29] += 1
        y = torch.tensor(type29, dtype=torch.long)
        if counter[type29] % ratio == 0:
            testset.append((text2feature2(text), y))
        else:
            trainset.append((text2feature2(text), y))
    print("split into %d train and %d test" % (len(trainset), len(testset)))
    return trainset, testset


def text2feature(text):
    return 'not using'
    x = torch.zeros(len(keywords), dtype=torch.float)
    for i, j in enumerate(keywords):
        x[i] = text.count(j)
    return x


def text2feature2(text):
    """
        k: max length of all keywords
        m: num of keywords
        n: len of text
        time complexity: nk
    """
    x = torch.zeros(len(keywords), dtype=torch.float)
    n = len(text)
    # marks a char has been in keywords or not
    inkws = torch.zeros(n, dtype=torch.bool)
    for l in range(kmax, 0, -1):
        i = 0
        while i <= n-l:
            while i <= n-l and (inkws[i:i+l].any() or text[i:i+l] not in keyword2idx):
                i += 1
            if i > n-l:
                break
            x[keyword2idx[text[i:i+l]]] += 1
            for j in range(i, i+l):
                inkws[j] = True
            i = i+l
    return x


def train_a_model(model, criterion, optimizer, traindl, testdl):
    best_model = None
    best_testscore = 0.0
    for epoch in range(50):
        totloss = 0.0
        totnum = 0
        for inputs, labels in traindl:
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            totloss += loss.item()
            totnum += len(labels)

        traincorr, _ = test(model, traindl)
        testcorr, confusion = test(model, testdl)
        if testcorr >= best_testscore:
            best_testscore = testcorr
            best_model = copy.deepcopy(model)
            print("----new best model!----")
            print('Epoch %2d, Train: %.6f, %.4f; Test: %.4f' % (
                epoch+1, totloss/totnum, traincorr*100, testcorr*100))
            if model.output_size < 3:
                print('\t(test) confusion matrix: %s' % (confusion))
            else:
                confusion = [(idx2lang[i+1], j, k, l)
                             for i, (j, k, l) in enumerate(confusion)]
                confusion.sort(key=lambda x: x[1]+x[2], reverse=True)
                print(confusion[0:10])
    return best_model


def train01():
    model = FClassifier(output_size=2)
    optimizer = optim.Adam(model.parameters(), lr=0.0001, weight_decay=0.0001)

    trainset, testset = load_data()
    with open("datar1d1.pickle", 'wb') as f:
        pickle.dump((trainset, testset), f)
    # with open("datar1d1.pickle", 'rb') as f:
    #     trainset, testset = pickle.load(f)
    eins = torch.tensor(1, dtype=torch.long)
    trainset = [(i, j if j == 0 else eins) for i, j in trainset]
    testset = [(i, j if j == 0 else eins) for i, j in testset]

    weight = [sum(1.0 for j, k in trainset if k == i)
              for i in range(model.output_size)]
    weight = torch.tensor(weight)
    weight = 1/weight
    weight /= weight.sum()
    print("weight", weight)
    criterion = nn.CrossEntropyLoss(weight=weight)

    traindl = DataLoader(dataset=trainset, batch_size=16,
                         shuffle=True, drop_last=True)
    testdl = DataLoader(dataset=testset, batch_size=16, shuffle=False)

    return train_a_model(model, criterion, optimizer, traindl, testdl)


def train28():
    model = FClassifier(output_size=28)
    optimizer = optim.Adam(model.parameters(), lr=0.002, weight_decay=0.002)

    # trainset, testset = load_data(elim={0, })
    # with open("datar1d1code.pickle", 'wb') as f:
    #     pickle.dump((trainset, testset), f)
    with open("datar1d1.pickle", 'rb') as f:
        trainset, testset = pickle.load(f)
    trainset = [(i, j-1) for i, j in trainset if j > 0]
    testset = [(i, j-1) for i, j in testset if j > 0]
    traindl = DataLoader(dataset=trainset, batch_size=16,
                         shuffle=True, drop_last=True)
    testdl = DataLoader(dataset=testset, batch_size=16, shuffle=False)
    print("train data len: %d" % (len(trainset)))

    ignore_lang = torch.tensor(
        [16, 25, 7, 26, 20, 18, 15, 5, 28])  # from OBJ_C to XML
    # weight = [sum(1.0 for j,k in trainset if k==i) for i in range(model.output_size)]
    # weight = torch.tensor(weight)
    # weight = 1/weight
    weight = torch.ones(model.output_size)
    # weight[ignore_lang-1] = 0.0
    # weight/= weight.sum()
    # weight*= model.output_size
    print("weight", weight)
    criterion = nn.CrossEntropyLoss(weight=weight)

    return train_a_model(model, criterion, optimizer, traindl, testdl)


def test(model, dl):
    """
    Best in Phase 1:
        Code/Other Detection: 62.7
        Language Detection: 79.5
    """
    model.eval()
    with torch.no_grad():
        totnum = 0
        corrnum = 0
        # false positive, false negative, totnumber
        confusion = [[0, 0, 0] for i in range(model.output_size)]
        for inputs, labels in dl:
            outputs = model(inputs)
            totnum += len(labels)
            predicted = outputs.argmax(dim=1)
            corrnum += (predicted == labels).sum().item()
            for i in range(model.output_size):
                confusion[i][2] += (labels == i).sum().item()
                confusion[i][0] += torch.logical_and(
                    predicted == i, labels != i).sum().item()
                confusion[i][1] += torch.logical_and(
                    predicted != i, labels == i).sum().item()
    model.train()
    return corrnum/totnum, confusion


def str_repr(word):
    word = repr(word)           # 去掉转义，比如\n
    word = word[1:len(word)-1]  # 去掉转义的同时会把两边的引号显现出来，把它去掉
    if '"' in word or "'" in word:
        i = 0
        while i < len(word):
            if word[i] == '"' or word[i] == "'":
                word = word[:i]+'\\'+word[i:]
                i += 1
            i += 1
    return word


def save_keywords(f):
    f.write("#define KEYWORDLEN %d\n" % (kmax))
    f.write("#define KEYWORDNUM %d\n" % (len(keywords)))
    f.write('const char *keywords_list[]={')
    for i, word in enumerate(keywords):
        f.write('"%s", ' % (str_repr(word)))
        if (i+1) % 10 == 0:
            f.write("\n")
    f.write('};\n')
    # f.write('const char *text_keywords_list[]={')
    # for i,word in enumerate(text_keywords):
    #     f.write('"%s", '%(str_repr(word)))
    #     if (i+1)%10==0:
    #         f.write("\n")
    # f.write('};\n')
    print("wrote keywords to", f)


def save_nn(netname, model, f):
    f.write("#define %s_HIDDENSIZE %d\n" % (netname, model.hidden_size))
    i = 1
    for name, parameters in model.named_parameters():
        numbers = parameters.data.tolist()
        if name.endswith('weight'):
            f.write('const float %s_wt%d[%d][%d] = {' % (
                netname, i, len(numbers), len(numbers[0])))
            for nums in numbers:
                f.write('{'+', '.join([str(num) for num in nums])+'},\n    ')
            f.write('};\n')
        else:
            f.write('const float %s_b%d[%d] = {' % (netname, i, len(numbers)))
            f.write(', '.join([str(num) for num in numbers])+'};\n')
            i += 1
    print("wrote nn parameters to", f)


def check_keyword_freq():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('select file_path,file_text,type29 from datasetr1 where type29>0 and type29<100 order by id limit 100;')
    for file_path, file_text, type29 in c.fetchall():
        print(file_path,type29)
        with open(file_path,'r') as f:
            file_text = f.read()
        print([(j.item(),keywords[i]) for i,j in enumerate(text2feature2(file_text)) if j>0])
        input()


if __name__ == "__main__":
    # stat()
    # trainset,testset = load_data()
    # print(testset[0])
    # check_keyword_freq()
    model01 = train01()
    model28 = train28()
    f = open('parameters.h', 'w')
    save_keywords(f)
    save_nn("net1", model01, f)
    save_nn("net2", model28, f)
    f.close()
