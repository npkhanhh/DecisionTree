import pandas as pd
import pylab as P
import numpy as np

df = pd.read_csv('train.csv', header=0)

df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
median_ages = np.zeros((2,3))


for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['Age'].dropna().median()

df['AgeFill'] = df['Age']

for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'AgeFill'] = median_ages[i,j]

print df[ df['Age'].isnull() ][['Gender','Pclass','Age','AgeFill']]

