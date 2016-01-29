#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from Tree import DecisionTree as dt
df = pd.read_csv('Car.csv', header=None, names=['BUYING','MAINT', 'DOORS', 'PERSON', 'LUGBOOT', 'SAFETY', 'CLASS'])


def data_cleaning():
    df.insert(1, 'BUY_PRICE', df['BUYING'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
    df.insert(3, 'MAIN_PRICE', df['MAINT'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
    df.insert(7, 'LUG', df['LUGBOOT'].map({'small': 0, 'med': 1, 'big': 2}).astype(int))
    df.insert(9, 'SAFE', df['SAFETY'].map({'low': 0, 'med': 1, 'high': 2}).astype(int))
    df.insert(11, 'DECISION', df['CLASS'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}).astype(int))

    data = df.drop(['BUYING', 'MAINT', 'LUGBOOT', 'SAFETY', 'CLASS'], axis = 1)
    return data

df2 = data_cleaning()
t = dt()
t.fit(df2)
print t

