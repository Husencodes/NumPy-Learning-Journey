import numpy as np

arr = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

print("Original Array:")
print(arr)

print("Row-wise Sorting:")
print(np.sort(arr, axis=1))

print("Column-wise Sorting:")
print(np.sort(arr, axis=0))