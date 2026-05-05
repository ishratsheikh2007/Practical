# Write a Python program that implements a menu-driven interface for managing a list of integers. The program should have the following menu options:

# 1. Add

# 2. Remove

# 3. Display

# 4. Quit

def Add(x):
	lst.append(x)
	print(f"List after adding: {lst}")

def Remove(x):
	for l in lst:
		if(x==l):
			found=True
			break
		else:
			found=False
			
	if(found):
		lst.remove(x)
		print(f"List after removing: {lst}")
	else:
		print("Element not found")
def Display():
	if(len(lst)==0):
		print("List is empty")
	else:
		print(lst)
lst=list()
for i in range(1,100):
	print("1. Add\n2. Remove\n3. Display\n4. Quit")
	Choice=int(input("Enter choice: "))
	if(Choice==1):
		x=int(input("Integer: "))
		Add(x)
	elif(Choice==2):
		if(len(lst)==0):
			print("List is empty")
		else:
			x=int(input("Integer: "))
			Remove(x)
	elif(Choice==3):
		Display()
	elif(Choice==4):
		break
	else:
		print("Invalid choice")