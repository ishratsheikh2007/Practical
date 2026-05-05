# Write a Python code to plot a boxplot that shows the distribution of the 'Age' column from the Titanic dataset based on whether passengers survived or not. The boxplot should display the following specifications:

# Use the Survived column to group the data for the boxplot (0 = Did not survive, 1 = Survived).
# Set the title of the plot to "Age by Survival".
# Remove the default subtitle with plt.suptitle('').
# Label the x-axis as 'Survived' and the y-axis as 'Age'.
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

# Write your code here for Box Plot for Age by Survived
data.boxplot(column='Age',by='Survived')
plt.title('Age by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.suptitle("")
plt.show()