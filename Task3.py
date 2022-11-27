import pandas as pd

train_data = pd.read_csv("train.csv")

print(train_data.groupby(["Embarked"])["Survived"].value_counts(normalize=True))
#больше всего пассажиров выжило со значеним порта посадки S, меньше -- C
