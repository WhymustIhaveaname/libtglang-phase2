#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset,DataLoader
from tqdm import tqdm
from constants import *
from datautils import *

class FClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        input_size = len(keywords)
        num_classes = len(TglangLanguage)
        self.fc = nn.Sequential(
            nn.Linear(input_size, 32),
            nn.ReLU(),
            nn.Linear(32, num_classes),
        )

    def forward(self, x):
        out = self.fc(x)
        return out

def load_data(ratio=10):
    data = read_db()
    print('totally %d datas'%(len(data)))
    trainset = []
    testset = []
    counter = {i:0 for i in range(29)}
    for text,type29 in tqdm(data):
        counter[type29] += 1
        if counter[type29]%ratio == 0:
            testset.append((text2feature(text),torch.tensor(type29,dtype=torch.long)))
        else:
            trainset.append((text2feature(text),torch.tensor(type29,dtype=torch.long)))
    print("split into %d train and %d test"%(len(trainset),len(testset)))
    return trainset,testset

def text2feature(text):
    x = torch.zeros(len(keywords))
    for i,j in enumerate(keywords):
        x[i] = text.count(j)
    return x

def train():
    model = FClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    trainset,testset = load_data()
    traindl = DataLoader(dataset=trainset,batch_size=16,shuffle=True,drop_last=True)
    testdl  = DataLoader(dataset=testset,batch_size=16,shuffle=False)

    for epoch in range(100):
        totloss = 0.0
        totnum  = 0
        for inputs,labels in traindl:
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            totloss += loss.item()
            totnum  += len(labels)

        if (epoch+1) % 10 == 0:
            trainloss,trainc1,trainc2 = test(model,traindl)
            testloss,testc1,testc2     =test(model,testdl)
            print('Epoch %d, Train: %.4f, %.2f, %.2f; Test: %.4f, %.2f, %.2f'%(epoch+1,trainloss,trainc1*100,trainc2*100,testloss,testc1*100,testc2*100))

def test(model,dl):
    model.eval()
    with torch.no_grad():
        criterion = nn.CrossEntropyLoss()
        totloss = 0.0
        totnum  = 0
        codetect = 0   #Code/Other Detection: 62.7
        langdetect = 0 #Language Detection: 79.5
        langnum    = 0
        for inputs,labels in dl:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            totloss += loss.item()
            totnum  += len(labels)
            predicted = outputs.argmax(dim=1)
            codetect += ((predicted==0)==(labels==0)).sum().item()
            langdetect += torch.logical_and(predicted==labels,predicted>0).sum().item()
            langnum    += (predicted>0).sum().item()
    model.train()
    return totloss/totnum, codetect/totnum, langdetect/langnum

if __name__=="__main__":
    #stat()
    # trainset,testset = load_data()
    # print(testset[0])
    train()