import numpy as np
from sympy import *

# X^t * X * c = X^t * y

rssis = Matrix([[1, 30, 30**2], [1,40, 40**2], [1,50, 50**2], [1,60, 60**2], [1,70, 70**2]])
distances = Matrix([[25],[100],[200],[325],[500]])

left_side = rssis.T*rssis
right_side = rssis.T*distances
whole = left_side.col_insert(len(left_side), right_side)
dimension = shape(whole)
rows = dimension[0]
columns = dimension[1]
whole = whole.rref()[0]
c = zeros(rows, 1)
for n in range(0, rows):
    c[n] = whole.row(n)[columns-1]
print(whole)
print(c)









