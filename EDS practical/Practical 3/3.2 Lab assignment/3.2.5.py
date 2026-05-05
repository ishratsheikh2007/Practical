# The given code takes a list of integers as input and converts it into a NumPy array. Your task is to complete the code by:

# Creating a view of the original_array and assigning it to view_array.
# Creating a copy of the original_array and assigning it to copy_array.

# After completing these steps, observe how modifying the view affects the original_array, while modifying the copy does not.

import numpy as np

inputlist = list(map(int,input().split(" ")))

# Original array
original_array = np.array(inputlist)

# Create a view
view_array = original_array.view()


# Create a copy
copy_array = original_array.copy()

# Modify the view
view_array[0] = 99
print("Original array after modifying view:", original_array)
print("View array:", view_array)

# Modify the copy
copy_array[1] = 88
print("Original array after modifying copy:", original_array)
print("Copy array:", copy_array)
