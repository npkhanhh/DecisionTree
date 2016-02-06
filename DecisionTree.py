#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Tree import DecisionTree as dt




def split(df, k):
    df = np.array_split(df, k)
    return df

k = 10

df = pd.read_csv('Car_Processed.csv')

df = split(df, k)

# for row in df[0].iterrows():
#     index, data = row
#     print(data.tolist())


remt_tree = dt()
cart_tree = dt()
count = []
count2 = []
for i in range(k):
    train_set = pd.concat(df[:i] + df[i+1:])
    test_set = df[i]
    print('start REMT')
    remt_tree.fit(train_set)
    train_set = train_set.drop(['temp'], axis = 1)
    count.append(remt_tree.test(test_set))
    print('start CART')
    cart_tree.fit(train_set, 'CART')
    count2.append(cart_tree.test(test_set))

    print i

pca = PCA(n_components=3)
n = df[1].shape[0]
df_draw = df[1].copy()
df_draw = df_draw.drop(['DECISION'], axis = 1)
X_R = pca.fit_transform(df_draw)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
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
print count2
for i in range(k):
    print sum(count[i]), float(sum(count[i]))/len(count[i]), sum(count2[i]), float(sum(count2[i]))/len(count2[i])

