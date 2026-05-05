# Write a Python program to create a NumPy array based on user input and display the following:

# The created NumPy array.
# The number of dimensions of the array using ndim
# The shape of the array using shape
# The total number of elements in the array using size
# Assume all input elements are valid integers.

import numpy as np

# write your code here...
rows,cols=map(int,input().split())
elements=[]
for _ in range(rows):
	elements.extend(map(int,input().split()))
array=np.array(elements).reshape(rows,cols)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)