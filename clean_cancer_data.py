import numpy as np
import pandas as pd
from random import randint

def shuffle(df, axis = 1):
    df = df.copy()
    df = df.reindex(np.random.permutation(df.index))
    return df


df = pd.read_csv('Cancer.csv', header=None, names=['AGE','MENOPAUSE', 'TUMOR-SIZE', 'INV-NODES', 'NODE-CAPS',
                                                   'DEG-MALIG', 'BREAST', 'BREAST-QUAD', 'IRRADIAT', 'CLASS'])

# df.insert(1, 'AGE', df['AGE'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
# df.insert(3, 'MAIN_PRICE', df['MAINT'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
# df.insert(5, 'DOOR', df['DOORS'].map({'2': 2, '3': 3, '4': 4, '5more': 5}).astype(int))
# df.insert(7, 'PASSENGER', df['PERSON'].map({'2': 2, '4': 4, 'more': 5}).astype(int))
# df.insert(9, 'LUG', df['LUGBOOT'].map({'small': 0, 'med': 1, 'big': 2}).astype(int))
# df.insert(11, 'SAFE', df['SAFETY'].map({'low': 0, 'med': 1, 'high': 2}).astype(int))
# df.insert(13, 'DECISION', df['CLASS'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}).astype(int))
#df = df.drop(['BUYING', 'MAINT', 'LUGBOOT', 'DOORS', 'PERSON', 'SAFETY', 'CLASS'], axis = 1)


df['AGE'].replace(["'10-19'", "'20-29'", "'30-39'", "'40-49'", "'50-59'", "'60-69'", "'70-79'", "'80-89'", "'90-99'"],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9], inplace=True)
df['MENOPAUSE'].replace(["'lt40'", "'ge40'", "'premeno'"], [1, 2, 3], inplace=True)
df['TUMOR-SIZE'].replace(["'0-4'", "'5-9'", "'10-14'", "'15-19'", "'20-24'", "'25-29'", "'30-34'", "'35-39'", "'40-44'",
                          "'45-49'", "'50-54'", "'55-59'"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)
df['INV-NODES'].replace(["'0-2'", "'3-5'", "'6-8'", "'9-11'", "'12-14'", "'15-17'", "'18-20'", "'21-23'", "'24-26'",
                         "'27-29'", "'30-32'", "'33-35'", "'36-39'"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                        inplace=True)
df['NODE-CAPS'].replace(["'yes'", "'no'"], [1, 2], inplace=True)
df['DEG-MALIG'].replace(["'1'", "'2'", "'3'"], [1, 2, 3], inplace=True)
df['BREAST'].replace(["'left'", "'right'"], [1, 2], inplace=True)
df['BREAST-QUAD'].replace(["'left_up'", "'left_low'", "'right_up'",	"'right_low'", "'central'"], [1, 2, 3, 4, 5],
                          inplace=True)
df['IRRADIAT'].replace(["'yes'", "'no'"], [1, 2], inplace=True)
df['CLASS'].replace(["'no-recurrence-events'", "'recurrence-events'"], [1, 2], inplace=True)
df.fillna(method='pad', inplace=True)

df = shuffle(df)

df.to_csv('Cancer_Processed.csv', index=False)