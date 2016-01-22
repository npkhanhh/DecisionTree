#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def data_cleaning():

    df = pd.read_csv('Car.csv', header=None, names=['BUYING','MAINT', 'DOORS', 'PERSON', 'LUGBOOT', 'SAFETY', 'CLASS'])

    df.insert(1, 'BUY_PRICE', df['BUYING'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
    df.insert(3, 'MAIN_PRICE', df['MAINT'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
    df.insert(7, 'LUG', df['LUGBOOT'].map({'small': 0, 'med': 1, 'big': 2}).astype(int))
    df.insert(9, 'SAFE', df['SAFETY'].map({'low': 0, 'med': 1, 'high': 2}).astype(int))
    df.insert(11, 'DECISION', df['CLASS'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}).astype(int))

    a = df[df['BUY_PRICE'] > 2].shape[0]
    print a

data_cleaning()


