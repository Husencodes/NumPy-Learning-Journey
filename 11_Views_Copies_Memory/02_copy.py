import numpy as np

a = np.array([10, 20, 30, 40])
b = a.copy()

b[0] = 100

print("Original:", a)
print("Copy:", b)