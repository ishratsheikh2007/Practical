# Write a Python program to perform insertion, update, deletion, and traversal operations on a dictionary. An initial dictionary containing 10 predefined records is already given in the program.



# Operations to be Performed:

# Insertion – Insert a new key-value pair into the dictionary using user input.
# Update – Update the value of an existing key using user input.
# Deletion – Delete a specified key from the dictionary using user input.
# Traversal – Traverse the final dictionary and display all key-value pairs.

# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...

print("Original Dictionary:",student)
key=int(input())
value=input()
student[key]=value
print("After Insertion:",student)
key=int(input())
value=input()
if key in student:
  student[key]=value
print("After Update:",student)
key=int(input())
if key in student:
  del student[key]
print("After Deletion:",student)
print("Traversing Dictionary:")
for key,value in student.items():
	print(key,":",(value))