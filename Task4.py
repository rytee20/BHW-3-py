import pandas as pd

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")
all_data = pd.concat([train_data, test_data])

lastnames={}
firstnames={}

for person in all_data.iterrows():
    person = person[1]
    lastname = person.Name.split(',')[0]
    lastnames[lastname] = lastnames.setdefault(lastname, 0) + 1

for person in all_data.iterrows():
    person = person[1]

    if(person.Name.find("(")!=-1):
        firstname = person.Name.split("(")[1]
        firstname = firstname.split(" ")[0]

    else:
        firstname = person.Name.split(", ")[1]
        firstname = firstname.split(" ")[1]

    firstnames[firstname] = firstnames.setdefault(firstname, 0) + 1

list_lastnames = list(lastnames.items())
list_lastnames.sort(key=lambda i: i[1])
list_firstnames = list(firstnames.items())
list_firstnames.sort(key=lambda i: i[1])

print("ТОП-10 популярных фамилий (в порядке убываня популярности):")
for i in range(10):
    print(list_lastnames[-i - 1][0])

print("\nТОП-10 популярных имен (среди первых) (в порядке убываня популярности):")
for i in range(10):
    print(list_firstnames[-i - 1][0])
