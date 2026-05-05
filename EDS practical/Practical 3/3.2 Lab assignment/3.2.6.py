# The given code in the editor takes a single array, array1, as space-separated integers as input from the user.

# Additionally, it takes the following inputs:

# search_value: The value to search for in the array.
# count_value: The value to count its occurrences in the array.
# broadcast_value: The value to add for broadcasting across the array.


# You need to complete the code to perform the following operations:

# 1. Searching: Find the indices where search_value appears in array1 and print these indices.

# 2. Counting: Count how many times count_value appears in array1 and print the count.

# 3. Broadcasting: Add broadcast_value to each element of array1 using broadcasting, and print the resulting array.

# 4. Sorting: Sort array1 in ascending order and print the sorted array.

import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
search_indices = np.where(array1 == search_value)[0]
print(search_indices)
# Count occurrences in array1
count_occurrences = np.count_nonzero(array1 == count_value)
print(count_occurrences)
# Broadcasting addition
broadcasted_array = array1 + broadcast_value
print(broadcasted_array)
# Sort the first array
sorted_array = np.sort(array1)
print(sorted_array)