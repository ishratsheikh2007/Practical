# Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

# The CSV file contains the following columns: Date, Product, Quantity, Price, and City.
# For each date, find all pairs of products that were sold together (i.e., two products sold on the same date).
# Output the product pair/s that was sold most frequently.
import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code
grouped = df.groupby("Date")["Product"].apply(list)
pairs_counter = Counter()
for products in grouped:
	pairs = combinations(sorted(products),2)
	pairs_counter.update(pairs)
max_frequency = max(pairs_counter.values())
most_common_pairs = [(pair, freq) for pair, freq in pairs_counter.items() if freq == max_frequency]
for (product1, product2), frequency in most_common_pairs:
	print(f"{product1} and {product2}: {frequency} times")
# Output the most frequent product pairs