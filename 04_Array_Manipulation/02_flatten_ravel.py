import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Flatten
flat = arr.flatten()

# Ravel
rav = arr.ravel()

print("Original:")
print(arr)

print("Flatten:", flat)
print("Ravel:", rav)