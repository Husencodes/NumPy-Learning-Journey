import numpy as np

arr = np.array([50, 10, 40, 20, 30])

# Ascending order
ascending = np.sort(arr)

# Descending order
descending = np.sort(arr)[::-1]

print("Original:", arr)
print("Ascending:", ascending)
print("Descending:", descending)