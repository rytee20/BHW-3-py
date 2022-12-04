import pandas as pd

train_data = pd.read_csv("train.csv")
# Значений не достает только в столбцах Age(Возраст), Cabin (Каюта) и Embarked (Порт посадки)
# Cabin и Embarked содержат текст, так что их заполнить медианой не получится

age_first=train_data['Age'].tolist()
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())
age_second=train_data['Age'].tolist()

for i in range(len(age_first)):
    print(age_first[i], " - ", age_second[i])
