import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

result = np.linalg.inv(A)

print("Original Matrix:")
print(A)

print("Inverse Matrix:")
print(result)