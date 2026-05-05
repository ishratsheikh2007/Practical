# Write a program to read a text file containing student information (name, age, and grade) using Pandas. Perform the following tasks:
# Display the first five rows of the data frame.
# Calculate the average age of the students (limit the average age up to 2 decimal places).
# Filter out the students who have a grade above a certain threshold (consider the threshold grade is 'B').
import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here..
print("First five rows:")
print(data.head())
average_age=round(data["Age"].mean(),2)
print(f"Average age: {average_age}")
filtered_students=data[data["Grade"]<="B"]
print("Students with a grade up to B")
print(filtered_students)