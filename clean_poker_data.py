import numpy as np
import pandas as pd

def shuffle(df, axis = 1):
    df = df.copy()
    df = df.reindex(np.random.permutation(df.index))
    return df


df = pd.read_csv('PokerRE.csv', header=None, names=['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5', 'CLASS'])

# df.insert(1, 'BUY_PRICE', df['BUYING'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
# df.insert(3, 'MAIN_PRICE', df['MAINT'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
# df.insert(5, 'DOOR', df['DOORS'].map({'2': 2, '3': 3, '4': 4, '5more': 5}).astype(int))
# df.insert(7, 'PASSENGER', df['PERSON'].map({'2': 2, '4': 4, 'more': 5}).astype(int))
# df.insert(9, 'LUG', df['LUGBOOT'].map({'small': 0, 'med': 1, 'big': 2}).astype(int))
# df.insert(11, 'SAFE', df['SAFETY'].map({'low': 0, 'med': 1, 'high': 2}).astype(int))
# df.insert(13, 'DECISION', df['CLASS'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}).astype(int))
# df = df.drop(['VENDOR NAME', 'MODEL NAME', 'ERP'], axis = 1)

df = shuffle(df)

df.to_csv('PokerRE_Processed.csv', index=False)