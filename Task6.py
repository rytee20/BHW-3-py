import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


pd.options.mode.chained_assignment = None
train_data = pd.read_csv('train.csv') # данные rain.csv
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median()) # заполням возраст медианой

data_to_train = train_data[[ # здесь можно закомментить те параметры, на которые мы не будем обращать внимания при 
    # предсказании или добавить новые 
    'Pclass',
    'Age',
    'Fare',
    'Sex']]
data_to_train['Sex'] = np.where(data_to_train['Sex'] == 'female', 0, 1) # даем полу числовае значения

test_data = pd.read_csv('test.csv')  # читаем файл test.csv
test_data['Age'] = test_data['Age'].fillna(test_data['Age'].median()) # заполняем медианой возраст
test_data['Fare'] = test_data['Fare'].fillna(test_data['Fare'].median()) # заполняем медианой цену билета

data_to_test = test_data[[ # здесь можно закомментить те параметры, на которые мы не будем обращать внимания при 
    # предсказании или добавить новые 
    'Pclass',
    'Age',
    'Fare',
    'Sex']]
data_to_test['Sex'] = np.where(data_to_test['Sex'] == 'female', 0, 1) # опять дем пол численным

expected_data = train_data['Survived'] # нам нужео предсказать выживаемисть
rf = RandomForestClassifier(n_estimators=100)
rf.fit(data_to_train, expected_data)
prediction = rf.predict(data_to_test) # предсказали

with open('output.csv', 'w') as f: # выводим
    f.write("PassengerId,Survived\n")
    i = 892
    for p in prediction:
        f.write(str(i) + "," + str(p) + "\n")
        i += 1

# Точность с учетом Пола, Класса и  Возраста (заполнен медианой) 0,64114
# Точность с учетом Пола, Класса и Цены билета (заполнена медианой) 0,76315
# Точность с учетом Пола, Класса, Цены билета (заполнена медианой) и Возраста (заполнен медианой) 0,74401
# Точность с учетом Пола и Класса 0,77511
