import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.searchsorted(arr, 35)

print("Original Array:", arr)
print("Insertion Position:", result)