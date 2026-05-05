# The given code takes two 3 x 3 matrices, matrix_a, and matrix_b, as input from the user and converts them into NumPy arrays.
import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
madd=matrix_a+matrix_b
print("Addition (A + B):")
print(madd)
# Subtraction
msub=matrix_a-matrix_b
print("Subtraction (A - B):")
print(msub)
# Multiplication (element-wise)
mmu1=matrix_a*matrix_b
print("Element-wise Multiplication (A * B):")
print(mmu1)
# Matrix multiplication (dot product)
mdot=np.dot(matrix_a,matrix_b)
print("A dot B:")
print(mdot)
# Transpose
Mtran=matrix_a.T
print("Transpose of A:")
print(Mtran)