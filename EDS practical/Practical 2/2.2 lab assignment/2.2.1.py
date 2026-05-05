# Write a program to check whether the given element is present or not in the array of elements using linear search.



# Input format:

# The first line of input contains the array of integers which are separated by space
# The last line of input contains the key element to be searched
def linear_search(arr, key):
	for index in range(len(arr)):
		if arr[index] == key:
			return index
	return -1
arr = list(map(int, input().split()))
key = int(input())
index = linear_search(arr,key)
if index != -1:
	print(index)
else:
	print("Not found")