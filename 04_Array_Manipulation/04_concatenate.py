import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print("Array A:", a)
print("Array B:", b)
print("Concatenated:", result)