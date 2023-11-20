#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import re
import time
import pickle
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


def load_data(ratio=10):
    data = read_db()
    print('totally %d datas' % (len(data)))
    trainset = []
    testset = []
    counter = {i: 0 for i in range(29)}
    for text, type29 in tqdm(data):
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


def train01():
    model = FClassifier(output_size=2)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # trainset, testset = load_data()
    # with open("datar1.pickle", 'wb') as f:
    #     pickle.dump((trainset, testset), f)
    with open("datar1.pickle", 'rb') as f:
        trainset, testset = pickle.load(f)
    trainset = [(i, j if j == 0 else torch.tensor(1, dtype=torch.long))
                for i, j in trainset]
    testset = [(i, j if j == 0 else torch.tensor(1, dtype=torch.long))
               for i, j in testset]

    traindl = DataLoader(dataset=trainset, batch_size=16,
                         shuffle=True, drop_last=True)
    testdl = DataLoader(dataset=testset, batch_size=16, shuffle=False)

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

        if (epoch+1) % 1 == 0:
            traincorr = test(model, traindl)
            testcorr = test(model, testdl)
            print('Epoch %2d, Train: %.4f, %.2f; Test: %.2f' % (
                epoch+1, totloss/totnum, traincorr*100, testcorr*100))
    return model


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
        for inputs, labels in dl:
            outputs = model(inputs)
            totnum += len(labels)
            predicted = outputs.argmax(dim=1)
            corrnum += (predicted == labels).sum().item()
    model.train()
    return corrnum/totnum


if __name__ == "__main__":
    # stat()
    # trainset,testset = load_data()
    # print(testset[0])
    model = train01()
    f = open('parameters.h', 'w')
    i = 1
    for name, parameters in model.named_parameters():
        numbers = parameters.data.tolist()
        if name.endswith('weight'):
            f.write('const float weight'+str(i))
        else:
            f.write('const float bias'+str(i))
            i += 1
        if type(numbers) == float:
            f.write('='+str(numbers)+';\n')
        elif type(numbers[0]) == float:  # vector
            f.write('['+str(len(numbers)) +
                    ']={'+', '.join([str(num) for num in numbers])+'};\n')
        else:  # matrix
            f.write('['+str(len(numbers))+']['+str(len(numbers[0]))+']={')
            for nums in numbers:
                f.write('{'+', '.join([str(num) for num in nums])+'},\n    ')
            f.write('};\n')
    f.close()
    # print(text2feature2("alignas alignof and and_eq as asm"))
