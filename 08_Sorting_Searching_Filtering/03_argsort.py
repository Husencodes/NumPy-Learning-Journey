import numpy as np

arr = np.array([40, 10, 30, 20])

result = np.argsort(arr)

print("Original:", arr)
print("Sorted Indices:", result)
print("Sorted Values:", arr[result])