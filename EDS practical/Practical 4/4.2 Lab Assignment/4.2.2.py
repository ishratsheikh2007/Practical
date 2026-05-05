# Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

# The CSV file contains the columns: Date, Product, Quantity, Price, and City.
# Find the product that sold the most in terms of quantity sold.
# Display the product that sold the most and the total quantity sold for that product.
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
product_sales = df.groupby("Product")["Quantity"].sum()

# Find the product with the highest total quantity sold
best_product = product_sales.idxmax()
highest_quantity = product_sales.max()

# Display the result
print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")
