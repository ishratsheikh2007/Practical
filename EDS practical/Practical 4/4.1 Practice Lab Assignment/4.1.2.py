# A dictionary of lists has been provided to you in the editor. Create a DataFrame from the dictionary of lists and perform the listed operations, then display the DataFrame before and after each manipulation.

import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
new_name=input("New name: ")
new_age=int(input("New age: "))
df.loc[len(df)]=[new_name,new_age]


# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
row_to_modify=int(input("Index of row to modify: "))
new_age_value=int(input("New age: "))
df.at[row_to_modify,"Age"]=new_age_value

# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
row_to_delete=int(input("Index of row to delete: "))
df=df.drop(index=row_to_delete).reset_index(drop=True)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
genders=input("Enter genders separated by space: ").split()
df["Gender"]=genders
# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df["Name"]=df["Name"].str.upper()
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df=df.drop(columns=["Age"])
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
