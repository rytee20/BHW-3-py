import pandas as pd

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")
all_data = pd.concat([train_data, test_data])
numbers_fields = ["Pclass", "Age", "SibSp", "Parch","Fare"]

print("Женщины:")
print(all_data[all_data["Sex"] == "female"][numbers_fields].describe())
print("\nМужчины:")
print(all_data[all_data["Sex"] == "male"][numbers_fields].describe())
