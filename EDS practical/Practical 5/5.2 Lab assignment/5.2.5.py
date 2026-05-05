# Write a Python code to plot a stacked bar chart that shows the count of passengers who survived and did not survive, grouped by passenger class (Pclass), in the Titanic dataset. The chart should display the following specifications:

# Group the data by the Pclass column and count the number of survivors (0 = Did not survive, 1 = Survived) for each class using value_counts().
# Use a stacked bar chart to display the survival counts.
# Add the title "Survival by Pclass" to the chart.
# Label the x-axis as 'Pclass' and the y-axis as 'Count'.
# The legend should indicate 'Not Survived' and 'Survived'.
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Bar Plot for Survival by Pclass

grouped = pd.crosstab(data['Pclass'],data['Survived'])
grouped.plot(kind='bar',stacked=True)
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.title('Survival by Pclass')
plt.legend(['Not Survived','Survived'])
plt.show()
