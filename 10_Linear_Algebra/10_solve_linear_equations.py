import numpy as np

# Equations:
# 2x + y = 5
# x + 3y = 6

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([5, 6])

solution = np.linalg.solve(A, B)

print("Solution:")
print("x =", solution[0])
print("y =", solution[1])