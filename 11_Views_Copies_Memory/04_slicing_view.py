import numpy as np

a = np.array([10, 20, 30, 40, 50])

b = a[1:4]
b[0] = 200

print("Original:", a)
print("Sliced:", b)