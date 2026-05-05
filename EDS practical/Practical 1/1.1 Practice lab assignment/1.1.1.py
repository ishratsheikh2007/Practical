# Write a program that accepts the mass of an object (in kilograms) and its velocity (in meters per second), then calculates and displays the momentum of the object. The momentum 
#  is calculated using the formula:


# where: p = m x v

# m is the mass of the object (in kilograms).

# v is the velocity of the object (in meters per second).

m=float(input())
v=float(input())
P=m*v
print(f"{P:.2f}kgm/s\n")