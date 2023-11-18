#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import time
import torch
import pickle
import graphviz
from tqdm import tqdm
from constants import *
from datautils import *

from catboost import CatBoostClassifier,Pool

def load_data(ratio=10):
    data = read_db()
    print('totally %d datas'%(len(data)))
    trainset = []
    testset = []
    counter = {i:0 for i in range(29)}
    for text,type29 in tqdm(data):
        counter[type29] += 1
        if counter[type29]%ratio == 0:
            testset.append((text2feature2(text),torch.tensor(type29,dtype=torch.long)))
        else:
            trainset.append((text2feature2(text),torch.tensor(type29,dtype=torch.long)))
    print("split into %d train and %d test"%(len(trainset),len(testset)))
    return trainset,testset

def text2feature2(text):
    """
        k: max length of all keywords
        m: num of keywords
        n: len of text
        time complexity: nk
    """
    x = torch.zeros(len(keywords),dtype=torch.float)
    n = len(text)
    inkws = torch.zeros(n,dtype=torch.bool) # marks a char has been in keywords or not
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

def train01():
    model = CatBoostClassifier(iterations=1,
                           learning_rate=0.5,
                           depth=3,
                           #loss_function='MultiClass',  # 使用多类别的损失函数
                           #verbose=True
                           )

    # trainset,testset = load_data()
    # with open("loaded_data.pickle",'wb') as f:
    #     pickle.dump((trainset,testset),f)
    with open("loaded_data.pickle",'rb') as f:
        trainset,testset = pickle.load(f)
    print('human ratio:',sum(1 for i in trainset if i[1]==0)/len(trainset))
    ptrain = Pool([i[0] for i in trainset],label=[0 if i[1]==0 else 1 for i in trainset])
    ptest  = Pool([i[0] for i in testset],label=[0 if i[1]==0 else 1 for i in testset])
    model.fit(ptrain,eval_set=ptest)
    print(model.get_all_params())
    test(model,trainset)
    test(model,testset)
    print("tree count after train",model.tree_count_)

    graph = model.plot_tree(tree_idx=0)
    graph.view()

    #print(model.get_feature_importance(data=ptrain))

def test(model,dataset):
    """
    Best in Phase 1:
    Code/Other Detection: 62.7
    Language Detection: 79.5
    """
    totnum  = len(dataset)
    predicted = torch.tensor(model.predict([i[0] for i in dataset])).flatten()
    labels    = torch.tensor([i[1] for i in dataset])
    detect01  = ((predicted==0)==(labels==0)).sum().item()/totnum
    detect29  = (predicted==labels).sum().item()/totnum
    print("code/human correct ratio, overall correct ratio: %.2f%%, %.2f%%"%(detect01*100,detect29*100))
    return detect01,detect29

if __name__=="__main__":
    print(keywords[272],keywords[273],keywords[81])
    #train01()