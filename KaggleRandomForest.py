from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import csv

df = pd.read_csv('train.csv', header=0)
tdf = pd.read_csv('test.csv', header=0)
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1}).astype(int)
tdf['Gender'] = df['Sex'].map( {'female': 0, 'male': 1}).astype(int)

df.loc[df.Embarked.isnull(), 'Embarked'] = 'C'
tdf.loc[df.Embarked.isnull(), 'Embarked'] = 'C'

df['Port'] = df['Embarked'].map({'C': 0, 'S': 1, 'Q': 2}).astype(int)
tdf['Port'] = df['Embarked'].map({'C': 0, 'S': 1, 'Q': 2}).astype(int)

median_ages = np.zeros((2,3))
median_fare = tdf.Fare.dropna().median()


for i in range(0, 2):
    for j in range(0, 3):
        median_ages[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['Age'].dropna().median()



for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'Age'] = median_ages[i,j]
        tdf.loc[ (tdf.Age.isnull()) & (tdf.Gender == i) & (tdf.Pclass == j+1),\
                'Age'] = median_ages[i,j]


df.drop(['PassengerId','Name','Sex', 'Ticket', 'Cabin', 'Embarked'], inplace=True, axis=1)
tdf.drop(['PassengerId','Name','Sex', 'Ticket', 'Cabin', 'Embarked'], inplace=True, axis=1)

print df.head()
tdf.loc[tdf.Fare.isnull()] = median_fare

train_data = df.values
test_data = tdf.values

forest = RandomForestClassifier(n_estimators = 100)

forest = forest.fit(train_data[0::,1::],train_data[0::,0])
output = forest.predict(test_data)

prediction_file = open("myRandomForest.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])

passengerId = 892

print(len(output))

for i in xrange(len(output)):
    prediction_file_object.writerow([passengerId, int(output[i])])
    passengerId += 1

prediction_file.close()