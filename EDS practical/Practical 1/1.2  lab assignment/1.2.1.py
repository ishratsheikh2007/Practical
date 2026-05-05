# Write a Python program that accepts the number of courses and the marks of a student in those courses.

# The grade is determined based on the aggregate percentage:

# If the aggregate percentage is greater than 75, the grade is Distinction.
# If the aggregate percentage is greater than or equal to 60 but less than 75, the grade is First Division.
# If the aggregate percentage is greater than or equal to 50 but less than 60, the grade is Second Division.
# If the aggregate percentage is greater than or equal to 40 but less than 50, the grade is Third Division.
n = int(input())
marks = list(map(int,input().split(" ")))
if all(mark>=40 for mark in marks):
	per = sum(marks)/n
	print(f"Aggregate Percentage: {per:.2f}")
	if per>=75:
		print("Grade: Distinction")
	elif 60<=per<75:
		print("Grade: First Division")
	elif 50<=per<60:
		print("Grade: Second Division")
	elif 40<=per<50:
		print("Grade: Third Division")
else:
	print("Fail")