from sympy import *

# Equation used
# X^t * X * c = X^t * y

# Test Data
rssis = Matrix([[1, 30, 30**2], [1,40, 40**2], [1,50, 50**2], [1,60, 60**2], [1,70, 70**2]])
distances = Matrix([[25],[100],[200],[325],[500]])

# Computes left hand side of the equation
left_side = rssis.T*rssis
# Computes right hand side of the equation
right_side = rssis.T*distances

# Adds right side of the equation to the left side of the equation to create the whole matrix for rref
whole = left_side.col_insert(len(left_side), right_side)

dimension = shape(whole)
rows = dimension[0]
columns = dimension[1]
whole = whole.rref()[0]
c = zeros(rows, 1)
for n in range(0, rows):
    c[n] = whole.row(n)[columns-1]

# The output is the coefficients for the equation for predicting possible locations based on input RSSI and distance
print(c)









