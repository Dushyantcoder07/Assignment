import numpy as np
from statistics import mode

arr1 = np.array([[3,4],
                 [5,6]])

arr2 = np.array([[1,0],
                 [7,8]])

# Average array
avg = (arr1 + arr2) / 2

print("Average Array:")
print(avg)

# Mean
mean_val = np.mean(avg)

# Median
median_val = np.median(avg)

# Mode
mode_val = mode(avg.flatten())

print("Mean =", mean_val)
print("Median =", median_val)
print("Mode =", mode_val)