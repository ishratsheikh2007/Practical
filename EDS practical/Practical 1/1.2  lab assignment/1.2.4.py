# Write a Python program to print a right-angled triangle pattern of numbers.
n=int(input())
for x in range(1,n+1):
	for y in range(1,x+1):
		print(f"{y}",end=" ")
	print()

