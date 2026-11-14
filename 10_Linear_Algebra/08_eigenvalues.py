import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

values, vectors = np.linalg.eig(A)

print("Eigenvalues:")
print(values)

print("Eigenvectors:")
print(vectors)