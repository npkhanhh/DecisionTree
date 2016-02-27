import numpy as np
import pandas as pd
from random import randint

def shuffle(df, axis = 1):
    df = df.copy()
    df = df.reindex(np.random.permutation(df.index))
    return df


df = pd.read_csv('Vote.csv', header=None, names=['HI','WPCS', 'AOTBR', 'PFF', 'ESA', 'RGIS', 'ASTB', 'ATNC', 'MM',
                                                 'I','SCC','ES','SRTS','C','DFE','EACSA','CLASS'])

df['HI'].replace(['y', 'n'], [1, 2], inplace=True)
df['WPCS'].replace(['y', 'n'], [1, 2], inplace=True)
df['AOTBR'].replace(['y', 'n'], [1, 2], inplace=True)
df['PFF'].replace(['y', 'n'], [1, 2], inplace=True)
df['ESA'].replace(['y', 'n'], [1, 2], inplace=True)
df['RGIS'].replace(['y', 'n'], [1, 2], inplace=True)
df['ASTB'].replace(['y', 'n'], [1, 2], inplace=True)
df['ATNC'].replace(['y', 'n'], [1, 2], inplace=True)
df['MM'].replace(['y', 'n'], [1, 2], inplace=True)
df['I'].replace(['y', 'n'], [1, 2], inplace=True)
df['SCC'].replace(['y', 'n'], [1, 2], inplace=True)
df['ES'].replace(['y', 'n'], [1, 2], inplace=True)
df['SRTS'].replace(['y', 'n'], [1, 2], inplace=True)
df['C'].replace(['y', 'n'], [1, 2], inplace=True)
df['DFE'].replace(['y', 'n'], [1, 2], inplace=True)
df['EACSA'].replace(['y', 'n'], [1, 2], inplace=True)
df['CLASS'].replace(['republican', 'democrat'], [1, 2], inplace=True)

df.fillna(method='pad', inplace=True)
df.fillna(method='bfill', inplace=True)


df = shuffle(df)

df.to_csv('Vote_Processed.csv', index=False)