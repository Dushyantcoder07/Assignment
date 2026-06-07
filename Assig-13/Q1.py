# Replace NaN with 0 and interchange rows columns 

import numpy as np 

arr = np.array([[6,-8,73,-110,],[np.nan, -8, 0, 94]])

#Replace NaN with 0
arr = np.nan_to_num(arr, nan=0)

print("After replacing NaN:")
print(arr)

#Interchange rows and columns (Transpose)
transpose_arr = arr.T

print("\n After Interchanging Rows and Columns:")
print(transpose_arr)