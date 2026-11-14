import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = np.transpose(A)

print("Original Matrix:")
print(A)

print("Transpose:")
print(result)