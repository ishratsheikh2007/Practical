# Write a Python code to plot a stacked bar chart showing the survival count for passengers based on their embarkation location in the Titanic dataset.

# The chart should display the following specifications:

# Use the Embarked column to determine the embarkation location. After converting this column into dummy variables (using pd.get_dummies()), plot the survival count based on the Embarked_Q column (representing passengers who embarked from Queenstown) in relation to survival.
# Set the chart type to 'bar' and make it stacked.
# Add the title "Survival by Embarked " to the chart.
# Label the x-axis as 'Embarked' and the y-axis as 'Count'.
# Include a legend to distinguish between survivors and non-survivors (label the legend as 'Survived' and 'Not Survived').
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

# Write your code here for Bar Plot for Survival by Embarked

survival_counts = data.groupby('Embarked_Q')['Survived'].value_counts().unstack()
survival_counts.plot(kind='bar',stacked=True)
plt.title('Survival by Embarked')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.legend(['Not Survived','Survived'])
plt.show()
