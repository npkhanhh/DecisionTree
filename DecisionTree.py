#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from random import shuffle,randint,choice
import numpy.random as nprnd
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Tree import DecisionTree as dt
import copy
import pylab as pl



def split(df, k):
    df = np.array_split(df, k)
    return df

k = 10

df = pd.read_csv('Car_Processed.csv')

#df = split(df, k)

# for row in df[0].iterrows():
#     index, data = row
#     print(data.tolist())


remt_tree = dt()
cart_tree = dt()
count_remt = []
count_cart = []

no_sample = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
no_class = 4

avg_err_remt = []
avg_err_cart = []
for i in no_sample:
    print i
    sum_remt = 0
    sum_cart = 0
    for j in range(k):
        test_set = df.copy(deep=True)
        train_label = nprnd.randint(no_class, size = i)
        while len(set(train_label))<no_class:
            train_label = nprnd.randint(no_class, size = i)
        train_set = pd.DataFrame(columns=test_set.columns)
        for label in train_label:
            row_indexes = test_set[test_set['CLASS'] == label].index.tolist()
            idx = choice(row_indexes)
            train_set = train_set.append(test_set.loc[idx], ignore_index=True)
            test_set.drop(idx)
        
        remt_tree.fit(train_set)
        count_remt = remt_tree.test(test_set)
        cart_tree.fit(train_set)
        count_cart = cart_tree.test(test_set)
        mae_remt = float(sum(count_remt))/test_set.shape[0]
        mae_cart = float(sum(count_cart))/test_set.shape[0]
        sum_remt += mae_remt
        sum_cart += mae_cart
        print j
    avg_err_remt.append(float(sum_remt)/k)
    avg_err_cart.append(float(sum_cart)/k)

    #for i in range(k):
    #print sum(count[i]), float(sum(count[i]))/len(count[i]), sum(count2[i]), float(sum(count2[i]))/len(count2[i])

print avg_err_remt
print avg_err_cart
pl.plot(no_sample, avg_err_remt, '*')
pl.plot(no_sample, avg_err_cart, '+')
pl.show()

#for i in range(k):
    # train_set = pd.concat(df[:i] + df[i+1:])
    # test_set = df[i]
    # print('start REMT')
    # remt_tree.fit(train_set)
    # train_set = train_set.drop(['temp'], axis = 1)
    # count.append(remt_tree.test(test_set))
    # print('start CART')
    # cart_tree.fit(train_set, 'CART')
    # count2.append(cart_tree.test(test_set))
    #
    # print i



# pca = PCA(n_components=3)
# n = df[1].shape[0]
# df_draw = df[1].copy()
# df_draw = df_draw.drop(['CLASS'], axis = 1)
# X_R = pca.fit_transform(df_draw)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for i in range(n):
#     if count[i] == 1 and count2[i] == 1:
#         ax.scatter(X_R[i][0], X_R[i][1], X_R[i][2], c='#1AA130')
#     if count[i] == 0 and count2[i] == 1:
#         ax.scatter(X_R[i][0], X_R[i][1], X_R[i][2], c='r')
#     if count[i] == 1 and count2[i] == 0:
#         ax.scatter(X_R[i][0], X_R[i][1], X_R[i][2], c='b')
#     if count[i] == 0 and count2[i] == 0:
#         ax.scatter(X_R[i][0], X_R[i][1], X_R[i][2], c='k')

#plt.show()
