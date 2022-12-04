import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


pd.options.mode.chained_assignment = None
train_data = pd.read_csv('train.csv')

train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())

data_to_train = train_data[['Pclass', 'Age', 'Sex']]
data_to_train['Sex'] = np.where(data_to_train['Sex'] == 'female', 0, 1)

test_data = pd.read_csv('test.csv')
test_data['Age'] = test_data['Age'].fillna(test_data['Age'].median())

data_to_test = test_data[['Pclass', 'Age', 'Sex', 'Fare']]
data_to_test['Sex'] = np.where(data_to_test['Sex'] == 'female', 0, 1)

expected_data = train_data['Survived']
rf = RandomForestClassifier(n_estimators=100)
rf.fit(data_to_train, expected_data)
pred = rf.predict(data_to_test)

with open('output.csv', 'w') as f:
    f.write("PassengerId,Survived\n")
    i = 892
    for p in pred:
        f.write(str(i) + "," + str(p) + "\n")
        i += 1
