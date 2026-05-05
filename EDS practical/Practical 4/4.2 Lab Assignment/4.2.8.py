# You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.
# Get the number of survivors by gender (Sex).
# Get the number of non-survivors by gender (Sex).
# Get the number of survivors by embarkation location (Embarked_S).
# Get the number of non-survivors by embarkation location (Embarked_S).
# Calculate the percentage of children (Age < 18) who survived.
# Calculate the percentage of adults (Age >= 18) who survived.
# Get the median age of survivors.
# Get the median age of non-survivors.
# Get the median fare of survivors.
# Get the median fare of non-survivors.
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


# 1. Get the number of survivors by gender
survivors_by_gender = data[data['Survived'] == 1]['Sex'].value_counts()
print(survivors_by_gender)

# 2. Get the number of non-survivors by gender
non_survivors_by_gender = data[data['Survived'] == 0]['Sex'].value_counts()
print(non_survivors_by_gender)
# 3. Get the number of survivors by embarked location
survivors_by_embarked_s = data[data['Survived'] == 1]['Embarked_S'].value_counts()
print(survivors_by_embarked_s)
# 4. Get the number of non-survivors by embarked location
non_survivors_by_embarked_s = data[data['Survived'] == 0]['Embarked_S'].value_counts()
print(non_survivors_by_embarked_s)

# 5. Calculate the percentage of children (Age < 18) who survived
children = data[data['Age'] < 18]
children_survival_rate = children['Survived'].mean()
print(children_survival_rate)
# 6. Calculate the percentage of adults (Age >= 18) who survived
adults =data[data['Age'] >= 18]
adults_survival_rate = adults['Survived'].mean()
print(adults_survival_rate)
# 7. Get the median age of survivors
median_age_survivors = data[data['Survived'] == 1]['Age'].median()
print(median_age_survivors)
# 8. Get the median age of non-survivors
print(data[data['Survived'] == 0]['Age'].median())

# 9. Get the median fare of survivors
print(data[data['Survived'] == 1]['Fare'].median())

# 10. Get the median fare of non-survivors
print(data[data['Survived'] == 0]['Fare'].median())
