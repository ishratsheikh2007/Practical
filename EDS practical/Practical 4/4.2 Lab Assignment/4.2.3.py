# Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

# The CSV file contains the columns: Date, Product, Quantity, Price, and City.
# Group the data by City and calculate the total quantity of products sold for each city.
# Find the city that sold the most products (based on the total quantity sold).
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# write the code..
city_sales = df.groupby("City")["Quantity"].sum()
best_city = city_sales.idxmax()
# Display the result
print(f"City sold the most products: {best_city}")
