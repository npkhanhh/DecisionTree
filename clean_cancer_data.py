import numpy as np
import pandas as pd

def shuffle(df, axis = 1):
    df = df.copy()
    df = df.reindex(np.random.permutation(df.index))
    return df


df = pd.read_csv('Cancer.csv', header=None, names=['AGE','MENOPAUSE', 'TUMOR-SIZE', 'INV-NODES', 'NODE-CAPS', 'DEG-MALIG', 'BREAST', 'BREAST-QUAD', 'IRRADIAT'])

# df.insert(1, 'AGE', df['AGE'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
# df.insert(3, 'MAIN_PRICE', df['MAINT'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
# df.insert(5, 'DOOR', df['DOORS'].map({'2': 2, '3': 3, '4': 4, '5more': 5}).astype(int))
# df.insert(7, 'PASSENGER', df['PERSON'].map({'2': 2, '4': 4, 'more': 5}).astype(int))
# df.insert(9, 'LUG', df['LUGBOOT'].map({'small': 0, 'med': 1, 'big': 2}).astype(int))
# df.insert(11, 'SAFE', df['SAFETY'].map({'low': 0, 'med': 1, 'high': 2}).astype(int))
# df.insert(13, 'DECISION', df['CLASS'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}).astype(int))
#df = df.drop(['BUYING', 'MAINT', 'LUGBOOT', 'DOORS', 'PERSON', 'SAFETY', 'CLASS'], axis = 1)

df['AGE'].replace(['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99'],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9])


df = shuffle(df)

df.to_csv('Cancer_Processed.csv', index=False)