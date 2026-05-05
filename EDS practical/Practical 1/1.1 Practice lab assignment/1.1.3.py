# Write a Python program to calculate number of days between two dates.

from datetime import date
from datetime import datetime
date1 = input().strip()
date2 = input().strip()

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")
difference = d2 - d1
print(difference.days)
	
