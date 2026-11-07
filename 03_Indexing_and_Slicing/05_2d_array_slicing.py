import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("First two rows:")
print(arr[0:2, :])

print("First two columns:")
print(arr[:, 0:2])

print("Selected elements:")
print(arr[0:2, 1:3])