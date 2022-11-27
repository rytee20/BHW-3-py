import pandas as pd

train_data = pd.read_csv("train.csv")
print("Статистика выживаемости мужчин и женщин в каждом классе:")
print(train_data.groupby(["Pclass", "Sex"])["Survived"].value_counts(normalize=True))
