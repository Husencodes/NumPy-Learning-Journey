import numpy as np

arr = np.array([1.234, 2.567, 3.891, 4.456])

print("Original:", arr)
print("Round:", np.round(arr, 2))
print("Floor:", np.floor(arr))
print("Ceil:", np.ceil(arr))
print("Truncate:", np.trunc(arr))