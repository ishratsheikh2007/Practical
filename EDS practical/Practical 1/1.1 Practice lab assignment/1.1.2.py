# Write a Python program that accepts an integer n as input. Depending on the number of digits in n .
# Constraints: 1 ≤ n  ≤  999
x=int(input())
if x>0 and x<10:
	result=x**2
	print(result)
elif x>9 and x<100:
	result=x**0.5
	print(f"{result:.2f}")
elif x>99 and x<1000:
	result=x**0.3333333
	print(f"{result:.2f}")
else:
	print("Invalid")