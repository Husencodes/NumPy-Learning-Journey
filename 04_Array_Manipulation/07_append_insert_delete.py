import numpy as np

arr = np.array([10, 20, 30, 40])

# Append
a = np.append(arr, 50)

# Insert
b = np.insert(arr, 2, 25)

# Delete
c = np.delete(arr, 1)

print("Original:", arr)
print("Append:", a)
print("Insert:", b)
print("Delete:", c)